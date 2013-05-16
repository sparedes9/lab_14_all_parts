"""
go_for_gold.py
=====
Translate an athlete's finishing placement 
(1st, 2nd and 3rd) into its Olympic medal value: 1 for gold, 
2 for silver, 3 for bronze and anything else means no medal.  
Do this by asking for user input.  For example:

What number should I translate into a medal?
>1
gold

What number should I translate into a medal?
>3
bronze

What number should I translate into a medal?
>23
no medal for you!

"""
medal = int(raw_input("What is your place? \n"))
if medal >= 1 and medal <= 3:
	print("GOLD")
elif medal >= 4 and medal <= 6:
	print("SILVER")
elif medal >= 7 and medal <= 9:
	print("BRONZE")
else:
	print("LOSER!")