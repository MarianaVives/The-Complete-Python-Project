import random

rand_num = random.randint(1, 11)
print(rand_num)

random_number_0_to_1 = random.random()*10
print(random_number_0_to_1) #will give floating point num

random_floating = random.uniform(2,8)
print(random_floating)

number = random.randint(1,10)
if 1<= number <10 :
    print("heads")
else:
    print("tails")