# Write your solution here
def op(cmd, n1, n2):
	s_split = cmd.strip().split()
	if s_split[2] == "==":
		if n1 == n2:
			return True
		return False
	if s_split[2] == "!=":
		if n1 != n2:
			return True
		return False
	if s_split[2] == "<":
		if n1 < n2:
			return True
		return False
	if s_split[2] == "<=":
		if n1 <= n2:
			return True
		return False
	if s_split[2] == ">=":
		if n1 >= n2:
			return True
		return False
	if s_split[2] == ">":
		if n1 > n2:
			return True
		return False

def run(program):
	vars = {}
	jumps = {}
	result = []
	for c in range(65, 91):
		vars[chr(c)] = 0
	cmd_len = len(program)
	i = 0
	while i < cmd_len:
		if program[i].islower():
			jumps[program[i].rstrip(":")] = i
		i += 1
	i = 0
	while i < cmd_len:
		if "MOV" in program[i]:
			c_split = program[i].strip().split()
			if c_split[2].isalpha():
				vars[c_split[1]] = int(vars[c_split[2]])
			else:
				vars[c_split[1]] = int(c_split[2])
		elif "ADD" in program[i]:
			c_split = program[i].strip().split()
			if c_split[2].isalpha():
				vars[c_split[1]] += int(vars[c_split[2]])
			else:
				vars[c_split[1]] += int(c_split[2])
		elif "SUB" in program[i]:
			c_split = program[i].strip().split()
			if c_split[2].isalpha():
				vars[c_split[1]] -= int(vars[c_split[2]])
			else:
				vars[c_split[1]] -= int(c_split[2])
		elif "MUL" in program[i]:
			c_split = program[i].strip().split()
			if c_split[2].isalpha():
				vars[c_split[1]] *= int(vars[c_split[2]])
			else:
				vars[c_split[1]] *= int(c_split[2])
		elif "PRINT" in program[i]:
			c_split = program[i].strip().split()
			if c_split[1].isalpha():
				result.append(vars[c_split[1]])
			else:
				result.append(int(c_split[1]))
		elif program[i].islower():
			jumps[program[i].rstrip(":")] = i
		elif "IF" in program[i]:
			c_split = program[i].strip().split()
			if c_split[1].isalpha():
				n1 = vars[c_split[1]]
			else:
				n1 = int(c_split[1])
			if c_split[3].isalpha():
				n2 = vars[c_split[3]]
			else:
				n2 = int(c_split[3])
			if op(program[i], n1, n2):
				i = int(jumps[c_split[5]])
				continue
		elif "JUMP" in program[i]:
			c_split = program[i].strip().split()
			i = int(jumps[c_split[1]])
			continue
		elif program[i] == "END":
			break
		i += 1
	return result

if __name__ == "__main__":
	# program1 = []
	# program1.append("MOV A 1")
	# program1.append("MOV B 2")
	# program1.append("PRINT A")
	# program1.append("PRINT B")
	# program1.append("ADD A B")
	# program1.append("PRINT A")
	# program1.append("END")
	# result = run(program1)
	# print(result)

	# program2 = []
	# program2.append("MOV A 1")
	# program2.append("MOV B 10")
	# program2.append("begin:")
	# program2.append("IF A >= B JUMP quit")
	# program2.append("PRINT A")
	# program2.append("PRINT B")
	# program2.append("ADD A 1")
	# program2.append("SUB B 1")
	# program2.append("JUMP begin")
	# program2.append("quit:")
	# program2.append("END")
	# result = run(program2)
	# print(result)

	program3 = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1', 'IF A <= N JUMP start']
	result = run(program3)
	print(result)