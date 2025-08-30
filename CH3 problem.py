

# Q1. WAP to display a user entered name followed by good afternoon usimg input ()function
 
name = input(" Enter the user name")

print(f"Good after noon {name}")

# Q2. write a program to fill in a letter template given below with name and date

letter = '''
Dear <|Name|>,
    You are  selected!
<|Date|>
'''

print(letter.replace("<|Name|>","Saroj").replace("<|Date|>","30 August 2025"))


# Q3. WAO a program to detect double space in string


name =  "saroj is a   bad   boy " 

print(name.find("  "))


#Q4. WAP  to replace the double space from problem 3 with single space

name = "saroj is  a  bad  boy"

print(name.replace("  "," ")) #imuutabe string:- this function name.replace make a new string of give name



#5. WAP  to formate the folloeing letter using escape sequence character


Letter = "Desr harry , this python course nice. Thanks!"

print("Dear harry\n\tthis python course is nice\nThanks!")




