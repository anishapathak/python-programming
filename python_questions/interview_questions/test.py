result = set()
input = 'anisha'

remaining = input
anagram = ""

def get_anagram(anagram, remaining):
	# print(result)

	if remaining == "":
		result.add(anagram)

	for i in range(len(remaining)):
		
		left = remaining[:i]
		right = remaining[i+1:]
		new_remaining = left+right

		ch = remaining[i]
		# print(i,anagram + ch,new_remaining)

		get_anagram(anagram + ch,new_remaining)
		
get_anagram(anagram,remaining)
print(result)
print(len(result))