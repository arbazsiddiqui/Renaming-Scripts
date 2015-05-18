__author__ = 'siddiqui'
import os
import sys
from os.path import basename


temp = os.walk(sys.argv[1], topdown=False)

handler = raw_input("Enter the handler you want to add :")

for root, dirs, files in temp:
    for i in files:
        folder = os.path.join(root)
        file = os.path.join(root,i)
        fileName, fileExtension = os.path.splitext(file)
        name = basename(os.path.join(root,i))
        name = name.replace(handler, " ") + fileExtension
        os.rename(file, os.path.join(root) + "\\" + name)
    for i in dirs:
        dir = os.path.join(root,i)
        name = basename(os.path.join(root,i))
        name = name.replace(handler, " ")
        os.rename(dir, os.path.join(root) + "\\" + name)

#TODO truncate white space
#TODO add more rippers
print "Renaming Complete"
raw_input()