class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age<18:
        raise InvalidAgeError("Age must be 18 or above 18.")
    else:
        print("Access granted. You are old enough!")



try:
    user_age = int(input("Enter your age:"))
    check_age(user_age)

except InvalidAgeError as e:
    print("InvalidAgeError:", e)

except ValueError:
    print("Please enter a valid number.")                



