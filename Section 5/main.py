# student_heights = input("Input a list of student heights ").split()
# for n in range(0,len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)


# all_heights = 0
# number = 0
# for height in student_heights:
#     all_heights = all_heights + int(height)
#     number = number + 1

# print("Average height is :",round(all_heights/number))
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "Pie")


student_scores = input("Input a list of student score: ").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
    print(student_scores)

max_score = student_scores[0]
for score in student_scores:
    if max_score < score:
        max_score = score
    else:
        continue

print(f"The highest score in the class is : {max_score}")

## Range
for number in range(1,11):
    print(number)

for number in range(1,11,3):
    print(number)

total = 0
for number in range(1,101):
    total += number
print(total)


sum_of_even_number = 0
for number in range(2,101,2):
    sum_of_even_number += number

print(sum_of_even_number)

total = 0
for number in range(1,101):
    if number % 2 == 0:
        total += number