import random


def time(car):
    l = int(car['li'])
    if (l % 10) == 0:
        t_1 = int(l // 10)
    else:
        t_1 = int(l // 10) + 1
    a1 = [-1, 0, 1]
    a = random.choice(a1)
    time = t_1 + a
    if time <= 0:
        time = 1
    return(time)


def azs(car, kolonki, counter):  # {'time1': '00:01', 'li': 10, 'fuel': 'АИ-80'}
    automat = car['fuel']  # АИ-80, azs.txt, 1
    auto1 = 0
    auto2 = 0
    auto3 = 0
    for i in kolonki:
        if counter == i[0]:
            auto1 += 1
            print('Автомат №' + i[0] + ';', 'максимальная очередь:', i[2] + ';', 'Марки бензина:', i[4:], '->' + auto1 * '*')
        elif counter == i[0]:
            auto2 += 1
            print('Автомат №' + i[0] + ';', 'максимальная очередь:', i[2] + ';', 'Марки бензина:', i[4:], '->' + auto2 * '*')
        else:
            auto3 += 1
            print('Автомат №' + i[0] + ';', 'максимальная очередь:', i[2] + ';', 'Марки бензина:', i[4:], '->' + auto3 * '*')
    return


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
    for i in car_list:
        time(i)

    # l = car['li']
    count = 0
    # a1 = {}
    # a2 = {}
    # a3 = {}
    for i in car_list:
        print(i)
        counter = 1
        for r in kolonki:
            if i['fuel'] in r:
                azs(i, kolonki, counter)
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
