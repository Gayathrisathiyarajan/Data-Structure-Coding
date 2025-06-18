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


# Stack

stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

# Peek
print(stack[-1])

# Pop
stack.pop()
print(stack)

# Check empty
if not stack:
    print("Stack is empty")

# Problem statement 1
# Given valid mathematical expressions in the form of a string. You are supposed to return true if the given expression contains a pair of redundant brackets, else return false. The given string only contains ‘(‘, ’)’, ‘+’, ‘-’, ‘*’, ‘/’ and lowercase English letters.

# Note :
# A pair of brackets is said to be redundant when a subexpression is surrounded by needless/ useless brackets.

# For Example :
# ((a+b)) has a pair of redundant brackets. The pair of brackets on the first and last index is needless. 
# While (a + (b*c)) does not have any pair of redundant brackets. 
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 50
# 3 <= |S| <= 10^4

# Time Limit: 1 sec
# Sample Input 1 :
# 2
# (a+b)
# (a+c*b)+(c))
# Sample Output 1 :
# No
# Yes
# Explanation of Sample Input 1 :
# In the first test case, there are no redundant brackets. Hence, the output is “No”. 

# In the second test case, the brackets around the alphabet ‘c’( index 8 and index 10) are redundant. Hence the output is “Yes”.
# Sample Input 2 :
# 2
# (a*b+(c/d))
# ((a/b))
# Sample Output 2 :
# No
# Yes
# Explanation of Sample Input 2 :
# In the first test case, there are no redundant brackets. Hence, the output is “No”. 

# In the second test case, the brackets around the subexpression “(a+b)” ( index 0 and index 6) are redundant. Hence the output is “Yes”.

def findRedundantBrackets(s: str) -> bool:
    stack = []
    for ch in s:
        if ch == ')':
            top = stack.pop()
            has_operator = False

            while top != '(':
                if top in "+-*/":
                    has_operator = True
                top = stack.pop()

            if not has_operator:
                return True
        else:
            stack.append(ch)
    return False 


# Problem Statement 2
# You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .

# Return true if the given string 'S' is balanced, else return false.

# For example:
# 'S' = "{}()".

# There is always an opening brace before a closing brace i.e. '{' before '}', '(' before ').
# So the 'S' is Balanced.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# [()]{}{[()()]()}
# Sample Output 1 :
# Balanced
# Explanation Of the Sample Input 1 :
# There is always an opening brace before a closing brace i.e. '{' before '}', '(' before '), '[' before ']'.
# So the 'S' is Balanced.
# Sample Input 2 :
# [[}[
# Sample Output 2 :
# Not Balanced
# Constraints:
# 1 <= 'N' <= 10^5

# Where 'N' is the length of the input string 'S'.
# Time Limit: 1 sec


def isValidParenthesis(s: str) -> bool:
    # Write your code here
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop()

    return not stack



# Queue
from collections import deque  

queue = deque() 

# Enqueue
queue.append("Gayu")
queue.append("Gayathri")
queue.append("Chitra")

# Dequeue
print(queue.popleft()) 

# Peek
print(queue[0]) 

# Rear
print(queue[-1])

# Size
print(len(queue))

# Empty Check
print(not queue)



# Problem Statement 1

# Design a data structure to implement deque of size ‘N’. It should support the following operations:

# pushFront(X): Inserts an element X in the front of the deque. Returns true if the element is inserted, otherwise false.

# pushRear(X): Inserts an element X in the back of the deque. Returns true if the element is inserted, otherwise false.

# popFront(): Pops an element from the front of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.

# popRear(): Pops an element from the back of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.

# getFront(): Returns the first element of the deque. If the deque is empty, it returns -1.

# getRear(): Returns the last element of the deque. If the deque is empty, it returns -1.

# isEmpty(): Returns true if the deque is empty, otherwise false.

# isFull(): Returns true if the deque is full, otherwise false.
# Following types of queries denote these operations:

# Type 1: for pushFront(X) operation.
# Type 2: for pushRear(X) operation.
# Type 3: for popFront() operation.
# Type 4: for popRear() operation.
# Type 5: for getFront() operation.
# Type 6: for getRear() operation.
# Type 7: for isEmpty() operation.
# Type 8: for isFull() operation.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= N <= 1000
# 1 <= Q <= 10^5 
# 1 <= P <= 8
# 1 <= X <= 10^5

# Time Limit: 1 sec

# Where ‘N’ represents the size of the deque, ‘Q’ represents the number of queries, ‘P’ represents the type of operation and ‘X’ represents the element.
# Sample Input 1:
# 5 7
# 7
# 1 10
# 1 20
# 2 30
# 5
# 4
# 4
# Sample Output 1:
# True 
# True 
# True
# True
# 20
# 30
# 10
# Explanation 1:
# For the given input, we have the number of queries, Q = 7.
# Operations performed on the deque are as follows:

# isEmpty(): Deque is initially empty. So, this returns true.
# pushFront(10): Insert the element ‘10’ in the front of the deque. This returns true.
# pushFront(20): Insert the element ‘20’ in the front of the deque. This returns true.
# pushRear(30): Insert the element ‘30’ in the back of the deque. This returns true.
# getFront(): Returns the front element of the deque i.e. 20
# popRear(): Pop an element from the back of the deque. This returns 30.
# popRear(): Pop an element from the back of the deque. This returns 10.

# The following image shows the snapshots of the deque after each operation:

# Sample Input 2:
# 2 5
# 1 15
# 2 25
# 1 20
# 8
# 6
# Sample Output 2:
# True
# True
# False
# True
# 25


