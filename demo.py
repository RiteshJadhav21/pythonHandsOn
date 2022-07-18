# str = " ritesh"
#
#
# print(str)
# print(len(str))
# print(str[0])
# print(str [2:6])
# print(str [2:])
# print(str * 2)
# print(str +" jadhav")
# print(str + str )

#list
# player_list = ["John", 25, 6.1]
# tiny_list = ["John", 25]

# print (player_list)
# print (player_list[0])
# print (player_list[1:3])
# print (player_list[2:])
# print (tiny_list * 2)
# print (player_list + tiny_list)

#tuples #tuples are immutables
#
# player_tuple = ("John", 25, 6.1)
# tiny_tuple = ("John", 25)
#can't change the values
# print (player_tuple)           # Prints complete tuple
# print (player_tuple[0])        # Prints first element of the tuple
# print (player_tuple[1:3])      # Prints elements starting from 2nd till 3rd
# print (player_tuple[2:])       # Prints elements starting from 3rd element
# print (tiny_tuple * 2)   # Prints tuple two times
# print (player_tuple + tiny_tuple)

# Dictionaries { key : value }

# player_dict = {"name" : "John",
#                "age" : 25,
#                "height" : 6.1}
#
# player_age = player_dict["age"]
#
# player_dict["game"] = "basket ball"
#
# print(player_dict)
# print(player_age)
# print(player_dict["game"])

# if else elif
# num=1000
# if num > 1000:
#  print("num is greater than 1000")
# else :
#     print("not greater tha 1000")
#
# if num > 1000:
#  print("num is greater than 1000")
# elif num<1000 :
#     print("less than")
# else:
#     print("equal")


# while

# num = int(input("Enter a number:"))
# while num > 0 :
#  print(num)
#  num -= 1

# for loop
#
# numbers = [11,33,55,38,55,75,37,21,23,41,13]
# for number in numbers:
#  if number%2 == 0:
#     print(f"The given list contains an even number {number}")
#
#     break
#  else:
#     print("The given list does not contain an even number")

# continue
# numbers = [11,33,55,39,55,28,75,37,21,16,23,41,90,13]
# even_list = []
# for number in numbers:
#  if number%2 != 0:
#   continue
#  even_list.append (number)
# print(even_list)


# pass

# numbers = [11,33,55,39,55,28,75,37,21,16,23,41,90,13]
# odd_list = []
# for number in numbers:
#  if number%2 != 0:
#   pass
#   odd_list.append (number)
#
#
# print(odd_list)


# functions
# def print_details(x, y):
#  print('Name is ', x)
#  print('Age is ', y)
#
# s=print_details('John',23)
#
# print(s)
#
# def new_fun():
#     s
#
# new_fun()


# lambda fun

# x = lambda a, b : a * b
#
#
# print(x(5, 6))


# v= lambda w,e,r : w+e+r
#
# print(v(4,5,6))

