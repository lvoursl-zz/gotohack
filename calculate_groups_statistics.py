from urllib.request import urlopen

token = '4f318b471cda5c6bd6337cfc2644b478038ee7bb09a6158395101a036b834fc315c19b3fec6b9e28ea370'

groups_file = tuple(open('groups_list.txt', 'r+'))
groups_list = [ ]

for group in groups_file:
	groups_list.append(int(group.replace('\n', '')))

for group in groups_list:
	#posts_list - лист идшников последних 100 постов группы group

	posts_file = tuple(open('groups_posts/' + str(group), 'r+'))
	posts_list = [ ]

	for post in posts_file:
		posts_list.append(int(post.replace('\n', '')))


	file_of_posts_likes = open('calculated_likes_for_posts/' + str(group), 'w+')
	
	# для VK API : type = post; owner_id = group; item_id = post; 
	for post in posts_list:
		post_likes = 0
		# считаем количество лайков для поста		
		for user_id in users_ids:
			request = urlopen('https://api.vk.com/method/likes.isLiked?user_id=' + str(user_id) + '&' + 'type=post&owner_id=' + str(group) + '&item_id=' + str(post) + '&access_token=' + token)
			data = eval(request.read())	
			# if data ne empty.. to post_likes += 1

		print(post_likes, file = file_of_posts_likes, end = '\n')		
	
	file_of_posts_likes.close()



