import random


def time(l):
    if (l%10) == 0:
        t_1 = int(l//10)
    else:
        t_1 = int(l//10) + 1
    a1 = [-1, 0, 1]
    a = random.choice(a1)
    time = t_1 + a
    if time <= 0:
        time = 1
    return time

cc = 1500
cl = 0

fuels = {}
with open('azs.txt') as f_a:
    fuels_0 = f_a.readlines()

for i in fuels_0:
    i = i.split(' ')
    i1 = i[2:]
    a = []
    b = 0
    for e in i1:
        ei = e[-1]
        eii = ei.isdigit()
        if eii == 0:
            e = e[:-1]
            e = e[:]
        a.append(e)
    # a = tuple(a)
    fuels[i[0]] = [int(i[1]), b, a, []]

with open('input.txt') as f_i:
    cars_0 = f_i.readlines()

for i in cars_0:

    i = i.split(' ')
    time_60 = (int(i[0][0:2]))*60 + int(i[0][3:5])

    l = int(i[1])
    t = time(l)
    i[1] = t

    i2 = i[2]
    i22 = i2[-1]
    iii = i22.isdigit()
    if iii == 0:
        i[2] = i[2][:-1]

    for x in fuels:
        for y in fuels[x][3]:
            if y <= time_60:
               fuels[x][3].remove(y)
               fuels[x][1] += -1


    kol = float('inf')
    sp = []
    for e in fuels:
        j = fuels[e]
        for w in j[2]:
            if w == i[2]:
                sp.append(e)
    sp_n = []
    for d in sp:
        fd = fuels[d]
        if fd[1] < kol:
            kol = fd[1]
    for d in sp:
        fd = fuels[d]
        if fd[1] == kol:
            sp_n.append(d)
    sp_nn = []
    for d in sp_n:
        fd = fuels[d]
        if fd[1] < fd[0]:
            sp_nn.append(d)
    num = float('inf')
    for d in sp_nn:
        d = int(d)
        if d < num:
            num = d
    if num == float('inf'):
        cl += 1
        print(i[0], 'машина покинула заправку бла-бла-бла')
        for h in fuels:
            print(fuels[h])

    else:
        num = str(num)
        fuels[num][1] += 1
        if len(fuels[num][3]) == 0:  #время в очереди (все время)
            to = time_60 + i[1]
        else:
            m = max(fuels[num][3])
            to = m + i[1]
        fuels[num][3].append(to)
        t = int(to) - int(time_60)
        if int(time_60) <= cc:
            print('В', i[0], 'новый клиент:', i[0], i[2], i[1], t, 'встал в очередь к автомату', '№' + num)
            cc = int(time_60) + int(t)
            for h in fuels:
                trew = 'Автомат № ' + str(h) + ';', 'максимальная очередь: ', str(fuels[h][0]), ';', 'Марки бензина:', \
                       str(fuels[h][2]) + '->', int(fuels[h][1]) * '*'
                print(*trew)
        else:
            new_gr_88 = (int(gr[4:]) + cc)
            new_gr = round(new_gr_88 / 60, 1)
            new_gr_int = int(new_gr)
            new_gr_min = int(round(new_gr % 1, 1) * 60)
            # print(new_gr_min)
            # print(new_gr_int)  # целые часы
            # print(new_gr)  # переведенные часы с минутыми
            if new_gr_int == 0:
                print('В', '0' + str(new_gr_int) + ':' + str(new_gr_min), 'клиент', gr, 'заправил свой автомобиль и покинул АЗС')
            elif new_gr_int == 0 and len(str(new_gr_min)) == 1:
                print('В', '0' + str(new_gr_int) + ':' + '0' + str(new_gr_min), 'клиент', gr, 'заправил свой автомобиль и покинул АЗС')
            elif len(str(new_gr_int)) == 1:
                print('В', '0' + str(new_gr_int) + ':' + str(new_gr_min), 'клиент', gr, 'заправил свой автомобиль и покинул АЗС')
            elif len(str(new_gr_int)) == 1 and len(str(new_gr_min)) == 1:
                print('В', '0' + str(new_gr_int) + ':' + '0' + str(new_gr_min), 'клиент', gr, 'заправил свой автомобиль и покинул АЗС')
            else:
                print('В', str(new_gr_int) + ':' + str(new_gr_min), 'клиент', gr, 'заправил свой автомобиль и покинул АЗС')
            cc = 1500
            for h in k:
                trew = 'Автомат № ' + str(h) + ';', 'максимальная очередь: ', str(k[h][0]), ';', 'Марки бензина:', \
                       str(k[h][2]) + '->', (int(k[h][1]) - 1) * '*'
                print(*trew)
            print('В', i[0], 'новый клиент:', i[0], i[2], i[1], t, 'встал в очередь к автомату', '№' + num)
            cc = int(time_60) + int(t)
            for h in fuels:
                trew = 'Автомат № ' + str(h) + ';', 'максимальная очередь: ', str(fuels[h][0]), ';', 'Марки бензина:', \
                       str(fuels[h][2]) + '->', int(fuels[h][1]) * '*'
                print(*trew)

        k = fuels
        gr = i[0]
                # print(fuels[h])

print("Сколько машин уехало не заправившись:", cl)