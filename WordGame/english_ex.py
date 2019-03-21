import requests
from bs4 import BeautifulSoup
import re
import json
import random
import os

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

def get_news():
    url = "https://www.huffingtonpost.com/"
    r = requests.get(url, headers=headers)

    bs = BeautifulSoup(r.content, "lxml")
    divs = bs.select("div.card--left.card--media-left") # select 는 리스트를 리턴한다.
    contents_string = ""

    for div in divs:
        links = div.select("a.card__link.yr-card-headline") # select 는 리스트를 리턴한다.
        if len(links) > 0:
            href = links[0].get("href")
            
            r = requests.get(href, headers=headers)
            bs = BeautifulSoup(r.content, "lxml")
            contents = bs.select("div.content-list-component.yr-content-list-text.text > p") # select 는 리스트 리턴
            for p in contents:
                contents_string += p.text
        break
    return contents_string

def naver_translate(word):
    try:
        url = "https://ac.dict.naver.com/enendict/ac?q={}&q_enc=utf-8&st=11001".format(word)
        r = requests.get(url, headers=headers)
        jdata = json.loads(r.text)
        return jdata["items"][0][0][1][0]
    except:
        pass
    return None

def make_question_list(strings):
    text_string = strings.lower()
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

    question_dict = []
    frequency = {}
    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    
    add_count = 0
    frequency_list = frequency.keys()
    for word in frequency_list:
        count = frequency[word]
        if count > 1:
            kor = naver_translate(word)
            if kor == "" or kor is None:
                continue
            question_dict.append({kor: word})
            add_count += 1
            if add_count > 20: 
                break
    return question_dict

def quize():
    news_string = get_news()
    question_list = make_question_list(news_string)
    random.shuffle(question_list)
    chance = 5
    for i in range(0, len(question_list)): # 문제 수 만큼 도는 for
        os.system("cls")
        q = question_list[i]
        kor = list(q.keys())[0]
        english = q.get(kor)

        print("*" * 90)
        print("문제: {}".format(kor))
        print("*" * 90)

        for j in range(0, chance): # 정답을 맞출 기회 횟수만큼
            user_input = input("위의 뜻이 의미하는 단어를 입력하세요> ")
            if user_input == english:
                print("정답!! {} 문제 남음".format(len(question_list) - i))
                os.system("pause")
                break
            else:
                n = chance - (j + 1)
                if j == 0:
                    print("{} 가 아닙니다!!! {} 번 기회가 있습니다.".format(user_input, n))
                elif j == 1:
                    print("{} 가 아닙니다!!! {} 번 기회가 있습니다. 힌트: {}로 시작".format(user_input, n, english[0]))
                elif j == 2:
                    hint = " _ " * int(len(english) - 2)
                    print("{} 가 아닙니다!!! {} 번 기회가 있습니다. 힌트: {} {} {}로 시작".format(user_input, n, english[0], english[1], hint))
                elif j == 3:
                    hint = " _ " * int(len(english) - 3)
                    print("{} 가 아닙니다!!! {} 번 기회가 있습니다. 힌트: {} {} {} {}로 시작".format(user_input, n, english[0], english[1], english[2], hint))
                else:
                    print("틀렸습니다!!!! 정답은 {} 입니다.".format(english))
                    os.system("pause")
    print("모든 문제를 종료했습니다.")    

quize()