inputStr = input("enter the name")
inputStr = inputStr.casefold() # convert all in lower case
print(inputStr)

vowels= "aeiou"

myList=[]

# for char in inputStr:
#     if char in vowels:
#         myList.append(char)
#
#
# print(myList)



# numVowel = [vow for vow in inputStr if vow in vowels]
#
# print(len(numVowel))
# print(numVowel)


# numCount ={}.fromkeys(vowels,0)
#
# print(numCount)
#
# for char1 in inputStr:
#     if char1 in vowels:
#         numCount[char1] += 1
#
# print(numCount)

def my_function(fname):
  print(fname )

my_function("Emil")
