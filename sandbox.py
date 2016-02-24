file_data = tuple(open("file_for_plot", 'r+'))

data = []

for p in file_data:
	data.append(int(p))


print(data)