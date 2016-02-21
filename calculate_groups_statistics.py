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
	for post in posts_list
		# считаем количество лайков для поста
		post_likes = 0
		print(post_likes, file = file_of_posts_likes, end = '\n')
	
	file_of_posts_likes.close()



