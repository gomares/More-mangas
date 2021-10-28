from mangaCode.manga import Manga

def main():
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


if __name__ == '__main__':
	main()