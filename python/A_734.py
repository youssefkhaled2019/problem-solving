"""
contest = https://codeforces.com/contest/734/problem/A
date = Tuesday, May 9, 2023
Verdict = Accepted
"""

n=int(input())
s=input()
a=s.count("A")
d=n-a
if(a>d):
    print("Anton")
elif(a<d):
     print("Danik")
else:   
     print("Friendship")