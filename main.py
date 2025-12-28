import sys

from stats import character_count, word_count, count_sorter, count_num

def get_book_text(file_path):
        with open(file_path) as f:
                book_contents = f.read()
        return book_contents

def main():
	if len(sys.argv) == 2:
		book_path = sys.argv[1]
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	text = get_book_text(book_path)
	num_words = word_count(text)
	char_dict = character_count(text)
	sorted_chars = count_sorter(char_dict)
	print("============ BOOKBOT ============")
	print(f'Analyzing book found at {book_path}...')
	print("----------- Word Count ----------")
	print(f'Found {num_words} total words')
	print("--------- Character Count -------")
	for entry in sorted_chars:
		ch = entry["char"]
		num = entry["num"]
		if ch.isalpha():
			print(f"{ch}: {num}")
	print("============= END ===============")

main()
