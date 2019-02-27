#! usr/bin/env python2.7
# coding: utf-8


word = list("##"+raw_input()+"##")

transitions = {
	0: 'accept', 
	1: {
		'a' : (2, 'c', 'L'),
		'b' : (3, 'c', 'L'),
		'c' : (4, 0, 'L'),
		'#' : (0, 0, 'R')
	},
	2: {
		'a' : (0, 'a', 'R'),
		'b' : (0, 'a', 'R'),
		'c' : (0, 'a', 'R'),
		'#' : (0, 'a', 'R')
	},
	3: {
		'a' : (0, 'b', 'R'),
		'b' : (0, 'b', 'R'),
		'c' : (0, 'b', 'R'),
		'#' : (0, 'b', 'R')
	},
	4: {
		'a' : (0, 'c', 'R'),
		'b' : (0, 'c', 'R'),
		'c' : (0, 'c', 'R'),
		'#' : (0, 'c', 'R')
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