class Deque:
    def __init__(self, size):
        # Write your code here
        self.size = size
        self.deque = []

    # Pushes 'X' in the front of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushFront(self, x):
        # Write your code here
        if len(self.deque) < self.size:
            self.deque.insert(0, x)
            return True
        return False

    # Pushes 'X' in the back of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushRear(self, x):
        # Write your code here
        if len(self.deque) < self.size:
            self.deque.append(x)
            return True
        return False

    # Pops an element from the front of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popFront(self):
        # Write your code here
        if self.deque:
            return self.deque.pop(0)
        return -1

    # Pops an element from the back of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popRear(self):
        # Write your code here
        if self.deque:
            return self.deque.pop()
        return -1
        

    # Returns the first element of the deque. If the deque is empty, it returns -1.
    def getFront(self):
        # Write your code here
        if self.deque:
            return self.deque[0]
        return -1

    # Returns the last element of the deque. If the deque is empty, it returns -1.
    def getRear(self):
        # Write your code here
        if self.deque:
            return self.deque[-1]
        return -1

    # Returns true if the deque is empty. Otherwise returns false.
    def isEmpty(self):
        # Write your code here
        return len(self.deque) == 0

    # Returns true if the deque is full. Otherwise returns false.
    def isFull(self):
        # Write your code here
        return len(self.deque) == self.size


# Push elements
queue.appendleft(10)  # pushFront
queue.append(20)      # pushRear

# Pop elements
front = queue.popleft() if queue else -1
rear = queue.pop() if queue else -1
print("Front:", front)
print("Rear:", rear)


# Recursion Function

# Print 1 to 5 using recursion
def print_numbers(n):
    if n > 5:
        return
    print(n)
    print_numbers(n + 1)  # recursion happens here

print_numbers(1)


# Problem Statement 1
# You are given three rods (numbered 1 to 3), and ‘N’ disks initially placed on the first rod, one on top of each other in increasing order of size ( the largest disk is at the bottom). You are supposed to move the ‘N’ disks to another rod(either rod 2 or rod 3) using the following rules and in less than 2 ^ (N) moves.

# 1. You can only move one disk in one move. 
# 2. You can not place a larger disk on top of a smaller disk.
# 3. You can only move the disk at the top of any rod.    
# Note :
# You may assume that initially, the size of the ‘i’th disk from the top of the stack is equal to ‘i’, i.e. the disk at the bottom has size ‘N’, the disk above that has size ‘N - 1’, and so on. The disk at the top has size 1.
# Example :

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 5
# 1 <= N <= 12

# Where ‘T’ denotes the number of test cases, ‘N’ denotes the number of disks.

# Time Limit: 1 sec
# Sample Input 1 :
# 2
# 1
# 2
# Sample Output 1 :
# 1
# 1
# Explanation of Sample Input 1 :
# In the first test case, 
# you can move the only disk to either rod 2 or rod 3. The matrix to be returned should be either { { 1, 2 } } or { {1, 3 } }.

# In the second test case, 
# you can move the topmost disk from rod 1 to rod 2. Then move the remaining disk from rod1 to rod 3. Now move the disk in rod 2 to rod 3. . One of the correct ways to return the output is { { 1, 2 }, { 1, 3 }, { 2, 3 } }.  
# Sample Input 2 :
# 1
# 3
# Sample Output 2 :
# 1
# Explanation of Sample Input 2 :
# One of the correct matrices is { { 1, 2 }, { 1, 3 }, { 2, 3 }, { 1, 2 }, { 3, 1 }, { 3, 2 }, { 1, 2 } }.

def towerOfHanoi(n):
    # Write your code here
    # Return a 2-D array
    result = []

    def solve(n, source, destination, auxiliary):
        if n == 0:
            return
        solve(n - 1, source, auxiliary, destination)
        result.append([source, destination])
        solve(n - 1, auxiliary, destination, source)
    solve(n, 1, 3, 2)
    return result


# Problem Statement 2

# Aakash is a member of Ninja club. He has a weird family structure. Every male member (M) gives birth to a male child first and then a female child, whereas every female (F) member gives birth to a female child first and then to a male child. Aakash analyses this pattern and wants to know what will be the Kth child in his Nth generation. Can you help him?

# A sample generation tree is shown, where ‘M’ denotes the male member and ‘F’ denotes the female member. 

# Note
# The generation tree starts with a male member i.e. Aakash. 
# Every member has exactly two children. 
# The given N and K will always be valid. 
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 2
# 2 2 
# 3 4  
# Sample Output 1:
# Female
# Male
# Explanation for Sample Input 1:
# Test Case 1:  2nd child of the 2nd generation is shown in green colour. 

# Test Case 2:  4th child of the 3rd generation is shown in green colour. 

# Sample Input 2:
# 3
# 5 1 
# 3 1
# 4 4  
# Sample Output 2:
# Male
# Male
# Male 

def checkGender(n,k):
    # Write your code here
    if n == 1 or k == 1:
        return True
    if k % 2 == 1:
        return checkGender(n,(k+1)/2)
    else:
        return not checkGender(n,k/2)

def kthChildNthGeneration(n, k):
    if checkGender(n,k) == True:
        return "Male"
    else:
        return "Female"
    
# Problem statement 3
# Problem statement
# You are given the first term (A), the common ratio (R) and an integer N. Your task is to find the Nth term of the GP series.

# The general form of a GP(Geometric Progression) series is A, A(R), A(R^2), A*(R^3) and so on where A is the first term of GP series

