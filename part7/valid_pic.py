# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
	if len(pic) != 11:
		return False
	ctrl_str = "0123456789ABCDEFHJKLMNPRSTUVWXY"
	day = pic[:2]
	month = pic[2:4]
	year = ""
	num_str = pic[:6] + pic[7:10]
	try:
		total_sum = int(num_str)
	except ValueError:
		return False
	if ctrl_str[total_sum % 31] != pic[10]:
		return False
	if pic[6] == '+':
		year = "18" + pic[4:6]
	elif pic[6] == '-':
		year = "19" + pic[4:6]
	elif pic[6] == 'A':
		year = "20" + pic[4:6]
	else:
		return False
	try:
		datetime(int(year), int(month), int(day))
	except ValueError:
		return False
	

	return True

if __name__ == "__main__":
	print(is_it_valid("230827-906F"))
	print(is_it_valid("120488+246L"))
	print(is_it_valid("310823A9877"))