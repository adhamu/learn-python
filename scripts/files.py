#!/usr/bin/env python3

import os
import shutil

# current file/directory
current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file)
cwd = os.getcwd()

print(current_file)
print(current_directory)
print(cwd)

# list files in directory
for file in os.listdir(current_directory):
    print(file)

# create directory
new_directory = current_directory + '/' + 'new-directory'

if not os.path.exists(new_directory):
    os.mkdir(current_directory + '/' + 'new-directory')

# create file
new_file = new_directory + '/' + 'new-file.txt'
fo = open(new_file, 'w+')
fo.write( "Python is a great language.\nYeah its great!!\n")
print("Name of the file: ", fo.name)
fo.close()

# rename a file
os.rename(new_file, new_directory + '/' + 'new-file2.txt')
new_file = new_directory + '/' + 'new-file2.txt'

# read a file
f = open(new_file, 'r')
print(f.read())

# read line by line
print(f.readline())

# delete a file
decide = input("delete the newly created file? ")
if decide == 'yes' and os.path.isfile(new_file):
    os.remove(new_file)
    print(new_file + ' deleted')

# delete a directory (only works if directory is empty)
decide = input("delete the newly created directory? ")
if decide == 'yes' and os.path.exists(new_directory):
    os.rmdir(new_directory)
    print(new_directory + ' deleted')

# delete a directory (deletes all contents inside)
decide = input("delete the newly created directory and all files inside? ")
if decide == 'yes' and os.path.exists(new_directory):
    shutil.rmtree(new_directory)
    print(new_directory + ' and all files inside deleted')