#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
king = word_to_vec_dict['king']
man = word_to_vec_dict['man']
woman = word_to_vec_dict['woman']
ret = distsim.show_nearest(word_to_vec_dict,
                           king-man+woman,
                           set(['king','man','woman']),
                           distsim.cossim_dense)
print("king : man :: {} : woman".format(ret[0][0]))
#
# king = word_to_vec_dict['cat']
# man = word_to_vec_dict['cats']
# woman = word_to_vec_dict['dogs']
# ret = distsim.show_nearest(word_to_vec_dict,
#                            king-man+woman,
#                            set(['cat','cats','dogs']),
#                            distsim.cossim_dense)
# print("cat : cats :: {} : dogs".format(ret[0][0]))
#
# king = word_to_vec_dict['invite']
# man = word_to_vec_dict['invitation']
# woman = word_to_vec_dict['decision']
# ret = distsim.show_nearest(word_to_vec_dict,
#                            king-man+woman,
#                            set(['confuse','confusion','decision']),
#                            distsim.cossim_dense)
# print("cat : cats :: {} : dogs".format(ret[0][0]))
#
# king = word_to_vec_dict['advice']
# man = word_to_vec_dict['advise']
# woman = word_to_vec_dict['choose']
# ret = distsim.show_nearest(word_to_vec_dict,
#                            king-man+woman,
#                            set(['advice','advise','choose']),
#                            distsim.cossim_dense)
# print("cat : cats :: {} : dogs".format(ret[0][0]))
