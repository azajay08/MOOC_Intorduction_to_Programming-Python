# Write your solution here
def anagrams(str1, str2):
	if sorted(str1) == sorted(str2):
		return True
	return False

if __name__ == "__main__":
	print(anagrams("tame", "meta")) # True
	print(anagrams("tame", "mate")) # True
	print(anagrams("tame", "team")) # True
	print(anagrams("tabby", "batty")) # False
	print(anagrams("python", "java")) # False