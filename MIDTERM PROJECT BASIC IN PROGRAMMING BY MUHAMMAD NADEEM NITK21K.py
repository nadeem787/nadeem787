import random

def Frequency(myfinal):
    freq = {}
    for ele in myfinal:
        if (ele in freq):
            freq[ele] += 1
        else:
            freq[ele] = 1
    for s, t in freq.items():  
        print("% d : % d" % (s, t))

mylist = []
for i in range(200):
    x = random.randint(1, 2)
    mylist.append(x)
print("200 observations")
print(Frequency(mylist))

for i in range(20000):
    x = random.randint(1, 2)
    mylist.append(x)
print("20000 observations")
print(Frequency(mylist))

for i in range(200000):
    x = random.randint(1, 2)
    mylist.append(x)
print("200000 observations")
print(Frequency(mylist))
