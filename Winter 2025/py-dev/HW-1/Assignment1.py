'''
COMP 3006
Homework 1 - Functional programming and OOP intro

General Homework Guidelines: 
- Homework must be submitted in a .py file. Please do not submit .ipynb files.
- Homework should not use packages or functions that have not yet been discussed in class.
- Use comments to explain what your code is doing. 
- Use a consistent coding style. 
- Use descriptive variable names.
- Test your code regularly using a variety of different inputs. 
- Every function must include a docstring for documentation (see: 
   https://realpython.com/documenting-python-code/). This docstring should include:
     - 1 or 2 lines describing what the function does
     - Args: input parameters, their types and what they are for
     - Returns: return data type and what it is
- All tests of your functions should be commented out in your final submission or
  encolosed with an if __name__=='__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.
'''


# Question 1:
# Write a function called paired_list that takes in two non-empty lists : a list of strings and 
# a list of integers. The function must combine the lists to form a single list and return it. 
# The lists do not need to be the same length. If the lists are the same length, then the values 
# should be paired up using a value from each list to form a tuple, i.e. ['Matt', 'Alice'] and 
# [99, 50] should result in the list [('Matt',99), ('Alice',50)].
# If the lists are not the same length, you should still pair up the values from each list but 
# you'll need to handle two cases:
#   -if the list containing strings is longer, you should use the placeholder value 'FNU' which stands
# for "first name unknown". Fro example for the lists ['Matt', 'Alice'] and [99, 50, 25] should result 
# in the list [('Matt',99), ('Alice',50), ('FNU', 25)].
#   -if the list containing integers is longer, you should use the average value of the integer list 
# as the value you pair up with the extra strings, i.e. for ['Matt', 'Alice', 'Tom', 'Jake'] and 
# [99, 50, 25] should result in the list [('Matt',99), ('Alice',50), ('Tom',25), ('Jake', 58)]. The
# last value 58 is (99+50+25)//3. Please note that "//" is integer division, so the result is rounded down.
# You can use a helper function to calculate the average value of the integers list.
# Note: you may find the itertools module helpful.




# Qeustion 2:
# Write a function called even_odd_pairs which takes a list of tuples (the output of paired_list function)
# and a boolean value, which should have a default value of True. If the boolean value is True, the function
# should filter the list of tuples and return a list containing only the tuples that have an even interger.
# For example if given [('Matt',99), ('Alice',50), ('FNU', 25)] and True, then the function should return
# [('Alice',50)].
# If the boolean value is False, the function should filter the list of tuples and return a list containing 
# only the tuples that have an odd interger. For example if given [('Matt',99), ('Alice',50), ('FNU', 25)] 
# and True, then the function should return [('Matt',99), ('FNU', 25)].





### ----------------------------------------------------------------------------------------- ###
### We wish to compare and store data on various types of shelters for when we go backpacking ###
### ----------------------------------------------------------------------------------------- ###

#Question 3:
# Create a class, called Tent, that contains the following attributes (in the order given):
# num_occupants (int)
# material (str)
# setup_time (int, number of minutes)
# sqft (float)
# vestibule (bool, True if tent has a vestibule)
# weight (ounces, float)
# structure_poles (bool, True if tent has structural poles. Should have a default value of True)
# seasons (int, 3 or 4. Should have a default value of 3)

#The class should also have the following methods: 
# __str__, no particular format is required
# __repr__, no particular format is required
# __lt__ (this should use the num_occupants and sqft attributes to determine if one tent is 
# less than another tent, please note that both attributes must be less in order to return True)
# is_better (a tent is considered better if and only if its weight and setup_time is less than 
# another tent whilst having equal or better season rating, 4 is better than 3. Again, both 
# attributes must be less)

#For example (__lt__ and is_better works similar for questions 4 and 5):
# tent1=Tent(num_occupants=4, material="polyester", setup_time=6, sqft=36, vestibule=False
# weight=12.5, structure_poles=True, seasons=3

# tent2=Tent(num_occupants=4, material="polyester", setup_time=5, sqft=35, vestibule=False
# weight=11.5, structure_poles=True, seasons=3

# tent3=Tent(num_occupants=3, material="polyester", setup_time=4, sqft=35, vestibule=False
# weight=11.0, structure_poles=True, seasons=4

# tent1 < tent2 --> False (num_occupant is equal, not less)
# tent1 < tent3 --> False (num_occupant and sqft are greater)
# tent3 < tent1 --> True (num_occupant and sqft are less)
# tent3 < tent2 --> False (num_occupant is less but sqft is the same)

# tent2.is_better(tent1) --> True (weight and setup_time for tent2 are less whilst maintaining 
# the same season rating)
# tent3.is_better(tent1) --> True (weight and setup_time for tent2 are less and the season 
# rating is better)
# tent1.is_better(tent2) --> False (heavier and longer setup_time)


#Question 4:
# We wish to compare and store data on various types of shelters for when we go backpacking.
# Create a class, called Hammock, that contains the following attributes (in the order given):
# num_occupants (int)
# material (str)
# setup_time (int, number of minutes)
# weight (ounces, float)
# length (int, length of hammock in feet. Should have a default value of 11)
# seasons (int, 3 or 4. Should have a default value of 3)

#The class should also have the following methods:
# __str__
# __repr__
# __lt__ (this should use the weight and setup_time attributes to determine if one hammock is 
# less than another hammock, please note that both attributes must be less in order to return True)
# is_better (a hammock is considered better if and only if its weight and setup_time is less than 
# another hammock whilst having equal or better season rating, 4 is better than 3)



#Question 5:
# Create a class, called Tarp, that contains the following attributes (in the order given):
# num_occupants (int)
# material (str)
# setup_time (int, number of minutes)
# sqft (float)
# weight (ounces, float)
# seasons (int, 3 or 4. Should have a default value of 3)

#The class should also have the following methods: 
# __str__, no particular format is required
# __repr__, no particular format is required
# __lt__ (this should use the num_occupants and sqft attributes to determine if one tarp is 
# less than another tarp, please note that both attributes must be less in order to return True)
# is_better (a tarp is considered better if and only if its weight and setup_time is less than 
# another tarp whilst having equal or better season rating, 4 is better than 3)



#Question 6 (optional):
# There is lots of repeated code above, let's create a parent class for Tent, Hammock and Tarp 
# called Shelter. The Shelter class should have:
# -a constructor that takes over all of the attributes that are common for Tent, Hammock and Tarp 
# -is_better method should be moved to the parent class from the Hammock, Tent and Tarp classes 
# since it uses weight, setup_time and season rating in the respective classes.
# -total_sleep_spots which will add up the total number of sleeping spots available from a 
# non-determined number of Shelters being passed into the method.
# -__str__ and __repr__ methods must also be defined inside of Shelter, no particular format is required
# -last but not least, the __lt__ method must be rewritten in the child classes, Hammock, Tent and 
# Tarp, to handle only the cases of comparing two objects of the same subclass (Hammock/Hammock, 
# Tent/Tent, Tarp/Tarp) using the same attributes used for the respective class in questions 3 thru 5. 
# If you are trying to compare two objects of different subclasses of Shelter, the Shelter class must 
# handle those comparisons using the num_occupants, weight and setup_time.

# Rewrite the Tent, Hammock and Tarp classes taking into account the changes brought on by using
# the Shelter parent class. Changes will be needed to the constructor, __lt__ and the removal of
# the method is_better.


















