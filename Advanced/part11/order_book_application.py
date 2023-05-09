# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task:
	task_count = 0
	def __init__(self, description: str, programmer: str, workload: int):
		self.description = description
		self.programmer = programmer
		self.workload = workload
		self.__finished = False
		Task.task_count += 1
		self.id = Task.task_count
		
	def is_finished(self):
		return self.__finished

	def mark_finished(self):
		self.__finished = True

	def __str__(self):
		if self.is_finished():
			return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
		return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"

class OrderBook:
	def __init__(self):
		self.__tasks = []
		
	def add_order(self, description: str, programmer: str, workload: int):
		task = Task(description, programmer, workload)
		self.__tasks.append(task)

	def all_orders(self):
		return self.__tasks

	def programmers(self):
		return list(set([task.programmer for task in self.__tasks]))
	
	def mark_finished(self, id: int):
		for task in self.__tasks:
			if task.id == id:
				task.mark_finished()
				return
		raise ValueError(f'Order with {id} does not exist')

	def finished_orders(self):
		return [task for task in self.__tasks if task.is_finished()]

	def unfinished_orders(self):
		return [task for task in self.__tasks if not task.is_finished()]

	def status_of_programmer(self, programmer: str):
		if programmer not in self.programmers():
			raise ValueError(f'{programmer} does not exists')
		tasks = [task for task in self.__tasks if task.programmer == programmer]
		finished = 0
		unfinished = 0
		finished_workload = 0
		unfinished_workload = 0
		for task in tasks:
			if task.is_finished():
				finished += 1
				finished_workload += task.workload
			else:
				unfinished += 1
				unfinished_workload += task.workload
		return (finished, unfinished, finished_workload, unfinished_workload)

class OrderBookApplication:
	def __init__(self):
		self.__orderbook = OrderBook()

	def programmer_status(self):
		prog = input('programmer: ')
		if prog not in self.__orderbook.programmers():
			print("erroneous input")
			return
		s = self.__orderbook.status_of_programmer(prog)
		print(f'tasks: finished {s[0]} not finished {s[1]}, hours: done {s[2]} scheduled {s[3]}')

	def programmers(self):
		for programmer in self.__orderbook.programmers():
			print(programmer)

	def mark_finished(self):
		try:
			id = int(input('id: '))
		except:
			print("erroneous input")
			return
		id_list = [task.id for task in self.__orderbook.all_orders()]
		if id not in id_list:
			print("erroneous input")
			return
		self.__orderbook.mark_finished(id)
		print('marked as finished')

	def list_unfinished_tasks(self):
		if len(self.__orderbook.unfinished_orders()):
			for task in self.__orderbook.unfinished_orders():
				print(task)
		else:
			print('no unfinished tasks')

	def list_finished_tasks(self):
		if len(self.__orderbook.finished_orders()):
			for task in self.__orderbook.finished_orders():
				print(task)
		else:
			print('no finished tasks')

	def add_order(self):
		description = input('description: ')
		prog_work = input('programmer and workload estimate: ').split()
		programmer = prog_work[0]
		try:
			workload = int(prog_work[1])
		except:
			print("erroneous input")
			return
		self.__orderbook.add_order(description, programmer, workload)
		print('added!')

	def help(self):
		print('commands:')
		print('0 exit')
		print('1 add order')
		print('2 list finished tasks')
		print('3 list unfinished tasks')
		print('4 mark task as finished')
		print('5 programmers')
		print('6 status of programmer')

	def execute(self):
		self.help()
		while True:
			print()
			cmd = int(input('command: '))
			if cmd == 0:
				break
			elif cmd == 1:
				self.add_order()
			elif cmd == 2:
				self.list_finished_tasks()
			elif cmd == 3:
				self.list_unfinished_tasks()
			elif cmd == 4:
				self.mark_finished()
			elif cmd == 5:
				self.programmers()
			elif cmd == 6:
				self.programmer_status()
			else:
				self.help()



app = OrderBookApplication()
app.execute()