import random
import os

# def input_check(msg, casting=int):
#     while True:
#         try:
#             user_input =  casting(input("숫자 말해봐요>"))
#             return user_input
#         except:
#             continue


ran_num = random.randint(1,1000)
os.system("cls")

while True:
    guess = input("숫자 말해봐>")
    if guess.isnumeric():
        guess = int(guess)
    else:
        print("제대로 입력하세요.")
        break
    
    if guess == ran_num:
        print("정답! 프로그램을 종료합니다~")
        break
    elif guess > ran_num:
        print("그것보단 작요")
        continue
    elif guess < ran_num:
        print("그것보단 커요")
        continue
 
    

