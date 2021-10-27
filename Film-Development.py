import time
import tkinter


def stabilizer():
    timer = 0
    print("Pour in stabilizer.")
    time.sleep(1)
    print("Agitate")
    time.sleep(10)
    while timer != 45:
        time.sleep(1)
        timer += 1
        print(timer)
        if timer == 15:
            print("Stop agitation.")
    print("Pour out stabilizer, hang film to dry.")

def rinse():
    timer = 0
    end = 0
    print("Pour in water and agitate.")
    time.sleep(10)
    while end != 120:
        time.sleep(1)
        end += 1
        timer += 1
        print(timer)
        if timer == 30:
            timer = 0
            print("Pour out water.")
            time.sleep(5)
            print("Pour in new water.")
            time.sleep(5)
            print("Agitate.")
            time.sleep(2)
    stabilizer()


def blix():
    timer = 485
    print("Pour in blix.")
    time.sleep(10)
    while timer != 490:
        time.sleep(1)
        timer += 1
        print(timer)
        if timer % 30 == 0:
            if timer != 630:
                print("Agitate")
    print("Pour out blix.")
    time.sleep(10)
    rinse()

def developer():
    timer = 205
    print("Pour in developer.")
    time.sleep(10)
    while timer != 210:
        time.sleep(1)
        timer += 1
        print(timer)
        if timer % 30 == 0:
            if timer != 210:
                print("Agitate")
    print("Pour out developer.")
    time.sleep(5)
    blix()





developer()
