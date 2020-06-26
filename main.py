import re
import random
from itertools import count


"""class to contain a word and its possible followers in a list
"""

class Word:


    def __init__(self, instance, **kwargs):             # initialize the word
        self.instance = instance                        # instance is the referenced word
        self.trees = []                                 # trees are the possible words that can come after it
        if 'follower' in kwargs:                        # adds the following word to trees
            self.trees.append(kwargs['follower'])
        if 'punctuation' in kwargs:
            self.trees.append(kwargs['punctuation'])


class WordContainer(dict):
    def added_ws(self):
        return list(self.keys())

    @classmethod
    def create(cls, e_list):
        returned_dict = cls()

        for w, n in zip(e_list, e_list[1:]):
            if w not in returned_dict.added_ws():
                returned_dict.update({w: Word(w, follower=n)})
            else:  # w in cls.added_list
                returned_dict[w].trees.append(n)
        return returned_dict






def find_whitespace(text):
    _list = [m.start(0) for m in re.finditer(r'\s', text)]
    return _list


"""main"""

#  set up objects Words in Word_Container

read_doc = open('document.txt', 'r')
long_string = read_doc.read()
spaces = find_whitespace(long_string)
# print(spaces)
WORDS = [first_word := long_string[:spaces[0]]]
# creating the WORDS list of strings
for n in range(1, len(spaces)):
    WORDS.append(long_string[spaces[n-1]:spaces[n]])
WORDS.append(last_word := long_string[spaces[-1]:])
for w in WORDS:
    w = w.lstrip()  # removes whitespace
word_container = WordContainer.create(WORDS)
# print(word_container)

#  create the list of string outputs

output_list = []
print(word_container[WORDS[0]].trees)





