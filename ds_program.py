# Array
numbers = ['hi', 20, 30, 40]
print(numbers[0])
print(numbers[2])

# Accessing
arr = [
  [ [1, 2], [3, 4] ],
  [ [5, 6], [7, 8] ]
]
print(arr[1][0][1])

names = ["Gayathri", "Babu", 1]
print(names)


for i in range(0,2,-1):
   print("Hello")

# To check   
print('s' in 'saif')

# Add elementss
arr = [10, 20, 30]
arr.append(40)
print(arr)


# 1st program

# Problem statement
# You are given an array ‘arr’ containing ‘n’ integers. You are also given an integer ‘num’, and your task is to find whether ‘num’ is present in the array or not.

# If ‘num’ is present in the array, return the 0-based index of the first occurrence of ‘num’. Else, return -1.

# Example:
# Input: ‘n’ = 5, ‘num’ = 4 
# 'arr' =  [6,7,8,4,1] 

# Output: 3

# Explanation:
# 4 is present at the 3rd index.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 5 4
# 6 7 8 4 1
# Sample Output 1 :
# 3
# Explanation Of Sample Input 1:
# 4 is present at the 3rd index.
# Sample Input 2:
# 4 2
# 2 5 6 2
# Sample Output 2 :
# 0
# Explanation Of Sample Input 1:
# 2 is not present in the given array.
# Expected time complexity:
# The expected time complexity is O(n).
# Constraints:
# 1  <= 'n' <= 10^6
# 1 <= 'arr'[i] <= 1000
# Time Limit: 1 sec

def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    for i in range(n):
        if arr[i] == num:
            return i
    return -1
    pass


# 2nd program
# Problem statement
# Given an array of size N, find the sum of its elements.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= n <= 100000
# -10000 <= ai <= 10000
# Output Format
# In single line, print one integer : sum of all the elements in the array
# Sample Input 1:
# 5
# 1 2 3 4 5 
# Sample Output 1:
# 15
# Sample Input 2:
# 4
# -1 5 3 0
# Sample Output 2:
# 7

# your code goes here
n = int(input())
arr = list(map(int, input().split()))
total=0
for num in arr:
    total += num
print(total)



# 3rd program

# Problem statement
# Given an array ‘arr’ of size ‘n’ find the largest element in the array.

# Example:

# Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]

# Output: 5

# Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample input 1:
# 6
# 4 7 8 6 7 6 
# Sample output 1:
# 8
# Explanation of sample input 1:
# The answer is 8.
# From {4 7 8 6 7 6}, 8 is the largest element.
# Sample input 2:
# 8
# 5 9 3 4 8 4 3 10 
# Sample output 2:
# 10
# Expected Time Complexity:
# O(n), Where ‘n’ is the size of an input array ‘arr’.
# Constraints :
# 1 <= 'n' <= 10^5
# 1 <= 'arr[i]' <= 10^9

# Time Limit: 1 sec


from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    # Write your code from here.
    large_element = arr[0]
    for i in range(1, n):
        if arr[i] > large_element:
            large_element = arr[i]
    return large_element
    pass


# Strings

# Creating a String
name = "Gayathri"
print(name)

# Accessing Characters in a String
print(name[3])

# Traversing String
for i in name:
    print(i)

# Find String Length
print(len(name))

# String Concatenation
a = "Data"
b = "Structure"
print(a + " " + b)

# String Slicing
city = "Chennai"
print(city[0:3])
print(city[:4])
print(city[3:])  # 3rd index to end
print(city[:])   # full string
print(city[-3:]) # Last 3 letters
print(city[::2]) # Every 2nd character

# Modify String
a= "Hello gayathri"
print(a.upper()) # Convert to UPPERCASE
print(a.lower()) # Convert to lowercase
print(a.title()) # First letter capital in every word
print(a.capitalize())  # Only 1st letter capital
print(a.swapcase())  # Upper → Lower, Lower → Upper

# Searching String
text = "Gayathri"
print("ri" in text) 

# Replacing String
text = "Hi Gayu"
print(text.replace("Gayu", "Gayathri")) 

# Splitting a string
data = "apple,banana,orange"
print(data.split(","))


# Problem 1

# Problem statement
# You are given a string 'STR'. You have to convert the first alphabet of each word in a string to UPPER CASE.

# For example:

# If the given string 'STR' = ”I am a student of the third year” so you have to transform this string to ”I Am A Student Of The Third Year"
# Note:

# 'STR' will contains only space and alphabets both uppercase and lowercase. The words will be separated by space.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= 'T' <= 10
# 1 <= |STR| <= 10^5

# Where |STR| denotes the length of the string.

# Time Limit: 1 sec
# Sample Input 1 :
# 3
# I love programming
# they are playing cricket
# good to see you
# Sample Output 1 :
# I Love Programming
# They Are Playing Cricket
# Good To See You
# Explanation of The Sample Input 1:
# For the first test case:
# Given string is “I love programming” we will convert every letter after space to uppercase to give the output as ”I Love Programming”.

