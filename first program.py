#Post 1

#Variables in Python:
#Variable is a name given to a memory location in a program, it is used to store data in a program, it is also used to represent real world entities like a person, a car, a router etc. In python we don't need to declare the type of variable, we can directly assign a value to a variable and python will automatically determine the type of variable based on the value assigned to it. Example below shows how to create variables in python and assign values to them.

router1 = "Cisco 2901" # here we are creating a variable router1 and assigning a value Cisco 2901 to it, it is a string data type in python
router2 = "Juniper SRX300" # here we are creating a variable router2 and assigning a value Juniper SRX300 to it, it is a string data type in python
router3 = "Huawei AR2220" # here we are creating a variable router3 and assigning a value Huawei AR2220 to it, it is a string data type in python
print(router1) # it will print Cisco 2901 on the screen 
print(router2) # it will print Juniper SRX300 on the screen
print(router3) # it will print Huawei AR2220 on the screen  


Hostname = "Router1" # here we are creating a variable Hostname and assigning a value Router1 to it, it is a string data type in python
IP_Address = "10.10.10.1" # here we are creating a variable IP_Address and assigning a value
is_up = True # here we are creating a variable is_up and assigning a value True to it, it is a boolean data type in python
print(Hostname) # it will print Router1 on the screen   
print(IP_Address) # it will print   
print(is_up) # it will print True on the screen

#Rules for variable names in python:
    
#1. Variable name must start with a letter or an underscore, it cannot start with a digit, example below

Myname = "thetechshift" # here we are creating a variable name and assigning a value "thetechshift" to it, it is a string data type in python, it is a valid variable name because it starts with a letter


_name = "thetechshift" # here we are creating a variable _name and assigning a value "thetechshift" to it, it is a string data type in python, it is a valid variable name because it starts with an underscore 

#2name = "thetechshift" # here we are creating a variable 2name and assigning a value "thetechshift" to it, it is a string data type in python, it is an invalid variable name because it starts with a digit, it will give a syntax error when we try to run this code  

#2. Variable name can only contain letters, digits and underscores, it cannot contain any special characters or spaces, example below

name = "thetechshift" # here we are creating a variable name and assigning a value  "thetechshift" to it, it is a string data type in python, it is a valid variable name because it only contains letters
name_1 = "thetechshift" # here we are creating a variable name_1 and assigning a value "thetechshift" to it, it is a string data type in python, it is a valid variable name because it only contains letters, digits and underscores
#name-1 = "thetechshift" # here we are creating a variable name-1 and assigning a value "thetechshift" to it, it is a string data type in python, it is an invalid variable name because it contains a special character - it will give a syntax error when we try to run this code  

#3. Variable name cannot be a reserved keyword in python, it cannot be a built in function name in python, it cannot be a built in data type name in python, example below
name = "thetechshift" # here we are creating a variable name and assigning a value "thetechshift" to it, it is a string data type in python, it is an invalid variable name because it is a reserved keyword in python, it will give a syntax error when we try to run this code


print("Hello, AI") # this is a comment, it is not executed by the python interpreter, it is used to explain the code, it is also used to make the code more readable, it is also used to debug the code, it is also used to provide information about the code, it is also used to provide instructions to the user, it is also used to provide documentation for the code, it is also used to provide information about the author of the code, it is also used to provide information about the date of creation of the code, it is also used to provide information about the version of the code, it is also used to provide information about the license of the code, it is also used to provide information about the copyright of the code, it is also used to provide information about the disclaimer of the code, it is also used to provide information about the warranty of the code, it is also used to provide information about the support of the code, it is also used to provide information about the contact details of the author of the code, it is also used to provide information about the website of the author of the code, it is also used to provide information about the social media handles of the author of the code, it is also used to provide information about the email address of the author of the code, it is also used to provide information about the phone number of the author of the code, it is also used to provide information about the address of the author of the code, it is also used to provide information about the company name of the author of the code, it is also used to provide information about the job title of the author of the code, it is also used to provide information about the skills of the author of the code, it is also used to provide information about the experience of the author of the code, it is also used to provide information about the education qualifications of the author of the code, it is also used to provide information about any awards or recognitions received by the author of the code.
print("The Tech ") # Print statment is used to print the output on the screen, it is a built in function in python, it is used to display the output of the program, it is also used to display the value of a variable, it is also used to display the result of an expression, it is also used to display the result of a function, it is also used to display the result of a method, it is also used to display the result of a class, it is also used to display the result of a module, it is also used to display the result of a package, it is also used to display the result of a library, it is also used to display the result of an API, it is also used to display the result of a framework, it is also used to display the result of a tool, it is also used to display the result of a software, it is also used to display the result of a hardware, it is also used to display the result of a network device, it is also used to display the result of a cloud service, it is also used to display the result of a database, it is also used to display the result of a data structure, it is also used to display the result of an algorithm, it is also used to display the result of a machine learning model, it is also used to display the result of an artificial intelligence model.


