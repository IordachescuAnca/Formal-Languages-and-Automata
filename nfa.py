from collections import defaultdict
import queue

class Nfa:
	def __init__(self, states = [], alphabet = [], starting_state = -1, final_states = [], transitions = defaultdict(list)):
		self.__states = states
		self.__alphabet = alphabet
		self.__starting_state = starting_state
		self.__final_states = final_states
		self.__transitions = transitions

	def reading_data(self):
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
			self.__transitions[(state1, letter)].append(state2)


	def write_data(self):
		print(self.__states)
		print(self.__alphabet)
		print(self.__starting_state)
		print(self.__final_states)
		print(self.__transitions)


	def check_word(self, word):
		Q = queue.Queue()
		Q.put(self.__starting_state)
		for letter in word:
			cnt = Q.qsize()
			for _ in range(0, cnt):
				current_state = Q.get()
				for state in self.__transitions[(current_state, letter)]:
					Q.put(state)

		while not Q.empty():
			state = Q.get()
			if state in self.__final_states:
				return "Yes"

		return "No"

'''-------------------------------------------------------------------------------------------------------'''

Automata = Nfa()
Automata.reading_data()


while True:
	choice = int(input("Enter 1 for checking a word or 0 for quitting: "))
	if choice == 1:
		word = input("Enter the word: ")
		print(Automata.check_word(word))
	elif choice == 0:
		break