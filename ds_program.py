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

