#숫자야구게임
import random

def makenum():
    ran_list = []
    while len(ran_list) < 4:
        num = random.randint(0,9)
        if num not in ran_list:
            ran_list.append(num)
        else: continue
    return ran_list


def guessnum():
    num = [int(x) for x in input("중복되지 않은 한 자리 숫자 4개>").split()]
    return num

def checknum(answer, guess):
    strike, ball, out = (0,0,0)
    for i,j in enumerate(guess):
        if answer[i] == j:
            strike += 1
        else:
            if j in answer:
                ball += 1
            else:
                out += 1
    arr = [strike, ball, out]
    return arr

ans = makenum()
print(ans)
while True:
    guess = guessnum()
    baseball = checknum(ans,guess)
    if baseball[0] == 4:
        print("정답!!")
        break
    else:
        print("{}스트라이크, {}볼, {}아웃".format(baseball[0], baseball[1], baseball[2]))
    