# print is a function of python to print the output on the screen, it is a built in function in python, it is used to display the output of the program, it is also used to display the value of a variable, it is also used to display the result of an expression, it is also used to display the result of a function, it is also used to display the result of a method, it is also used to display the result of a class, it is also used to display the result of a module, it is also used to display the result of a package, it is also used to display the result of a library, it is also used to display the result of an API, it is also used to display the result of a framework, it is also used to display the result of a tool, it is also used to display the result of a software, it is also used to display the result of a hardware, it is also used to display the result of a network device, it is also used to display the result of a cloud service, it is also used to display the result of a database, it is also used to display the result of a data structure, it is also used to display the result of an algorithm, it is also used to display the result of a machine learning model, it is also used to display the result of an artificial intelligence model.
# in python we can print multiple values in a single print statement by separating them with a comma, example below
print("Hello", "World") # it will print Hello World on the screen, it will print both the values Hello and World in a single print statement by separating them with a comma, it will add a space between the two values by default, we can also change the separator by using the sep parameter in the print function, example below
print("Hello", "World", sep="-") # it will print Hello-World on the screen, it will print both the values Hello and World in a single print statement by separating them with a comma, it will change the separator from space to hyphen by using the sep parameter in the print function.
#Print function also has end parameter which is used to change the end character of the print statement, by default it is a new line character which means after printing the output it will move to the next line, we can change it to any character we want, example below
print("Hello", end=" ") # it will print Hello on the screen and it will change the end character from new line to space by using the end parameter in the print function, it will not move to the next line after printing Hello, it will add a space after Hello and it will wait for the next print statement to print on the same line, example below
#print("World") # it will print World on the same line as Hello because we have changed the end character of the previous print statement to space, it will print Hello World on the same line.  

#Character - A character is a single letter, digit, symbol or space, it is represented by a single quote or double quote in python, example below
char1 = 'A' # here we are storing a character A in a variable char1, it is represented by a single quote in python
char2 = "B" # here we are storing a character B in a variable char2, it is represented by a double quote in python
char3 = '1' # here we are storing a character 1 in a variable char3, it is represented by a single quote in python
char4 = "@" # here we are storing a character @ in a variable char4, it is represented by a double quote in python
char5 = " " # here we are storing a space character in a variable char5, it is represented by a double quote in python
print(char1) # it will print A on the screen
print(char2) # it will print B on the screen
print(char3) # it will print 1 on the screen        
print(char4) # it will print @ on the screen
print(char5) # it will print a space on the screen  
#Character can be of different types, it can be a letter, a digit, a symbol or a space, example below    

#Suppose we want to store a character in a variable and we want to check the type of that variable, example below
char = 'A' # here we are storing a character A in a variable char, it   is represented by a single quote in python
print(type(char)) # it will print <class 'str'> on the screen, it will show that the type of the variable char is string, because in python a character is also considered as a string of length 1, it is not a separate data type in python, it is a part of string data type in python.   

#Data Types supported in python are:
#1. String : it is a sequence of characters, it is represented by single quote or double quote in python, example below
str1 = 'Hello' # here we are storing a string Hello in a variable str1, it is represented by a single quote in python
str2 = "World" # here we are storing a string World in a variable str2  , it is represented by a double quote in python
print(str1) # it will print Hello on the screen 
print(str2) # it will print World on the screen     

