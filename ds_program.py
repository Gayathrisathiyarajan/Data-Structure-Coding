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

def findAllPaths(arr):
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

def nQueens(n):
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

    arr.sort(reverse=True) 
    return backtrack(0, k, 0)
    return

# Problem Statement 9 -  Binary strings with no consecutive 1s.

# Problem statement
# You have been given an integer 'N'. Your task is to generate and return all binary strings of length 'N' such that there are no consecutive 1's in the string.

# A binary string is that string which contains only ‘0’ and ‘1’.

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
        if last_char != '1':
            backtrack(current + '1', '1')
    backtrack("", '0')  # Start with empty string and last_char='0'
    return result


# Problem Statement 10 -  Reverse Stack Using Recursion.
# Problem statement
# Reverse a given stack of 'N' integers using recursion. You are required to make changes in the input parameter itself.

# Note: You are not allowed to use any extra space other than the internal stack space used due to recursion.

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


def generateIPAddress(s):
    result = []
    def IPAddress(part):
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
                if IPAddress(part):
                    backtrack(start + length, path + [part])
    backtrack(0, [])
    result.sort()
    return result

# Problem Statement 14 -  Subsequences of String

# Problem statement
# You are given a string 'STR' containing lowercase English letters from a to z inclusive. Your task is to find all non-empty possible subsequences of 'STR'.

# A Subsequence of a string is the one which is generated by deleting 0 or more letters from the string and keeping the rest of the letters in the same order.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10 
# 1 <=  |STR| <= 16


# Solution
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

# Solution
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


# Problem statement -  Binary Search
# You are given an integer array 'A' of size 'N', sorted in non-decreasing order. You are also given an integer 'target'. Your task is to write a function to search for 'target' in the array 'A'. If it exists, return its index in 0-based indexing. If 'target' is not present in the array 'A', return -1.

# Note:
# You must write an algorithm whose time complexity is O(LogN)

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^9
# 1 <= target <= 10^9
# Time Limit: 1 sec
# Sample Input 1:
# 7
# 1 3 7 9 11 12 45
# 3
# Sample Output 1:
# 1
# Explanation of sample output 1:
# nums = [1, 3, 7, 9, 11, 12, 45],
# The index of element '3' is 1.
# Hence, the answer is '1'.

# Sample Input 2:
# 7
# 1 2 3 4 5 6 7
# 9
# Sample Output 2:
# -1
# Explanation of sample output 2:
# nums = [1, 2, 3, 4, 5, 6, 7],
# Element '9' doesn't exist.
# Hence, the answer is '-1'.

# Solution
def BinarySearch(nums: [int], target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1 
    return -1 


# Reverse the string

# Problem statement

# Given an array/list 'ARR' of integers and a position ‘M’. You have to reverse the array after that position.

# Hints:
# 1. Try to think by creating another array
# 2. Try to think which elements are beign swapped.

# Code
def reverseArray(arr, m):
    array_of_value = arr[:m+1]
    for i in range (len(arr)):
        if arr[i] == arr[m]:
            Rev = arr[:m:-1]
            array_of_value.extend(Rev)
            break
    return array_of_value


# Problem statement - Swap Two Numbers
# You are given two numbers 'a' and 'b' as input.

# You must swap the values of 'a' and 'b'.

# Solution
def swapNumber(a:list,  b: list) -> None:
    # write your code here
    c = a[0]
    a[0] = b[0]
    b[0] = c


# Problem Statement -  First and Last Position of an Element In Sorted Array

# You have been given a sorted array/list 'arr' consisting of ‘n’ elements. You are also given an integer ‘k’.
# Now, your task is to find the first and last occurrence of ‘k’ in 'arr'.
# Note :
# 1. If ‘k’ is not present in the array, then the first and the last occurrence will be -1. 
# 2. 'arr' may contain duplicate elements.


# Code
def firstAndLastPosition(arr, n, k):
    first = -1
    last = -1
    for i in range(len(arr)):
        if arr[i] == k:
            if first == -1:
                first = i
            last = i
    if first == -1:
        return("-1 -1")
    else:
        return(first, last)
