#getting name input
name = input("Enter your name: ")

def remove_non_letters(text):
    """Remove any character that isn't a letter"""
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters += all_letters.upper()

    clean_text = ""
    for char in text:
        if char in all_letters:
          clean_text += char  
    return clean_text


def palindrome_test(sample):
    """Reversing the argument then testing if it is the same as original"""
    #remove non-letters
    sample = remove_non_letters(sample)
    #make it lowercase
    sample = sample.lower()
    #removes spaces
    # new_sample = sample.replace(" ","") - redundant with removing non-letters
    #reverses characters
    reverse = sample[::-1]
    #testing to see if forward = reverse, and printing the response
    if reverse == sample:
        print("Is a palindrome")
    else:
        print("Is not a palindrome")

palindrome_test(name)



# def palin_test(word):
#     """using indexes (indices?) to determine palindrome validity"""
#     #setting counter
#     x = 0
#     #setting judgment variable. this feels weird, there must be a better way to do this
#     judge = ''
#     #removing non-letters
#     word = remove_non_letters(word)
#     #make lowercase
#     word = word.lower()
#     # word = word.replace(" ","") - redundant due to removing non-letters
#     while x < len(word):
#         if word[x] != word[-x - 1]:
#             judge = "Is not a palindrome"
#             break
#         else:
#             judge = "Is a palindrome"
#         x += 1
#     print(judge)
#     return

# palin_test(name)
        