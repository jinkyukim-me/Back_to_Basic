
# solution
# sum = 0
# count = 0
# while True:
#     number_input = input("숫자를 입력해주세요. (입력된 숫자의 평균을 구합니다.) - ")
#     number_input_int = int(number_input)
#     sum += number_input_int
#     if number_input_int == 0:
#         break
#     count += 1
#

# solution 1
input_number = int(input("(This number will make a pyramid) What is your number?  - "))

if input_number <= 5:
    for i in range(input_number):
        print("*" * (i + 1))
elif input_number > 5:
    for i in range(5):
        print("*" * (i + 1))
    for i in range(input_number - 5):
        print("*" * 5)

# solution 2
# input_number = int(input("(This number will make a pyramid.) What is your number?  - "))
#
# if input_number <= 5:
#     for i in range(input_number):
#         print("*" * (i + 1))
# else:
#     for i in range(5):
#         print("*" * (i + 1))
#     for i in range(input_number - 5):
#         print("*" * 5)


