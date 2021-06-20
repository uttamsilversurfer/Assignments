from main import Behaviors

def WelcomeScreen(behaviors):
	try:
		options = ["Press 1 to login as another user", "Press 2 to create an user", "Press 3 to edit role"]
		for i in options:
			print(i)

		selectedOption = int(input())
		if(selectedOption == 1):
			behaviors.login()
		elif(selectedOption == 2):
			behaviors.createUser()
		elif(selectedOption == 3):
			behaviors.editRole()
		else:
			print("Select a valid option")
		WelcomeScreen(behaviors)

	except Exception:
		print("Something went wrong! Try again..")
		WelcomeScreen(behaviors)

if __name__ == '__main__':
	behaviors = Behaviors()
	behaviors.initiateResource()
	behaviors.initiateDefaultUsers()
	WelcomeScreen(behaviors)

