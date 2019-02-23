import random


def time(car):
    l = car['li']
    if (l%10) == 0:
        t_1 = int(l//10)
    else:
        t_1 = int(l//10) + 1
    a1 = [-1, 0, 1]
    a = random.choice(a1)
    time = t_1 + a
    if time <= 0:
        time = 1
    return(time)


def azs(car, text2, counter):
    automat = car['fuel']
    auto1 = 0
    auto2 = 0
    auto3 = 0
    for i in text2:
        if counter == i[0]:
            auto1 += 1
            print('Автомат №'+i[0], 'максимальная очередь:', i[2], 'Марки бензина:', i[4:],'->' + auto1*'*' )
        elif counter == i[0]:
            auto2 += 1
            print('Автомат №' + i[0], 'максимальная очередь:', i[2], 'Марки бензина:', i[4:], '->' + auto2 * '*')
        else:
            auto3 += 1
            print('Автомат №' + i[0], 'максимальная очередь:', i[2], 'Марки бензина:', i[4:], '->' + auto3 * '*')
    return



def main():
    price_d = {'АИ-80': '34', 'АИ-92': '41', 'АИ-95': '43.9', 'АИ-98': '48.1'}
    with open('input.txt') as f_in1:
        t1 = f_in1.readline()
        text1 = f_in1.readlines()
    with open('azs.txt') as f_in2:
        text2 = f_in2.readlines()
    car = {'time1': '00:01', 'li': 10, 'fuel': 'АИ-98'}
    time(car)
    l = car['li']
    count = 0
    a1 = {}
    a2 = {}
    a3 =  {}
    for i in text1:
        counter = 1
        for r in text2:
            if car['fuel'] in r:
                azs(car, text2, counter)


            else:
                counter += 1



        count += 1
        if count == 1:
            continue
        else:
            car['time1'] = i[0]
            car['li'] = i[2]
            car[i[4]] = price_d[i[2]]
        l += car['li']




if __name__ == "__main__":
    main()