from urllib.request import urlopen
from time import sleep

token = 'a0d09cab75e648f5ed37b6e00232b97f459528c0045b1d2f550d6725ce7903b8b6c74978690bc71a4dfa137ba1c7e'

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
for group in groups_list[16:]:
	group_members = ""
	members_counter = 0
	group_file = open('membership/' + str(group), 'w+')

	print('I am counting group: ' + str(group))
	counter = 0
	for user_id in users_ids:
		try:
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
		except Exception as e:
			print(e)

	print(group_members, file = group_file)

	print(str(group) + ' ' + str(members_counter), file = membership_counter)