#Rules for string in python:
#1. A string can be enclosed in single quotes or double quotes, but it must be consistent, example below
str1 = 'Hello' # here we are storing a string Hello in a variable str1, it is represented by a single quote in python
str2 = "World" # here we are storing a string World in a variable str2, it is represented by a double quote in python
str3 = 'Hello World' # here we are storing a string Hello World in a variable str3, it is represented by a single quote in python
str4 = "Hello World" # here we are storing a string Hello World in a variable str4, it is represented by a double quote in python
print(str1) # it will print Hello on the screen     
print(str2) # it will print World on the screen
print(str3) # it will print Hello World on the screen
print(str4) # it will print Hello World on the screen
#2. If we want to include a single quote in a string that is enclosed in single quotes, we can use escape character \ to escape the single quote, example below
str1 = 'It\'s a nice day' # here we are storing a string It's a nice day in a variable str1, it is represented by a single quote in python, we are using escape character \ to escape the single quote in the string, it will print It's a nice day on the screen
print(str1) # it will print It's a nice day on the screen           
 #or we can use double quotes to enclose the string that contains a single quote, example below
str1 = "It's a nice day" # here we are storing a string It's a nice day in a variable str1, it is represented by a double quote in python, we don't need to use escape character \ to escape the single quote in the string, it will print It's a nice day on the screen
print(str1) # it will print It's a nice day on the screen       

#3. If we want to include a double quote in a string that is enclosed in double quotes, we can use escape character \ to escape the double quote, example below
str1 = "She said, \"Hello\"" # here we are storing a string She said, "Hello" in a variable str1, it is represented by a double quote in python, we are using escape character \ to escape the double quote in the string, it will print She said, "Hello" on the screen
print(str1) # it will print She said, "Hello" on the screen 
#or we can use single quotes to enclose the string that contains a double quote, example below
str1 = 'She said, "Hello"' # here we are storing a string She said  , "Hello" in a variable str1, it is represented by a single quote in python, we don't need to use escape character \ to escape the double quote in the string, it will print She said, "Hello" on the screen
print(str1) # it will print She said, "Hello" on the screen 

#4. We can also use triple quotes to enclose a string that contains both single quotes and double quotes, example below
str1 = '''She said, "It's a nice day"''' # here we are storing a string She said, "It's a nice day" in a variable str1, it is represented by triple quotes in python, we don't need to use escape character \ to escape the single quote and double quote in the string, it will print She said, "It's a nice day" on the screen
print(str1) # it will print She said, "It's a nice day" on the screen

#5. We can also use triple double quotes to enclose a string that contains both single quotes and double quotes, example below
str1 = """She said, "It's a nice day""" # here we are storing a string She said, "It's a nice day in a variable str1, it is represented by triple double quotes in python, we don't need to use escape character \ to escape the single quote and double quote in the string, it will print She said, "It's a nice day" on the screen
print(str1) # it will print She said, "It's a nice day" on the screen       

#6. We can also use raw string to enclose a string that contains escape characters, example below
str1 = r'It\'s a nice day' # here we are storing a string It's a nice day in a variable str1, it is represented by raw string in python, we are using raw string to enclose the string that contains escape characters, it will print It\'s a nice day on the screen, it will not interpret the escape character \ as an escape character, it will treat it as a normal character and it will print the string as it is on the screen
print(str1) # it will print It\'s a nice day on the screen, it will not interpret the escape character \ as an escape character, it will treat it as a normal character and it will print the string as it is on the screen 

#7. We can also use f string to enclose a string that contains variables, example below
name = "TheTechShift" # here we are storing a string TheTechShift in a variable name, it is represented by a string in python
str1 = f"Hello, {name}!" # here we are storing an f string Hello, TheTechShift! in a variable str1, it is represented by f string in python, we are using f string to enclose the string that contains the variable name, it will print Hello, TheTechShift! on the screen
print(str1) # it will print Hello, TheTechShift! on the screen

#What is a string? A string is a sequence of characters, it is represented by single quote or double quote in python, example below
str1 = 'Hello' # here we are storing a string Hello in a variable str1  , it is represented by a single quote in python
str2 = "World" # here we are storing a string World in a variable str2, it is represented by a double quote in python
print(str1) # it will print Hello on the screen 

