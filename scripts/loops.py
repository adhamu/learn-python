#!/usr/bin/env python

words = ['python', 'looks', 'like', 'it', 'could', 'be', 'fun']

for word in words:
    print word, len(word)

for num in range(0, 5):
    print num

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
else:
    print 'The count is 9. Finishing'

password = ""
while password != "secret":
    password = raw_input("Please enter the password: ")
    if password == "secret":
        print "Thank you. You have entered the correct password"
    else:
        print "Sorry the value entered in incorrect - try again"