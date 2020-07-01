import os


from docx import Document
import win32com.client

import re

docxpath = "C:/Users/萝卜ovo/Desktop/杂/赵如/西方经济学/"
newdocxpath = "C:/Users/萝卜ovo/Desktop/杂/赵如/西方经济学/1/"

tihuanci = {
    '1、':'1.',
    '2、':'2.',
    '3、':'3.',
    '4、':'4.',
    '5、':'5.',
}



def check_and_change(document , tihuanci):
    for para in document.paragraphs:
        for i in range(len(para.runs)):
            for key,value in tihuanci.item():
                for key in para.run[i].text:
                    print(para.runs[i].text)
                    para.runs[i].text = para.runs[i].text.replace(key,value)
    return document

def main():
    for name in os.listdir(docxpath):
        print(name)
        docxpath = docxpath + name
        newdocxpath = newdocxpath + name
        if name.split(".")[1] == 'docx':
            document = Document(docxpath)
            document = check_and_change(document,tihuanci)
            document.save(newdocxpath)
        print("^"*30)


if __name__ == '__main__':
    # printdocumet()
    # zhuanhuanzifu()
    main()