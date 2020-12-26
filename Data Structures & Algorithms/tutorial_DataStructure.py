import sys
import math
import random
import threading
import time
from functools import reduce

def printName():
    # Accept user input and store it in a variable
    name = input("What is your name ")
    print("Hi ", name)

# If you want to extend a statement to multiple lines you can use parentheses or \
def printMultiLine():
    v1 = (
        1 + 2
        + 3
    )
    print("v1 = ", v1)
    v2 = 1 + 2 \
           + 3
    print("v2 = ", v2)
    # put multiple statements on 1 line using ;
    v3 = 5; v3 = v3 - 1
    print("v3 = ", v3)

# ----Variables-----
# Variables are names assigned to values. the 1st character must be _ or a letter
# then you can use letters, numbers or _
# variables names are type sensitive
def Variable():
    v2 = 1
    V2 = 2 # v2 is different from V2, case sensitive
    v3 = v4 = 20 # you can assign multiple variables with same number
    print("v2 + V2 + v3 + v4 = ", v2 + V2 + v3 + v4)

# --- DATA TYPES -----
# Data in Python is dynamically typed and that data type can change. All data is an object which I cover later
# The basic types are integers, floats, complex numbers, strings, booleans
# Python doesn't have a character type

def DataTypes():
    # How to get the type
    print(type(10))

    # There is no limit to the size of integers. This is a way to get a practical max size.
    print(sys.maxsize)

    # Floats are values with decimal values. This is how to get a max float
    print(sys.float_info.max)

    # But, they are accurate to 15 digits
    f1 = 1.1111111111111111
    f2 = 1.1111111111111111
    f3 = f1 + f2
    print(f3)

    # Complex numbers are [real part] + [imaginary part]
    cn1 = 5 + 6j
    print(cn1)

    # Booleans are either True or False
    b1 = True
    b2 = False

    # Strings are surrounded by ' or "
    str1 = "Escape Sequences \' \t \" \\ and \n"
    str2 = '''Triple quoted strings can contain ' and " '''
    print(str1)
    print(str2)

    # you can cast to different types with int, float, str, chr
    print("Cast ", type(int(5.4)))  # to int
    print("Cast 2 ", type(str(5.4)))  # to string
    print("Cast 3 ", type(chr(97)))  # to string (no character type in python)
    print("Cast 4 ", type(ord('a')))  # convert individual character to int

    # you can define a separator for print
    print(12, 21, 1977, sep='/')  # DOB

    # eliminate newline
    print("No newline", end='')

    # string formatting %e for exponent
    print("\n%04d %s %0.2f %c" %(1, "Jadav", 1.234, 'A'))


