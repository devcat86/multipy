from random import *
from time import *
from turtle import *
import base64
import pelmen_fun
devcount = 0 
def devmode(devcount):
    if devcount == 1:
        print("<<<Dev Mode>>>")
        print("Тут я тестирую разное что добавляю ;)")
        print("Доступны: ультра быстрый таймер")
        per2 = int(input("Что выбираете?"))
        if per2 == 1:
            timer1 = int(input("УЛЬТРА Таймер обратного отсчета. Введите секунды."))
        for i in range(timer1, -1, -1):
            print(i)
    if devcount != 1:
        print("Blocked!!")
def main():
    length = int(input("Введите длину пароля: "))
    password = pelmen_fun.generate_password(length)
    print("Сгенерированный пароль:", password)
print("Привет! Это Project PelmenBot! Мои функции: \n1-заказ еды \n2-погода(ненастоящая) \n3-розыгрыш \n4-о чатботе \n5-что нового? \n6-погода \n7-секудомер \n8-таймер обратного отсчета \n9-генератор цифр \n10-шифратор паролей в base64 \n11-проверка длинны пароля \n12-игра КНБ \n13-тест\nВыбирай цифру!")
ipt = int(input("Что вы хотите сделать?(введите 0 для выхода):"))
while ipt != 0:
    if ipt == 1:
        pelmen_fun.eda()
    elif ipt == 2:
        pelmen_fun.pogod()
    elif ipt == 3:
        print("Угадайте число от 1 до 100!")
        count = randint(1,100)
        price = int(input("Введите число: "))
        while price != count:
            if price > 101:
                print("Сказали же, ДО 100 xD")
            elif price > count:
                print("Число меньше!")
            elif price < count:
                print("Число больше!")
            else:
                break
            price = int(input("Введите число: "))
        if price == count:
                print("Вы угадали!")
        if price != count:
            print("Повезет в другой раз!")
    elif ipt == 4:
        print("Чатбот projectpb(Пельмень). Версия 1.5.0 от 19.07.23. Все права съедены шлепой. 6,10 пункты взяты из интернета, я не писал их сам.")
    elif ipt == 5:
        pelmen_fun.info()
    elif ipt == 999:
        if devcount == 0:
            devcount += 1
            print("ok!")
            per2 = int(input("Войти в режим разработчика? 1 or 0"))
            if per2 == 1:
                devmode(devcount)
        if devcount != 1:
            print("Blocked!!")
    elif ipt == 6:
        city = input("Введите название города: ")
        weather = pelmen_fun.get_weather(city)
        print(weather)
    elif ipt == 7:
        sec_start = int(input("1 - запустить таймер, 0 - выйти"))
        if sec_start == 1:
            start = time()
            sec_end = int(input("0 - стоп"))
            end = time()
            total_time = (end - start)
            print("Время -",round(total_time, 3))
    elif ipt == 8:
        timer1 = int(input("Таймер обратного отсчета. Введите секунды."))
        for i in range(timer1, -1, -1):
            print(i)
            sleep(1)
    elif ipt == 9:
        passw = "0"
        gen_ipt = int(input("Введите длинну пароля:"))
        for i in range(gen_ipt):
            passw += str(randint(0,9))
        print("Ваш пароль:", passw)
    elif ipt == 10:
        q = input("Введите пароль: ")
        b = q.encode("UTF-8")
        e = base64.b64encode(b)
        s1 = e.decode("UTF-8")
        print(s1)
    elif ipt == 11:
        per3 = input("Введите пароль: ")
        print("Длинна пароля:", len(per3))
        if len(per3) < 8:
            print("Слишком короткий пароль! Рекомендую заменить на более надежный!")
    elif ipt == 12:
            pelmen_fun.knb() 
    elif ipt == 13:
        hideturtle()
        def fun1():
            color("blue")
            pensize(2)
            speed(15)
            for i in range(36):
                color("blue")
                bebra()
                left(10)
                color("green")
                bebra()
                left(10)
        def bebra():
            forward(100)
            left(120)
        fun1()
    elif ipt == 14:
        ran1 = randint(1,9)
        ran2 = randint(1,9)
        if ran1 == 1:
            color1 = "blue"
        if ran1 == 2:
            color1 = "yellow"
        if ran1 == 3:
            color1 = "green"
        if ran1 == 4:
            color1 = "red"
        if ran1 == 5:
            color1 = "coral"
        if ran1 == 6:
            color1 = "cyan"
        if ran1 == 7:
            color1 = "pink"
        if ran1 == 8:
            color1 = "darkgreen"
        if ran1 == 9:
            color1 = "blueviolet"
        def fun1(color1, ran2):
            color(color1)
            if ran2 == 1:
                circle(20)
            if ran2 == 2:
                begin_fill()
                circle(20)
                end_fill
            if ran2 == 3:
                forward(30)
            if ran2 == 4:
                left(90)
            if ran2 == 5:
                for i in range(4):
                    forward(100)
                    left(90)
            if ran2 == 6:
                circle(100)
            if ran2 == 7:
                begin_fill()
                circle(20)
                x = 0
                y = 0
                y += 20
                goto(x, y)
            if ran2 == 8:
                per11 = 0
                for i in range(26):
                    forward(per11)  
                    per11 += 5
                    left(90) 
            if ran2 == 9:
                circle(20)
        for i in range(20):
            ran1 = randint(1,9)
            ran2 = randint(1,9)
            if ran1 == 1:
                color1 = "blue"
            if ran1 == 2:
                color1 = "yellow"
            if ran1 == 3:
                color1 = "green"
            if ran1 == 4:
                color1 = "red"
            if ran1 == 5:
                color1 = "coral"
            if ran1 == 6:
                color1 = "cyan"
            if ran1 == 7:
                color1 = "pink"
            if ran1 == 8:
                color1 = "darkgreen"
            if ran1 == 9:
                color1 = "blueviolet"
            fun1(color1, ran2)
    else: 
        print("Прости, я тебя не понял:(")
    ipt = int(input("Что вы хотите сделать?(введите 0 для выхода):"))
print("Пока ;)")