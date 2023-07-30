# importing the pandas library
import pandas as pd


# creating a dataframe object
student_register = pd.DataFrame()

# assigning values to the
# rows and columns of the
# dataframe
student_register['Name'] = ['Abhijit',
							'Smriti',
							'Akash',
							'Roshni']

student_register['Age'] = [20, 19, 20, 14]
student_register['Student'] = [False, True,
							True, False]

print(student_register)
