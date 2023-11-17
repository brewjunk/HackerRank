#Designer PDF Viewer | HackerRank

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = 'zaba'


def designerPdfViewer(h, word):
	heights = []
	for letter in word:
		heights.append(h[(ord(letter)-97)])
	word_length = len(word)
	min_height = min(heights)
	max_height = max(heights)
	result = word_length*max_height
	return result


print(designerPdfViewer(h,word))