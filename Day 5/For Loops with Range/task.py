#Range Function should be used in conjunction
number = [1,2,3,4,5,6,7,8,9,10]

print(range(1,10))

for n in range(1,10): #not including 10
    print(n)
for n in range(1,10,2): #not including 10 skipping 2
    print(n)

total =0
for n in range(1, 100+1):
    total += n
print(total)