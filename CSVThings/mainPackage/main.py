# main.py
# Name: Brianna Jarrell
# email: jarrelbc@mail.uc.edu
# Assignment Number: 
# Due Date: 2-13-24
# Course/Section: IS 4010 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Learning how to use CSV files
# Citations: 
# Anything else that's relevant:

from utilsPackage.utils import *

# Call the function and store what it returns 
#  in a variable called data

if __name__ == "__main__":
    data = read_CSV_file()
    print("# of rows in dataset:", len(data))
    # print the first and last rows in data
    print(data[0])
    print(data[-1])
    
    #I want a list comprehension expression 
    #Pull out all of the collision types into a set
    #Modify the previous expression to exclude the blank expression 
    collisionTypes = {myData[6] for myData in data} # grabs 6 column in row to make a set
    print(collisionTypes)
    print("# of collision types:", len(collisionTypes))
    
    