from urllib.request import urlopen
from time import sleep

token = '716811d6fede604077e74356456329209720bfa835433ea49d4db53ae2a8935fdceae78b5a93fe3ea651f'

groups_file = tuple(open('groups_list.txt', 'r+'))
groups_list = [ ]

for group in groups_file:
	groups_list.append(int(group.replace('\n', '')))

users_ids_file = tuple(open('shkolniki.txt', 'r+'))
users_ids = [ ]

for user_id in users_ids_file:
	users_ids.append(int(user_id.replace('\n', '')))

print('File parsing ends')

membership_counter = open('counted/membership_counter', 'w+')

# group - ид группы
for group in groups_list[10:]:
	group_members = ""
	members_counter = 0
	group_file = open('membership/' + str(group), 'w+')

	print('I am counting group: ' + str(group))
	counter = 0
	for user_id in users_ids:
			counter += 1
			request = urlopen('https://api.vk.com/method/groups.isMember?group_id=' + str(group) + '&' + 'user_id=' + str(user_id))
			data = eval(request.read())	
			
			if (data['response'] == 1):
				print(members_counter)
				members_counter += 1
				group_members = str(group_members) + str(user_id) + '\n'

			if (counter % 100 == 0): 
				print('Counter = ' + str(counter))
				sleep(0.2)

	print(group_members, file = group_file)

	print(str(group) + ' ' + str(members_counter), file = membership_counter)