# Note :
# As the answer can be large enough, return the answer modulo 10^9 + 7.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10
# 1 <= N <= 10^8
# 0 <= A <= 50 
# 0 <= R <= 100

# Time limit: 1 second
# Sample input 1 :
# 1
# 5 3 2 
# Sample output 1 :
# 48
# Explanation :
# For N=5, A=3, and R=2. The GP series will be 3, 6, 12, 24, 48, and so on. Thus, the 5th term will be 48.  
# Sample input 2 :
# 2
# 4 1 2
# 6 2 1 
# Sample output 2 :
# 8
# 2

import sys
from sys import stdin

def nthTermOfGP(n, a, r):
    #Write your code here
    MOD = 10 ** 9 + 7
    nth_term = (a * pow(r, n-1, MOD)) % MOD
    return nth_term

t = int(sys.stdin.readline().strip())
while(t > 0):   
    n, a, r = map(int,input().split())
    print(nthTermOfGP(n,a,r))
    t = t - 1


# Problem statement 4
# Problem statement
# You have given two positive integers N and K. Your task is to print a series of numbers i.e subtract K from N until it becomes 0 or negative then add K until it becomes N. You need to do this task without using any loop.

# For Example:
# For  N = 5 , K = 2 
# Series = [ 5, 3, 1, -1, 1, 3, 5]
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 100   
# 1 <= N <= 3000 
# 1 <= K <= N 

# Time Limit: 1sec
# Sample Input 1 :
# 2 
# 3 2
# 5 4
# Sample Output 1 :
# 3 1 -1 1 3
# 5 1 -3 1 5
# Explanation For Sample 1:
# For the 1st test case:
# The numbers in the sequence are 3, 3 - 2, 3 - 2 - 2, 3 - 2 - 2 + 2, 3 - 2 - 2 + 2 + 2, which is the same as 3, 1, -1, 1, 3. 

# For the 2nd test case:
# The numbers in the sequence are 5, 5 - 4, 5 - 4 - 4, 5 - 4 - 4 + 4, 5 - 4 - 4 + 4 + 4, which is the same as 5, 1, -3, 1, 5. 
# Sample Input 2 :
# 1
# 4 2
# Sample Output 2 :
# 4 2 0 2 4

def printSeriesHelper(current, n, k, down, result):
    result.append(current)  
    if current <= 0:
        down = False  # Switch direction
    if not down and current == n:
        return
    if down:
        printSeriesHelper(current - k, n, k, down, result)
    else:
        printSeriesHelper(current + k, n, k, down, result)

def printSeries(n, k):
    result = []
    printSeriesHelper(n, n, k, True, result)
    return result  # ? Return the result instead of printing it


# Problem statement 5
# Problem statement
# Given an integer array 'ARR' of size 'N' and an integer 'K', return all the subsets of 'ARR' which sum to 'K'.

# Subset of an array 'ARR' is a tuple that can be obtained from 'ARR' by removing some (possibly all) elements of 'ARR'.

# Note :
# The order of subsets is not important. 

# The order of elements in a particular subset should be in increasing order of the index.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= 'N' <= 16
# - (10 ^ 6) <= ARR[i] <= (10 ^ 6)
# - 16 * (10 ^ 6) <= 'K' <= 16 * (10 ^ 6)

# Where ‘ARR[i]’ denotes the value for ‘ith’ element of the array ‘ARR’ and 'K' is the given sum.

# Time Limit: 1 sec.
# Sample Input 1:
# 3
# 2 4 6
# 6
# Sample Output 1:
# 2 4
# 6
# Explanation of the Sample Input 1:
# For the array'ARR' = {2, 4, 6}, we can have subsets {}, {2}, {4}, {6}, {2, 4}, {2, 6}, {4, 6}, {2, 4, 6}. Out of these 8 subsets, {2, 4} and {6} sum to the given 'K' i.e. 6. 
# Sample Input 2:
# 6 
# 5 -1 8 2 7 0
# 7
# Sample Output 2:
# -1 8 
# -1 8 0 
# 5 2 
# 5 2 0 
# 7 
# 7 0 

def findSubsetsHelper(arr, index, current_subset, current_sum, target, result):
    # Base case
    if index == len(arr):
        if current_sum == target:
            result.append(current_subset[:])  # store a copy of the valid subset
        return
    # Include current element
    current_subset.append(arr[index])
    findSubsetsHelper(arr, index + 1, current_subset, current_sum + arr[index], target, result)
    # Exclude current element (backtrack)
    current_subset.pop()
    findSubsetsHelper(arr, index + 1, current_subset, current_sum, target, result)

def findSubsetsThatSumToK(arr, n, k):
    result = []
    findSubsetsHelper(arr, 0, [], 0, k, result)
    return result


# Recursion and Backtracking

# Problem Statement 1

# You have been given a 9 X 9 2D matrix 'MATRIX' with some cells filled with digits(1 - 9), and some empty cells (denoted by 0).

# You need to find whether there exists a way to fill all the empty cells with some digit(1 - 9) such that the final matrix is a valid Sudoku solution.

# A Sudoku solution must satisfy all the following conditions-

# 1. Each of the digits 1 - 9 must occur exactly once in each row.
# 2. Each of the digits 1 - 9 must occur exactly once in each column.
# 3. Each of the digits 1 - 9 must occur exactly once in each of the 9, 3 x 3 sub-matrices of the matrix.
# Note
# 1. There will always be a cell in the matrix which is empty.
# 2. The given initial matrix will always be consistent according to the rules mentioned in the problem statement.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= 'T' <= 5
# N = 9
# 0 <= MATRIX[i][j] <= 9

