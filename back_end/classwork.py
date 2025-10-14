# Create a simple class names pet 
class pet:
    # This should have features name, species, and age
    def __init__(self, name, species, age): 
        print('Creating a new pet profile')
        self.name = name
        self.species = species
        self.age = age
        print(f'I have a {species}, his name is {name} aged {age}') 
    
    
# Write a function to celebrate the pet's birthday
    def generate_dob(self): 
        from datetime import datetime
        return f'{datetime(2022, 8, 8).strftime('%m-%d-%Y')}'

bruno = pet('Bruno', 'Toy poodle', 3) # Include a function to display the class information

print(f'{bruno.name} was born on {bruno.generate_dob()}')







