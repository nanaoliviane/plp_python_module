#prompting user for input
name = input("Enter your name: ")
age = input("Enter your age: ")
location = input("Enter your location: ")

#printing personalized message
#print("Hello[name],you are[age]years old and live in[location].")
print("Hello {}, you are {} years old and live in {}.".format(name, age, location))