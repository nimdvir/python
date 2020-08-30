#a program for a basic string extraction.
import re
#take user input
inputS = input('Enter Some String: ')
# find only chars
inputSOnlyChar = " ".join(re.findall("[a-zA-Z]+", inputS))
# display final result (only chars, lowercase)
print('The final result:', inputSOnlyChar.lower())
