import math, random
#Task_1
user_number = input('Insert number: ')
answer = 0
for i in range(len(user_number)):
    try:
        answer += int(user_number[i])
    except:
        continue
print(f'{user_number} -> {answer}')

#Task_2
user_number = int(input('Insert number: '))
answer = []
for i in range(user_number):
    answer.append(math.factorial(i+1))
print(answer)
#Task_3
user_number = int(input('Insert number: '))
summ = 0
for i in range(user_number):
    summ+=(1+(1/(i+1)))**(i+1)
print(round(summ, 2))
#Task_4
user_number = int(input('Insert number: '))
user_list = []
for i in range(-user_number, user_number+1):
    user_list.append(i)
print(user_list)
with open('file.txt', 'r', encoding='utf-8') as f:
    answer = 1
    for line in f:
        answer*=user_list[int(line.strip())]
    print(answer)
#Task_5
my_list = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(my_list)
print(my_list)
#Task_6
array_a, array_b = [1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2]
answer = []
for i in array_a:
    if i in array_b:
        answer.append(i)
print(answer)