import csv
import tkinter

window=tkinter.Tk()

window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)



print("추출할 파일 텍스트 이름을 입력하세요")
chat_text_file = input()
chat_text_file += '.txt'

txtFile = open(chat_text_file, 'r', encoding='UTF8')

chats = txtFile.readlines()

print("이건 성공한 댓글인가요 실패한 댓글인가요? - 성공 : 1, 실패 : 0")
label = input()

chat_output = []


for chat in chats:
    chat_with_nickname = chat[chat.find(']') + 2 :]
    actual_chat = chat_with_nickname[chat_with_nickname.find(':') + 2 : chat_with_nickname.find('\n')]
    
    chat_output.append([actual_chat, label])


print("출력 파일명 입력")
filename = input()
filename = filename + '.csv'

with open(filename, 'w', newline='') as file:
    write = csv.writer(file)
    write.writerows(chat_output)