import requests

print ("WARNING this process works in a loop and can only be closed by exiting the program")
print ("Do you want continue? (y/n)")
start = input()
if start == "y":
	print ("Surf..")
	while True:
		r = requests.get('https://vk.com')
		print ("VK")
		r = requests.get('https://vk.com/im')
		print ("VK_IM")
		r = requests.get('https://vk.com/audio')
		print ("VK_AUDIO")
		r = requests.get('https://vk.com/friends')
		print ("VK_FRIENDS")
		r = requests.get('https://vk.com/id1')
		print ("VK_ID1")
		r = requests.get('https://vk.com/id2')
		print ("VK_ID2")
		r = requests.get('https://vk.com/id3')
		print ("VK_ID3")
		r = requests.get('https://vk.com/id4')
		print ("VK_ID4")
		r = requests.get('https://vk.com/id5')
		print ("VK_ID5")
		r = requests.get('https://vk.com/id4')
		print ("VK_ID4")
		r = requests.get('https://vk.com/id5')
		print ("VK_ID5")
		r = requests.get('https://vk.com/id6')
		print ("VK_ID6")
		r = requests.get('https://vk.com/id7')
		print ("VK_ID7")
		r = requests.get('https://vk.com/id8')
		print ("VK_ID8")
		r = requests.get('https://vk.com/id9')
		print ("VK_ID9")
		r = requests.get('https://vk.com/id10')
		print ("VK_ID10")
		r = requests.get('https://vk.com/id11')
		print ("VK_ID11")
		r = requests.get('https://vk.com/id12')
		print ("VK_ID12")
		r = requests.get('https://vk.com/id13')
		print ("VK_ID13")
		r = requests.get('https://vk.com/id14')
		print ("VK_ID14")
		r = requests.get('https://vk.com/id15')
		print ("VK_ID15")
		r = requests.get('https://vk.com/id16')
		print ("VK_ID16")
		r = requests.get('https://vk.com/id17')
		print ("VK_ID17")
		r = requests.get('https://vk.com/id18')
		print ("VK_ID18")
		r = requests.get('https://vk.com/id19')
		print ("VK_ID19")
		r = requests.get('https://vk.com/id20')
		print ("VK_ID20")
		r = requests.get('https://yandex.ru')
		print ("YANDEX")
		r = requests.get('https://yandex.ru/video/')
		print ("YANDEX_VIDEO")
		r = requests.get('https://yandex.ru/images/')
		print ("YANDEX_IMAGES")
		r = requests.get('https://yandex.ru/news/')
		print ("YANDEX_NEWS")
		r = requests.get('https://yandex.ru/maps/')
		print ("YANDEX_MAPS")
		r = requests.get('https://yandex.ru/all')
		print ("YANDEX_ALL")
		r = requests.get('https://www.google.com')
		print ("GOOGLE")
		r = requests.get('https://www.google.com/search')
		print ("GOOGLE_SEARCH")
		r = requests.get('https://www.youtube.com/')
		print ("YOUTUBE")
else:
	print ("exiting..")
	exit()
