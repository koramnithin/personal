#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
###Provide your answer below

###Answer examples
print distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['hello'],set(['hello']),distsim.cossim_dense)
print distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['handsome'],set(['handsome']),distsim.cossim_dense)
print distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['india'],set(['india']),distsim.cossim_dense)
print distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['dog'],set(['dog']),distsim.cossim_dense)
print distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['pretty'],set(['pretty']),distsim.cossim_dense)
print distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['walk'],set(['walk']),distsim.cossim_dense)
