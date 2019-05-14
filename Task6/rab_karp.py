text, pattern = str(raw_input()), str(raw_input())
d, q = len(set(text)), 41

data = dict(zip(set(text), range(d)))

n, m = len(text), len(pattern)
h = d**(m-1) % q
p, t = 0, 0

for i in range(m):
	p = (d*p + data[pattern[i]]) % q
	t = (d*t + data[text[i]]) % q
	
for s in range(n-m):
	if p == t:
		if pattern[:m] == text[s:s+m]:
			print s
	if s < n-m:
		t=(d*(t-data[text[s]]*h) + data[text[s+m]]) % q
