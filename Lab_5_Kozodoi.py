#1
# hat_list = [1, 2, 3, 4, 5]
#
# print("Заменіть число у списку \nВведіть порядковий номер числа: ")
# n=int(input())-1
# print("Ведіть число на яке хочете замінити: ")
# hat_list[n] = int(input())
#
# del hat_list[len(hat_list)-1]
#
# print("Lenght aftel del 1 el.: " + len(hat_list))
# print(hat_list)

#2
# my_list = [1, 7, 23, 34, 0]
# n = len(my_list)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if my_list[j] > my_list[j+1]:
#                 my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
#
# print(my_list)

#3
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# n = len(my_list)
# for i in range(n-1, -1, -1):
#     for j in range(i-1, -1, -1):
#         if my_list[i] == my_list[j]:
#             del my_list[i]
#             break
# print("The list with unique elements only:")
# print(my_list)

#4
chessboard = [['_'] * 8 for _ in range(8)]

chessboard[0][0] = 'T'
chessboard[0][7] = 'T'
chessboard[7][0] = 'T'
chessboard[7][7] = 'T'

for row in chessboard:
    print(' '.join(row))
