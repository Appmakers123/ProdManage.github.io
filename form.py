#!usr/bin/python

import cgi
form = cgi.FieldStorage()
with open ('https://github.com/Appmakers123/ProdManage.github.io/blob/master/form.txt','w') as fileOutput:
    fileOutput.write(form.getValue('firstname'))
    fileOutput.write(form.getValue'(lastname'))
