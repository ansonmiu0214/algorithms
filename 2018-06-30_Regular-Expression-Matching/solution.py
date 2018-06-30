#!/bin/python3

from collections import deque

def isMatch(s, p):
	nfa, accept = pattern_to_nfa(p)
	table, accepting = nfa_to_dfa(nfa, accept)

	return match(s, table, accepting)


def match(s, table, accepting, curr_state = 0):
	if s == "":
		return curr_state in accepting

	if curr_state not in table:
		return False
	
	letter = s[0]
	next_states = []
	if letter in table[curr_state]:
		next_states.append(table[curr_state][letter])
	
	if '.' in table[curr_state]:
		next_states.append(table[curr_state]['.'])

	res = False
	for state in next_states:
		res = res or match(s[1:], table, accepting, state)

	return res
	

def pattern_to_nfa(p, start = 0):
	p_ptr, p_end = 0, len(p)
	if p_ptr == p_end:
		return ([], start)

	next = start
	letter = p[p_ptr]
	transitions = []
	p_ptr += 1

	transitions.append((start, letter, start + 1))
	if p_ptr < p_end and p[p_ptr] == '*':
		p_ptr += 1
		next += 1
		
		transitions.append((start + 1, '', start))
		transitions.append((start + 1, '', start + 2))
		transitions.append((start, '', start + 2))

	next += 1
	rest, accept = pattern_to_nfa(p[p_ptr:], next)
	return transitions + rest, accept
	

def get_transitions(nfa, curr_state, epsilons, curr_closure):
	# Get non-epsilon edges from NFA
	edges = [(curr_state, token, epsilons[e]) for (s, token, e) in nfa if (s in curr_closure and token != '')]

	transitions = dict()
	for (curr, tok, next) in edges:
		if (curr, tok) in transitions:
			transitions[(curr, tok)] = transitions[(curr, tok)].union(next)
		else:
			transitions[(curr, tok)] = next

	for key in transitions:
		transitions[key] = frozenset(transitions[key])

	return transitions


def nfa_to_dfa(nfa, accept):
	# Generate e-closures
	epsilons = [epsilon_closure(nfa, i) for i in range(accept + 1)]

	# Mapping of DFA accepting states
	accepting = dict()
	curr_state = 0

	# Mapping of state closures to id of DFA states
	state_map = dict()

	# Maintain queue of new closures to explore; initialise to e-closure of 0
	queue = deque()
	queue.append((None, epsilons[0]))

	table = dict()

	# Iterate through new unseen states
	while queue:
		prev, closures = queue.popleft()

		# Add mapping to current state (and accepting if necessary)
		state_map[closures] = curr_state
		if accept in closures:
			accepting[curr_state] = True

		# Get non-epsilon transitions from NFA
		transitions = get_transitions(nfa, curr_state, epsilons, closures)
		
		for (_, tok), next_state in transitions.items():
			if next_state not in state_map:
				# Explore next state later
				queue.append(((curr_state, tok), next_state))
			else:
				# State already explored; add mapping
				if curr_state not in table:
					table[curr_state] = { tok: state_map[next_state]}
				else:
					table[curr_state][tok] = state_map[next_state]

		if prev is not None:
			s, tok = prev
			if s not in table:
				table[s] = { tok: curr_state }
			else:
				table[s][tok] = curr_state			

		curr_state += 1
	
	return table, accepting


# Computes epsilon closure of @param state.
def epsilon_closure(ts, state):
	closure = set()
	closure.add(state)

	new_entries = deque()
	new_entries.append(state)
	while new_entries:
		st = new_entries.popleft()
		for (s, letter, e) in ts:
			if not (s == st and letter == ''):
				continue

			if e not in closure:
				new_entries.append(e)

			closure.add(e)

	return frozenset(closure)
	

if __name__ == "__main__":
	print("Enter input string: ", end="")
	s = input().strip()
	
	print("Enter regex pattern: ", end="")
	p = input().strip()

	res = isMatch(s, p)
	print(res)