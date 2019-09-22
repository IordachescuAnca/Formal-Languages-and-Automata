from collections import defaultdict
import queue

class Lnfa:
	def __init__(self, states = [], alphabet = [], starting_state = -1, final_states = [], transitions = defaultdict(list), lambda_transitions = defaultdict(list)):
		self.__states = states
		self.__alphabet = alphabet
		self.__starting_state = starting_state
		self.__final_states = final_states
		self.__transitions = transitions
		self.__lambda_transitions = lambda_transitions

	def read_data(self):
		number_states = int(input("Enter the number of states. "))
		for _ in range(0,number_states):
			state = input()
			self.__states.append(state)

		number_alphabet = int(input("Enter how many letters the alphabet has. "))
		for _ in range(0, number_alphabet):
			letter = input()
			self.__alphabet.append(letter)

		self.__starting_state = input("Enter the starting state. ")

		number_final_states = int(input("Enter the number of final states. "))
		for _ in range(0, number_final_states):
			final_state = input()
			self.__final_states.append(final_state)

		number_transitions = int(input("Enter the number of transitions. "))
		self.__transitions = defaultdict(list)
		for _ in range(0, number_transitions):
			state1, letter, state2 = input("Enter state1, letter, state2: ").split()
			if letter == '.':
				self.__lambda_transitions[state1].append(state2)
			else:
				self.__transitions[(state1, letter)].append(state2)


	def write_data(self):
		print(self.__states)
		print(self.__alphabet)
		print(self.__starting_state)
		print(self.__final_states)
		print(self.__transitions)
		print(self.__lambda_transitions)


	def lambda_closure(self, state):
		closure = []
		is_visited = {}
		S = queue.LifoQueue()
		S.put(state)
		while not S.empty():
			current_state = S.get()
			if current_state not in is_visited:
				is_visited[current_state] = 1
				closure.append(current_state)
			for new_state in self.__lambda_transitions[current_state]:
				if new_state not in is_visited:
					S.put(new_state)
		return closure

	def check_word(self, word):
		
		state_set = []
		state_set.append(self.__starting_state)

		for letter in word:
			closure = []
			for current_state in state_set:
				current_closure = self.lambda_closure(current_state)
				closure = closure + list(set(current_closure) - set(closure))
			new_state_set = []
			for current_state in closure:
				set1 = []
				for state in self.__transitions[(current_state, letter)]:
					set1.append(state)
				new_state_set = new_state_set + list(set(set1) - set(new_state_set)) 
			state_set = new_state_set[:]

		for current_state in state_set:
			current_closure = self.lambda_closure(current_state)
			if len(list(set(self.__final_states) & set(current_state))) != 0:
				return "Yes"

		return "No"

'''---------------------------------------------------------------------------------------------------------------------------'''


Automata = Lnfa()
Automata.read_data()



while True:
	choice = int(input("Enter 2 for checking a word,1 for lambda closure or 0 for quitting: "))
	if choice == 2:
		word = input("Enter the word: ")
		print(Automata.check_word(word))
	elif choice == 1:
		state = input("Enter a state: ")
		print(Automata.lambda_closure(state))
	elif choice == 0:
		break