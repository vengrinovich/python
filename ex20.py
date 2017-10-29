import random

sample = random.sample(range(10), 8)
sample.sort()
digit = random.choice(range(10))

print sample
print digit

"""on_the_list = 0

for number in sample:
	if digit == number:
		on_the_list += 1
	
if on_the_list == 1:
	print True
else:
	print False"""

# using binary search
def binarySearch(sample, digit):
	first = 0
	last = len(sample)-1
	found = False
5	
while first < last and not found:
	midpoint = (first + last)//2
8		if sample[midpoint] == digit:
9		found = True
10	    else:
11	    	if item < sample[midpoint]:
12	        	last = midpoint-1
13	        else:
14	            first = midpoint+1
15	
16	    return found