# For the second test case:
# Given string is “they are playing cricket” we will convert every letter after space to uppercase to give the output as  “They Are Playing Cricket”. 

# For the third test case:
# Given string is “good to see you” we will convert every letter after space to uppercase to give the output as “Good To See You”. 
# Sample Input 2 :
# 3
# why you are confused
# Its a good day to be here
# go and do your work
# Sample Output 2 :
#  Why You Are Confused
#  Its A Good Day to Be Here
#  Go And Do Your Work

def convertString(str):
    # Write your code here
    words = str.split()
    result = []
    for w in words:
        if w:
            # Capitalize first character only, keep rest as-is
            new_word = w[0].upper() + w[1:]
            result.append(new_word)
        else:
            result.append(w)
    return ' '.join(result)


# Problem 2

# Problem statement
# You are given two non-negative integers, ‘NUM1’ and ‘NUM2’, in the form of strings. Return the sum of both strings.

# Note :
# You do not need to print anything, it has already been taken care of. Just implement the given function.
# Example:
# Let ‘NUM1’ be: “5”
# Let ‘NUM2’ be: “21”
# The sum of both numbers will be: “26”.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10
# 1 <= |NUM1|, |NUM2| <= 10^5

# NUM1 and NUM2 don’t have leading zeroes.
# Where |NUM1| and |NUM2| denote the length of the respective strings.

# Time limit: 1 sec
# Sample Input 1 :
# 2
# 5 21
# 10 9
# Sample output 1 :
# 26
# 19
# Explanation For Sample Output 1 :
# For the first test case:
# The sum of both numbers will be: “26”.

# For the second test case:
# The sum of both numbers will be: “19”.
# Sample Input 2 :
# 2
# 9 9
# 21 10
# Sample output 2 :
# 18
# 31

def stringSum(num1: str, num2: str) -> str:
    # Write your code here.\
    c = int(num1)
    d = int(num2)
    return c + d
    pass


# Linked List

# Problem statement 1

# You are given a Singly Linked List of integers with a head pointer. Every node of the Linked List has a value written on it.

# A sample Linked List:

# Now you have been given an integer value, 'K'. Your task is to check whether a node with a value equal to 'K' exists in the given linked list. Return 1 if node exists else return 0.

# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 3 6 2 7 9 -1
# 2
# Sample Output 1:
# 1
# Explanation for Sample Input 1:
# As value 2 exists in the given linked list. So we will return 1 in this case.

# Sample Input 2:
# 1 2 3 7 -1
# 7
# Sample Output 2:
# 1
# Explanation for Sample Input 2:
# As the value 7 exists in the Linked List, our answer is 1.

# Expected Time Complexity:
# Try solving this in O(L).

# Constraints:
# 1 <= 'L' <= 10^5
# 1 <= 'data' <= 10^9 and 'data' != -1
# 1 <= 'K' <= 10^9   

# Where 'L' represents the total number of nodes in the Linked List, 'data' represents the value at each node, and 'K' is the given integer.

# Time Limit: 1 sec.

def searchInLinkedList(head, k):
    # Your code goes here.
    current = head
    while current is not None:
        if current.data == k:
            return 1
        current = current.next
    return 0


# Problem Statement 2

# Given a singly linked list of 'N' nodes. The objective is to determine the middle node of a singly linked list. However, if the list has an even number of nodes, we return the second middle node.

# Note:
# 1. If the list is empty, the function immediately returns None because there is no middle node to find.
# 2. If the list has only one node, then the only node in the list is trivially the middle node, and the function returns that node.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 5
# 1 2 3 4 5
# Sample Output 1 :
# 3 4 5
# Explanation Of Sample Input 1 :

# We can clearly see that there are 5 elements in the linked list therefore the middle node is the node with value '3'.
# Sample Input 2 :
# 6
# 1 2 3 4 5 6
# Sample Output 2 :
# 4 5 6
# Explanation Of Sample Input 2 :

# We can clearly see that there are 6 elements in the linked list and the middle nodes are  nodes with values 3 and 4 hence we return a second middle node having value '4'.
# Constraints :
# 1 <= 'N' <= 10^4
# 0 <= 'data' <= 10^3 

# Where 'N' is the length of the linked list.
# Time Limit: 1 sec

def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# Problem Statement 3

# You are given a Singly Linked List of integers. You need to reverse the Linked List by changing the links between nodes.

# Note :
# You do not need to print anything, just return the head of the reversed linked list. 
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= 'N' <= 10^4
# 0 <= 'data' <= 10^9

# Where 'N' is the number of nodes in the linked list.

# Time Limit: 1 sec
# Sample Input 1 :
# 1 2 4 -1
# Sample Output 1 :
# 4 2 1 -1
# Explanation for Sample Input 1 :
# 1->2->4 is the initial linked list. If we reverse this, we get 4->2->1.
# Sample Input 2 :
# 1
# 1 1 1 -1
# Sample Output 2 :
# 1 1 1 -1

def reverseLinkedList(head):
    # write your code here
    prev = None
    current = head
    while current:
        next_node  = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