def Math():
    print("5 + 2 = ", 5 + 2)
    print("5 - 2 = ", 5 - 2)
    print("5 * 2 = ", 5 * 2)
    print("5 / 2 = ", 5 / 2)
    print("5 % 2 = ", 5 % 2)
    print("5 ** 2 = ", 5 ** 2)
    print("5 // 2 = ", 5 // 2)

    # shortcuts
    i1 = 2
    i1 += 1
    print("i1 ", i1)

    # Math functions
    print("abs(-1) ", abs(-1))
    print("max(5, 4) ", max(5, 4))
    print("min(5, 4) ", min(5, 4))
    print("pow(2, 2) ", pow(2, 2))
    print("ceil(4.5) ", math.ceil(4.5))
    print("floor(4.5) ", math.floor(4.5))
    print("round(4.5) ", round(4.5))
    print("exp(1) ", math.exp(1))  # e**x
    print("log(e) ", math.log(math.exp(1)))
    print("log(100) ", math.log(100, 10))  # Base 10 Log
    print("sqrt(100) ", math.sqrt(100))
    print("sin(0) ", math.sin(0))
    print("cos(0) ", math.cos(0))
    print("tan(0) ", math.tan(0))
    print("asin(0) ", math.asin(0))
    print("acos(0) ", math.acos(0))
    print("atan(0) ", math.atan(0))
    print("sinh(0) ", math.sinh(0))
    print("cosh(0) ", math.cosh(0))
    print("tanh(0) ", math.tanh(0))
    print("asinh(0) ", math.asinh(0))
    print("acosh(pi) ", math.acosh(math.pi))
    print("atanh(0) ", math.atanh(0))
    print("hypot(0) ", math.hypot(10, 10))  # sqrt(x*x + y*y)
    print("radians(0) ", math.radians(0))
    print("degrees(pi) ", math.degrees(math.pi))

    # Generate a random int
    print("Random", random.randint(1, 101))

    # inf is infinity
    print(math.inf > 0)

    # NaN is used to represent a number that can't be defined
    print(math.inf - math.inf)


def ConditionalOperator():
    # Comparison Operators : < > <= >= == !=

    # if, else & elif execute different code depending on conditions
    age = 30
    if age > 21:
        # Python uses indentation to define all the code that executes if the above is true
        print("You can drive a tractor trailer")
    elif age >= 16:
        print("You can drive a car")
    else:
        print("You can't drive")

    # Make more complex conditionals with logical operators
    # Logical Operators : and or not
    if age < 5:
        print("Stay Home")
    elif (age >= 5) and (age <= 6):
        print("Kindergarten")
    elif (age > 6) and (age <= 17):
        print("Grade %d", (age - 5))
    else:
        print("College")

    # Ternary operator in Python
    # condition_true if condition else condition_false
    canVote = True if age >= 18 else False
    print(canVote)

def String():
    # Raw strings ignore escape sequences
    print(r"I'll be ignored \n")

    # Combine strings with +
    print("Hello " + "You")

    # Get string length
    str3 = "Hello You"
    print("Length ", len(str3))

    # Character at index
    print("1st ", str3[0])

    # Last character
    print("Last ", str3[-1])

    # 1st 3 chrs
    print("1st 3 ", str3[0:3])  # Start, up to not including

    # Get every other character
    print("Every Other ", str3[0:-1:2])  # Last is a step

    # You can't change an index value like this
    # str3[0] = "a" because strings are immutable
    # (Can't Change)
    # You could do this
    str3 = str3.replace("Hello", "Goodbye")
    print(str3)

    # You could also slice front and back and replace what you want to change
    str3 = str3[:8] + "y" + str3[9:]
    print(str3)

    # Test if string in string
    print("you" in str3)

    # Test if not in
    print("you" not in str3)

    # Find first index for match or -1
    print("You Index ", str3.find("you"))

    # Trim white space from right and left
    # also lstrip and rstrip
    print("    Hello    ".strip())

    # Convert a list into a string and separate with spaces
    print(" ".join(["Some", "Words"]))

    # Convert string into a list with a defined separator or delimiter
    print("A, string".split(", "))

    # Formatted output with f-string
    int1 = int2 = 5
    #print(f'{int1} + {int2} = {int1 + int2}')

    # To lower and upper case
    print("A String".lower())
    print("A String".upper())

    # Is letter or number
    print("abc123".isalnum())

    # Is characters
    print("abc".isalpha())

    # Is numbers
    print("abc".isdigit())

def List():
    # Lists can contain mutable pieces of data of varying data types or even functions
    l1 = [1, 3.14, "Ram", True]

    # Get length
    print("Length ", len(l1))

    # Get value at index
    print("1st", l1[0])
    print("Last", l1[-1])

    # Change value
    l1[0] = 2

    # Change multiple values
    l1[2:4] = ["Bob", False]

    # Insert at index without deleting
    # Also l1.insert(2, "Paul")
    l1[2:2] = ["Paul", 9]

    # Add to end (Also l1.extend([5, 6]))
    l2 = l1 + ["Egg", 4]

    # Remove a value
    l2.remove("Paul")

    # Remove at index
    l2.pop(0)
    print("l2", l2)

    # Add to beginning (Also l1.append([5, 6]))
    l2 = ["Egg", 4] + l1

    # Multidimensional list
    l3 = [[1, 2], [3, 4]]
    print("[1, 1]", l3[1][1])

    # Does value exist
    print("1 Exists", (1 in l1))

    # Min & Max
    print("Min ", min([1, 2, 3]))
    print("Max ", max([1, 2, 3]))

    # Slice out parts
    print("1st 2", l1[0:2])
    print("Every Other ", l1[0:-1:2])
    print("Reverse ", l1[::-1])

# ----- LOOPS -----
def Loops():
    # While : Execute while condition is True
    w1 = 1
    while w1 < 5:
        print(w1)
        w1 += 1

    w2 = 0
    while w2 <= 20:
        if w2 % 2 == 0:  # even number
            print(w2)
        elif w2 == 9:
            # Forces the loop to end all together
            break
        else:
            # Shorthand for i = i + 1
            w2 += 1
            # Skips to the next iteration of the loop
            continue
        w2 += 1

    # Cycle through list
    l4 = [1, 3.14, "Ram", True]
    while len(l4):
        print(l4.pop(0))  # it deletes one element in each loop

    # For Loop
    # Allows you to perform an action a set number of times
    # Range performs the action 10 times 0 - 9
    # end="" eliminates newline
    for x in range(0, 10):  # kicks out values from 0 to 9
        print(x, ' ', end="")
    print('\n')

    # Cycle through list
    l4 = [1, 3.14, "Ram", True]
    for x in l4:
        print(x)

    # You can also define a list of numbers to
    # cycle through
    for x in [2, 4, 6]:
        print(x)

    # You can double up for loops to cycle through lists
    num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
    for x in num_list:
        print(x)

    for x in num_list:
        for y in x:
            print(y)

# ----- ITERATORS -----
# You can pass an object to iter() which returns an iterator which allows you to cycle
def Iterator():
    l5 = [6, 9, 12]
    itr = iter(l5)
    print(next(itr))  # Grab next value
    print(next(itr))
    print(next(itr))


# ----- RANGES -----
# The range() function creates integer iterables
def Range():
    print(list(range(0, 5)))

    # You can define step
    print(list(range(0, 10, 2)))
    num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
    for x in range(0, 3):
        for y in range(0, 3):
            print(num_list[x][y])


# ----- TUPLES -----
# Tuples are just like lists except they are immutable
def Tuple():
    t1 = (1, 3.14, "Ram", False)

    # Get length
    print("Length ", len(t1))

    # Get value / values
    print("1st", t1[0])
    print("Last", t1[-1])
    print("1st 2", t1[0:2])
    print("Every Other ", t1[0:-1:2])
    print("Reverse ", t1[::-1])

    # Everything you can do with lists you can do with
    # tuples as long as you don't change values

# ----- DICTIONARIES -----
# Dictionaries are lists of key / value pairs
# Keys and values can use any data type
# Duplicate keys aren't allowed
def Dictionary():
    heroes = {
        "Superman": "Clark Kent",
        "Batman": "Bruce Wayne"
    }
    # another way of defining dictionary.
    villains = dict([
        ("Lex Luthor", "Lex Luthor"),
        ("Loki", "Loki")
    ])

    print("Length", len(heroes))

    # Get value by key
    # Also heroes.get("Superman")
    print(heroes["Superman"])

    # Add more
    heroes["Flash"] = "Barry Allan"

    # Change a value
    heroes["Flash"] = "Barry Allen"

    # Get list of tuples
    print(list(heroes.items()))

    # Get list of keys and values
    print(list(heroes.keys()))
    print(list(heroes.values()))

    # Delete
    del heroes["Flash"]

    # Remove a key and return it
    print(heroes.pop("Batman"))

    # Search for key
    print("Superman" in heroes)

    # Cycle through a dictionary
    for k in heroes:
        print(k)

    for v in heroes.values():
        print(v)

    # Formatted print with dictionary mapping
    d1 = {"name": "Bread", "price": .88}
    print("%(name)s costs $%(price).2f" % d1)

# ----- SETS -----
# Sets are lists that are unordered, unique and while values can change those values must be immutable
def Set():
    s1 = set(["Ram", 1])

    s2 = {"Shyam", 1}

    # Size
    print("Length", len(s2))

    # Join sets
    s3 = s1 | s2
    print(s3)

    # Add value
    s3.add("Jadu")
    print(s3)

    # Remove value
    s3.discard("Ram")

    # Remove random value
    print("Random", s3.pop())

    # Add values in s2 to s3
    s3 |= s2

    # Return common values (You can include multiple sets as attributes)
    print(s1.intersection(s2))

    # All unique values
    print(s1.symmetric_difference(s2))

    # Values in s1 but not in s2
    print(s1.difference(s2))

    # Clear values
    s3.clear()

    # Frozen sets can't be edited
    s4 = frozenset(["Paul", 7])

# ----- FUNCTIONS -----
# Functions provide code reuse, organization and much more
# Add 2 values using 1 as default
# You can define the data type using function annotations

def get_sum(num1: int = 1, num2: int = 1):
    return num1 + num2

# Accept multiple values: don't know how many values get in
def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

# Return multiple values
def next_2(num):
    return num + 1, num + 2

# A function that makes a function that multiplies by the given value
def mult_by(num):
    # You can create anonymous (unnamed functions) with lambda
    return lambda x: x * num

# Pass a function to a function
def mult_list(list, func):
    for x in list:
        print(func(x))

def Functions():
    print(get_sum(5, 4))
    print(get_sum2(1, 2, 3, 4))
    i1, i2 = next_2(5)
    print(i1, i2)
    print("3 * 5 =", (mult_by(3)(5)))
    mult_by_4 = mult_by(4)
    mult_list(list(range(0, 5)), mult_by_4)

    # Create list of functions
    power_list = [lambda x: x ** 2,
                  lambda x: x ** 3,
                  lambda x: x ** 4]

# ----- MAP -----
# Map is used to execute a function on a list
def Map():
    one_to_4 = range(1, 5)
    times2 = lambda x: x * 2
    print(list(map(times2, one_to_4)))

# ----- FILTER -----
# Filter selects items based on a function
# Print out the even values from a list
def Filter():
    print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# ----- REDUCE -----
# Reduce receives a list and returns a single result
# Add up the values in a list
def Reduce():
    print(reduce((lambda x, y: x + y), range(1, 6)))


# ----- EXCEPTION HANDLING -----
# You can handle errors that would otherwise crash your program
# By giving the while a value of True it will cycle until a break is reached
def Exception():
    while True: # infinite loop

        # If we expect an error can occur surround
        # potential error with try
        try:
            number = int(input("Please enter a number : "))
            break

        # The code in the except block provides an error message to set things right
        # We can either target a specific error
        # like ValueError
        except ValueError:
            print("You didn't enter a number")

        # We can target all other errors with a
        # default
        except:
            print("An unknown error occurred")

    print("Thank you for entering a number")


# ----- FILE IO -----
# We can save and read data from files
# We start the code with with which guarantees the file will be closed if the program crashes
# mode w overwrites file
# mode a appends
def FileIO():
    with open("mydata.txt", mode="w", encoding="utf-8") \
            as myFile:
        # You can write to the file with write
        # It doesn't add a newline
        myFile.write("Some random text\nMore random text\nAnd some more")

    # Open a file for reading
    with open("mydata.txt", encoding="utf-8") as myFile:
        # Use read() to get everything at once
        print(myFile.read())

    # Find out if the file is closed
    print(myFile.closed)


# ----- CLASSES OBJECTS -----
# Real world objects have
# attributes : height, weight
# capabilities : run, eat

# Classes are blueprints for creating objects
class Square:
    # init is used to set values for each Square
    def __init__(self, height="0", width="0"):
        self.height = height # self is used to refer the object you are using
        self.width = width

    # This is the getter
    # self is used to refer to an object that
    # we don't possess a name for
    @property  # This is a getter function
    def height(self):
        print("Retrieving the height")
        # Put a __ before this private field
        return self.__height

    # This is the setter
    @height.setter
    def height(self, value):
        # We protect the height from receiving
        # a bad value
        if value.isdigit():
            # Put a __ before this private field
            self.__height = value
        else:
            print("Please only enter numbers for height")

    # This is the getter
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    # This is the setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def get_area(self):
        return int(self.__width) * int(self.__height)

def ExClass():
    # Create a Square object
    square = Square()
    square.height = "10"
    square.width = "10"
    print("Area", square.get_area())


# ----- INHERITANCE & POLYMORPHISM-----
# When a class inherits from another it gets all its fields and methods and can change as needed
class Animal:
    def __init__(self, name="unknown", weight=0): # init -> initialization function
        self.__name = name
        self.__weight = weight

    @property
    def name(self, name):
        self.__name = name

    def make_noise(self):
        return "Grrrrr"

    # Used to cast to a string type
    def __str__(self):
        return "{} is a {} and says {}".format(self.__name, type(self).__name__, self.make_noise())

    # Magic methods are used for operator overloading
    # Here I'll define how to evaluate greater than between 2 Animal objects
    def __gt__(self, animal2):
        if self.__weight > animal2.__weight:
            return True
        else:
            return False
    # Other Magic Methods
    # __eq__ : Equal
    # __ne__ : Not Equal
    # __lt__ : Less Than
    # __gt__ : Greater Than
    # __le__ : Less Than or Equal
    # __ge__ : Greater Than or Equal
    # __add__ : Addition
    # __sub__ : Subtraction
    # __mul__ : Multiplication
    # __div__ : Division
    # __mod__ : Modulus


# Dog inherits everything from Animal
class Dog(Animal):
    def __init__(self, name="unknown", owner="unknown", weight=0):
        # Have the super class handle initializing
        Animal.__init__(self, name, weight)
        self.__owner = owner

    # Overwrite str
    def __str__(self):
        # How to call super class methods
        return super().__str__() + " and is owned by " + \
               self.__owner


def ExInheritance():
    animal = Animal("Spot", 100)
    print(animal)

    dog = Dog("Bowser", "Bob", 150)
    print(dog)

    # Test the magic method
    print(animal > dog)

    # Polymorphism in Python works differently from
    # other languages in that functions accept any
    # object and expect that object to provide the
    # needed method

    # This isn't something to dwell on. Just know
    # that if you call on a method for an object
    # that the method just needs to exist for
    # that object to work.


# ----- THREADS -----
# Threads are blocks of code that takes turns executing and then go to sleep for a random
# period of time and then wake up and start executing again
# you need to import module for that
def execute_thread(i):
    # strftime or string formatted time allows you to define how the time is displayed.
    # You could include the date with
    # strftime("%Y-%m-%d %H:%M:%S", gmtime())

    # Print when the thread went to sleep
    print("Thread {} sleeps at {}".format(i,
                                          time.strftime("%H:%M:%S", time.gmtime())))

    # Generate a random sleep period of between 1 and 5 seconds
    rand_sleep_time = random.randint(1, 5)

    # Pauses execution of code in this function for a few seconds
    time.sleep(rand_sleep_time)

    # Print out info after the sleep time
    print("Thread {} stops sleeping at {}".format(i,
                                                  time.strftime("%H:%M:%S", time.gmtime())))
def ExThread():
    for i in range(10):
        # Each time through the loop a Thread object is created
        # You pass it the function to execute and any arguments to pass to that method
        # The arguments passed must be a sequence which is why we need the comma with 1 argument
        thread = threading.Thread(target=execute_thread, args=(i,))
        thread.start()

        # Display active threads
        # The extra 1 is this for loop executing in the main
        # thread
        print("Active Threads :", threading.activeCount())

        # Returns a list of all active thread objects
        print("Thread Objects :", threading.enumerate())


# Regular expressions allow you to locate and change strings in very powerful ways.
# They work in almost exactly the same way in every programming language as well.

# Regular Expressions (Regex) are used to
# 1. Search for a specific string in a large amount of data
# 2. Verify that a string has the proper format (Email, Phone #)
# 3. Find a string and replace it with another string
# 4. Format data into the proper form for importing for example

# import the Regex module
import re

def Regex():
    # ---------- Was a Match Found ----------

    # Search for ape in the string
    if re.search("ape", "The ape was at the apex"):
        print("There is an ape")

    # ---------- Get All Matches ----------

    # findall() returns a list of matches
    # . is used to match any 1 character or space
    allApes = re.findall("ape.", "The ape was at the apex")

    for i in allApes:
        print(i)

    # finditer returns an iterator of matching objects
    # You can use span to get the location

    theStr = "The ape was at the apex"

    for i in re.finditer("ape.", theStr): # ape followed by .
        # Span returns a tuple
        locTuple = i.span()

        print(locTuple)

        # Slice the match out using the tuple values
        print(theStr[locTuple[0]:locTuple[1]])


# Here I'll show you how to work with SQLite databases in Python

# A database makes it easy for you to organize your data for storage and fast searching
import sqlite3
import sys
import csv

# connect() will open an SQLite database, or if it doesn't exist it will create it
# The file appears in the same directory as this Python file
db_conn = sqlite3.connect('test.db')

print("Database Created")

# A cursor is used to traverse the records of a result
theCursor = db_conn.cursor()

def printDB():
    # To retrieve data from a table use SELECT followed by the items to retrieve and the table to retrieve from

    try:
        result = theCursor.execute("SELECT id, FName, LName, Age, Address, Salary, HireDate FROM Employees")

        # You receive a list of lists that hold the result
        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")

def ExDataBase():
    # execute() executes a SQL command
    # We organize our data in tables by defining their name and the data type for the data

    # We define the table name
    # A primary key is a unique value that differentiates each row of data in our table
    # The primary key will auto increment each time we add a new Employee
    # If a piece of data is marked as NOT NULL, that means it must have a value to be valid

    # NULL is NULL and stands in for no value
    # INTEGER is an integer
    # TEXT is a string of variable length
    # REAL is a float
    # BLOB is used to store binary data

    # You can delete a table if it exists like this
    # db_conn.execute("DROP TABLE IF EXISTS Employees")
    # db_conn.commit()

    try:
        db_conn.execute(
            "CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")

        db_conn.commit()

        print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")

    # To insert data into a table we use INSERT INTO
    # followed by the table name and the item name
    # and the data to assign to those items

    db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate)"
                    "VALUES ('Derek', 'Banas', 41, '123 Main St', '500,000', date('now'))")

    db_conn.commit()

    print("Employee Entered")

    # Print out all the data in the database
    printDB()

    # Closes the database connection
    db_conn.close()

# ---------- RECURSIVE FUNCTIONS ----------
# A function that refers to itself is a recursive function

# ——— MODULES ———
import myfunc

def Module1():
    print(myfunc.factorial(4))

# OR

from myfunc import factorial

def Module2():
    print(factorial(4))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    Multi-line comment
    printName()
    """
    # printMultiLine()
    # Variable()
    # DataTypes()
    # Math()
    # ConditionalOperator()
    # String()
    # List()
    # Loops()
    # Iterator()
    # Range()
    # Tuple()
    # Dictionary()
    # Set()
    # Functions()
    # Map()
    # Filter()
    # Reduce()
    # Exception()
    # FileIO()
    # ExClass()
    # ExInheritance()
    # ExThread()
    # Regex()
    # ExDataBase()
    # Module1()
    # Module2()





