# Write your solution here
def make_cookbook(filename: str):
	meal = {}
	with open(filename) as file:
		words = [[]]
		reci = []
		for line in file:
			if line == '\n':
				words.append(reci)
				reci = []
				continue
			reci.append(line.strip())
		words.append(reci)
		words.remove(words[0])
		for word in words:
			recipe = {}
			ingredients = []
			prep = int(word[1])
			recipe['prep_time'] = prep
			for ingred in word[2:]:
				ingredients.append(ingred)
			recipe['ingredients'] = ingredients
			meal[word[0]] = recipe
	return meal

def search_by_time(filename: str, prep_time: int):
	cookbook = make_cookbook(filename)
	recipe = []
	# print(cookbook)
	for k, v in cookbook.items():
		# print(v['prep_time'])
		if v['prep_time'] <= prep_time:
			recipe.append(f"{k}, preparation time {v['prep_time']} min")
	return recipe

def search_by_name(filename: str, word: str):
	cookbook = make_cookbook(filename)
	recipes = []
	# print(cookbook)
	for meals in cookbook:
		# print(meals)
		if word.lower() in str(meals).lower():
			recipes.append(meals)
	return recipes

def search_by_ingredient(filename: str, ingredient: str):
	cookbook = make_cookbook(filename)
	recipes = []
	for k, v in cookbook.items():
			# print(v['prep_time'])
		if ingredient in v['ingredients']:
			recipes.append(f"{k}, preparation time {v['prep_time']} min")
	return recipes

if __name__ == "__main__":
	found_recipes = search_by_name("recipes1.txt", "cake")
	for recipe in found_recipes:
		print(recipe)

	found_recipe = search_by_time("recipes1.txt", 20)
	for recipes in found_recipe:
		print(recipes)

	found_recipes = search_by_ingredient("recipes1.txt", "eggs")

	for recipe in found_recipes:
		print(recipe)