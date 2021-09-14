# Create a dictionary

country_codes = {'finland': 'fi', 'south africa': 'sa', 'nepal': 'np'}
print('Dictionary Country_Codes -- ' + str(country_codes))
print('length of the dictionary - ' + str(len(country_codes)))

country_codes.clear()

if country_codes:
    print('Country_codes not empty')
else:
    print('Country Codes is empty')

days_per_month = {'January': 31, 'Februrary': 28, 'March': 31}
for months, days in days_per_month.items():
    print(f'{months} has {days} days')

print('Value of January in days_per_month - ' + str(days_per_month['January']))
days_per_month['Februrary'] = 29
print('days_per_month in leap year - ' + str(days_per_month))
del days_per_month['Februrary']
print('days_per_month after deletion - ' + str(days_per_month))
print('days_per_month after pop() - ' + str(days_per_month["January"]))

month = {'January': 1, 'Februrary': 2, 'March': 3}
for i in month.keys():
    print(str(i), end=' ')

for j in month.values():
    print(str(j), end=' ')

print('\n Month Keys List   ' + str(list(month.keys())))
print('Month Values List ' + str(list(month.values())))
print('Month  List ' + str(list(month.items())))
print('Month  Sorted List ' + str(sorted(month.items())))

country_codes_copy = {'finland': 'fi', 'south africa': 'sa', 'INDIA': 'IN'}

print(country_codes_copy == country_codes)
print(country_codes_copy != country_codes)

# Most common words in a text

test = 'this is a sample text with several words ! This is more sample text with some different words'
word_counts = {}

for word in test.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(f'{"WORDS:<12"}COUNTS')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('Number of Unique words in test ' + str(len(word_counts)))

from collections import Counter

counter = Counter(test.split())
for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')

print('Number of Unique words in test ' + str(len(counter)))

test = 'To be or not to be ime after time · Heart to heart · Boys will be boys · Hand in hand · Get ready; get set; ' \
       'go · Hour to hour '
word_counts = {}

for word in test.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(f'{"WORDS:<12"}COUNTS')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('Number of Unique words in test ' + str(len(word_counts)))

from collections import Counter

counter = Counter(test.split())
for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')

print('Number of Unique words in test ' + str(len(counter)))

# Sets

colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}

print('Set Colors are - ' + str(colors))
print('Length of Set Colors are - ' + str(len(colors)))

print('red' in colors)
print('pink' in colors)

for color in colors:
    print(color.upper(), end=' ')

set_numbers = list(range(10)) + list(range(5))
print('set_numbers -- ' + str(set_numbers))
print('set_numbers -- ' + str(set(set_numbers)))
