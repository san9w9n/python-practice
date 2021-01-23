import random

eng_words = {"사자":"lion", "호랑이":"tiger", "달력":"calendar", "멍청이":"stupid", "사랑":"love"}
#iterable 하지 않은 딕셔너리. 그래서 리스트에 담아주어야한다!!

word = [x for x in eng_words]
random.shuffle(word)

correct = 0
for i, j in enumerate(word):
    user_ans = input("{}를 영어로 하면?>".format(j))
    answer = eng_words[j]
    if user_ans.strip().lower() == answer:
        #strip는 양쪽 공백제거
        print("정답!")
        correct += 1
    else:
        print("오답!ㅋㅋ")

print("{}문제 맞힘~".format(correct))
