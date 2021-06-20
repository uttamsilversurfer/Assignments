from Resource import Resource
from Roles import Roles
from Users import Users

class Behaviors:
	def __init__(self):
		self.allUser = []
		self.allResource = []
		self.currentUserName = None
		self.currentUserRole = None

	def initiateResource(self):
		video_1 = Resource("Whatsapp_Vid_1", Roles(1))
		video_2 = Resource("Whatsapp_Vid_2", Roles(0))
		image_1 = Resource("Whatsapp_Img_1", Roles(1))
		image_2 = Resource("Whatsapp_Img_2", Roles(0))
		self.allResource.append(video_1)
		self.allResource.append(video_2)
		self.allResource.append(image_1)
		self.allResource.append(image_2)

	def initiateDefaultUsers(self):
		defaultAdmin = Users("admin", Roles(1))
		self.allUser.append(defaultAdmin)
		self.currentUserName = "admin"
		self.currentUserRole = 1
		print("hi! you are logged in as admin")

	def createUser(self):
		print("Enter Username:")
		username = str(input())
		print("Select role [0 for member/ 1 for admin/ 2 for both]:")
		role = int(input())
		user = Users(username, Roles(role))
		self.allUser.append(user)
		print("User created!")

	def editRole(self):
		if(self.currentUserRole == 1 or self.currentUserRole == 2):
			print("Please select user:")
			selectedUser = str(input())
			userAvailable = False
			for x in self.allUser:
				if(selectedUser == x.username):
					userAvailable = True
					print("Please assign new role [0 for member/ 1 for admin/ 2 for dual access]:")
					newRole = int(input())
					x.role.roleCode = newRole
					print("New role assigned!")
					if(x.username == self.currentUserName):
						self.currentUserRole = newRole
			if(userAvailable == False):
				print("User not found! Try again..")
		else:
			print("Unauthorized Access! Only admin can edit role..")

	def login(self):
		print("Enter username:")
		username = str(input())
		userFound = False
		for y in self.allUser:
			if(username == y.username):
				userFound = True
				self.currentUserName = username
				self.currentUserRole = y.role.roleCode
				print("Hi! You are logged in as "+username)
				self.postLoginOptions()
		if(userFound == False):
			print("User not found! Try again..")

	def postLoginOptions(self):
		postOptions = ["Press 1 to login as another user", "Press 2 to view role", "Press 3 to view/access resources", "Press 4 to upload/write a resource", "Press 5 to delete a resource", "Press 6 to logout"]
		for i in postOptions:
			print(i)

		selected = int(input())
		if(selected == 1):
			self.login()
		elif(selected == 2):
			self.viewRole()
			self.postLoginOptions()
		elif(selected == 3):
			self.viewResource()
			self.postLoginOptions()
		elif(selected == 4):
			self.writeResource()
			self.postLoginOptions()
		elif(selected == 5):
			self.deleteResource()
			self.postLoginOptions()
		elif(selected == 6):
			self.currentUserName = None
			self.currentUserRole = None
			pass

	def viewRole(self):
		if(self.currentUserRole == 0):
			print("Current role is: member")
		elif(self.currentUserRole == 1):
			print("Current role is: admin")
		elif(self.currentUserRole == 2):
			print("Current role is: admin + member")

	def viewResource(self):
		print("Your accessible resources are: ")
		for z in self.allResource:
			if self.currentUserRole >= z.accessLevel.roleCode:
				print(z.name)

	def writeResource(self):
		try:
			print("Enter resource name:")
			newResourceName = str(input())
			newResource = Resource(newResourceName, Roles(self.currentUserRole))
			self.allResource.append(newResource)
			print("Resource inserted successfully!")
		except Exception:
			print("Something went wrong! Try again..")
			self.writeResource()

	def deleteResource(self):
		try:
			print("Enter serial number of resource that you want to delete..")
			order = 1
			for z in self.allResource:
				if self.currentUserRole >= z.accessLevel.roleCode:
					print(str(order) + ". " + z.name)
					order += 1
			serialNumber = int(input())
			self.allResource.pop(serialNumber-1)
			print("Resource deleted successfully!")
		except Exception:
			print("Enter correct value!")
			self.deleteResource()