#2. Integer : it is a whole number, it can be positive, negative or zero, it is represented by int data type in python, example below
int1 = 10 # here we are storing an integer 10 in a variable int1, it is represented by int data type in python
int2 = -5 # here we are storing an integer -5 in a variable int2, it is represented by int data type in python
int3 = 0 # here we are storing an integer 0 in a variable int3, it is represented by int data type in python
print(int1) # it will print 10 on the screen            
print(int2) # it will print -5 on the screen
print(int3) # it will print 0 on the screen

#3. Float : it is a decimal number, it can be positive, negative or zero, it is represented by float data type in python, example below
float1 = 3.14 # here we are storing a float 3.14 in a variable float1, it is represented by float data type in python
float2 = -2.5 # here we are storing a float -2.5 in a variable float2, it is represented by float data type in python
float3 = 0.0 # here we are storing a float 0.0 in a variable float3, it is represented by float data type in python
print(float1) # it will print 3.14 on the screen    
print(float2) # it will print -2.5 on the screen
print(float3) # it will print 0.0 on the screen

#4. Boolean : it is a data type which can have only two values True or False, it is represented by bool data type in python, example below
bool1 = True # here we are storing a boolean value True in a variable bool1, it is represented by bool data type in python
bool2 = False # here we are storing a boolean value False in a variable bool2,  it is represented by bool data type in python
print(bool1) # it will print True on the screen     
print(bool2) # it will print False on the screen

#5. Character : it is a single letter, digit, symbol or space, it is represented by a single quote or double quote in python, example below
char1 = 'A' # here we are storing a character A in a variable char1     , it is represented by a single quote in python
char2 = "B" # here we are storing a character B in a variable char2, it is represented by a double quote in python
char3 = '1' # here we are storing a character 1 in a variable char  3, it is represented by a single quote in python    
char4 = "@" # here we are storing a character @ in a variable char4, it is represented by a double quote in python
char5 = " " # here we are storing a space character in a variable char5,    it is represented by a double quote in python
print(char1) # it will print A on the screen    
print(char2) # it will print B on the screen
print(char3) # it will print 1 on the screen            
print(char4) # it will print @ on the screen
print(char5) # it will print a space on the screen      

#6. List : it is a collection of data types, it is represented by square brackets in python, example below
list1 = [1, 2, 3, 4, 5] # here we are storing a list of integers in a variable list1, it is represented by square brackets in python
list2 = ["Hello", "World"] # here we are storing a list of strings in   a variable list2, it is represented by square brackets in python
list3 = [1, "Hello", 3.14, True] # here we are storing a list of different data types in a variable list3, it is represented by square brackets in python
print(list1) # it will print [1, 2, 3, 4  , 5] on the screen
print(list2) # it will print ['Hello', 'World'] on the screen   
print(list3) # it will print [1, 'Hello', 3.14, True] on the screen

#7. tuple : it is a collection of data types, it is represented by parentheses in python, example below
tuple1 = (1, 2, 3, 4, 5) # here we are storing a tuple of integers in a variable tuple1, it is represented by parentheses in python
tuple2 = ("Hello", "World") # here we are storing a tuple of strings in a variable tuple2, it is represented by parentheses in python
tuple3 = (1, "Hello", 3.14, True) # here we are storing a tuple of different data types in a variable tuple3, it is represented by parentheses in python
print(tuple1) # it will print (1, 2, 3, 4   , 5) on the screen
print(tuple2) # it will print ('Hello', 'World') on the screen          
print(tuple3) # it will print (1, 'Hello', 3.14, True) on the screen

#Characterstic
# Letters -A to Z, a to z
# Digit - 0 to 9

print ("My name is Shubham", "I ma 32 year old")

##############################################################################################

#Variable : a Variable is a name given to a memoery location in a program

#name : shubham

#Here name is the name of the varibale and Shubham is the value of varibale 

name = "shubham" # its a string :  any words or sentence have to be in quotes, anything in quote is called string.
age = 23     # storying a value 23 in variable age.
price = 100
print(name)  #to use the varisble value we don't need quotes
print(age)
print(price)


print (name, age, price)
print ("My name is :" , name)
print ('My age is :' , age)


