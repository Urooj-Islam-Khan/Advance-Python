# for printing single line use "" or ''
print("Hello World")

# for printing multiple line use """ """ 
recepe = """
1. Heat the pan and add oil
2. Crack the egg
3. Add salt in egg and mix well
4. Pour the mixture in pan
5. Fry on medium heat
"""
print(recepe)

# creating a variable of datatype String.
my_message = "Hello from Urooj"
print(my_message)

# for finding length of string.
print(len(my_message))

# index() : The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
# finding letter on a given index.
print(my_message[4])

# strip() : The strip() method removes any white spaces before and after the string.
rollnum = ' 2k22/SWE/123 '
print('before strip '+rollnum)
print('after strip '+rollnum.strip())

# rstrip() : the rstrip() removes any trailing characters.
str = "Hy !!!"
print(str.rstrip('!'))

# slicing in string
print(my_message[0:5]) #in this it include letter at index 0(starting point) but 5 is stopping point so letter at index 5(ending point) is not included.

print(my_message[:5]) # this also print Hello as the above one.

print(my_message[6:]) # it will print from the index 6.

# to print lowercase letter.
print(my_message.lower())

# to print uppercase letter.
print(my_message.upper())

# count() : The count() method returns the number of times the given value has occurred within the given string.
# to count anything from string.
print(my_message.count('o'))

# find() : The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
# to find a word or letter
print(my_message.find('Urooj'))

# replace() : the replace() method replaces a string with another string.
# replace word direct in print statement.
print(my_message.replace('Urooj','Sassi'))

# replace word in a string by making variable.
pet_name = my_message.replace('Urooj','Sassi')
print(pet_name)

# split() : The split() method splits the give string at the specified instance and returns the separated strings as list items.
print(my_message.split())

# capitalize() : The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
str2 = 'i am urooj'
print(str2.capitalize())

# concatenate two Strings.
name = 'Urooj'
cast = 'Khan'
print(name + " " + cast)

love  = "Urooj is Love"

# one more way to concatenate string.
# The format() methods places the arguments within the string wherever the placeholders are specified.
myname = "I'm {} {}, Welcome!".format(name, cast)
print(myname)

# center() : The center() method aligns the string to the center as per the parameters given by the user.
print(name.center(100))

# We can also provide padding character. It will fill the rest of the fill characters provided by the user.
str1 = "Welcome to the Urooj's World!!!"
print(str1.center(50, "."))

# endswith() : The endswith() method checks if the string ends with a given value. If yes then return True, else return False. 
print(str1.endswith('~'))
print(str1.endswith('World!!!'))


# using fstring.
greeting = 'Hello'
message = f"{greeting}, I'm {name}"
print(message)

# dir() it gives all method of strings.
print(dir(name))

#to take all info about string function use help().
print(help(str))

#if we forget the purpose of any function use.
print(help(str.lower))