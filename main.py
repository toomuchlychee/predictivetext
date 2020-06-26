import re
import random


"""class to contain a word and its possible followers in a list
"""

class Word:


    def __init__(self, instance, **kwargs):             # initialize the word
        self.instance = instance                        # instance is the referenced word
        self.trees = []                                 # trees are the possible words_raw that can come after it
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

#  set up objects in Word_Container

read_doc = open('document.txt', 'r')
long_string = read_doc.read()
spaces = find_whitespace(long_string)
# print(spaces)
words_raw = [first_word := long_string[:spaces[0]]]
# creating the words_raw list of strings
for n in range(1, len(spaces)):
    words_raw.append(long_string[spaces[n-1]:spaces[n]])
words_raw.append(last_word := long_string[spaces[-1]:])
words_stripped = []
for w in words_raw:
    words_stripped.append(w.lstrip())
word_container = WordContainer.create(words_stripped)
# print(word_container)

#  create the list of string outputs

output_list = []
# add the 1st word of words_stripped to output_list
output_list.append(words_stripped[0])
for n in range(len(words_stripped)-1):
    if word_container[output_list[n]].trees:
        output_list.append(random.choice(word_container[output_list[n]].trees))
# print(output_list)
output_string = ''
for s in output_list:
    output_string += ' '
    output_string += s
print(output_string)





