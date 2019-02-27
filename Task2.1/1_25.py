#! usr/bin/env python2.7
# coding: utf-8


word = list("##"+raw_input()+"##")

transitions = {
	0: 'accept', 
	1: {
		'a' : (2, 0, 'R'),
		'b' : (1, 0, 'R'),
		'c' : (1, 0, 'R'),
		'#' : (5, 0, 'L')
	},
	2: {
		'a' : (2, 0, 'R'),
		'b' : (3, 0, 'L'),
		'c' : (1, 0, 'R') 
	},
	3: {
		'a' : (4, 'x', 'R'),
		'b' : (4, 'x', 'R'),
		'c' : (4, 'x', 'R') 
	},
	4: {
		'a' : (1, 'c', 'R'),
		'b' : (1, 'c', 'R'),
		'c' : (1, 'c', 'R') 
	},
	5: {
		'a' : (5, 0, 'L'),
		'b' : (5, 0, 'L'),
		'c' : (5, 0, 'L'),
		'#' : (0, 0, 'R'),
		'x' : (6, 0, 'R')
	},
	6: {
		'a' : (7, 0, 'L'),
		'b' : (8, 0, 'L'),
		'c' : (9, 0, 'L'),
		'#' : (11, 0, 'L')
	},
	7: {
		'a' : (10, 'a', 'R'),
		'b' : (10, 'a', 'R'),
		'c' : (10, 'a', 'R'),
		'x' : (10, 'a', 'R')
	},
	8: {
		'a' : (10, 'b', 'R'),
		'b' : (10, 'b', 'R'),
		'c' : (10, 'b', 'R'),
		'x' : (10, 'b', 'R') 
	},
	9: {
		'a' : (10, 'c', 'R'),
		'b' : (10, 'c', 'R'),
		'c' : (10, 'c', 'R'),
		'x' : (10, 'c', 'R') 
	},
	10: {
		'a' : (6, 0, 'R'),
		'b' : (6, 0, 'R'),
		'c' : (6, 0, 'R')
	},
	11: {
		'a' : (5, '#', 'L'),
		'b' : (5, '#', 'L'),
		'c' : (5, '#', 'L')
	}
}

cur_state = 1
cur_char_ind = 2


while transitions[cur_state] != 'accept':
	state, change, step = transitions[cur_state][word[cur_char_ind]]
	if change != 0:
		word[cur_char_ind] = change

	if step == 'R':
		cur_char_ind += 1
	else:
		cur_char_ind -= 1

	cur_state = state

	print word, cur_state, cur_char_ind

print "".join(word).replace("#","")