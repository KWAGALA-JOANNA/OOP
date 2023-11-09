# values = { 4:4, 8:8, "Q":10, "ACE":11 }
# card = ("Q", "Hearts")
# print(f"{values[card[0]]}")

# creating and instantiating classes
# creating my first class
class car():
    pass #simply using as a placeholder until we add more code tomorrow
# OR a no-operation statement the pass allows your code to run 
# without python throwing an error

# instantiating an object from a class
class car(): # the parenthesis are optional for this case
    pass
ford = car() # creates an instance of the Car class and stores into the variable ford
print(ford)
# output
# “<__main__.Car object at 0x0332DB>”. This is describing the 
# class that the instance was built from “Car,” and the 
# location in memory that the class itself is stored “0x0332DB.” 
# creating multiple instances
fortuner = car()
Jeep = car()
Mercedees = car()
vogue = car()
print(hash(Jeep))
print(hash(fortuner))
print(hash(Mercedees))
print(hash(vogue))
# hash outputs a numerical representation of the location in memory for the variable

