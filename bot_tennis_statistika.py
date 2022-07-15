# -- coding: utf-8 --﻿
import vk_api
import time
import json
import os
import psutil
import random

vk = vk_api.VkApi(token=) # This code is hidden for privacy and copyright reasons
vk._auth_token()

def get_button (label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

class VkUpload(object):
    __slots__ = ('vk',)

    def __init__(self, vk):
        if not isinstance(vk, (VkApi, VkApiMethod)):
            raise TypeError(
                'The arg should be VkApi or VkApiMethod instance'
            )

        if isinstance(vk, VkApiMethod):
            self.vk = vk
        else:
            self.vk = vk.get_api()

    def photo_messages(self, photos):
        url  = self.vk.photos.getMessagesUploadServer()['upload_url']
        with FilesOpener(photos) as photo_files:
            response = self.http.post(url, files=photo_files)
        return self.vk.photos.saveMessagesPhoto(**response.json())

keyboard = {
    "one_time": False,
    "buttons": [
    [get_button(label="Запуск программы", color="positive")],
    [get_button(label="Настройки", color="primary")]
    ]
}

keyboardd = {
    "one_time": True,
    "buttons": [
        
    [get_button(label="Нет! Вернуться", color="positive")],
    [get_button(label="Да!", color="negative")]
    
    ]
}
keyboarddd = {
    "one_time": True,
    "buttons": [
        
    [get_button(label="Да", color="positive")],
    [get_button(label="Нет", color="negative")]
    
    ]
}
keyboardddd = {
    "one_time": False,
    "buttons": [
    [get_button(label="Рестартер", color="primary"),
    get_button(label="Глобальный цикл", color="primary")],
    [get_button(label="Назад", color="negative")]
    
    ]
}

keyboard5 = {
    "one_time": True,
    "buttons": [
    [get_button(label="Активация программы", color="positive")],
    [get_button(label="Назад", color="negative")]
    ]
}

keyboard6 = {
    "one_time": True,
    "buttons": [
    [get_button(label="Нет ключа!", color="primary")],
    [get_button(label="Назад", color="negative")]
    ]
}

#positive, negative, primary, default. 
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

keyboardd = json.dumps(keyboardd, ensure_ascii=False).encode('utf-8')
keyboardd = str(keyboardd.decode('utf-8'))

keyboarddd = json.dumps(keyboarddd, ensure_ascii=False).encode('utf-8')
keyboarddd = str(keyboarddd.decode('utf-8'))

keyboardddd = json.dumps(keyboardddd, ensure_ascii=False).encode('utf-8')
keyboardddd = str(keyboardddd.decode('utf-8'))

keyboard5 = json.dumps(keyboard5, ensure_ascii=False).encode('utf-8')
keyboard5 = str(keyboard5.decode('utf-8'))

keyboard6 = json.dumps(keyboard6, ensure_ascii=False).encode('utf-8')
keyboard6 = str(keyboard6.decode('utf-8'))

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body == "Нет! Вернуться":
                vk.method('messages.send', {"peer_id":id, "message": "Хорошо! Выберите действие!", "random_id": random.randint(1, 1000000), "keyboard": keyboard})
            elif body.lower() == "меню":
                vk.method('messages.send', {"peer_id":id, "message": "Хорошо! Выберите действие!", "random_id": random.randint(1, 1000000), "keyboard": keyboard})
            elif body == "Деньги":
                vk.method('messages.send', {"peer_id":id, "message": "Функция пока недоступна!", "random_id": random.randint(1, 1000000), "keyboard": keyboard})
            elif body.lower() == "скрин":
                VkUpload.photo_messages("path")     # This code is hidden for privacy and copyright reasons
                vk.method('messages.send', {"peer_id":id, "message": "Функция пока недоступна!", "random_id": random.randint(1, 1000000), "keyboard": keyboard})
            elif body.lower() == "активация программы":
                s = 2
                vk.method('messages.send', {"peer_id":id, "message": "Введите ключ авторизации!", "random_id": random.randint(1, 1000000), "keyboard": keyboard6})
                while s == 2:
                    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20})
                    if messages["count"] >= 1:
                        body = messages["items"][0]["last_message"]["text"]
                        if body.lower() == 'назад':
                            break
                        if body.lower() == 'нет ключа!':
                            vk.method('messages.send', {"peer_id":id, "message": "Обратитесь к администратору за приобретением ключа!", "random_id": random.randint(1, 1000000), "keyboard": keyboard})
                            break
                        if body != "Введите ключ авторизации!":
                            s = 1
                            body = str(body)
                            f = open('keys.txt', 'r')
                            keys = f.read()
                            f.close()
                            f = open('keys.txt', 'w')
                            f.write('')
                            f.close()
                            a1 = 0
                            a2 = 19
                            flag_vhod = False
                            flag = True
                            while True:
                                key = keys[a1:a2]
                                a1 += 20
                                a2 += 20
                                if body != key:
                                    if flag == True:
                                        f = open('keys.txt', 'w')
                                        f.write(key)
                                        f.close()
                                        flag = False
                                    else:
                                        f = open('keys.txt', 'a')
                                        f.write('\n' + key)
                                        f.close()
                                else:
                                    flag_vhod = True
                                    id_us = messages["items"][0]["last_message"]["from_id"]
                                    id_us = str(id_us)
                                    f = open('user_id.txt', 'a')
                                    f.write('\n' + id_us)
                                    f.close()
                                    vk.method('messages.send', {"peer_id":id, "message": "Ваш ID записан!", "random_id": random.randint(1, 1000000)})
                                    vk.method('messages.send', {"peer_id":id, "message": "Программа успешно активирована!", "random_id": random.randint(1, 1000000)})
                                if keys[a1:a2] == '':
                                    if flag_vhod == False:
                                        vk.method('messages.send', {"peer_id":id, "message": "Ключ не найден! Повторите попытку или обратитесь к администратору!", "random_id": random.randint(1, 1000000), "keyboard": keyboard5})
                                    break
            elif body.lower() == "глобальный цикл":
                f = open('global_prog.txt', 'r')
                while_ = f.read()
                f.close()
                f = open('for_bot.txt','w')
                f.write("True")
                f.close()
                if while_ == 'True':
                    vk.method('messages.send', {"peer_id":id, "message": "Глобальный цикл находиться в работе!\nВыключить глобальный цикл?", "random_id": random.randint(1, 1000000), "keyboard": keyboarddd})
                    f = open('for_bot_2.txt','w')
                    f.write("True")
                    f.close()
                elif while_ == 'False':
                    vk.method('messages.send', {"peer_id":id, "message": "Глобальный цикл отключен!\nВключить глобальный цикл?", "random_id": random.randint(1, 1000000), "keyboard": keyboarddd})
                    f = open('for_bot_2.txt','w')
                    f.write("False")
                    f.close()
                else:
                    vk.method('messages.send', {"peer_id":id, "message": "Не указан параметр (цикл выключен)!", "random_id": random.randint(1, 1000000)})
            elif body.lower() == 'да':
                vk.method('messages.send', {"peer_id":id, "message": "Понял Вас!", "random_id": random.randint(1, 1000000)})
                f = open('for_bot.txt', 'r')
                text = f.read()
                f.close()
                if text == 'True':
                    f = open('for_bot_2.txt','r')
                    flags = f.read()
                    f.close()
                    if flags == "True":
                        f = open('global_prog.txt', 'w')
                        f.write('False')
                        f.close()
                        vk.method('messages.send', {"peer_id":id, "message": "Глобальный цикл отключен!", "random_id": random.randint(1, 1000000), "keyboard": keyboard})
                        f = open('for_bot.txt','w')
                        f.write("False")
                        f.close()
                    else:
                        f = open('global_prog.txt', 'w')
                        f.write('True')
                        f.close()
                        vk.method('messages.send', {"peer_id":id, "message": "Глобальный цикл запущен!", "random_id": random.randint(1, 1000000), "keyboard": keyboard})
                        f = open('for_bot.txt','w')
                        f.write("False")
                        f.close()
                else:
                    pass
            elif body.lower() == 'нет':
                    vk.method('messages.send', {"peer_id":id, "message": "Хорошо!", "random_id": random.randint(1, 1000000), "keyboard": keyboard})
            elif body.lower() == "рестартер":
                f = open('TFclear.txt','w')
                f.write('True')
                f.close()
                vk.method('messages.send', {"peer_id":id, "message": "Рестартер запущен!", "random_id": random.randint(1, 1000000), "keyboard": keyboardddd})
            elif body.lower() == 'настройки':
                vk.method('messages.send', {"peer_id":id, "message": "Ок", "random_id": random.randint(1, 1000000), "keyboard": keyboardddd})
            elif body.lower() == 'назад':
                vk.method('messages.send', {"peer_id":id, "message": "Ок", "random_id": random.randint(1, 1000000), "keyboard": keyboard})
            elif body == "Да!":
                vk.method('messages.send', {"peer_id":id, "message": "Пока-пока!", "random_id": random.randint(1, 1000000)})
            elif body.lower() == "запуск программы":
                id_us = messages["items"][0]["last_message"]["from_id"]
                id_us = str(id_us)
                f = open('user_id.txt', 'r')
                users = f.read()
                f.close()
                if (id_us in users) == True:
                    vk.method('messages.send', {"peer_id":id, "message": "Понял! Запускаю программу!", "random_id": random.randint(1, 1000000)})
                else:
                    vk.method('messages.send', {"peer_id":id, "message": "Программа не активирована!", "random_id": random.randint(1, 1000000), "keyboard": keyboard5})
            elif body.lower() == "начать":
                vk.method('messages.send', {"peer_id":id, "message": "Для дальнейшей работы напишите: меню", "random_id": random.randint(1, 1000000)})
            else:
                vk.method('messages.send', {"peer_id":id, "message": "Не понял вас!", "random_id": random.randint(1, 1000000)})
        time.sleep(0.5)
    except Exception as E:
        time.sleep(0.5)
