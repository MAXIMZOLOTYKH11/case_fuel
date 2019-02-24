import random


def t(i):
    l = int(i['li'])
    if (l % 10) == 0:
        t_1 = int(l // 10)
    else:
        t_1 = int(l // 10) + 1
    a1 = [-1, 0, 1]
    a = random.choice(a1)
    time = t_1 + a
    if time <= 0:
        time = 1
    return time


def azs(car, kolonki, counter, auto1, auto2, auto3):  # {'time1': '00:01', 'li': 10, 'fuel': 'АИ-80'}
    automat = car['fuel']  # АИ-80, azs.txt, 1
    if counter == 1:
        auto1 += 1
    elif counter == 2:
        auto2 += 1
    if counter == 3:
        auto3 += 1
    c = 0
    for i in kolonki:
        c += 1
        if c == 1:
            print('Автомат №' + i[0] + ';', 'максимальная очередь:', i[2] + ';', 'Марки бензина:', i[4:], '->' + auto1 * '*')
        if c == 2:
            print('Автомат №' + i[0] + ';', 'максимальная очередь:', i[2] + ';', 'Марки бензина:', i[4:], '->' + auto2 * '*')
        if c == 3:
            print('Автомат №' + i[0] + ';', 'максимальная очередь:', i[2] + ';', 'Марки бензина:', i[4:], '->' + auto3 * '*')
    a1 = auto1
    a2 = auto2
    a3 = auto3
    return a1,a2,a3


def main():
    # price_d = {'АИ-80': '34', 'АИ-92': '41', 'АИ-95': '43.9', 'АИ-98': '48.1'}
    with open('input.txt') as f_in1:
        text1 = f_in1.readlines()
        car_list = []
        for i in text1:
            car = i.split()
            d = {}
            d['time1'] = car[0]
            d['li'] = car[1]
            d['fuel'] = car[2]
            car_list.append(d)  # создали список(car_list) из словарей(d) машин

    with open('azs.txt') as f_in2:
        kolonki = f_in2.readlines()

    # car = {'time1': '00:01', 'li': 10, 'fuel': 'АИ-80'}
    count = 0
    auto1 = 0
    auto2 = 0
    auto3 = 0
    g = None
    for i in car_list:
        print(i)
        counter = 1
        go = 100
        cc = 0
        go = int(i['time1'][3:]) + t(i)
        for r in kolonki:
            if i['fuel'] in r:
                # azs(i, kolonki, counter, auto1, auto2, auto3)
                if go < int(i['time1'][3:]):
                    print('В', '00:'+str(go), 'клиент', car_list[cc]['time1'], car_list[cc]['fuel'], car_list[cc]['li'],'заправил свой автомобиль и покинул АЗС.')
                    cc += 1
                else:
                    print('В', i['time1'], 'новый клиент:', i['time1'], i['fuel'], i['li'], t(i), 'встал в очередь к автомату №' + str(counter))
                    if counter == 1:
                        auto1 += 1
                    elif counter == 2:
                        auto2 += 1
                    if counter == 3:
                        auto3 += 1
                    c = 0
                    for l in kolonki:
                        c += 1
                        if c == 1:
                            print('Автомат №' + l[0] + ';', 'максимальная очередь:', l[2] + ';', 'Марки бензина:', l[4:],
                                  '->' + auto1 * '*')
                        if c == 2:
                            print('Автомат №' + l[0] + ';', 'максимальная очередь:', l[2] + ';', 'Марки бензина:', l[4:],
                                  '->' + auto2 * '*')
                        if c == 3:
                            print('Автомат №' + l[0] + ';', 'максимальная очередь:', l[2] + ';', 'Марки бензина:', l[4:],
                                  '->' + auto3 * '*')
                    go = int(i['time1'][3:]) + t(i)
                    g = i
            else:
                counter += 1
        count += 1
        print('____________________________________________________________________________')
        print()
        # if count == 1:
        #     continue
        # else:
        #     car['time1'] = i[0]
        #     car['li'] = i[2]
        #     # car[i[4]] = price_d[i[2]]
        # l += car['li']


if __name__ == "__main__":
    main()
