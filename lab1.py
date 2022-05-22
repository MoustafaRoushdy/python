import math 
from collections import Counter
import sys

def p1(x1,x2,y1,y2):
   return math.sqrt((x2-x1)**2 + (y2-y1)**2) 


def p2(mylist):
    return list(set(mylist))


def p3(s1,s2):
    return s1[:math.ceil(len(s1)/2)]+s2[:math.ceil(len(s2)/2)] , s1[math.ceil(len(s1)/2):]+s2[math.ceil(len(s2)/2):]


def p5(s):
    return "".join([ x for x in s if x not in "aeouiAEOUI" ])


def p6(s,c):
    return [ i for i,x in enumerate(s)  if x == c ]


def p4():
    f = open(sys.argv[len(sys.argv)-1],"r")
    text = f.read()
    f.close()
    words = Counter(text.split()).most_common(20)
    words = [x[0] for x in words ]
    f = open("popular_words.txt", "w")
    f.write("\n". join(map(lambda x: str(x), words)))
    f.close()


p4()