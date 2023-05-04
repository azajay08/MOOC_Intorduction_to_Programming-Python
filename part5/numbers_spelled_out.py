# Write your solution here
def dict_of_numbers():
	new_d = {}
	single = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	decs = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	special = {
		0: 'zero',
		10: 'ten',
		11: 'eleven',
		12: 'twelve',
		13: 'thirteen',
		14: 'fourteen',
		15: 'fifteen',
		16: 'sixteen',
		17: 'seventeen',
		18:	'eighteen',
		19: 'nineteen',

	}
	for i in range(100):
		if i in special:
			new_d[i] = special[i]
		elif i > 20 and i % 10:
			new_d[i] = decs[i // 10] + '-' + single[i % 10]
		else:
			new_d[i] = decs[i // 10] + single[i % 10]
	return new_d