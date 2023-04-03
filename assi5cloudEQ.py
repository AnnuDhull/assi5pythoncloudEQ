import function
function.greatest(a, b, c)
# --------------------------------------------
import random
namee = random.randint(0 , 28)
print(namee)
# --------------------------------------------
import json 
x = '{ "Annu":"Dhull" , "Age": 23 ,"course" : "MCA"}'
nameee = json.loads(x)
print(type(x))

# ---------------------------------------------------------------------------------------------------------------------------------

# Ques  :    In dumps function what are the parameters that we have and what do they do, explain with small program ?

# """There are 4 arguments to pass inside dumps() method"""
# 1. An object which we need to convert
# 2. indent , give spaces to read and understand it in a eficient manner
# 3. sort_keys , to sort the content alphabetically or numerically
# 4. seperators , it is used to seperate the key values pair to better understanding and readability (",",".","=")

import json

myDict ={ "Name":"Annu Dhull",
    "Mother Name":"Sunita" ,
    "age":22 ,
    "Siblings":["komal","Dhruv" ] ,
    "Father Name" : "Daya singh Dhull" , 
    "profession":"Software Engineer"
    }
print(type(myDict))
x=json.dumps(myDict, indent=4, sort_keys=True, separators=(".","="))
print(x)

# --------------------------------------------------------------------------------------------------------------------------------

try:
    print(x)
except:
    print("It's an error .") 
else:
    print("No correction needed !")
finally:
    print("Its working is Progressing....")

# Ques  :  How can we raise an exception, WAP. ?

Age = int(input("enter your Age : "))
if Age >=18:
    print(" YOU ARE AN ADULT")

else:
    raise Exception(" YOU ARE AN ADOLESCENT ")

# -----------------------------------------------------------------------------------------------------------------------------

# Ques  :  WAP on normal list comprehension and  another program on list comprehension by using condition ? 

fruits = ["guvava", "papaya","watermelon", "Dragonfruit","grapes","lichi","pineapple","orange","cherry" ,"mulberry"]
newlist = []

for x in fruits:
    if "p" in x :
        newlist.append(x)
        print(newlist)

newlist = [x for x in fruits if "g" in x]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)
