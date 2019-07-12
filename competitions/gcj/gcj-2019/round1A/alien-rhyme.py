registered  = []
t = int(input())
for i in range (1, t+1):
	n = int(input())
	w = []
	for j in range(0, n):
		input_w = str(input())
		assert input_w.isupper()
		w.append(input_w)
	
	reverse_w = []
	for x in w:
		reverse_string = x[::-1]
		reverse_w.append(reverse_string)
	reverse_w.sort()

	#iterate the suffix
	print(reverse_w[0][:1])
	t_suffix_stack = []
	for k in range(0, len(reverse_w)-1):
		if reverse_w[k][:k+1] == reverse


		