# Where 'N' denotes the size of the given square matrix.

# Time Limit: 1sec
# Sample Input 1:
# 1
# 9 0 0 0 2 0 7 5 0 
# 6 0 0 0 5 0 0 4 0 
# 0 2 0 4 0 0 0 1 0 
# 2 0 8 0 0 0 0 0 0 
# 0 7 0 5 0 9 0 6 0 
# 0 0 0 0 0 0 4 0 1 
# 0 1 0 0 0 5 0 8 0 
# 0 9 0 0 7 0 0 0 4 
# 0 8 2 0 4 0 0 0 6
# Sample Output 1:
# yes
# Explanation of the Sample Input1:
# One of the possible solutions is:
# 9 4 1 3 2 6 7 5 8
# 6 3 7 1 5 8 2 4 9
# 8 2 5 4 9 7 6 1 3
# 2 6 8 7 1 4 3 9 5
# 1 7 4 5 3 9 8 6 2
# 3 5 9 6 8 2 4 7 1
# 4 1 3 2 6 5 9 8 7
# 5 9 6 8 7 3 1 2 4
# 7 8 2 9 4 1 5 3 6
# Sample Input 2:
# 1
# 1 5 9 0 0 6 0 3 2
# 2 7 4 0 0 0 0 0 0
# 3 8 6 2 0 0 0 0 5
# 4 9 2 5 0 1 0 8 0
# 6 3 7 0 4 0 0 0 0
# 5 1 0 8 2 0 0 0 0
# 8 2 1 0 0 0 0 0 0
# 7 6 0 1 0 0 4 2 0
# 9 4 3 0 7 0 0 6 1
# Sample Output 2:
# no
# Explanation of the Sample Input2:
# In the third column from the left, there are two empty cells out of which one has to be filled with ‘8’, but we can’t put 8 in any of those two cells.

def isItSudoku(matrix):
    # Write your code here.
    def isValid(matrix, row, col, num):
        # Check if num is in the current row
        for x in range(9):
            if matrix[row][x] == num:
                return False
        # Check if num is in the current column
        for x in range(9):
            if matrix[x][col] == num:
                return False
        # Check if num is in the current 3x3 box
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if matrix[startRow + i][startCol + j] == num:
                    return False
        return True

    def solve(matrix):
        for row in range(9):
            for col in range(9):
                if matrix[row][col] == 0:
                    for num in range(1, 10):
                        if isValid(matrix, row, col, num):
                            matrix[row][col] = num
                            if solve(matrix):
                                return True
                            matrix[row][col] = 0
                    return False
        return True
    return solve(matrix)


# Problem Statement 2

# Given a singly linked list of integers. Your task is to return the head of the reversed linked list.

# For example:
# The given linked list is 1 -> 2 -> 3 -> 4-> NULL. Then the reverse linked list is 4 -> 3 -> 2 -> 1 -> NULL and the head of the reversed linked list will be 4.
# Follow Up :
# Can you solve this problem in O(N) time and O(1) space complexity?
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 5
# 0 <= L <= 10^5
# 1 <= data <= 10^9 and data != -1

# Time Limit: 1 sec
# Sample Input 1 :
# 1
# 1 2 3 4 5 6 -1
# Sample Output 1 :
# 6 5 4 3 2 1 -1
# Explanation For Sample Input 1 :
# For the first test case,  After changing the next pointer of each node to the previous node, The given linked list is reversed.
# Sample Input 2 :
# 1
# 10 21 3 2 4 -1
# Sample Output 2 :
# 4 2 3 21 10 -1


def reverseLinkedList(head):
    # Write your code here.
    prev = None
    curr = head
    while curr:
        next_node = curr.next  
        curr.next = prev       
        prev = curr
        curr = next_node
    return prev



# Problem Statement 3

# Problem statement
# Given a source point (sx, sy) and a destination point (dx, dy), the task is to check if it is possible to reach the destination point using the following valid moves:

# (a, b) -> (a + b, b)
# (a, b) -> (a, a + b)
# Your task is to find if it is possible to reach the destination point using only the desired moves or not.

# For example:
# For the coordinates, source point = (1, 1) and destination point = (3, 5)
# The output will be true as the destination point can be reached using the following sequence of moves:
# (1, 1) -> (1, 2) -> (3, 2) -> (3, 5)
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 100
# 1 <= x, y <= 3000

# Where ‘T’ is the number of test cases and ‘x’, ‘y’ are the coordinates of the given points.

# Time Limit: 1sec
# Sample Input 1:
# 2
# 1 1 3 5
# 1 1 1 4
# Sample Output 1:
# True
# True
# Explanation For Sample Input 1:
# For the first test case
# The output will be true as destination point can be reached using the following sequence of moves:
# (1, 1) -> (1, 2) -> (3, 2) -> (3, 5)

# For the second test case
# The output will be true as destination point can be reached using the following sequence of moves:
# (1, 1) -> (1, 2) -> (1, 3) -> (1, 4)
# Sample Input 2:
# 2
# 1 1 2 2
# 1 1 1 1
# Sample Output 2:
# False
# True

def reachDestination(sx,sy,dx,dy):    
    #Your code goes here
    while dx >= sx and dy >= sy:
        if dx == sx and dy == sy:
            return True
        if dx > dy:
            dx -= dy
        else:
            dy -= dx
    return False


# Problrm Statement 4

