# task: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
	n = len(string) // k
	for _ in range(n):
		t = string[:k]
		print("".join(sorted(set(t), key=t.index)))
		string = string[k:]
