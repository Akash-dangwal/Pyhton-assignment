import re

def validating(password, username, lastThreePasswords):
    if len(password) < 10:
        return False, "Password must be at least 10 characters long."
    if not (sum(1 for c in password if c.isupper()) >= 2 and
            sum(1 for c in password if c.islower()) >= 2 and
            sum(1 for c in password if c.isdigit()) >= 2 and
            sum(1 for c in password if c in '@#$%&*!') >= 2):
        return False, "Password must contain at least 2 uppercase letters, 2 lowercase letters, 2 digits, and 2 special characters."

    if re.search(r'(.)\1{3}', password):
        return False, "No character should repeat more than three times in a row."

    for i in range(len(password) - 2):
        if password[i:i+3] in username:
            return False, "Password should not contain any sequence of three or more consecutive characters from the username."

    if password in lastThreePasswords:
        return False, "Password cannot be the same as the last three passwords used."

    return True, "Password meets all criteria."


def main():
    username = input("Enter your username: ")
    lastThreePasswords = []

    for i in range(3):
        password = input("Enter one of your last three passwords: ")
        is_valid, message = validating(password, username, lastThreePasswords)
        if not is_valid:
            print("Invalid password:", message)
            while not is_valid:
                password = input("Enter a valid password: ")
                is_valid, message = validating(password, username, lastThreePasswords)
        lastThreePasswords.append(password)

    while True:
        password = input("Enter your new password: ")
        is_valid, message = validating(password, username, lastThreePasswords)
        if is_valid:
            print("Password set successfully.")
            break
        else:
            print("Invalid password:", message)

if __name__ == "__main__":
    main()

