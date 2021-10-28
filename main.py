from mangaCode.manga import Manga
from mangaCode.usuario import User

# It do not print passwords when users are typing them
import getpass

def main():
	"""
	print("Creating a manga...\n")

	name = input("Input name: ")
	description = input("Input description: ")
	genre = input("Input genre: ")
	num_chapters = input("Input num of chapters: ")
	mangaka = input("Input mangaka: ")

	manga = Manga(name,description,genre,num_chapters,mangaka)

	print("\nA new manga has been created with the following information: ")
	print("Name: " + manga.get_name())
	print("Description: " + manga.get_description())
	print("Genre: " + manga.get_genre())
	print("Num of Chapters: " + manga.get_num_chapters())
	print("Mangaka: " + manga.get_mangaka())

	"""

	print("\nCreating a user...\n")

	nickname = input("Enter nickname: ")
	name = input("Enter name: ")
	usernames = input("Enter usernames: ")
	email = input("Email: ")

	passwd1 = ""
	passwd2 = "a"

	while passwd1 != passwd2:
		passwd1 = getpass.getpass("Enter passwd: ")
		passwd2 = getpass.getpass("Enter passwd again: ")

		if passwd1 != passwd2:
			print("\nPassword do not match!\n")

	user = User(nickname,name,usernames,email,passwd1)

	print("\nA new user has been created with the following information: ")
	print("Nickname: " + user.get_nickname())
	print("Name: " + user.get_name())
	print("Email: " + manga.get_email())
	print("Password: " + manga.get_passwd())


if __name__ == '__main__':
	main()