# Problem statement
# You are given a 2-D matrix consisting of 0’s and 1’s with ‘N’ rows and ‘N’ columns, you are supposed to find all paths from the cell (0,0) (top-left cell) to the cell (N-1, N-1)(bottom-right cell). All cells with value 0 are blocked and cannot be travelled through while all cells with value 1 are open.

# If you are currently at cell (x,y) then you can move to (x+1,y)(denoted by ‘D’), (x-1,y)(denoted by ‘U’), (x,y+1)(denoted by ‘R’), (x,y-1)(denoted by ‘L’) in one move. You cannot move out of the grid.

# Example :

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 5
# 1 <= N <= 5
# 0 <= ARR[i][j] <= 1

# Where ‘T’ denotes the number of test cases, ‘N’ denotes the number of rows and columns of the given matrix, and ARR[i] denotes the value of the cell (i,j) in the given matrix.

# Time Limit: 1 sec
# Sample Input 1 :
# 2
# 2
# 1 1
# 1 1
# 2
# 1 0
# 1 1
# Sample Output 1 :
# DR RD
# DR
# Explanation of Sample Input 1 :
# In the first test case, there are two paths from (0,0) to (1,1). The first path is (0,0)->(1,0)->(1,1) and the second path is (0,0)->(0,1)->(1,1)

# In the second test case, there is only one path since the cell at (0,1) is blocked. The path is (0,0)->(1,0)->(1,1).
# Sample Input 2 :
# 2
# 3
# 1 0 1
# 1 0 0
# 1 1 1
# 3
# 1 1 1
# 1 0 1
# 1 1 1
# Sample Output 2 :
# DDRR
# DDRR RRDD
# Explanation of Sample Input 2 :
# In the first test case, there is only one path from (0,0) to (2,2). The path is (0,0)->(1,0)->(2,0)->(2,1)->(2,2).

# In the second test case, there are two paths from (0,0) to (2,2). The first path is (0,0)->(1,0)->(2,0)->(2,1)->(2,2). and the second path is (0,0)->(0,1)->(0,2)->(1,2)->(2,2).

def findAllPaths(arr):
    # Write your code here
    # Return all paths
    def dfs(x, y, path):
        if x == n - 1 and y == n - 1:
            res.append(path)
            return
        vis[x][y] = True
        for dx, dy, move in [(1,0,'D'), (0,-1,'L'), (0,1,'R'), (-1,0,'U')]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and arr[nx][ny]:
                dfs(nx, ny, path + move)
        vis[x][y] = False

    n = len(arr)
    res, vis = [], [[False]*n for _ in range(n)]
    if arr[0][0]: dfs(0, 0, "")
    return sorted(res)


# Problem Statement 5

# Problem statement
# The N Queens puzzle is the problem of placing N chess queens on an N * N chessboard such that no two queens attack each other.

# Given an integer ‘N’, print all distinct solutions to the ‘N’ queen puzzle.

# Two queens on the same chessboard can attack each other if any of the below condition satisfies:  
# 1. They share a row. 
# 2. They share a column. 
# 3. They share a diagonal. 
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 1
# 4   
# Sample Output 1:
# 0 0 1 0 1 0 0 0 0 0 0 1 0 1 0 0
# 0 1 0 0 0 0 0 1 1 0 0 0 0 0 1 0 
# Explanation for Sample Input 1:
# The 4 queens can be placed in two ways in a 4*4 chessboard. Both the configurations are shown in the below figure. 

# The chessboard matrix for the first configuration looks as follows:-
# 0 0 1 0
# 1 0 0 0
# 0 0 0 1
# 0 1 0 0
# Queen contained cell is depicted by 1. As we can see, No queen is in the same row, column or diagonal of the other queens. Hence this is a valid configuration.

# Similarly, the chessboard matrix for the second configuration looks as follows:-
# 0 1 0 0
# 0 0 0 1
# 1 0 0 0
# 0 0 1 0
# Queen contained cell is depicted by 1. As we can see, No queen is in the same row, column or diagonal of the other queens. Hence this is also a valid configuration.

# These are the only two valid configurations for 4-Queens. 
# Sample Input 2:
# 1
# 3
# Sample Output 2:
# Explanation of Sample Input 2:
# Since no possible configuration exists for 3 Queen's, the output remains empty. 


def nQueens(n):
    # Write your code here
    def solve(r, board, c, d1, d2):
        if r == n:
            res.append(sum(board, []))
            return
        for i in range(n):
            if i not in c and r - i not in d1 and r + i not in d2:
                solve(r + 1, board + [[0]*i + [1] + [0]*(n - i - 1)], 
                      c | {i}, d1 | {r - i}, d2 | {r + i})
    res = []
    solve(0, [], set(), set(), set())
    return res


# Problem Statement 6
# Problem statement
# Given a string S containing digits from 2 to 9 inclusive. Your task is to find all possible letter combinations that the number could represent.

# A mapping from Digits to Letters (just like in Nokia 1100) is shown below. Note that 1 does not map to any letter.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10 
# 1 <= |S| <= 10 
# 2 <= S[i] <=9  

# Where |S| is the length of string 'S" and 'S[i]' represents the element of the string S. 

# Time Limit: 1 sec
# Sample Input 1:
# 1 
# 23
# Sample Output 1:
# ad ae af bd be bf cd ce cf
# Explanation of sample input 1:
# The letters corresponding to 2 are ‘a’, ‘b’, ‘c’ and corresponding to 3 are ‘d’, ‘e’, ‘f’. All the possible letter combinations for “23” will be "ad","ae","af","bd","be","bf","cd","ce","cf".
# Sample Input 2:
# 1
# 2
# Sample Output 2:
# a b c
# Explanation of sample input 2:
# The letters corresponding to 2 are ‘a’, ‘b’, ‘c’.

