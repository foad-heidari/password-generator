import string
import random

pass_string = ""
pass_length = None
pass_count = None
max_pass_length = 60
max_pass_count = 30
lowercase = None
uppercase = None
digits = None
pass_types = None
add_space = "-------\n"

# ask user the length of the password
while True:
    try:
        # ask the user about password length
        if not pass_length:
            pass_length = int(input(f"{add_space}Length of the password: "))
            if pass_length > max_pass_length:
                pass_length = None
                print(f"Max length of the password can't be more then {max_pass_length}")
                continue
        
        # ask the user about password count
        if not pass_count:
            pass_count = int(input(f"{add_space}How many password would you like? "))
            if pass_count > max_pass_length:
                pass_count = None
                print(f"[!] Max number of the password can't be more then {max_pass_count}")
                continue
        
        # ask the user if wanna lowercase letters
        if not pass_string:
            pass_types = str(input(f"{add_space}How Your password should be look like?\nU:uppercase, L:lowercase, N:Number (e.g. ULN): "))
            if "U" in pass_types.upper():
                pass_string += string.ascii_uppercase
            if "L" in pass_types.upper():
                pass_string += string.ascii_lowercase
            if "N" in pass_types.upper():
                pass_string += string.digits
            if not pass_string:
                print("[!] Please Enter a valid input!")
                continue

        break
    except ValueError:
        print("[!] Please Enter a valid password Type!")

# Generate the random passwords
def generate(pass_c):
    password = ''
    for s in range(pass_length):
        password += random.choice(pass_string)
    print("{0:0=2d}. {1}".format(pass_c, password))

# generate how much password user want
for x in range(pass_count):
        generate(x + 1)
