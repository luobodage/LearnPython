import os
from docx import Document

#要读取的文件的上层文件夹路径



document = Document("C:/Users/萝卜ovo/Desktop/Python/超星试卷处理/《经济学原理》评分标准和标准答案（A卷）.docx")

def printdocumet(): 
    for para in document.paragraphs:
        print(para.text)

if __name__ == '__main__':
    printdocumet()
