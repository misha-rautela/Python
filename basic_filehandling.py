# This file has basic file handling methods used in perl
import os
#opens a file in read write mode, if file doesn't exit, it creates one
file = open('myfile.txt','w+')
#writing to the file
file.write('This is the first line of the newly created file')
print " Name of the newly created file", file.name
print "Mode of the newly created file", file.mode
print "file is closed or not", file.closed
#tell method tells the current position within the file.
pos= file.tell()
print pos
# seek method changes the current position to the begining of the file
pos = file.seek(0,0)
#reading from the file
str1 = file.read();
print "content of the file is \n", str1
#closing the file
file.close()
print"file is closed or not", file.closed
#renaming file
os.rename(file.name, 'myfile2.txt')
#open the renamed file in read mode 
file1 = open('myfile2.txt', 'r')
str2 = file1.read();
print"content of the renamed file is \n ", str2
#removes file
os.remove('myfile2.txt')
#removes the directory
os.removedirs("/home/misha/workspace/testdir")
#creates the directory
os.mkdir("/home/misha/workspace/testdir")
str3 = os.getcwd();
print "The current working directory is ", str3
os.chdir("/home/misha")
str4 = os.getcwd();
print "The current working directory is ", str4
