import random

words_dict = {
    "사자": "lion", 
    "사과": "apple",
    "비행기": "airplane",
    "동물원": "zoo",
    "태양": "sun",
}

words = []
for word in words_dict:
    words.append(word)

random.shuffle(words)
chance = 5
for i in range(0, len(words_dict)):
    question = words[i]

    for j in range(0, chance):
        answer = input("{} 의 영어 단어를 입력하세요> ".format(question))
        english = words_dict[question]
        if answer == english:
            print("정답!!!")
            break
        else:
            print("틀렸습니다.")

    if answer != english:
        print("정답은 {} 이였습니다.".format(english))