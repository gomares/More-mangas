class User:
	def __init__(self, nickname, name, surnames, email, passwd):
		self._nickname = nickname
		self._name = name
		self._surnames = surnames
		self._email = email
		self._passwd = passwd

	def get_nickname(self):
		return self._nickname

	def get_name(self):
		return self._name

	def get_surnames(self):
		return self._surnames

	def get_email(self):
		return self._email

	def get_passwd(self):
		return self._passwd