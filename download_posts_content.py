from urllib.request import urlopen
from time import sleep 

token = '4f318b471cda5c6bd6337cfc2644b478038ee7bb09a6158395101a036b834fc315c19b3fec6b9e28ea370'

groups_file = tuple(open('groups_list.txt', 'r+'))
groups_list = [ ]

for group in groups_file:
	groups_list.append(int(group.replace('\n', '')))


for group in groups_list:
	#posts_list - лист идшников последних 100 постов группы group
	print('Group:' + str(group))
	posts_file = tuple(open('groups_posts/' + str(group), 'r+'))
	posts_list = [ ]

	for post in posts_file:
		posts_list.append(int(post.replace('\n', '')))

	counter = 0

	for post in posts_list:
		print(post)
		counter += 1
		# скачиваем контент постов
		request = urlopen('https://api.vk.com/method/wall.getById?posts=-' + str(group) + '_' + str(post) + '&access_token=' + token)
		data = eval(request.read())	
		post_file = open('posts_data/' + str(group) + '/' + str(post), 'w+')
		try:
			print(data['response'], file = post_file)
		except:
			pass
		post_file.close()

		if counter % 3 == 0:
			sleep(0.4)
		