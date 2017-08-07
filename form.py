#!usr/bin/python

import cgi
form = cgi.FieldStorage()
with open ('https://docs.google.com/document/d/1O0ATtykKI3HVIDB48ObjwEQ2l2pEmKqT6CV4ekWrvwQ/edit','w') as fileOutput:
    fileOutput.write(form.getValue('firstname'))
    fileOutput.write(form.getValue'(lastname'))
