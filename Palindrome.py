#getting name input
name = input("Enter your name: ")

def palindrome_test(sample):
    """Reversing the argument then testing if it is the same as original"""
    sample = sample.lower()
    new_sample = sample.replace(" ","")
    reverse = new_sample[::-1]
    if reverse == new_sample:
        print("Is a palindrome")
    else:
        print("Is not a palindrome")

palindrome_test(name)



# def palin_test(word):
#     x = 0
#     judge = ''
#     while x < len(word):
#         print(word[x])
#         print(judge)
#         if word[x] == word[-x - 1]:
#             judge == True
#         else:
#             judge == False
#             break
#         x += 1
#         return

# palin_test(name)
        