import vk_api
import random
import time
import random

token = "613084d1708901a7657805fc0ad2fce1a209e4c09ef047eb81e1e6757bce906b2ecbff8ee005318971d07"

def say(id, mess):
	vk.method("messages.send", {"peer_id": id, "message": mess, "random_id": random.randint(1, 2147483647)})

def add(sub, what):
	
	subs[sub] = what

	s = ""
	for x, hw in subs.items():
		s += str(x) + "{hw} \n"

	with open('Hw.txt', 'w') as obj:
		obj.write(s)


	return 'Всё ок!!!'

def prnt(sub):
	return subs[sub]

def conc(X):
	s = ""
	for x in X:
		s+=x + ' '
	return s


subs = dict()

with open('Hw.txt', 'r') as obj:
	lines = obj.readlines()
	for line in lines:
		message = line.split()
		subs[message[0]] = conc(message[1:])


vk = vk_api.VkApi(token=token)
vk._auth_token()


while True:

    print('Бот запущен')
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]

        print(body.lower())
        message = str(body.lower()).strip()

        try:
        	if message == 'off':
        		say(id, 'Бля?')
        		break

        	elif message[:3] == 'add':
        		message = message.split()
        		say(id, add(message[1], conc(message[2:])))
        	elif message[:3] == 'chk':
        		message = message.split()
        		say(id, prnt(message[1]))
        	elif message == 'descr':
        		s = ""
        		for x, hw in subs.items():
        			s += "* ", str(x)," -> ", str(hw), "\n\n\n" 
        			say(id, s)
        	else:
        		say(id, (['Упс что-то пошло не так...','Дура тупая писать научись (((((((((((('][random.randint(0,1)]))    
        except:
        	say(id, 'Несёшь хуйню')




        	

            
        


