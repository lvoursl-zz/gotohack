groups_list = tuple(open('groups_list.txt', 'r+'))
clear_groups_list = [ ]

for group in groups_list:
	clear_groups_list.append(int(group.replace('\n', '')))

for group in clear_groups_list:
	out_file = open('calculated_likes/' + str(group), 'w')
	
