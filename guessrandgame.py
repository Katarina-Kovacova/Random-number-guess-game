import random

def guess():
	global guessed_number
	print()
	while True:
          try:
             guessed_number = int(input(f'Guess a number between 1 and 10: '))    
             if 0 < guessed_number < 11:
               print('Thank you')
               break
             else: 
               print('Hey, only numbers between 1 and 10!')
          except ValueError: 
               print('No other characters except numbers 1 to 10 please! ')       
        
guess()        			
 

def random_choice():
	#generate random number using random module
	global random_number
	random_number = random.randint(1,10)	
	print('Random number is.....', random_number)

random_choice()

#compare guessed number and random number
while True:
	if guessed_number == random_number:
		print('It\'s a match! Congratulations, you are a genius!')
		break
	else: 
		print('It\'s not a match! Try again!')
		guess()
		random_choice()

  