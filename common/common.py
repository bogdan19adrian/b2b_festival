import re

# Make a regular expression
# for validating an Email
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


# Define a function for
# for validating an Email
def validate_email(email):
    # pass the regualar expression
    # and the string in search() method
    if (re.search(regex, email)):
        print("Valid Email " + email)
        return True
    else:
        print("Invalid Email " + email)
        return False