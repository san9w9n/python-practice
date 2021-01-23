#스마트계산기
import os

os.system("cls")
operator = ["+", "-", "*", "/", "="]
lop = 0
string_list = []
user_input = input("계산식을 입력하세요> ")

for i, s in enumerate(user_input):
    if s in operator:
        if user_input[lop:i].strip() != "":
            string_list.append(user_input[lop:i].strip())
            string_list.append(s)
            lop = i + 1
string_list.append(user_input[lop:])

string = ""
count = 2
last = 0
while True:
    string += ''.join(string_list[last:count+1])
    string = str(eval(string))
    last = count + 1
    count += 2
    if count > len(string_list): break

print(string_list)
print(string)
     
