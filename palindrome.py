def palindrome(string):
    # palindrome = lambda string: string == string[::-1]        
    try:
        if len(string) == 0:
            raise ValueError("Cannot enter an empty string")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False