def combinations(s):
    # Write your code here
    if not s:
        return []

    digit_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index, path):
        if index == len(s):
            result.append(path)
            return
        for char in digit_map[s[index]]:
            backtrack(index + 1, path + char)

    backtrack(0, "")
    return result


# Problem Statement 7

# Problem statement
# You are a coach of a group consisting of 'N' students. The ith student has a strength Arr[i]. For a Tug of War game, you want to divide students into two teams of equal size (If N is odd, then size of one team should be (N-1)/2 and size of other team should be (N+1)/2). You want a game that is fun, for this the absolute difference between the team’s strength should be as minimum as possible. A team's strength is the sum of the strengths of the students in the team.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10
# 2 <= N <= 20
# 0 < Arr[i] <= 10^5
# Where T is the number of test cases, N is the number of students and Arr[i] is the strength of ith student.
# Sample Input 1:
# 3
# 4
# 1 2 3 4
# 3
# 4 2 1
# 2
# 6 8
# Sample Output 1:
# 0
# 1
# 2
# Explanation for Sample Input 1:
# In the 1st test case, the first team contains students with strength {1, 4} and the second team contains students with strength {2, 3}, the absolute difference between the team’s strength is (1+5)-(2+3)=0.

# In the 2nd test case, the first team contains students with strength {1, 2} and the second team contains students with strength {4}, the absolute difference between the team’s strength is (4)-(1+2)=1.

# In the 3rd test case, the first team contains students with strength {6} and the second team contains students with strength {8}, the absolute difference between the team’s strength is (8)-(6)=2.
# Sample Input 2:
# 2
# 3
# 10 10 10
# 4
# 10 1 2 5
# Sample Output 2:
# 10
# 4

def tugOfWar(arr, n):
    # write your code here
    total = sum(arr)
    min_diff = [float('inf')]

    def helper(i, team1, team2, sum1, sum2):
        if i == n:
            if abs(len(team1) - len(team2)) <= 1:
                min_diff[0] = min(min_diff[0], abs(sum1 - sum2))
            return
        if len(team1) < (n + 1) // 2:
            helper(i + 1, team1 + [arr[i]], team2, sum1 + arr[i], sum2)
        if len(team2) < (n + 1) // 2:
            helper(i + 1, team1, team2 + [arr[i]], sum1, sum2 + arr[i])

    helper(0, [], [], 0, 0)
    return min_diff[0]


# Problem Statement 8

# Problem statement
# You are given an array of integers "ARR" of length 'N' and an integer 'K'. Your task is to find whether or not you can divide the array "ARR" into 'K' subsets with equal sum.

# A subset of an array "ARR" is another array whose every element is present in array "ARR".

# For example:
# If ARR = {1, 2, 3, 4}, then array {3,4} is a subset of "ARR" because both 3 and 4 are also elements of "ARR".
# For example:

# Consider array ARR = {3, 5, 2, 4, 4} and K = 2, i.e. you have to divide "ARR" into 2 subsets with equal sum. The division will be {4, 5} and {2, 3, 4} with sum 9.
# Note:

# Every element of the array must occupy only one subset.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 3 
# 5 2
# 3 5 2 4 4
# 9 6 
# 1 9 6 8 6 9 9 9 9
# 7 4
# 4 4 4 1 1 1 1
# Sample Output 1:
# TRUE
# FALSE
# TRUE
# Explanation For Sample Input 1:
# For first case, 
# Array can be divided into 2 subsets as {2, 3, 4} and {4, 5} with sum 9.

# For the second case,
# Array can not be divided into 6 subsets with equal sum.

# For the third case, 
# Array can be divided into 4 subsets as {4}, {4}, {4} and {1, 1, 1, 1} with sum 4.
# Sample Input 2:
# 5
# 10 5
# 1 2 3 4 5 6 7 8 9 10
# 7 7
# 7 7 7 7 7 7 7
# 7 3
# 1 2 3 4 5 6 7
# 5 2
# 3 5 7 11 13
# 3 5
# 1 2 3
# Sample Output 2:
# TRUE
# TRUE
# FALSE
# FALSE
# FALSE

def splitArray(arr,k):
    
    total_sum = sum(arr)
    n = len(arr)

    if total_sum % k != 0:
        return False

    target = total_sum // k
    used = [False] * n

    def backtrack(start, k, curr_sum):
        if k == 0:
            return True
        if curr_sum == target:
            return backtrack(0, k - 1, 0)

        for i in range(start, n):
            if not used[i] and curr_sum + arr[i] <= target:
                used[i] = True
                if backtrack(i + 1, k, curr_sum + arr[i]):
                    return True
                used[i] = False
        return False

    arr.sort(reverse=True)  # optimization to help early pruning
    return backtrack(0, k, 0)
    return

# Problem Statement 9 -  Binary strings with no consecutive 1s.

# Problem statement
# You have been given an integer 'N'. Your task is to generate and return all binary strings of length 'N' such that there are no consecutive 1's in the string.

# A binary string is that string which contains only ‘0’ and ‘1’.

# For Example:
# Let ‘N'=3, hence the length of the binary string would be 3. 

# We can have the following binary strings with no consecutive 1s:
# 000 001 010 100 101 
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 4
# Sample Output 1:
# 0000 0001 0010 0100 0101 1000 1001 1010 
# Explanation of sample input 1:
# For N = 4 we get the following Strings:

# 0000 0001 0010 0100 0101 1000 1001 1010 

