# TASK - ask a person from stackoverflow, why that error keeps coming
def print_valid(address):
    points = 0
    count = 0
    chars = [char for char in address]
    unallowed_symbols = ["#", "$", "%", "^", "&", "*", "/"]
    email_providers = ["@outlook", "@gmail", "@hotmail", "@yahoo"]

    # point one
    if "@" in address:
        points += 1
        
    # point two
    for letters in chars:
        if "@" in letters:
            count += 1

    if count < 1 or count > 1:
        points -= 1 
    else: 
        points += 1

    # point three
    for symbols in unallowed_symbols:
        if symbols in address:
            points -= 1
        else:
            break
    points += 1

    # point four
    for provider in email_providers:
        if provider in address:
            points += 1
        else:
            points -= 1

    # check points
    if points == 4:
        return "Valid address"
    else: 
        return "Invalid address"

email = str(input("Enter email: "))
print(print_valid(email))