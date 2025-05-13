# Given the following nested dictionary, write code to 
# calculate the total age of all male family members:

family = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'}
}

def total_age(input_dict):
    total = 0
    
    for name in input_dict:
        if input_dict[name]['gender'] == 'male':
            total += input_dict[name].get('age', 0)
    
    return total

print(total_age(family))

# revised solution:

# def total_age(input_dict):
#     total = 0
    
#     for name, person in input_dict.items():
#         if person.get('gender') == 'male':
#             total += person.get('age', 0)
    
#     return total