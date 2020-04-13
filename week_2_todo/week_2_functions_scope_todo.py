"""
Working with functions and scope
"""

# TODO: create a function that takes a dictionary as an argument and returns
# TODO: the iteration number, the key, and the value in a readable way
# TODO: (i.e. "iteration number 1 returns the key firstKey and the value firstValue")

# here is an example dictionary
EXAMPLE_DICTIONARY = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}

# TODO: place the function below
def dict(keys_value):
    print("Below is a Dictionary")
    for keys in keys_value:
        print(keys + " this is the key and " + keys_value[keys] + " this is a value.")

    print("Dictionary End")

dict(EXAMPLE_DICTIONARY)