# Note that none of the strings has consecutive 1s. Also, note that they are in a lexicographically increasing order.
# Sample Input 2:
# 2
# Sample Output 2:
# 00 01 10
# Constraints:
# 1 <= 'N' <= 20
# Time limit: 1 second

from typing import List

def generateString(N: int) -> List[str]:
    # write your code here
    result = []
    def backtrack(current: str, last_char: str):
        if len(current) == N:
            result.append(current)
            return
        # Always can add '0'
        backtrack(current + '0', '0')
        # Add '1' only if last character is not '1'
        if last_char != '1':
            backtrack(current + '1', '1')
    backtrack("", '0')  # Start with empty string and last_char='0'
    return result


# Problem Statement 10 -  Reverse Stack Using Recursion.
# Problem statement
# Reverse a given stack of 'N' integers using recursion. You are required to make changes in the input parameter itself.

# Note: You are not allowed to use any extra space other than the internal stack space used due to recursion.

# Example:
# Input: [1,2,3,4,5] 
# Output: [5,4,3,2,1]

# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 3
# 2 1 3
# Sample Output 1 :
# 3 1 2
# Explanation to Sample Input 1 :
# Reverse of a give stack is 3 1 2 where first element becomes last and last becomes first.                   
# Sample Input 2 :
# 2
# 3 2
# Sample Output 2 :
# 2 3
# Constraints :
# 0 <= N <= 10^3
# Where 'N' is the number of elements in the given stack.

# Time Limit: 1 sec

def reverseStack(stack: List[int]) -> None:
    # Write your code here.
    if stack:
        x = stack.pop()
        reverseStack(stack)
        stack.insert(0, x)

# Problem Statement 11 -   Closest Distance Pair.

# Problem statement
# You are given an array containing 'N' points in the plane. The task is to find out the distance of the closest points.

# Note :
# Where distance between two points (x1, y1) and (x2, y2) is calculated as [(x1 - x2) ^ 2] + [(y1 - y2) ^ 2].
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 2 <= 'N' <= 10^5
# -10^5 <= 'x' <= 10^5 
# -10^5 <= 'y' <= 10^5

# Time Limit: 1 sec
# Sample Input 1:
# 5
# 1 2
# 2 3
# 3 4
# 5 6
# 2 1
# Sample Output 1:
# 2
# Explanation of Sample Output 1:
# We have 2 pairs which are probable answers (1, 2) with (2, 3) and (2, 3) with (3, 4). The distance between both of them is equal to 2.
# Sample Input 2 :
# 3
# 0 0
# -3 -4
# 6 4
# Sample Output 2 :
# 25
# Explanation of Sample Output 1 :
# If we choose the pairs (0, 0) and (-3, -4), the distance between them is 3^2 + 4^2 = 25. This is the optimal answer for this test case.

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

def closest_util(px, py):
    n = len(px)
    if n <= 3:
        min_d = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                min_d = min(min_d, dist(px[i], px[j]))
        return min_d

    mid = n // 2
    mid_point = px[mid]

    pyl = list()
    pyr = list()

    for point in py:
        if point.x < mid_point.x or (point.x == mid_point.x and point in px[:mid]):
            pyl.append(point)
        else:
            pyr.append(point)

    dl = closest_util(px[:mid], pyl)
    dr = closest_util(px[mid:], pyr)
    d = min(dl, dr)

    strip = [p for p in py if abs(p.x - mid_point.x) < d]
    min_d_strip = d
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            min_d_strip = min(min_d_strip, dist(strip[i], strip[j]))

    return min_d_strip

def closestPair(cordinates, n):
    px = sorted(cordinates, key=lambda p: (p.x, p.y))
    py = sorted(cordinates, key=lambda p: (p.y, p.x))
    return closest_util(px, py)

# Fast input
def takeInput():
    n = int(input().strip())
    if n == 0:
        return [], n
    cordinates = [point(0, 0) for _ in range(n)]
    for i in range(n):
        arr = list(map(int, stdin.readline().strip().split()))
        cordinates[i] = point(arr[0], arr[1])
    return cordinates, n

# main
cordinates, n = takeInput()
print(closestPair(cordinates, n))

# Problem Statement 12 -   All Possible Permutations - String

# Problem statement
# You are given an input string 'S'. Your task is to find and return all possible permutations of the input string.

# Note:
# 1. The input string may contain the same characters, so there will also be the same permutations.

# 2. The order of permutation does not matter.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# cba
# Sample Output 1:
# abc
# acb
# bac
# bca
# cab
# cba
# Explanation for Sample Output 1:
# All the possible permutations for string "cba" will be "abc", "acb", "bac", "bca", "cab" and "cba".
# Sample Input 2:
# xyx
# Sample Output 2:
# xyx
# xxy
# yxx
# yxx
# xyx
# xxy
# Explanation for Sample Output 2:
# All the possible permutations for string "xyx" will be "xyx", "xxy", "yxx", "yxx", "xyx" and "xxy". Here, all three permutations "xyx", "yxx", "xxy" are repeating twice but we need to print all the possible permutations and hence we are printing them twice..

