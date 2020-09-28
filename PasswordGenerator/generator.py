# import libraries
import random

# Step 1. set up the password strings

num_str="1234567890"
sym_str="!@#$%^&*"
letter_str="qwertyuiopasdfghjklzxcvbnm"
cap_letter_str="QWERTYUIOPASDFGHJKLZXCVBNM"


# Step 2. define some functions to generate passwords

# sample pattern with given password length and string
def patterns(pw_len, pw_strings):
    pw=""
    while pw_len > 0:
        pw_len-=1
        ran_char = pw_strings[random.randint(0, len(pw_strings)-1)]
        pw=pw+ran_char
    return pw

# Step 3. execute the functions that generate passwords

print("PW1: "+patterns(8, sym_str))
print("PW2: "+patterns(8, letter_str))
print("PW3: "+patterns(8, num_str))
print("PW4: "+patterns(8, num_str+letter_str))
print("PW5: "+patterns(8, sym_str+num_str+cap_letter_str))






