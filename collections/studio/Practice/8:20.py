# print (5 == 5)
# print ('abc' == 'def')
# other_num = 5
# print("hello" == other_num -3)
# text = "Don't Panic"
# if len(text) >= 10:
#     print(text, "has more than 10 characters")
# name = input('Please enter a username: ')
# if len(name) >= 8:
#     print("Welcome, " + name + "!")
# else: 
#     print("Invalid username.")
# name = input('Please enter a useraname: ')
# if len(name) > 5:
#     print("Welcome, " + name + "!")
# else:
#     print("Invalid username.")
# name = input('Please enter a username:')
# if len(name) > 5 and len(name) < 10:
#     print("Welcome, " + name + "!")
# print(not True)
# print(not False)
# num = 5 
# print(num > 0 and num < 10) 
# print(7 > num and num == 3)
# print(num*5 >100 and 'dog' == 'cat')
# print(not(num < 7))
# print(not('dog' == 'cat'))
# print(not(num*5 > 100 or 'dog' == 'cat'))
# num = 5
# python = 'Awesome!'

# print(num > 0 and num < 10 and 'dog' == 'cat')
# print(num > 7 or num == 3 or 'dog' == 'cat' or python == 'Awesome!')
# entry = int(input('Enter a whole number:'))
# if entry%2 == 0:
#     print("Even!")

#     if entry > 0:
#         print("Positive")
# word = input('Please enter a word that is longer than 4 characters:')

# if len(word) == 4:
#     print("We need you to think of a word that is longer than 4 characters")
# else: 
#     if len(word) < 4:
#         print("You can think of a longer word than that!")
#     else:
#         print("Excellent Word!")
# for num in range(51):
#     print(num)

# print("Not in the loop!")
# for num in range(4):
#     print(num)
#     print("Hello"* num)

# print("Done!")
num = 13

for number in range(13):
    if number%3 == 0:
        print(number)
        print("Number is divisable by 3")
    else:
        print(number)
        print("Number is not divisable by 3")