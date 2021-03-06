"""
name_that_roll.py
=====
Write a program that names the rolls of two dice in a dice game called 
craps...

* ask the user for the values of two dice rolls.  
* output the name of the roll using Wikipedia's article on Craps
	* http://en.wikipedia.org/wiki/Craps#Rolling
* only check for the following rolls:
	* _Snake Eyes_
	* _Hard Four_ 
	* _Easy Four_  
* print out "I don't know yet" for any other rolls.  Example output:
* example interaction:

What roll did you get for the first die?
> 1
What roll did you get for the second die?
> 1
Snake Eyes!

Press ENTER or type command to continue
What roll did you get for the first die?
> 1
What roll did you get for the second die?
> 3
Easy Four
"""
die1 = int(raw_input('What was your first number? \n'))
die2 = int(raw_input('What was your second number? \n'))

if die1 == 1 and die2 == 1:
	print('Snake Eyes')
elif die1 == 2 and die2 == 2:
	print('Hard Four')
elif die1 == 1 and die2 == 3 or die1 == 3 and die2 == 1:
	print('Easy Four')
else:
	print('You got something else!')