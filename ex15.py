# -- coding: utf-8 -- ��
#��sys(ģ��/��)�е���(import)argv����
from sys import argv
     #������argv���
script, filename = argv


#ָ����һ���ļ�
txt = open(filename)



#��ӡ�ļ���
print ("Here's your file %r:" %filename)
#��ӡ�ļ�����
print (txt.read())

print ("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print (txt_again.read())

