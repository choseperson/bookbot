def word_count(book_contents):
        words = book_contents.split()
        return len(words)

def character_count(text):
	counts = {}
	for ch in text:
		ch = ch.lower()
		if ch in counts:
			counts[ch] += 1
		else:
			counts[ch] = 1
	return counts

def count_num(entry):
	return entry["num"]

def count_sorter(counts):
	sorted_list = []

	for char, num in counts.items():
		entry = {"char": char, "num": num}
		sorted_list.append(entry)

	sorted_list.sort(reverse=True, key=count_num)
	return sorted_list
