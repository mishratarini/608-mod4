# Part 1 of Assignment 4

c = [1, 2, 3, 4, 5]

print("List of Integers - " + str(c))

print("First item in the list is " + str(c[0]))

print("Fifth item in the list is " + str(c[4]))

print("Number the Elements in the list is " + str(len(c)))

print("Last item in the list is " + str(c[-1]))

# print("Index is out of range for c[100] " + str(c[100]))

print("Sum of first 3 items in the list = " + str(c[0] + c[1] + c[2]))

c += [6, 7]
print("List after Append -- " + str(c))
c1 = [8, 9, 10]
print("Concatenate C + C1 " + str(c + c1))

colors = ['Red', 'Blue', 'Green', 'Pink', 'Violet']
print(f'List # : Colors')
for i in range(len(colors)):
    print(f'Item {i + 1} : {colors[i]}')

list1 = ['1', '2', '3']
list2 = ['1', '2', '3']
list3 = ['2', '3', '4', '5']

print(list1 == list2)
print(list1 < list3)
print(list3 >= list2)
print(list1 > list2)


def cube_list(values_of_list):
    for i in range(len(values_of_list)):
        values_of_list[i] **= 3
    return values_of_list


print("Print the cube for every item in the list - " + str(cube_list(c)))

rainbow_tuple = ('V', 'I', 'B', 'G', 'Y', 'O', 'R')
print("Number the Elements in the Rainbow Tuple is " + str(len(rainbow_tuple)))
print(f'List # : Colors')
for i in range(len(rainbow_tuple)):
    print(f'Item {i + 1} : {rainbow_tuple[i]}')

rainbow_tuple += ('A', 'B', 'C')
print("Number the Elements in the Rainbow Tuple is " + str(len(rainbow_tuple)))

student_tuple = ()
student_tuple = 'John', ['95', '88', '77']
print(str(student_tuple))
first_name, grades = student_tuple
print(str(first_name))
print(str(grades))

numbers = [19, 3, 15, 7, 11]
print(f'Index{"Value":>8}   Bar')
for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')

numbers_slice = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
print("Even numbers -- " + str(numbers_slice[1:len(numbers_slice):2]))
numbers_slice[5:10] = [0] * len(numbers_slice[5:10])
print("Numbers Slice after replacing 5:10 with 0" + str(numbers_slice))
numbers_slice[5:] = []
print("Numbers Slice first 5 elements -- " + str(numbers_slice))
numbers_slice[:] = []
print("Numbers Slice all elements deleted -- " + str(numbers_slice))

Freind_name = ['romeo', 'juliet']
print('Freinds name before replacement -- ' + str(Freind_name))
Freind_name[:1] = ['Python']
print('Freinds name -- ' + str(Freind_name))

numbers_del = list(range(0, 10))
print('numbers_del -- ' + str(numbers_del))
del numbers_del[0]
print('numbers_del after deletion -- ' + str(numbers_del))


def passlisttofunction(items_list):
    for i in range(len(items_list)):
        items_list[i] *= 2
    return items_list


numberslist = [10, 3, 7, 1, 9]
print('After passing a list to a function---' + str(passlisttofunction(numberslist)))

numbersforsorting = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
numbersforsorting.sort()
print('Sorted List---' + str(numbersforsorting))
numbersforsorting.sort(reverse=True)
print('Reverse Sorted List---' + str(numbersforsorting))
sorted(numbersforsorting)
print('Sorted List---' + str(sorted(numbersforsorting)))

foods = ['cookies', 'pizza', 'grapes', 'apples', 'steak', 'Beacon']
foods.sort()
print('Sorted Foods List---' + str(foods))

print('Index function -- ' + str(numbersforsorting.index(5, 4, 6)))
print(5 in numbersforsorting)
print(11 not in numbersforsorting)

list2 = [item for item in range(0, 16)]
print('List 2 is item for item in range(0, 1600) ' + str(list2))

print("list with filter and Lamda function" + str(list(filter(lambda x: x % 2 != 0, numbersforsorting))))
print("list with MAP amd Lambda function" + str(list(map(lambda x: x * 2, numbersforsorting))))

a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
for row in a:
    for item in row:
        print(str(item), end=' ')
    print()

for i , row in enumerate(a):
    for j,item in enumerate(row):
        print(f'a{i}{j} = {item} ', end = ' ')
    print()
