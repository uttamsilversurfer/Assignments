class Roles:
	def __init__(self, roleCode):
		'''
		Role codes:
		0 for member (Weakest Power)
		1 for admin
		2 for dual role (admin + member) (Strongest Power)
		'''
		self.roleCode = roleCode
