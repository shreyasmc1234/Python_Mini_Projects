# -*- coding: utf-8 -*-
"""functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ASzvhDgyPj_xFFiVRqm0qn0rwcnrthwk

Function is a block of code that can be used again
"""

n=int(input("Enter the number"))
j=1

if n==0:
  print(f"The factorial of 0 is {j}")
else:
  for i in range(1,n+1):
    j=j*i
  print("The factorial of "+str(i)+" is "+str(j))

def factorial_of_number(n):
  j=1

  if n==0:
    return j
  else:
    for i in range(1,n+1):
      j=j*i
    return j

print(factorial_of_number(5))

print(factorial_of_number(10))

