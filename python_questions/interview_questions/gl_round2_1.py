# anagram question from global logic 
# string 
# input = 'anisha'

# all possible words distinct permuations of this word:

# aanish



def anagrams(s):
    result = []

    def helper(path, remaining):
        # if no letters left → one full word ready
        if remaining == "":
            result.append(path)
            return

        # try each character
        for i in range(len(remaining)):
            ch = remaining[i]   # pick one character

            # remove that character from remaining
            left = remaining[:i]
            right = remaining[i+1:]
            new_remaining = left + right

            # go deeper
            helper(path + ch, new_remaining)

    helper("", s)
    return result


# run
# print(anagrams("abc"))

remaining = 'abc'
print(len(remaining))
left = remaining[:0]
print(left)
right = remaining[0+1:]
print(right)    


# list_of_character = [a,n,i,s,h,a]

# possible_word = [x,x,x,x,x,x]
# final_word []

# 1 2 3

# [3, 3, 3]

# 1 2 3
# 2 1 3

# 3*3*3 = 9

# i = 0
# for i in range(0,7):
    

# for char in input_word:
#     possible_word[0] = char
#     i = i + 1 




