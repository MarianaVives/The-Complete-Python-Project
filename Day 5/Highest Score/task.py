student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total = sum(student_scores)

print("Sum is " + str(total))

sum = 0
for s in student_scores:
    sum += s
print("For loop sum: " + str(sum))

max_score = 0
for scores in student_scores:
    if max_score < scores:
        max_score =scores
print(max_score)