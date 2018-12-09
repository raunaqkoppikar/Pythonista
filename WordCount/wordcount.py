import sys
import re
filename = sys.argv[1]
most_popular = open('most_popular.txt', 'w+')
alphabetical_order = open('alphabetical.txt', 'w+')
with open(filename) as fr:
    content = fr.read()
words = re.findall(r'[a-zA-Z0-9\-\']+[\-\']*[a-zA-Z0-9]*', content)
word_dict = {}
for word in words:
	word = word.lower()
	if word in word_dict:
		word_dict[word] = word_dict[word] + 1
	else:
		word_dict[word] = 1
most_popular_list = sorted(word_dict.items(), key=lambda word_dict: word_dict[1], reverse = True)
for each in most_popular_list:
	most_popular.write(each[0] + ' ' + str(each[1]) + '\n')
alphabet = sorted(word_dict.items(), key=lambda word_dict: word_dict[0])
for each in alphabet:
	alphabetical_order.write(each[0] + ' ' + str(each[1]) + '\n')
alphabetical_order.close()
fr.close()