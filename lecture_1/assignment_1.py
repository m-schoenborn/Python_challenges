list_of_elements = ['a', 'b', 'c', 1]

def element_in_list(x):
    if x in list_of_elements:
        print(x + " is in the list!")
    else:
        print(x + " is not in the list.")

input = input("Find out if this is in the list: ")
print(element_in_list(input))
print('\n')


def isPalindrome(s):
    return s == s[::-1]

s = "otto"
ans = isPalindrome(s)

if ans:
    print("Yes, " + s + " is a palindrome")
else:
    print("No, " + s + " is not a palindrome")

