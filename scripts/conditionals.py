#!/usr/bin/env python3

# switch
def hello():
  print ("Hello")

def bye():
  print ("Bye")

def hola():
  print ("Hola is Spanish for Hello")

def adios():
  print ("Adios is Spanish for Bye")

menu = [hello,bye,hola,adios]
menu[1]()

# if/elseif/else
language = input('Please enter a language: ')

if language == 'python':
    print('Correct')
elif language == 'php':
    print('PHP? Are you serious?')
else:
    print('Incorrect. Come on, you know what we\'re writing here')
