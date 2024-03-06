"""
import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
"""


import sys
input = sys.stdin.readline
"""
백준 1759 암호 만들기

일단 입력받고 sort

재귀를 돌릴건데, 파라미터로 모음과 자음의 개수, 암호를 넘긴다.
만약 암호의 길이가 L이면 출력. 
"""

l,c = map(int,input().split())
chars = list(input().split())
chars.sort()
vowels_ = set(['a','e','i','o','u'])
def make(num_vowel, num_con, password):
    if l - num_vowel - num_con == 0:
        if num_vowel >= 1 and num_con >= 2:
            print(password)
            return
    for i in range(len(password),c):
        if password[-1] < chars[i]:
            if chars[i] in vowels_:
                make(num_vowel+1, num_con, password+chars[i])
            else:
                make(num_vowel, num_con+1, password+chars[i])
for i in range(c-l+1):
    if chars[i] in vowels_:
        make(1,0,chars[i])
    else:
        make(0,1,chars[i])