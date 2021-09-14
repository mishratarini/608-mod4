# how to read a text file in python

from collections import Counter

file = open("readthisfile.txt")
data = file.read()

counter = Counter(data.split())
print(f'{"WORDS": <12}COUNTS')
for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')

print('Number of Unique words in test ' + str(len(counter)))



