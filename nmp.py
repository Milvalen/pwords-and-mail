from random import randint, randrange, sample
from codecs import open
import json


# основной цикл
while True:
    with open("names.jsonl", "r", "utf_8_sig") as names, open("surnames.jsonl", "r", "utf_8_sig") as surnames:
        i = 0
        k = 0
        rn = randint(1, 108)
        rs = randint(1, 60)
        rnf = randint(1, 92)
        rsf = randint(1, 58)
        g = randint(1, 2)
        if g == 1:


            # генерация мужских имён
            for line in names:
                data = json.loads(line)
                if "ethnic" in data:
                    if "gender" in data:
                        if data["ethnic"] == ['slav']:
                            if data["gender"] == 'm':
                                i += 1
                                if i == rn:
                                    n = data["text"]
            for line in surnames:
                data = json.loads(line)
                if "ethnic" in data:
                    if "gender" in data:
                        if data["ethnic"] == ['slav']:
                            if data["gender"] == 'm':
                                k += 1
                                if k == rs:
                                    s = data["text"]


        # 50/50 шанс генерации мужского/женского имени
        else:

            
            # генерация женских имён
            for line in names:
                data = json.loads(line)
                if "ethnic" in data:
                    if "gender" in data:
                        if data["ethnic"] == ['slav']:
                            if data["gender"] == 'f':
                                i += 1
                                if rnf == i:
                                    n = data["text"]
            for line in surnames:
                data = json.loads(line)
                if "ethnic" in data:
                    if "gender" in data:
                        if data["ethnic"] == ['slav']:
                            if data["gender"] == 'f':
                                k += 1
                                if rsf == k:
                                    s = data["text"]


        # генерация почты и пароля
        random_value = randrange(1, 10)
        mail_server_list = ['gmail.com', 'yandex.ru', 'outlook.com', 'mail.ru']
        random_mail = sample('abcdefghijklmnopqrstuvwxyz0123456789', random_value)
        random_mail = ''.join(random_mail)
        random_mail_server = mail_server_list[randrange(0, len(mail_server_list))]
        random_mail = random_mail + '@' + random_mail_server
        rp = sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&', 16)
        rp = ''.join(rp)
        print(f"Name: {n} {s}")
        print(f"Mail: {random_mail}")
        print(f"Pass: {rp}")
    input()