import csv
import re

def Find_Special_Pattern(string):
    return_string = ""
    
    if string.find('ㄹㅇㅋㅋ') != -1 :
        return_string += ' ㄹㅇㅋㅋ '
    if string.find('ㅗㅜㅑ') != -1 :
        return_string += 'ㅗㅜㅑ'
        
    return return_string



print("추출할 파일 텍스트 이름을 입력하세요")
chat_text = input()
chat_text_file = chat_text + '.txt'
txtFile = open(chat_text_file, 'r', encoding='UTF8')

chats = txtFile.readlines()

print("이 당시 배율을 입력해 주세요")
label = input()

chat_output = []

for chat in chats:
    
    chat_with_nickname = chat[chat.find(']') + 2 :]
    actual_chat = chat_with_nickname[chat_with_nickname.find(':') + 2 : chat_with_nickname.find('\n')]
    
    special = Find_Special_Pattern(actual_chat)
    
    actual_chat = re.sub('[^가-힣\s]', '', actual_chat)
    actual_chat += special
    
    if(not (actual_chat and actual_chat.strip())):
        continue
    
    chat_output.append([actual_chat, label])

print("csv 파일로 출력중...")
filename = chat_text + '.csv'

with open(filename, 'w', newline='') as file:
    write = csv.writer(file)
    write.writerows(chat_output)
print("csv 파일로 출력 완료")