# in maths we type a = b , it means a and b are equal, howeverin pyhton when we say a = b , it
# means we are storing a value that in b in a 
# in below example stored a value 23 in variable a , stored a value a in b, since a's value was 23 it will show b as value 23 
# example below
a = 23
b = a
print (b)


# Identifiers # Identifiers are the names, it can name of the variable as well, we have some rule for names or we can identifiers
# for example age = "32" : Here age is the name of the varibales and 32 is the value of that variable.

a=int(input('enter the value of a='))
b=int(input('enter the value of b='))
print (a+b)

Name = (input("enter your name"))
print(Name.__len__())
print(Name.replace('s', 'o'))
print(Name.count('$'))




Mark = (input('Enter your Marks:') )
if ( int(Mark) >= 80 ):
    print("grade=a")
elif ( int(Mark) >= 50 and int(Mark) <= 80 ):
    print("grade b")
elif ( int(Mark) < 50 ):
    print("grade=c")



Numbers = 41

if ( Numbers >= 80 ): # here we are checking if the value of numbers is greater than or equal to 80 then we will store grade a in variable grade
    grade= "x" # here we are storing grade a in variable grade if the condition is true
elif (Numbers >= 50 and Numbers <= 80):
    grade= "y"
elif (Numbers <50):
    grade = "z"

print(grade)

# list is built in data types which stores multiple values in a single variable,
# it is a collection of data types.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1]

print(list)

print(type(list))  # to print the type of data type we can use type function


list.pop(6) # pop is a function which removes the value of the index we have given, in this case it will remove 7 from the list as 7 is on index 6
print(list)

list.count(1) # count is a function which counts the number of times a value is present in the list, in this case it will count the number of times 1 is present in the list and return that value
print(list.count(1)) # it will print 4 as 1 is present 4 times in the list
list.reverse() # reverse is a function which reverses the order of the elements in the list Example: if list is [1, 2, 3] then after reverse it will be [3, 2, 1]
print(list) 


movies =(input("enter your 3 best movies:")) # here we are taking input from the user and storing it in a variable movies, since we are taking input it will be in string format, if we want to store it in list format we can use split function to split the string into list of movies
movies_list = movies.split(",")   # split function will split the string into list of movies based on the separator we have given, in this case we have given comma as separator so it will split the string into list of movies based on comma
print(movies_list) # it will print the list of movies

# or we can directly store the input in list format by using split function while taking input from the user, example below
list= [movies]  
print(list)


# in a list we can store multiple value of different data types, for example we can store string, integer, float, boolean in a list, example below
my_list = ["shubham", 23, 3.14, True] # here we are storing string, integer, float and boolean in a list
print(my_list) # it will print the list with all the values of different data types 

#list are mutable which means we can change the value of the list, we can add new value to the list, we can remove value from the list, we can change the value of the list, example below
my_list[0] = "shubham kumar" # here we are changing the value of the first element of the list from "shubham" to "shubham kumar"
print(my_list) # it will print the list with the updated value of the first element as "shubham kumar" instead of "shubham" 



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Dictionary in Python

#Dictonary is a built in data type in python which stores data in key value pair, it is a collection of key value pairs, it is also called as associative array or hash map in other programming languages, example below
my_dict = {"name": "shubham", "age": 23, "city": "patna"} # here we are storing data in key value pair, where name is the key and shubham is the value, age is the key and 23 is the value, city is the key and patna is the value
print(my_dict) # it will print the dictionary with all the key value pairs

my_dict = {"Hostname" : "Router1", "IP Address" : "10.10.10.1" , "Subnet Mask" : "255.255.255.0" , "Model" : "Cisco 2901" , "Location" : "Patna"} # here we are storing data in key value pair, where Hostname is the key and Router1 is the value, IP Address is the key and 10.10.10.1 is the value, Subnet Mask is the key and 255.255.255.0 is the value, Model is the key and Cisco 2901 is the value, Location is the key and Patna is the value
print(my_dict) # it will print the dictionary with all the key value pairs


