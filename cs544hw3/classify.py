#!/usr/bin/env python
import gzip
from collections import defaultdict
from csv import DictReader, DictWriter

import itertools
import nltk
import codecs
import sys,re
from nltk.corpus import wordnet as wn, stopwords
from nltk.tokenize import TreebankWordTokenizer

kTOKENIZER = TreebankWordTokenizer()

def morphy_stem(word):
    """
    Simple stemmer
    """
    stem = wn.morphy(word)
    if stem:
        return stem.lower()
    else:
        return word.lower()

class FeatureExtractor:
    def __init__(self):
        """
        You may want to add code here
        """
        None

    # def remove_stopWords(self,text,d):
    #     # stopWords = set(stopwords.words('english'))
    #     # text = re.sub('[^a-zA-Z0-9 \n]', '', text)
    #     # words = nltk.word_tokenize(text)
    #     # wordsFiltered = []
    #     for ii in kTOKENIZER.tokenize(text):
    #         # if ii not in stopWords:
    #             d[morphy_stem(ii)] += 1
    #     # text = ' '.join(wordsFiltered)
    #     # print text
    #     return d
    #
    #
    # def bigram_word(self,text,d):
    #     bigrams = []
    #     for item in nltk.bigrams(text.split()):
    #         d[item] += 1
    #     # print bigramFeatureVector
    #     return d

    def features(self, text):
        d = defaultdict(int)
        stopWords = set(stopwords.words('english'))

        text = text.lower()
        # pronouns = ['she','he','they','there','it','but','has','then','with',"a","an","are","are","as","at","be","by","for","from","has","he","in","is","it","its","of","on","that","the"]
        words = kTOKENIZER.tokenize(text)
        bigrams = nltk.bigrams(words)
        trigrams = nltk.trigrams(words)
        lent_len = 0
        for ii in words:
            lent_len += len(ii)
            ii = re.sub('[^a-zA-Z0-9 \']', '', ii)
            if len(words[::-1])>2:
                d['rhyme'] = len(words[::-1])
            if len(words[0])>1 :
                d['lastword'] = len(words[0])
            if ii not in stopWords:
                # if ii not in pronouns:
                d[morphy_stem(ii)] += 1

        d['len'] = len(words)
        d['letlen'] = lent_len
        d['letavg'] = lent_len/len(words)

        # for jj in bigrams:
        #     d[jj] +=1
        for kk in trigrams:
            d[kk] += 1
        # print d
        return d
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

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--trainfile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input train file")
    parser.add_argument("--testfile", "-t", nargs='?', type=argparse.FileType('r'), default=None, help="input test file")
    parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="output file")
    parser.add_argument('--subsample', type=float, default=1.0,
                        help='subsample this fraction of total')
    args = parser.parse_args()
    trainfile = prepfile(args.trainfile, 'r')
    if args.testfile is not None:
        testfile = prepfile(args.testfile, 'r')
    else:
        testfile = None
    outfile = prepfile(args.outfile, 'w')

    # Create feature extractor (you may want to modify this)
    fe = FeatureExtractor()
    # trainfile = fe.remove_stopWords(trainfile)
    
    # Read in training data
    train = DictReader(trainfile, delimiter='\t')
    
    # Split off dev section
    dev_train = []
    dev_test = []
    full_train = []

    for ii in train:
        if args.subsample < 1.0 and int(ii['id']) % 100 > 100 * args.subsample:
            continue
        feat = fe.features(ii['text'])
        # feat = fe.remove_stopWords(ii['text'],feat)
        # feat = fe.bigram_word(ii['text'],feat)
        if int(ii['id']) % 5 == 0:
            dev_test.append((feat, ii['cat']))
        else:
            dev_train.append((feat, ii['cat']))
        full_train.append((feat, ii['cat']))

    # Train a classifier
    sys.stderr.write("Training classifier ...\n")
    print
    classifier = nltk.classify.NaiveBayesClassifier.train(dev_train)

    right = 0
    total = len(dev_test)
    for ii in dev_test:
        prediction = classifier.classify(ii[0])
        if prediction == ii[1]:
            right += 1
    sys.stderr.write("Accuracy on dev: %f\n" % (float(right) / float(total)))

    if testfile is None:
        sys.stderr.write("No test file passed; stopping.\n")
    else:
        # Retrain on all data
        classifier = nltk.classify.NaiveBayesClassifier.train(dev_train + dev_test)

        # Read in test section
        test = {}
        for ii in DictReader(testfile, delimiter='\t'):
            test[ii['id']] = classifier.classify(fe.features(ii['text']))

        # Write predictions
        o = DictWriter(outfile, ['id', 'pred'])
        o.writeheader()
        for ii in sorted(test):
            o.writerow({'id': ii, 'pred': test[ii]})
