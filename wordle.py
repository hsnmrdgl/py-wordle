import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)

#################################################################

def printBoard(x):
	for i in range (x):
		print(" _  _  _  _  _")
	print("")


def getWords(liste):
	file = open('words.txt', 'r')

	for line in file:
		if len(line.strip()) == 5 and " " not in line:
			liste.append(line.strip().lower())
		else:
			pass

#################################################################

restart = 1

words = []
getWords(words)

while(restart):

	letters = []
	
	count = 6
	check = True
	word = random.choice(words)

	print("\n###################################\n"
			"#           WORDLE TR             #\n"
			"###################################")

	while(count):
		
		printBoard(count)
		
		guess = str(input(">>"))

		if (len(guess) > 5 or len(guess) < 5):
			print("5 harfli bir kelime yazın!")
			check = False
		elif (guess not in words):
			print("Kelime listesinde yok!")
			check = False

		if(check):
			for i in range (5):
				if guess[i] == word[i]:
					print(f"{Fore.GREEN} " + word[i], end =" ")
				elif guess[i] in word:
					print(f"{Fore.YELLOW} " + guess[i], end =" ")
				else:
					print(f"{Fore.RED} " + guess[i], end =" ")
					letters.append(guess[i])
					
			list_set = set(letters)
			unique_letters = (list(list_set))
			print("    Olmayan harfler" , unique_letters)
			count -= 1
		
		check = True

		if(guess == word):
			printBoard(count)
			count = 0
			break


	if (guess == word):
		print("Tebrikler! Kazandınız.")
		answer = str(input("Yeniden oynamak için (Y) basın : "))
		if(answer == "Y" or answer == "y"):
			restart = 1
		else:
			restart = 0

	else:
		print("Oyun bitti! Doğru kelime : " + word.upper())
		answer = str(input("Yeniden oynamak için (Y) basın : "))
		if(answer == "Y" or answer == "y"):
			restart = 1
		else:
			restart = 0
