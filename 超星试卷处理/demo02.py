import os
from docx import Document

#要读取的文件的上层文件夹路径



document = Document("C:/Users/萝卜ovo/Desktop/Python/超星试卷处理/西方经济学答案汇总.docx")

number = ['1','2','3','4','5','6','7','8','9']


with open('整理.txt','w') as f :
    f.write("")

def printdocumet():
    for para in document.paragraphs:

        for i in range(len(number)):
            if number[i] in para.text:
                with open('整理.txt','a',encoding='utf-8') as f:
                    f.write(para.text)
                    f.write("\n")
                # print(para.text)
                break
            if '二、' in para.text:
                return

if __name__ == '__main__':
    printdocumet()
