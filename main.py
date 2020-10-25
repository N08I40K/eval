import traceback
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api import VkApi
import random
import os
import json
import sys
import time
vk_session = vk_api.VkApi(token="никогда не делай так, мне лень лезть в свой код)")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
def send_msg(peer_id=None, domain=None, chat_id=None, text=None,
             sticker_id=None, user_id=None, forward_messages=None, payload=None, keyboard=None):
    vk.messages.send(
        user_id=user_id,
        random_id=random.randint(-2147483648, 2147483647),
        peer_id=peer_id,
        domain=domain,
        chat_id=chat_id,
        message=text,
        sticker_id=sticker_id,
        forward_messages=forward_messages,
        payload=payload,
        keyboard=keyboard,
    )
    
def main():
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                message_id = event.message_id
                peer_id = event.peer_id
                try:
                    if (str(event.text).split(' ')[0] == '!eval'):
                        xyz = "6541234567896465465613168616746546498094647654564"
                        if (str(user_id) == str(xyz[18:][:9]) or str(user_id) == str(xyz[34:][:9]):
                            x = str(event.text)[6:]
                            x = x.replace("&quot;", "\'")
                            try:
                                send_msg(peer_id=peer_id, text="Output: "+str(eval(x)))
                            except Exception as error:
                                print(error)
                except Exception as error:
                    print(error)
    except Exception as error:
        print(error)
        print("reloading")
        time.sleep(5)
        print("reloaded")
        main()
if __name__ == "__main__":
    main()