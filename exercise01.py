"""
练习课（一）
基础练习
    1.struct作业完成
    2.文件分离练习
        一个文件，文件名：“talk.txt”.在文件中保存着一些对话信息，格式如下

        老王：吃了么
        老李：没那，您呢
        老张：您二位干啥呢
        老李：遛弯啊，刚买菜回来
        老张：是啊


    通过程序将该文件进行分离，每个人物的说话内容，重新写入到一个新的文件中，，文件以这个人的名字命名

    3.一个目录，在目录下有若干文件（有子目录和普通文件）。编程将该目录下的普通文件复制到家目录下的
        “备份”这个目录中

提高练习
    知识点涵盖
        文件读写
        网络套接字传输
        数据逻辑处理
        封装思想
        基础逻辑
    题目要求
        1.编写一组程序，分为客户端和服务端
        2.客户端用于于用户交互，用客户端通过input（）选择一个文本文件（存在大量的括号内容（），[],{}
        《》，但是这些括号可能存在匹配不正确的情况），将这个文件发送给服务端
        3.服务端需要判断发过来的文件中的括号匹配是否正确，如果正确则给客户端回复完全正确的信息，如果不
            正确，须告知客户端不正确，并且指出括号不正确的位置
            比如此时客户端会收到：“在第18个字符位置”

扩展练习
    要求：1.通过客户端选择图片，向服务器发送。同时告知服务端图片类型
         2.服务端利用接口完成对图片的识别，并将最后的判断结果发送给客户端
"""
#2
# f=open("file","r")
# for item in f:
#     w,x=item.split("：",1)
#     f1=open(w,"a")
#     f1.write(x)
#     f1.close()
# f.close()
#3
import os
home="/home/tarena/备份/"
dir=input(">>")
if dir[-1]!="/":
    dir+="/"


def copy(file):
    fr=open(dir+file,"rb")
    fw=open(home+file,"wb")
    while True:
        data=fr.read()
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

def main():
    file_list=os.listdir(dir)
    for file in file_list:
        if os.path.isfile(dir+file):
            copy(file)
main()











