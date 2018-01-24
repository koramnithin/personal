from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """

    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.add_state('next')
    f1.add_state('1')
    f1.add_state('2')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.initial_state = 'start'

    # Set all the final states
    f1.set_final('next')
    f1.set_final('1')
    f1.set_final('2')
    f1.set_final('3')
    f1.set_final('4')
    f1.set_final('5')
    f1.set_final('6')

    dict1 = {
        '1':['b','f','p','v'],
        '2':['c','g','j','k','q','s','x','z'],
        '3':['d','t'],
        '4':['l'],
        '5':['m','n'],
        '6':['r']
    }

    # Add the rest of the arcs
    for letter in string.ascii_lowercase:
        if letter not in 'aehiouwy':
            for i in dict1.keys():
                if letter in dict1[i]:
                    f1.add_arc('start', i, (letter), (letter))
                    f1.add_arc('next', i, (letter), (i))
                    f1.add_arc(i, i, (letter), ())
                    for x in '123456':
                        if i != x:
                            f1.add_arc(x, i, (letter), (i))
                    break
        else:
            f1.add_arc('start', 'next', (letter), (letter))
            f1.add_arc('next', 'next', (letter), ())
            for x in '123456':
                f1.add_arc(x, 'next', (letter), ())
    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    f2.add_state('5')
    f2.initial_state = '1'
    f2.set_final('1')
    f2.set_final('2')
    f2.set_final('3')
    f2.set_final('4')
    f2.set_final('5')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '2', (letter), (letter))

    for n in range(10):
        f2.add_arc('1', '3', (str(n)), (str(n)))
        f2.add_arc('2', '3', (str(n)), (str(n)))
        f2.add_arc('3', '4', (str(n)), (str(n)))
        f2.add_arc('4', '5', (str(n)), (str(n)))
        f2.add_arc('5', '5', (str(n)), ())
    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('n')
    f3.add_state('na')
    f3.add_state('nb')
    f3.add_state('1a')
    f3.add_state('1b')
    f3.add_state('2')
    
    f3.initial_state = '1'
    f3.set_final('2')

    for letter in string.letters:
        f3.add_arc('1', 'n', (letter), (letter))
    for number in xrange(10):
        f3.add_arc('1', '1a', (str(number)), (str(number)))
        f3.add_arc('n', 'na', (str(number)), (str(number)))
        f3.add_arc('n', '1a', (), ('0'))
        f3.add_arc('na', 'nb', (str(number)), (str(number)))
        f3.add_arc('na', '1b', (), ('0'))
        f3.add_arc('nb', '2', (str(number)), (str(number)))
        f3.add_arc('nb', '2', (), ('0'))

    f3.add_arc('1', '1a', (), ('0'))
    f3.add_arc('1a', '1b', (), ('0'))
    f3.add_arc('1b', '2', (), ('0'))
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))
