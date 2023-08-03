import pyinputplus as pyip
num = pyip.inputNum()
print(num)
string = pyip.inputStr()
print(string)
choice_list=['a','b'] # list of choices to choose from, default is ['y
choice = pyip.inputMenu(choice_list)
print(choice)
datetime = pyip.inputDatetime()
print(datetime)
yes_no = pyip.inputYesNo()
print(yes_no)
bool = pyip.inputBool()
print(bool)
email = pyip.inputEmail()
print(email)
file_path = pyip.inputFilepath()
print(file_path)
password = pyip.inputPassword()
print(password) 

'''
The pyinputplus library has several functions for different kinds of input.

inputStr()
inputNum()
inputChoice()
inputMenu()
inputDatetime()
inputYesNo()
inputBool()
inputEmail()
inputFilepath()
inputPassword()
'''