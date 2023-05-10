# Write your solution here:
class Series:
	def __init__(self, title: str, seasons: int, genres: list):
		self.title = title
		self.seasons = seasons
		self.genres = genres
		self.count = 0
		self.ratings = 0
		self.rating = 0

	def rate(self, rating: int):
		self.count += 1
		self.ratings += rating
		if self.ratings > 0:
			self.rating = self.ratings / self.count
		else:
			self.rating = 0

	def __str__(self):
		genre_string = ", ".join(self.genres)
		if self.rating == 0:
				return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\nno ratings"
		return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{self.count} ratings, average {self.rating:.1f} points"

def minimum_grade(rating: float, series_list: list):
		rate_list = []
		for i in series_list:
			if i.rating >= rating:
				rate_list.append(i)
		return rate_list

def includes_genre(genre: str, series_list: list):
	genre_list = []
	for i in series_list:
		for g in i.genres:
			if genre == g:
				genre_list.append(i)
	return genre_list

if __name__ == "__main__":
	dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
	print(dexter)
	s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
	s1.rate(5)

	s2 = Series("South Park", 24, ["Animation", "Comedy"])
	s2.rate(3)

	s3 = Series("Friends", 10, ["Romance", "Comedy"])
	s3.rate(2)
	series_list = [s1, s2, s3]
	print("a minimum grade of 4.5:")
	
	for series in minimum_grade(4.5, series_list):
		print(series.title)

	print("genre Comedy:")
	for series in includes_genre("Comedy", series_list):
		print(series.title)