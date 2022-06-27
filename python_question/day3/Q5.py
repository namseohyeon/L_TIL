#로또 번호 추첨

import random

lotto_list =[]

def lotto():
    print("***로또 추첨을 시작합니다***")
    for i in range (0,6):
        lotto= random.randrange(1,46)
        lotto_list.append(lotto)
    print("추첨된 로또 번호 ===>"+str(lotto_list))


lotto()