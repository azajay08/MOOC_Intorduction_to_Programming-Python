# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
	c_bike = {}
	with open(filename) as file:
		for line in file:
			l_split = line.strip().split(";")
			if l_split[0] == "Longitude":
				continue
			c_bike[l_split[3]] = (float(l_split[0]), float(l_split[1]))
		# print(c_bike)
	return c_bike

def distance(stations: dict, station1: str, station2: str):
	longitude1 = stations[station1][0]
	longitude2 = stations[station2][0]
	latitude1 = stations[station1][1]
	latitude2 = stations[station2][1]
	x_km = (longitude1 - longitude2) * 55.26
	y_km = (latitude1 - latitude2) * 111.2
	distance_km = math.sqrt(x_km**2 + y_km**2)
	return distance_km

def greatest_distance(stations: dict):
	dist = 0
	for st in stations:
		for comp in stations:
			temp = distance(stations, st, comp)
			if temp > dist:
				st1 = st
				st2 = comp
				dist = temp

	return (st1, st2, dist)

if __name__ == "__main__":
	stations = get_station_data('stations1.csv')
	d = distance(stations, "Designmuseo", "Hietalahdentori")
	print(d)
	d = distance(stations, "Viiskulma", "Kaivopuisto")
	print(d)
	stations = get_station_data('stations1.csv')
	station1, station2, greatest = greatest_distance(stations)
	print(station1, station2, greatest)