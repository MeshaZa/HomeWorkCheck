import vk_api
import random
import time
import requests

token = "613084d1708901a7657805fc0ad2fce1a209e4c09ef047eb81e1e6757bce906b2ecbff8ee005318971d07"

def say(id, mess):
    vk.method("messages.send", {"peer_id": id, "message": mess, "random_id": random.randint(1, 2147483647)})

def add(sub, what):
    
    subs[sub] = what

    s = ""
    for x, hw in subs.items():
        s += "{0} {1} \n".format(x, hw) 

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

def check(X, liss):
    for l in liss:
        if l[:len(X)].lower() == X:
            return l
    return 0

def send_nudes(id):
    vk.method("messages.send", {"peer_id": id, "message": "Расписание:", "attachment": "photo-198555383_457239021", "random_id": 0})


subs = dict()

with open('Hw.txt', 'r') as obj:
    lines = obj.readlines()
    for line in lines:
        message = line.split()
        subs[message[0]] = conc(message[1:])

vk = vk_api.VkApi(token=token)
vk._auth_token()

all_hw = ['Алгебра',
          'Русский',
          'Английский',
          'Информатика',
          'История',
          'Физика',
          'География',
          'Геометрия',
          'Литература',
          'Михалыч']

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
            elif message == 's':
                s = ""
                for w in all_hw:
                    s += "⚠ " + w + '\n'
                say(id, s)
            elif message == 'r':
                send_nudes(id)
            elif message == '/h':
                say(id, '✅ Для записи новой домашки пиши -> \n a {название предмета} {домашка} \n можешь писать первые несколько символов предмета если лень\n\n\n' +
                        '✅ Для списка всех заданий пиши -> \n d\n\n\n'+
                        '✅ Чтобы узнать полное задание предмета пиши -> \n c {название предмета} \n можешь писать первые несколько символов предмета если лень\n\n\n'  +
                        '✅ Чтобы узнать список предметов пиши -> \n s \n\n\n' + 
                        '✅ Чтобы узнать расписание пиши  -> \n r \n\n\n')

            elif message[0] == 'a':
                
                message = message.split()

                if not check(message[1], all_hw):
                    say(id, 'Ой такого нету😳')
                    continue

                say(id, add(check(message[1], all_hw), conc(message[2:])))

            elif message[0] == 'c':


                message = message.split()

                if not check(message[1], all_hw):
                    say(id, 'Ой такого нету😳')
                    continue

                say(id, prnt(check(message[1], all_hw)))

            elif message == 'd':
                s = ""
                for x, hw in subs.items():
                    s += "⚠ {0} -> {1} \n\n\n".format(x, hw)
                say(id, s)

            else:

                s = (['Похоже у вас 14 IQ 😳\n\n','Ой, у вас хромосома выпала 😳\n\n'][random.randint(0,1)])
                s += 'Для списка комманд напиши /h'
                say(id, s)
                

        except Exception as obj:
            print(obj)
            say(id, 'Твои шаловливые ручки привели к ошибке программы')




            

            
        


