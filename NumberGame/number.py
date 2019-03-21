import random

count = 0
number = random.randint(1, 99)
print("자 1 부터 99까지의 제가 생각한 숫자를 10번 안에 맞춰보세요")

while count < 10:
    count += 1
    user_input = int(input("몇 일까요? "))
    if user_input == number:
        break
    if user_input < number:
        print("너무 낮은 숫자 입니다.")
    if user_input > number:
        print("너무 큰 값 입니다.")

if user_input == number:
    print("성공!!! 제가 생각한 숫자는 {} 가 맞습니다.".format(number))
else:
    print("이런!! 제가 생각한 숫자는 {} 입니다.".format(number))