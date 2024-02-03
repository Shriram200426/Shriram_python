a="welcome to python class"
print(a.isupper())#all are caps lock
print(a.islower())#all are small 
print(a.isalnum())#combination of no and alphabets
print(a.isnumeric())#all are no
print(a.isalpha())#all are alphabets
print(a.isspace())# all are space
print(a.upper())# coverts to upper
print(a.lower())#converts to lower
print(a.swapcase())#converts uppercase to lowercase and vice versa
print(a.replace("class","session"))#replace words
print(a.startswith("we"))#check if its starts with we
print(a.startswith("to",0,10ml))#check if its start with to in 8yh index
print(a.endswith("ss"))#check if its end with ss
print(a.endswith("on",16))#check if its ends with on in index
print(a.ljust(30,"1"))#fills 30 values with 1 at the rear
print(a.rjust(30,"1"))#fills 1 in front of welcome
print(a.center(30,"-"))#fills the '-' in splitiing the center
print(a.zfill(30))#fills 0 automaticall in front 
print(a.strip("a"))#removes a from front and back and can be used only after using ljust or rjust
print(a.lstrip("a"))#removes 'a' from front of the sentence
print(a.rstrip("a"))#removes 'a' from last of the sentence
print(a.capitalize())#coverts the starting letter of the para to uppercase
print(a.title())#converts the strating of the sentence or words to uppercase
print(a.count("e"))#counts how many words are there
print(a.count("e",5))#counts how many e are there after 5th position
print(a.index("w"))# gives the position of w first w no repition 