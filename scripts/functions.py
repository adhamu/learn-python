#!/usr/bin/env python3

# No arguments
def whats_my_name():
    return "your name is amit"

print(whats_my_name())

# Arguments
def my_name_is(name):
    return "my name is " + name

print(my_name_is("amit"))

# Default arguments
def default_name(name = None):
    if name is None:
        name = "Unknown"
    return "my name is " + name

print(default_name())
print(default_name("Amit"))
