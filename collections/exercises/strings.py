# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.
print(len(text))

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
new_string = text[24:36]
print(new_string)

# 3. Print a slice of the middle 12 characters from 'text'.
new_string = text[12:24]
print(new_string)

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
for num in range(len(word)):
    print(word[num])

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
for num in range (len(word) -1, -1, -1):
    print(word[num])

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
reversed_word = ""
for num in range (len(word) -1, -1, -1):
    reversed_word += word[num]
print(word + reversed_word)
