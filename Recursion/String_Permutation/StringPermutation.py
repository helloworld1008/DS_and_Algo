#!/usr/bin/env python

user_input = raw_input("Enter a string: ")

def perm(init_string,remainder_string):

        if len(remainder_string) == 1:

                print init_string + remainder_string
        c = 0

        while (c < len(remainder_string)):

                remainder_string = remainder_string[1:] + remainder_string[0]

                perm(init_string + remainder_string[0], remainder_string[1:])

                c = c + 1

perm("",user_input)
