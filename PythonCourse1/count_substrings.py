def count_substring(string, sub_string):
	positions = []
	count = 0

	string = string.lower()
	sub_string = sub_string.lower()

	n = 0
	while n<len(string):
		if sub_string[0] == string[n]:
			positions.append(n)
		n+=1
	j=0
	while j < len(positions):
		temp_string = string[positions[j]:(positions[j]+len(sub_string))]
		if temp_string == sub_string:
			count+=1
		j+=1
	return count

print(count_substring("AngelAngelAngel", "ang"))
