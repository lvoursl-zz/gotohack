# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urlencode
import json 

token = '4f318b471cda5c6bd6337cfc2644b478038ee7bb09a6158395101a036b834fc315c19b3fec6b9e28ea370'

groups_list = tuple(open('groups_list.txt', 'r+'))
clear_groups_list = [ ]

for group in groups_list:
	clear_groups_list.append(int(group.replace('\n', '')))


for group in clear_groups_list:
	out_file = open('groups_posts/' + str(group), 'w')

	request = urlopen('https://api.vk.com/method/wall.get?owner_id=-'+ str(group) + '&count=100&filter=owner' + '&access_token=' + token)
	data = eval(request.read())	

	for i in range(1, len(data['response'])):
	 	if data['response'][i]['id']:
	 		print(data['response'][i]['id'], file = out_file, end = '\n')

	
	out_file.close()