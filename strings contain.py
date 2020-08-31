# How to check if Python string contains another string

# The find method

# string.find(substring)

a_string="PythonProgramming" 
substring1="Programming" 
substring2="Language" 
print("Check if "+a_string+" contains "+substring1+":")
print(a_string.find(substring1)) 
print("Check if "+a_string+" contains "+substring2+":")
print(a_string.find(substring2))

# The in operator
# substring in string

a_string="PythonProgramming"
substring1="Programming"
substring2="Language"
print("Check if "+a_string+" contains "+substring1+":")
print(substring1 in a_string)
print("Check if "+a_string+" contains "+substring2+":")
print(substring2 in a_string)

# The count method
# string.count(substring)

a_string="PythonProgramming"
substring1="Programming"
substring2="Language"
print("Check if "+a_string+" contains "+substring1+":")
print(a_string.count(substring1))
print("Check if "+a_string+" contains "+substring2+":")
print(a_string.count(substring2))