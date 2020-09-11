#!/usr/bin/env python3


if __name__ == '__main__':
	a = int(input())
	data = {}
	for i in range(a):
		name = input()
		score = float(input())
		data[name] = score
	print(data)
	second_score = sorted(list(set(data.values())))[1]
	print(second_score)
	second_scores = []
	for name, score in data.items():
		if score == second_score:
			second_scores.append(name)
	print(second_scores)
	second_scores_sorted = sorted(second_scores)
	for n in second_scores_sorted:
		print(n)