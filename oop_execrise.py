# A user class with properties ie name, age, location
class user:
    name = "Victor"
    age = 21
    location = 'Kasangati'
user_info =user() # the new insatnce(object)
print(user_info.name)
print(user_info.age)

# create a function for the user class that prints a user's location
# using the _init_ function to print the user's location

class user:
    def __init__(user001, location):
        user001.location = location 
        # sets the property location the value passed in
user_info = user("Kasangati")
print(user_info.location)