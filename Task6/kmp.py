#! usr/bin/env python2.7
# coding: utf-8

def compute_pref_func(pattern):
	m = len(pattern)
	pattern = list(pattern)
	pref_list = [0 for i in range(m+1)]
	k = 0
	for i in range(2, m+1):
		while k > 0 and pattern[k] != pattern[i-1]:
			k = pref_list[k]
		if pattern[k] == pattern[i-1]:
			k += 1
		pref_list[i] = k

	return pref_list

def kmp_matcher(text, pattern):
	n, m = len(text), len(pattern)
	text = list(text)
	pattern = list(pattern)
	pref_list = compute_pref_func(pattern)
	q = 0
	for i in range(1, n+1):
		while q > 0 and pattern[q] != text[i-1]:
			q = pref_list[q]
		if pattern[q] == text[i-1]:
			q += 1
		if q == m:
			print i-m
			q = pref_list[q]

if __name__ == '__main__':
	
	text, pattern = str(raw_input()), str(raw_input())
	kmp_matcher(text, pattern)
	#print compute_pref_func(pattern)