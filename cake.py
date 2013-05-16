"""
cake.py
=====
Write a program that asks for cake and handles a yes, no, 
or anything other than yes or no.  It will say different things 
depending on the user's answer.  Here's an example:

Do you want cake?
> yes
Here, have some cake.

Do you want cake?
> no
No cake for you.

Do you want cake?
> blearghhh
I do not understand.
"""

cake = raw_input("Do you want cake? \n")
if cake == 'yes' or cake == 'sure' or cake == 'yeah':
	print('HERE YOU GO!!!')
elif cake == 'no' or cake == 'nope' or cake == 'nah':
	print('HA NO CAKE FOR YOU!')
else: 
	print('MAKE UP YOUR FUCKING MIND!')