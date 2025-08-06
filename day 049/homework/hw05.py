people = [
    {"name": "barbare", "age": 25},
    {"name": "meore barbare", "age": 17},
    {"name": "mesame barbare", "age": 30},
    {"name": "meotxe barbare", "age": 16}
]

for person in people:
    if person["age"] > 18:
        print(person)