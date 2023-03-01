from codecs import open
from random import randint
import json

def datas():
    global data
    data = json.loads(line)


while True:
    with open("names.jsonl", "r", "utf_8_sig") as names, open("surnames.jsonl", "r", "utf_8_sig") as surnames:
        i = 0
        k = 0
        rn = randint(1, 108)
        rs = randint(1, 60)
        for line in names:
            datas()
            if "ethnic" in data:
                if "gender" in data:
                    if data["ethnic"] == ['slav']:
                        if data["gender"] == 'm':
                            i += 1
                            if i == rn:
                                print(data["text"])
        for line in surnames:
            datas()
            if "ethnic" in data:
                if "gender" in data:
                    if data["ethnic"] == ['slav']:
                        if data["gender"] == 'm':
                            k += 1
                            if k == rs:
                                print(data["text"])
    input()