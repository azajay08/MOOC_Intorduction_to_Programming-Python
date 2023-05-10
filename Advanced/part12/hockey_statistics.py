# Write your solution here
import json

class Player:
	def __init__(self, name:str, nat:str, assists:int, goals:int, pens:int, team:str, games:str):
		self.name = name
		self.nationality = nat
		self.assists = assists
		self.goals = goals
		self.penalties = pens
		self.team = team
		self.games = games
		self.points = assists + goals

	def __str__(self):
		return f'{self.name:21}{self.team:3}{self.goals:4} + {self.assists:2} = {(self.points):3}'

class HockeyApplication:   
	def __init__(self):
		self.players = []

	def add_players(self, player_data: list):
		for p in player_data:
			player = Player(p['name'],
			p['nationality'],
			p['assists'],
			p['goals'],
			p['penalties'],
			p['team'],
			p['games'])
			self.players.append(player)

	def read_json(self):
		if True:
			filename = input('file name: ')
		else:
			filename = 'partial.json'
		with open(filename) as file:
			return json.loads(file.read())
		
	def search_player(self):
		name = input('name: ')
		for player in self.players:
			if player.name == name:
				print(player)

	def list_teams(self):
		teams = map(lambda player: player.team, self.players)
		for team in sorted(set(list(teams))):
			print(team)

	def list_countries(self):
		countries = map(lambda player: player.nationality, self.players)
		for country in sorted(set(list(countries))):
			print(country)

	def order_by_points(self, player):
		return [player.points, player.goals]

	def list_players_in_team(self):
		team = input('team: ')
		players = filter(lambda player: player.team == team, self.players)
		for player in sorted(players, key=self.order_by_points, reverse=True):
			print(player)

	def list_players_in_country(self):
		country = input('country: ')
		players = filter(lambda player: player.nationality == country, self.players)
		for player in sorted(players, key=self.order_by_points, reverse=True):
			print(player)

	def list_most_points(self):
		limit = int(input('how many: '))
		players = sorted(self.players, key=self.order_by_points, reverse=True)
		count = 1
		for player in players:
			if count <= limit:
				print(player)
				count += 1
	
	def order_by_goals(self, player):
		return [player.goals, (player.games)* - 1]

	def list_most_goals(self):
		limit = int(input('how many: '))
		players = sorted(self.players, key=self.order_by_goals, reverse=True)
		count = 1
		for player in players:
			if count <= limit:
				print(player)
				count += 1


	def help(self):
		print('commands:')
		print('0 quit')
		print('1 search for player')
		print('2 teams')
		print('3 countries')
		print('4 players in team')
		print('5 players from country')
		print('6 most points')
		print('7 most goals')

	def execute(self):
		player_data = self.read_json()
		print(f'read the data of {len(player_data)} players')
		self.add_players(player_data)
		self.help()
		while True:
			print()
			command = input('command: ')
			if command == '0':
				break
			elif command == '1':
				self.search_player()
			elif command == '2':
				self.list_teams()
			elif command == '3':
				self.list_countries()
			elif command == '4':
				self.list_players_in_team()
			elif command == '5':
				self.list_players_in_country()
			elif command == '6':
				self.list_most_points()
			elif command == '7':
				self.list_most_goals()


app = HockeyApplication()
app.execute()