def findPermutations(s):
    def backtrack(path, used):
        if len(path) == len(s):
            result.append(''.join(path))
            return
        for i in range(len(s)):
            if not used[i]:
                used[i] = True
                path.append(s[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

    result = []
    backtrack([], [False]*len(s))
    return result

# Problem Statement 12 - Generate Parentheses

# Problem statement
# Given N pairs of parentheses, write a function to generate and print all combinations of well-formed parentheses. That is, you need to generate all possible valid sets of parentheses that can be formed with a given number of pairs.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= N <= 10

# Time Limit: 1sec
# Sample Input 1:
# 3
# Sample Output 1:
# {{{}}}
# {{}{}}
# {{}}{}
# {}{{}}
# {}{}{}
# Explanation For Sample Input 1:
# These are the only five sequences of balanced parentheses formed using 3 pairs of balanced parentheses.
# Sample Input 2:
# 2
# Sample Output 2:
# {{}}
# {}{}

def printParantheses(n):
    def Parantheses(current, open_count, close_count, max_pairs):
        if len(current) == max_pairs * 2:
            print(current)
            return
        if open_count < max_pairs:
            Parantheses(current + '{', open_count + 1, close_count, max_pairs)
        if close_count < open_count:
            Parantheses(current + '}', open_count, close_count + 1, max_pairs)

    Parantheses('', 0, 0, n)

# Problem Statement 13 -  Restore IP Addresses

# Problem statement
# You are given a string 'S' containing only digits. Your task is to find all possible IP addresses that can be obtained from string 'S' in lexicographical order.

# Note:
# A valid IP address consists of exactly four integers, each integer is between 0 and 255 separated by single dots, and cannot have leading zeros except in the case of zero itself.
# For example:
# The following are valid IP addresses:
# 0.1.24.255
# 18.5.244.1

# Following are invalid IP addresses:
# 0.01.24.255  (as  01  contains one leading zero).
# 18.312.244.1 (as 312 not lies between 0 and 255).
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 1000
# 1 <= |S| <= 15

# Where |'S'| denotes the length of string 'S' and 'S' contains only digits from 0 to 9.

# Time Limit: 1 sec
# Note:
# You do not need to print anything, it has already been taken care of. Just implement the given function.
# Sample Input 1 :
# 2 
# 2122
# 23579
# Sample Output 1 :
# [“2.1.2.2”]
# [“2.3.5.79”, “2.3.57.9”, “2.35.7.9”, “23.5.7.9”]
# Explanation for sample Input 1:
# For the first test case, there is only one possible IP address that is [2.1.2.2]

# For the second test case, all possible IP addresses are shown below.
# [2.3.5.79], [2.3.57.9], [2.35.7.9], [23.5.7.9]
# Sample Input 2 :
# 2
# 123
# 02300
# Sample Output 2 :
# []
# [“0.2.30.0”, “0.23.0.0”]
# Explanation for sample Input 2:
# For the first test case, there is no possible IP address. Therefore then answer is []

# For the second test case, there are only 2 possible IP addresses are shown below.
# [0.2.30.0], [0.23.0.0]


def generateIPAddress(s):
    result = []
    def isValid(part):
        if len(part) > 1 and part[0] == '0':
            return False
        return 0 <= int(part) <= 255

    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                result.append('.'.join(path))
            return
        for length in range(1, 4):
            if start + length <= len(s):
                part = s[start:start + length]
                if isValid(part):
                    backtrack(start + length, path + [part])
    backtrack(0, [])
    result.sort()  # Lexicographical order
    return result

# Problem Statement 14 -  Subsequences of String

# Problem statement
# You are given a string 'STR' containing lowercase English letters from a to z inclusive. Your task is to find all non-empty possible subsequences of 'STR'.

# A Subsequence of a string is the one which is generated by deleting 0 or more letters from the string and keeping the rest of the letters in the same order.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10 
# 1 <=  |STR| <= 16

# Where |STR| represents the length of the string 'STR'.

# Time Limit: 1 sec
# Sample Input 1:
# 1 
# abc
# Sample Output 1:
# a ab abc ac b bc c
# Explanation of sample input 1:
# All possible subsequences of abc are :  
# “a” , “b” , “c” , “ab” , “bc” , “ac”, “abc”
# Sample Input 2:
# 1
# bbb
# Sample Output 2:
# b b b bb bb bb bbb

def subsequences(s):
    result = []
    def backtrack(index, path):
        if index == len(s):
            if path:
                result.append(path)
            return
        # Include s[index]
        backtrack(index + 1, path + s[index])
        # Exclude s[index]
        backtrack(index + 1, path)
    backtrack(0, "")
    return result

# Problem Statement 14 -  Combination Sum
# Problem statement
# You are given an array 'ARR' of 'N' distinct positive integers. You are also given a non-negative integer 'B'.

# Your task is to return all unique combinations in the array whose sum equals 'B'. A number can be chosen any number of times from the array 'ARR'.

# Elements in each combination must be in non-decreasing order.

# For example:
# Let the array 'ARR' be [1, 2, 3] and 'B' = 5. Then all possible valid combinations are-

# (1, 1, 1, 1, 1)
# (1, 1, 1, 2)
# (1, 1, 3)
# (1, 2, 2)
# (2, 3)
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 3 8
# 2 3 5
# Sample Output 1:
# Yes
# Explanation Of Sample Input 1 :
# All possible valid combinations are:
# 2 2 2 2
# 2 3 3
# 3 5
# Sample Input 2 :
# 3 5
# 1 2 3 
# Sample Output 2:
# Yes
# Constraints:
# 1 <= 'N' <= 15
# 1 <= 'B' <= 20
# 1 <= 'ARR[i]' <= 20

# Time Limit: 1sec

def combSum(ARR, B):
    def CombinationSum(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(ARR)):
            if ARR[i] > target:
                continue
            path.append(ARR[i])
            CombinationSum(i, target - ARR[i], path)  # Reuse same element
            path.pop()

    ARR.sort()
    result = []
    CombinationSum(0, B, [])
    return result