#Output: Print the value of the key in the dictionary, example below
print(my_dict["Hostname"]) # it will print the value of the key Hostname which is Router1
print(my_dict["IP Address"]) # it will print the value of the key IP Address which is 10.10.10.1
print(my_dict["Subnet Mask"]) # it will print the value of the key Subnet Mask which is 255.255.255.0
print(my_dict["Model"]) # it will print the value of the key Model which is Cisco 2901
print(my_dict["Location"]) # it will print the value of the key Location which is Patna 

#Dictionary are mutable which means we can change the value of the key in the dictinary, we can add new key value pair to the dictionary, we can remove key value pair from the dictionary, we can change the value of the key in the dictionary, example below
my_dict["Hostname"] = "Router2" # here we are changing the value of the key Hostname from Router1 to Router2
print(my_dict) # it will print the dictionary with the updated value of the key Hostname which is Router2 instead of Router1.
my_dict["IP Address"] = "10.10.10.2" # here we are changing the value of the key IP Address from 10.10.10.1 to 10.10.10.2
print(my_dict) # it will print the dictionary with the updated value of the key IP Address which is 10.10.10.2 instead of 10.10.10.1.


#Dictionary are unordered which means the order of the key value pairs in the dictionary is not guaranteed, it can change at any time, example below
my_dict = {"name": "shubham", "age": 23, "city": "patna"} # here we are storing data in key value pair, where name is the key and shubham is the value, age is the key and 23 is the value, city is the key and patna is the value
print(my_dict) # it will print the dictionary with all the key value pairs, but the order of the key value pairs may change at any time, it is not guaranteed to be in the same order as we have defined it.    

#Dictionary are also called as associative array or hash map in other programming languages, it is a collection of key value pairs, where each key is unique and maps to a value, it is used to store data in a structured way, it is also used to represent real world entities like a person, a car, a router etc.
#Dictionary are also used to represent JSON data in python, it is a common data format used in web development, it is used to exchange data between client and server, it is also used to store configuration data in python applications.  Exmaple below shows how to represent JSON data in python using dictionary.
my_dict = {"Router1": {"Hostname": "Router1", "IP Address": "10.10.10.1"} , "Router2": {"Hostname": "Router2", "IP Address": "10.10.10.2"}}

#In dictionary we can also have nested dictionary which means we can have a dictionary inside a dictionary, example below
my_dict = {"Router1": {"Hostname": "Router1", "IP Address": "10.10.10.1"} , "Router2": {"Hostname": "Router2", "IP Address": "10.10.10.2"}} # here we have a dictionary with two key value pairs, where the value of each key is also a dictionary, for example the value of the key Router1 is a dictionary with two key value pairs, where Hostname is the key and Router1 is the value, IP Address is the key and 10.10.10.1 is the value        
print(my_dict) # it will print the dictionary with all the key value pairs, where the value of each key is also a dictionary, it will show the nested structure of the dictionary.

#In dictionary we can also have list as a value of the key, example below

my_dict = {"Router1": ["Hostname", "IP Address", "Subnet Mask"], "Router2": ["Hostname", "IP Address", "Subnet Mask"]} # here we have a dictionary with two key value pairs, where the value of each key is a list, for example the value of the key Router1 is a list with three elements, where Hostname is the first element, IP Address is the second element and Subnet Mask is the third element, similarly the value of the key Router2 is also a list with three elements, where Hostname is the first element, IP Address is the second element and Subnet Mask is the third element

#In dictionary we can also have tuple as a value of the key, example below  

my_dict = {"Router1": ("Hostname", "IP Address", "Subnet Mask"), "Router2": ("Hostname", "IP Address", "Subnet Mask")} # here we have a dictionary with two key value pairs, where the value of each key is a tuple, for example the value of the key Router1 is a tuple with three elements, where Hostname is the first element, IP Address is the second element and Subnet Mask is the third element, similarly the value of the key Router2 is also a tuple with three elements, where Hostname is the first element, IP Address is the second element and Subnet Mask is the third element    

my_dict = {"Router1": {"Hostname": "Router1", "IP Address": "10.10.10.1"}}
print(my_dict["Router1"]["Hostname"]) # it will print the value of the key Hostname which is Router1, here we are accessing the value of the key Hostname which is inside the dictionary that is the value of the key Router1, it will show how to access nested dictionary in python.  
