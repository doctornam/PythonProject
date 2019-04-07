'''
포함하는 숫자
포함하지 않는 숫자
연속넘버
'''
import random
import numpy

def make_number():
    number_list = []
    rand_num = random.randint(1, 46)
    for i in range(6):
        while rand_num in number_list:
            rand_num = random.randint(1, 46)
        number_list.append(rand_num)

def make_lotto_win_number(**kwargs):
    complete = False
    while complete == False:
        rand_number = numpy.random.choice(range(1, 46), 6, replace=False)
        rand_number.sort()

        complete_number = [] # 최종 완성된 번호
        tmp_number = [] # 임시 번호
        if kwargs.get("include") is not None:
            inc_number = kwargs.get("include")
            complete_number.extend(inc_number)
            make_count = 6 - len(inc_number)
            for i in range(make_count):
                for j in rand_number:
                    if complete_number.count(j) == 0:
                        complete_number.append(j)
                        break
        else:
            complete_number.extend(rand_number)
        
        if kwargs.get("exclude") is not None:
            exc_number = kwargs.get("exclude")
            complete_number = list(set(complete_number) - set(exc_number))
            make_count = 6 - len(complete_number)
            rand_number = numpy.random.choice(range(1, 46), 6, replace=False)
            for i in range(make_count):
                for j in rand_number:
                    if complete_number.count(j) == 0:
                        complete_number.append(j)
                        break
        
        if kwargs.get("continuty") is not None:
            seq_count = 0
            seq_num = []
            for i in range(0, len(complete_number)):
                for j in range(i + 1, len(complete_number)):
                    if complete_number[i] + 1 == complete_number[j]:
                        seq_count += 1
                        seq_num.append(complete_number[i])
                        seq_num.append(complete_number[j])
            if seq_count < kwargs.get("continuty"):
                #[10, 2, 4, 5, 9, 22]
                make_numbers = []
                make_count = kwargs.get("continuty") - seq_count
                while make_count > 0:
                    rnd_pos = random.randint(1, 4)
                    n = complete_number[rnd_pos]
                    if complete_number.count(n+1) > 0:
                        continue
                    complete_number.insert(rnd_pos + 1, n + 1)
                    make_numbers.append(n)
                    make_numbers.append(n+1)

                    for i, num in enumerate(complete_number, start=0):
                        if num not in make_numbers:
                            if len(complete_number) > 6:
                                complete_number.pop(i)
                    make_count -= 1
        complete_number.sort()
        print(complete_number)
        complete = True

make_lotto_win_number(continuty=3)
