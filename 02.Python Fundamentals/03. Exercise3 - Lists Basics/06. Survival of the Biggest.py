# list_of_integers = list(input().split())
# n = int(input())
# for i in range(len(list_of_integers)):
#     list_of_integers[i] = int(list_of_integers[i])
#
# for i in range(n):
#     sorted_list = list_of_integers.copy()
#     sorted_list.sort()
#     list_of_integers.remove(sorted_list[0])
#
# print(list_of_integers)


list_of_integers = list(input().split())
n = int(input())

for i in range(len(list_of_integers)):
    list_of_integers[i] = int(list_of_integers[i])

sorted_list = list_of_integers.copy()
sorted_list.sort()

for i in range(n):
    list_of_integers.remove((sorted_list[i]))

print(list_of_integers)

# И ДВАТА ВАРИАНТА РАБОТЯТ
