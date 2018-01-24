#!/usr/bin/env python
import distsim

# you may have to replace this line if it is too slow 
word_to_ccdict = distsim.load_contexts("nytcounts.4k")


### provide your answer below

###Answer examples
print distsim.show_nearest(word_to_ccdict, word_to_ccdict['hello'],set(['hello']),distsim.cossim_sparse)
print distsim.show_nearest(word_to_ccdict, word_to_ccdict['handsome'],set(['handsome']),distsim.cossim_sparse)
print distsim.show_nearest(word_to_ccdict, word_to_ccdict['india'],set(['india']),distsim.cossim_sparse)
print distsim.show_nearest(word_to_ccdict, word_to_ccdict['dog'],set(['dog']),distsim.cossim_sparse)
print distsim.show_nearest(word_to_ccdict, word_to_ccdict['pretty'],set(['pretty']),distsim.cossim_sparse)
print distsim.show_nearest(word_to_ccdict, word_to_ccdict['walk'],set(['walk']),distsim.cossim_sparse)
