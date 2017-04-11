# Define a dictionary that contains information about several members of your family. 

my_family = { # {0, 1{0, 1}}
    'younger sister': {
        'name': 'Shaunda',
        'age': 26
    },
    'mother': {
        'name': 'Julia',
        'age': 55
    },
    'eldest brother': {
        'name': 'Alex',
        'age': 30
    },
    'father': {
        'name': 'Keith',
        'age': 55
    },
    'youngest brother': {
        'name': 'Myron',
        'age': 25
    },
    'older brother': {
        'name': 'Byron',
        'age': 28
    }
}

# print("This is my family:", my_family)



# Using a dictionary comprehension, produce output that looks like the following example.
# my_family[1].relationship[] is my [relationship] and is [relationship] years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

for (relationship, data) in my_family.items():
    print("----------------")
    family = [data['name'] + " is my " + relationship + " and is " + str(data['age']) + "years old."]
    for members in family:
        print(relationship, data) # key, value pairs
        print(members)