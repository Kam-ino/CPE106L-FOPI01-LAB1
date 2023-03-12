import math
import statistics
from collections import Counter

data = [12, 43,23, 55, 765,54, 234, 243, 34,34,34,34,12,12,12 ,546, 100, 465,65, 123, 786]

def MEAN(data):
    n = len(data)
    sum = 0

    for i in data:
        sum = sum + i
        MEAN = sum/n
    return MEAN

def MEDIAN(x):
    data.sort()
    n = len(data)
    midnum = int(n/2)
    
    if(n%2 == 1):
        MEDIAN = data[midnum]
        return MEDIAN
    else:
        MEDIAN = (data[midnum]+data[midnum+1])/2
        return MEDIAN

def MODE(data):
    MODE = []
    data1 = Counter(data) 
    temp = data1.most_common(1)[0][1] 
    for ele in data:
        if (data.count(ele) == temp):
            MODE.append(ele)
    MODE = list(set(MODE))
    return str(MODE)

print("Data = ", data)
print("MEAN", MEAN(data))
print("MEDIAN", MEDIAN(data))
print("MODE", MODE(data))
