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
