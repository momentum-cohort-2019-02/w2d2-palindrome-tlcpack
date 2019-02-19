#getting name input
name = input("Enter your name: ")

# def palindrome_test(sample):
#     """Reversing the argument then testing if it is the same as original"""
#     #make it lowercase
#     sample = sample.lower()
#     #removes spaces
#     new_sample = sample.replace(" ","")
#     #reverses characters
#     reverse = new_sample[::-1]
#     #testing to see if forward = reverse, and printing the response
#     if reverse == new_sample:
#         print("Is a palindrome")
#     else:
#         print("Is not a palindrome")

# palindrome_test(name)



def palin_test(word):
    x = 0
    judge = ''
    word = word.lower()
    while x < len(word):
        if word[x] != word[-x - 1]:
            print("Is not a palindrome")
        else:
            print("Is a palindrome")
        x += 1
        return

palin_test(name)
        