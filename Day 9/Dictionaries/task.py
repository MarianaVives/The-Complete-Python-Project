programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

print(colours["apple"])
print(programming_dictionary["Bug"])

my_empty_dictionary = {}

my_empty_dictionary["dog"]="Luna"
my_empty_dictionary["cat"]="Mandy"
my_empty_dictionary["turtle"]="Ted"

print(my_empty_dictionary) #{'dog': 'Luna', 'cat': 'Mandy', 'turtle': 'Ted'}
print(my_empty_dictionary["dog"]) #Luna

#Loop through a dictionary and print all keys
for key in colours:
    print(key)

#Loop through a dictionary and print all values
for value in colours:
    print(colours[value])