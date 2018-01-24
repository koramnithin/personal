#!/usr/bin/env python
import argparse
import sys
import codecs

from nltk.corpus import cmudict

if sys.version_info[0] == 2:
  from itertools import izip
else:
  izip = zip
from collections import defaultdict as dd
import re
import os.path
import gzip
import tempfile
import shutil
import atexit

# Use word_tokenize to split raw text into words
from string import punctuation

import nltk
from nltk.tokenize import word_tokenize

scriptdir = os.path.dirname(os.path.abspath(__file__))

reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')

def prepfile(fh, code):
  if type(fh) is str:
    fh = open(fh, code)
  ret = gzip.open(fh.name, code if code.endswith("t") else code+"t") if fh.name.endswith(".gz") else fh
  if sys.version_info[0] == 2:
    if code.startswith('r'):
      ret = reader(fh)
    elif code.startswith('w'):
      ret = writer(fh)
    else:
      sys.stderr.write("I didn't understand code "+code+"\n")
      sys.exit(1)
  return ret

def addonoffarg(parser, arg, dest=None, default=True, help="TODO"):
  ''' add the switches --arg and --no-arg that set parser.arg to true/false, respectively'''
  group = parser.add_mutually_exclusive_group()
  dest = arg if dest is None else dest
  group.add_argument('--%s' % arg, dest=dest, action='store_true', default=default, help=help)
  group.add_argument('--no-%s' % arg, dest=dest, action='store_false', default=default, help="See --%s" % arg)



class LimerickDetector:

    def __init__(self):
        """
        Initializes the object to have a pronunciation dictionary available
        """
        self._pronunciations = nltk.corpus.cmudict.dict()


    def num_syllables(self, word):
        """
        Returns the number of syllables in a word.  If there's more than one
        pronunciation, take the shorter one.  If there is no entry in the
        dictionary, return 1.
        """

        # TODO: provide an implementation!
        my_word = []
        if word in self._pronunciations.keys():
            my_word = self._pronunciations[word]
        else:
            return 1
        if len(my_word) > 0:
            my_word.sort(key=len)
        else:
            return 1
        count = 0
        small_word = my_word[0]
        if type(small_word) is list:
            for j in small_word:
                if any(char.isdigit() for char in j):
                    count += 1
        return count

    def guess_syllables(self,word):
        vowels = ['a','e','i','o','u','y']
        num_of_vowels = 0
        prev_letter_vowel = False
        for i in word:
            if i in vowels:
                if not prev_letter_vowel:
                    num_of_vowels += 1
                prev_letter_vowel = True
            else:
                prev_letter_vowel = False
        if len(word) > 1 and word[-1:] == "e":
            if word[-3] in vowels:
                num_of_vowels -= 1
        return num_of_vowels

    def check_rhyme(self,list1, list2):
        i=len(list1)-1
        j=len(list2)-1
        while not i<0 and not j<0:
            if list1[i] != list2[j]:
                return False
            i-=1
            j-=1
        return True


    def rhymes(self, a, b):
        """
        Returns True if two words (represented as lower-case strings) rhyme,
        False otherwise.
        """
        # TODO: provide an implementation!
        a_pronun = self._pronunciations[a]
        b_pronun = self._pronunciations[b]
        for i in range(len(a_pronun)):
            con = 0
            for j in range(len(a_pronun[i])):
                if not any(char.isdigit() for char in a_pronun[i][j]):
                    con += 1
                else:
                    break
            a_pronun[i] = a_pronun[i][con:]
        for i in range(len(b_pronun)):
            con = 0
            for j in range(len(b_pronun[i])):
                if not any(char.isdigit() for char in b_pronun[i][j]):
                    con += 1
                else:
                    break
            b_pronun[i] = b_pronun[i][con:]
        result = False
        for i in a_pronun:
            for j in b_pronun:
                result = self.check_rhyme(i,j)
                if result == True:
                    return True
        return result

    def apostrophe_tokenize(self,text):
        tokens = word_tokenize(text)
        n=len(tokens)
        i=0
        while i<n-1:
            if '\'' in tokens[i+1] :
                tokens[i] = tokens[i] + tokens[i+1]
                tokens.remove(tokens[i+1])
                n=n-1
            i+=1
        return tokens

        pass


    def is_limerick(self, text):
        """
        Takes text where lines are separated by newline characters.  Returns
        True if the text is a limerick, False otherwise.

        A limerick is defined as a poem with the form AABBA, where the A lines
        rhyme with each other, the B lines rhyme with each other, and the A lines do not
        rhyme with the B lines.


        Additionally, the following syllable constraints should be observed:
          * No two A lines should differ in their number of syllables by more than two.
          * The B lines should differ in their number of syllables by no more than two.
          * Each of the B lines should have fewer syllables than each of the A lines.
          * No line should have fewer than 4 syllables

        (English professors may disagree with this definition, but that's what
        we're using here.)


        """
        # TODO: provide an implementation!
        sens = text.strip().split('\n')
        tokens=[]
        num_tokens=[]
        for i in sens:
            i = re.sub('[^a-zA-Z0-9 \']', '', i)
            i = re.sub(' +', ' ', i)
            line_tokens = word_tokenize(i)
            tokens.append(line_tokens)
            sum=0
            for j in line_tokens:
                sum += self.num_syllables(j)
            if(sum<4):
                return False
            num_tokens.append(sum)

        if len(tokens) != 5:
            return False
        if abs(num_tokens[0] - num_tokens[1])>2 or abs(num_tokens[0] - num_tokens[4])>2:
            return False
        if abs(num_tokens[2] - num_tokens[3])>2:
            return False
        if min(num_tokens[0],num_tokens[1],num_tokens[4]) < max(num_tokens[2],num_tokens[3]):
            return False

        if self.rhymes(tokens[0][-1],tokens[1][-1]):
            if self.rhymes(tokens[2][-1], tokens[3][-1]):
                if self.rhymes(tokens[0][-1], tokens[4][-1]):
                    return True
        return False


# The code below should not need to be modified
def main():
  parser = argparse.ArgumentParser(description="limerick detector. Given a file containing a poem, indicate whether that poem is a limerick or not",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  addonoffarg(parser, 'debug', help="debug mode", default=False)
  parser.add_argument("--infile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input file")
  parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="output file")




  try:
    args = parser.parse_args()
  except IOError as msg:
    parser.error(str(msg))

  infile = prepfile(args.infile, 'r')
  outfile = prepfile(args.outfile, 'w')

  ld = LimerickDetector()
  lines = ''.join(infile.readlines())
  outfile.write("{}\n-----------\n{}\n".format(lines.strip(), ld.is_limerick(lines)))

if __name__ == '__main__':
  main()
