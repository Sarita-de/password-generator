import random
import string


length= int(input(" length of the password"))


upper_case= string.ascii_uppercase
lower_case= string.ascii_lowercase
number= string.digits
symbols = string.punctuation

all= upper_case + lower_case + number + symbols

temp = random.sample(all,length)
password= " ".join(temp)
print (password)

