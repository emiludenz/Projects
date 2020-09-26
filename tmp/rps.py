import random

choice = ["Rock","Paper","Scissors"]

def computer_choice():
	return random.choice(choice)

def player_pick():
	i=input()
	if int(i) < 4 and int(i) > 0:
		return choice[i-1]

def main():
	print(computer_choice())




if __name__ == '__main__':
	main()