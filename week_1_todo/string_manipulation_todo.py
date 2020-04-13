"""
Personality questionnaire
"""

# TODO: ask a user to input their full name and test it by entering lower case letters for your name

# TODO: write a program that asks a user 6 unique questions about them and see if it works!
# TODO: use input functions however you would like (i.e. print question then get input, or include
# TODO: the question within the input variable.)

# TODO: print out the results in a neat format and make sure to capitalize the user's name with the
# TODO: title function

first_name = input("What is your first name?")
last_name = input("What is your last name?")
dog_cat = input("Do you prefer cats or dogs?")
School = input("What school do you attend?")
dream_job = input("What is your dream job?")
fav_place = input("What is your favorite place?")           
print("My name is", first_name.title(), last_name.title(), ". I prefer", dog_cat, "and I attend", School.upper(), ". My dream job is", dream_job,"and my favorite place is", fav_place)