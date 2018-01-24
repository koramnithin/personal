from french_count import french_count, prepare_input

if __name__ == '__main__':
    french = french_count()
    for i in range(1000):
        print " ".join(french.transduce(prepare_input(i)))