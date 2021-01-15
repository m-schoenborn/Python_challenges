#check if element is in list
list_of_elements = ['a', 'b', 'c', 1]

def element_in_list(x):
    if x in list_of_elements:
        print(x + " is in the list!")
    else:
        print(x + " is not in the list.")

input = input("Find out if this is in the list: ")
print(element_in_list(input))
print('\n')

#check if word is palindrome
def isPalindrome(s):
    return s == s[::-1]

s = "otto"
ans = isPalindrome(s)

if ans:
    print("Yes, " + s + " is a palindrome")
else:
    print("No, " + s + " is not a palindrome")

# list returning length of string
l = ['I love','ESCP','and','Math']
length = list(map(lambda x : len(x),l))
print(length)

#return whether number is even or not
li = [1,3,5,8,9,12,13]
even = list(map(lambda x : x%2 == 0,li ))
print(even)

#introducing class
class MyOtherClass:
    num = 12345
    def __init__(self, num=0):
        self.num = num

x = MyOtherClass()
print(x.num)

class Dog:
    kind = 'Canine' #class variable shared by all instances
    def __init__(self, name):
        self.name = name #instance variable unique to each instance

a = Dog('Astro')
b = Dog('Buddy')
print(a.kind)
print(b.kind)

#calculate area of rectangle
class Rectangle():
    def __init__(self, l = 0, w = 0):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length * self.width

newRectangle = Rectangle(10,10)
print(newRectangle.rectangle_area())
