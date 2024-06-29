from ctypes import *
import time
import random

valuta       = "$"
money        = 0
startMoney   = 0
playGame     = True
defaultMoney = 10_000
windll.Kernel32.GetStdHandle.restype = c_long
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

def pobeda(result):
    color(14)
    print(f"    You won! {valuta}{result}")
    print(f"    Your current balance: {valuta}{money}")


def loss(result):
    color(12)
    print(f"  You lost! {valuta}{result}")
    print(f"    Your current balance: {valuta}{money}")


def getMaxCount(digit, v1, v2, v3, v4, v5):
    ret = 0
    if digit == v1:
        ret += 1
    if digit == v2:
        ret += 1
    if digit == v3:
        ret += 1
    if digit == v4:
        ret += 1
    if digit == v5:
        ret += 1
    return ret


def getOHBRes(stavka):
    res = stavka
    d1  = 0
    d2  = 0
    d3  = 0
    d4  = 0
    d5  = 0

    getD1 = True
    getD2 = True
    getD3 = True
    getD4 = True
    getD5 = True
    col   = 10

    while (getD1 or getD2 or getD3 or getD4 or getD5):
        if getD1:
            d1 += 1
        if getD2:
            d2 -= 1
        if getD3:
            d3 += 1
        if getD4:
            d4 -= 1
        if getD5:
            d5 += 1

        if d1 > 9:
            d1 = 0
        if d2 < 0:
            d2 = 9
        if d3 > 9:
            d3 = 0
        if d4 < 0:
            d4 = 9
        if d5 > 9:
            d5 = 0

        if random.randint(0, 20) == 1:
            getD1 = False
        if random.randint(0, 20) == 1:
            getD2 = False
        if random.randint(0, 20) == 1:
            getD3 = False
        if random.randint(0, 20) == 1:
            getD4 = False
        if random.randint(0, 20) == 1:
            getD5 = False


        time.sleep(0.01)
        color(col)
        col += 1
        if col > 15:
            col = 10

        print("    " + "%" * 10)
        print(f"   {d1}{d2}{d3}{d4}{d5}")

    maxCount = getMaxCount(d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d2, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d3, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d4, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d5, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

    color(14)
    if maxCount == 2:
        print(f" Совпадение двух чисел! Твой выигрыш в размере ставки: {valuta}{res}")
    elif maxCount == 3:
        res *= 2
        print(f" Совпадение трих чисел! Твой выигрыш 2:1 {valuta}{res}")
    elif maxCount == 4:
        res *= 5
        print(f" Совпадение четырех чисел! Твой выигрыш 5:1 {valuta}{res}")
    elif maxCount == 5:
        res *= 10
        print(f" БИНГО! Совпадение пяти чисел! Твой выигрыш 10:1 {valuta}{res}")

    color(11)
    print()
    input(" Нажмите Enter для продолжения...")
    return res


def oneHandBandit():
    global money
    playGame = True

    while playGame:
         colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В ОДНОРУКОГО БАНДИТА!")
         color(14)
         print(f"\n   Ваш текущий баланс: {valuta}{money}\n")
         color(5)
         print("Правила игры: ")
         print("  1. При совпадении 2-х чисел ставка не списывается.")
         print("  2. При совпадении 3-х чисел выигрыш 2:1.")
         print("  3. При совпадении 4-х чисел выигрыш 5:1.")
         print("  4. При совпадении 5-ти чисел выигрыш 10:1.")
         print("  0. Выйти из игры.\n")

         stavka = getIntInput(0, money, f"  Введите вашу ставку от 0 до {money}: ")
         if stavka == 0:
            return 0
        
        money -= stavka
        money += getOHBRes(stavka)

        if money <= 0:
            playGame = False

def getDice():
    count = random.randint(3, 8)
    sleep = 0

    while count > 0:
        color(count + 7)
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(" " * 10, "----- -----")
        print(" " * 10, f"| {x} | | {y} |")
        print(" " * 10, "----- -----")
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1
    return x + y


def dice():
    global money
    playGame = True

    while playGame:
        print()
        colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!")
        color(14)
        print(f"\n Ваш текущий баланс: {valuta}{money}\n")
        color(7)
        stavka = getIntInput(0, money, f"    Введите вашу ставку в пределах {valuta}{money}: ")

        if stavka == 0:
            return 0

        playRound = True
        control   = stavka
        oldResult = getD1ice()
        firstPlay = True

        while playRound and stavka > 0 and money > 0:
            if stavka > money:
                stavka = money

            color(11)
            print(f"\n    Ваш текущий баланс: {valuta}{money}")
            color(12)
            print(f"\n    Текущая сумма чисел на кости: {oldResult}")
            color(11)
            print(f"\n    Сумма чисел на гранях будет больше, меньше или равна предыдущей?")
            color(7)
            x = getInput("0123", "   Введите 1 - больше, 2 - меньше, 3 - равно или 0 - выход: ")

            if x != "0":
                firstPlay = False
                if stavka > money:
                    stavka = money

                money -= stavka 
                diceResult = getD1ice()
                win = (oldResult > diceResult and x == "2") or (oldResult < diceResult and x == "1") or (oldResult < diceResult and x == "1")
                





























