user_score=0
computer_score=0

def game():
	global user_score
	global computer_score

	import random
	choices =["S","W","G"]
	a=random.choice(choices)

	userstr=input("Enter the first letter of your choice (S, W, G):	")
	b=userstr.capitalize()

	dict={"S": "Snake" ,
 	"W":"Water",
 	"G": "Gun"}

	print(f"The computer chose '{dict[a]}'")
	print(f"You chose '{dict[b]}'")

	if a==b:
		print("It's a draw")
		user_score+=1
		computer_score+=1
		print("Scores:")
		print(f"USER: {user_score}")
		print(f"COMPUTER: {computer_score}")
	else:
		if a=="S" and b=="W":
			print("Computer won")
			user_score+=0
			computer_score+=1
			print("Scores:")
			print(f"USER: {user_score}")
			print(f"COMPUTER: {computer_score}")
		elif a=="S" and b=="G":
			print("You won")
			user_score+=1
			computer_score+=0
			print("Scores:")
			print(f"USER: {user_score}")
			print(f"COMPUTER: {computer_score}")
		elif a=="W" and b=="S":
			print("You won")
			user_score+=1
			computer_score+=0
			print("Scores:")
			print(f"USER: {user_score}")
			print(f"COMPUTER: {computer_score}")
		elif a=="W" and b=="G":
			print("Computer won")
			user_score+=0
			computer_score+=1
			print("Scores:")
			print(f"USER: {user_score}")
			print(f"COMPUTER: {computer_score}")
		elif a=="G" and b=="S":
			print("Computer won")
			user_score+=0
			computer_score+=1
			print("Scores:")
			print(f"USER: {user_score}")
			print(f"COMPUTER: {computer_score}")
		elif a=="G" and b=="W":
			print("You won")
			user_score+=1
			computer_score+=0
			print("Scores:")
			print(f"USER: {user_score}")
			print(f"COMPUTER: {computer_score}")
		else:
			print("There is an error")
		
	user=input("Wanna play again?(Y/N)	")
	again=user.capitalize()
	if again=="Y":
		game()
	elif again=="N":
		print("Thank you for playing!")
	else:
		print("Invalid input")
		
game()
print("FINAL SCORES")
print(f"USER: {user_score}")
print(f"COMPUTER: {computer_score}")
if (user_score>computer_score):
	print("YOU WON")
elif(user_score==computer_score):
	print("IT'S A DRAW")
else:
	print("YOU LOSE")
