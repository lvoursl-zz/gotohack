import os

groups_file = tuple(open('groups_list.txt', 'r+'))
groups_list = [ ]

for group in groups_file:
	groups_list.append(int(group.replace('\n', '')))


for group in groups_list:
	if not os.path.exists('posts_data/' + str(group)):
	    os.makedirs('posts_data/' + str(group))