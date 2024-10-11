import re

def check_paswd(input_passwords):
    password_pattern = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$'
    )

    # Split the input string into individual passwords
    passwords = input_passwords.split(',')
    print(passwords)
    match_passwords = []

    # Check each password against the pattern
    for password in passwords:
        if password_pattern.match(password):
            match_passwords.append(password)
    print(match_passwords)
    # Join valid passwords with a comma and return
    return ','.join(match_passwords)

input_password = "asqwr1234@1,aF145#,2w3E*,2We3345"
output = check_paswd(input_password)
print(output)