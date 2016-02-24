import re

def killshit(text):
    temp = text.split(' ')
    ans = ""
    for i in range (len(temp)):
        if len(temp[i]) > 4 and len(temp[i]) < 21:
            ans += temp[i]
            ans += ' '
    return ans

delete = re.compile(u'\W+?', re.UNICODE)

groups_file = tuple(open('groups_list.txt', 'r+'))
groups_list = [ ]

for group in groups_file:
	groups_list.append(int(group.replace('\n', '')))

file_for_plot = open('file_for_plot', 'w+')

for j in range(1, 150):
	a_lot_of_texts_posts = 0

	for group in groups_list:
		#posts_list - лист идшников последних 100 постов группы group
		#print('Group:' + str(group))
		posts_file = tuple(open('groups_posts/' + str(group), 'r+'))
		posts_list = [ ]

		for post in posts_file:
			posts_list.append(int(post.replace('\n', '')))

		words_dict = {}
		result_string_of_posts = ""

		for post in posts_list:
			try:			
				post_data_file = open('posts_data/' + str(group) + '/' + str(post), 'r+')
				all_post_data = post_data_file.read()
			
				post_data_text = re.findall(r'\'text\':(.*?),', str(all_post_data))			
				post_data_text = str(post_data_text)
				post_data_text = post_data_text.replace("<br>", " ")
				post_data_text = post_data_text.replace("original", " ")			
				
				post_data_text = delete.sub(' ', post_data_text)
				post_data_text = killshit(post_data_text)
				#print(post_data_text)
				post_data_text = post_data_text.lower()

				#print(len(post_data_text))

				if (len(post_data_text) > j): a_lot_of_texts_posts += 1

				#post_data_text = post_data_text.strip()

			except Exception as e:
				print(e)
				pass
			
	
	print(a_lot_of_texts_posts, file = file_for_plot)	

print(a_lot_of_texts_posts)