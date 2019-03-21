import random
import time
import hgtk
import os

WORD_LIST = [
    "구글 뉴스는 구글이 제공하고 운영하는 무료 뉴스 애그리게이터이다.",
    "자동 집계 알고리즘에 의해 수천 곳의 발행사로부터 최신의 정보를 선별한다.",
    "현 총괄자는 리처드 징그러스이다.",
    "2002년 9월 출범한 이 서비스는 2006년 1월까지 3년에 걸쳐 베타 테스트로 표기되었다",
]

random.shuffle(WORD_LIST)
list_len = len(WORD_LIST)
current_count = 0

while current_count < list_len:
    os.system("cls")
    q = WORD_LIST[current_count]
    current_count += 1

    start_time = time.time()
    user_input = input(q + '\n')
    end_time = time.time() - start_time

    src = hgtk.text.decompose(q).replace("ᴥ", "")
    tar = hgtk.text.decompose(user_input).replace("ᴥ", "")

    correct = 0
    for i, c in enumerate(src, start=0):
        try:
            if tar[i] == c:
                correct += 1
        except:
            pass
    
    src_len = len(src)
    c = correct / src_len * 100 # 정확도
    e = (src_len - correct) / src_len * 100 # 오타율
    speed = float(correct / end_time) * 60
    
    print("속도: {:0.2f} 정확도: {:0.2f} % 오타율: {:0.2f} %".format(speed, c, e))
    os.system("pause")

