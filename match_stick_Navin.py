#Version 3.0
#Problem Statement
'''You are given a set of sticks with different lengths. You want to place the sticks in a square pattern with k rows,
where each row contains either a single stick with length k, or two sticks with the sum of their lengths k-1, separated by a space of length 1.
Find the largest possible k. If it is not possible to create such a pattern, return 0. It is not necessary to use all the sticks when creating a pattern.
Lengths of the sticks will be stored in an array int[] len. The maximum number of sticks will be 40, and the maximum length for each stick also will be 40.
Examples:
{1,1,3,1,1} -> return 3
- -
---
- -
{1,2,2,3,5,5,5} -> return 5
-----
-- --
--- -
-----
-----
{1} -> return 1
{1,2,3,1,2,4,2,3,1} -> return 4
{1,1,1,1,1,1} -> return 3'''

#Program begins

from math import ceil,sqrt
from sys import exit

#function to get matchsticks length from user
def getMatchStickLength():
    global numOfMatchStick
    global lengths,lengthSum
    lengthSum = 0
    lengths = []
    numOfMatchStick = input("Enter number of Match Sticks: ")
    print 'Type the length of each matchstick and press Enter'
    # check if the number of matchsticks are less than 40
    if ((numOfMatchStick > 40) or (numOfMatchStick <= 0)):
        print 'Number of matchsticks exceeded 40 or negative or zero!!! (Input array)'
        exit(0)
    else:
        for i in range(numOfMatchStick):
            length = input()
            lengthSum = lengthSum + length
            # Exit the program if length of any matchstick is greater than 40 or if length is zero 
            if length > 40 or length <= 0 :
                print 'Bad Input - Size of a matchstick exceeded 40!!! or Size of a matchstick cannot be zero or negative!!!'
                exit(0)
            lengths.append(length)

#chooses 2 possible matchsticks for given 'k' value           
def twoMatchStick(lengthCopy,element,k1,i):
    flag = 0
    for j in range(i+1,numOfMatchStick):
        if(element+lengthCopy[j]) == k1-1 :
            lengthCopy[j] = 0
            flag = 1
            break
    return flag
        
#function to find optimal 'k' value for given input    
def squareCheck(k1,lengthCopy):
    row = 0
    for i in range(numOfMatchStick):
        if lengthCopy[i] == k1:
            lengthCopy[i] = 0
            row = row + 1
        elif lengthCopy[i] == k1-1:
            lengthCopy[i] = 0
    
    for i in range(numOfMatchStick-1):
        if((lengthCopy[i] != 0) and (row < k1)):
            #Backtracking to choose the matchsticks for the rows with single space
            x = twoMatchStick(lengthCopy,lengthCopy[i],k1,i)
            if x == 1:
                row = row + 1
                lengthCopy[i] = 0
        elif(row >= k1):
            break

    if row == k1:
        return row
    else:
        return 0

def main():
    lengthCopy = []
    getMatchStickLength()
    lengthCopy = list(lengths)
    print 'Input List(Array) values :' , lengths

    #to find maximum possible value of 'k' for given input
    maxPossibleK = int(ceil(sqrt(lengthSum)))

    #to find optimal 'k'
    print '------------------------------------------------'
    print 'Checking for k = ', maxPossibleK
    k = squareCheck(maxPossibleK,lengthCopy)

    while maxPossibleK > 2:
        maxPossibleK = maxPossibleK - 1
        if k == 0 :
            print '-----------------------------------------------'
            print 'Checking for k = ',maxPossibleK
            lengthCopy = list(lengths)
            k = squareCheck(maxPossibleK,lengthCopy)
        else:
            break

    
    #to print optimal 'k' value
    if k == 0:
        for i in range(numOfMatchStick):
            if lengths[i] == 1:
                k = 1
                break
        print "Max value of K for the given matchsticks : ", k
    else:
        print "Max value of K for the given matchsticks : " , k
        
main()
