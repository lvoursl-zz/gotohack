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

for group in groups_list:
	#posts_list - лист идшников последних 100 постов группы group
	print('Group:' + str(group))
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
			#post_data_text = post_data_text.strip()
			result_string_of_posts = result_string_of_posts + post_data_text + ' ' 
		except Exception as e:
			print(e)
			pass
		
		
		result_string_of_posts = killshit(result_string_of_posts)
		
		print(result_string_of_posts)

		for i in result_string_of_posts.split():
			if i in words_dict:
				words_dict[i] += 1
			else:
				words_dict[i] = 1
		#print(result_string_of_posts)
		for w in sorted(words_dict, key = words_dict.get, reverse = True):
		    for char in w:    	
		    	if char.isdigit():    		
		    		words_dict.pop(str(w), 0)
		    		break

		posts_stats_file = open('groups_top_words/' + str(group), 'w+')

		for w in sorted(words_dict, key = words_dict.get, reverse = True)[:40]:
			print(w, words_dict[w], file = posts_stats_file)

