# Write your solution here
def first_word(sen):
	word = sen.split()
	return word[0]
	# i = 0
	# while sen[i] != " ":
	# 	i += 1
	# return sen[0:i]

def second_word(sen):
	word = sen.split()
	return word[1]

def last_word(sen):
	word = sen.split()
	return word[-1]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))