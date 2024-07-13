import re

def pass_strength(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    numb_criteria = re.search(r'[0-9]', password) is not None
    special_character_criteria = re.search(r'[\W_]', password) is not None

    # Calculate strength score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, numb_criteria, special_character_criteria])

    # Provide feedback based on the score
    if score == 5:
        strength = "Very Strong password"
    elif score == 4:
        strength = "Strong passowrd"
    elif score == 3:
        strength = "Medium password"
    elif score == 2:
        strength = "Weak password"
    else:
        strength = "Very Weak password"

    return {
        "strength": strength,
        "criteria": {
            "length": length_criteria,
            "uppercase": uppercase_criteria,
            "lowercase": lowercase_criteria,
            "number": numb_criteria,
            "special_char": special_character_criteria,
        }
    }

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    result = pass_strength(password)

    # Print feedback
    print(f" The Password Strength is: {result['strength']}")
    print("Criteria succesfully met:")
    print(f" - Minimum length (8 characters): {'Yes' if result['criteria']['length'] else 'No'}")
    print(f" - Uppercase letter: {'Yes' if result['criteria']['uppercase'] else 'No'}")
    print(f" - Lowercase letter: {'Yes' if result['criteria']['lowercase'] else 'No'}")
    print(f" - Number: {'Yes' if result['criteria']['number'] else 'No'}")
    print(f" - Special character: {'Yes' if result['criteria']['special_char'] else 'No'}")

if __name__ == "__main__":
    main()



