#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import pyautogui as pg
pg.PAUSE = 0.5

# from pyscreeze import ImageNotFoundException

def handler(func, *args):
    return func(*args)

def ckick(locate):
    print("click", locate)
    return pg.click(locate)

    # while True:
    #     locate = None
    #     for x in d.keys():
    #         locate = pg.locateCenterOnScreen(d[x]["pic"], confidence=0.90)
    #         if not locate is None:
    #             print(">>> ", x, locate)
    #             handler(d[x]["func"], locate)
    #             break
    #             # return x, locate
    #     if locate is None:
    #         print("targets not found")
    #         time.sleep(2)

    #     # pg.moveTo(1, 1, duration=random.random()+0.1)

if __name__=="__main__":

    # open notebook
    pg.press('win')
    pg.typewrite('notebook')
    pg.press('enter')

    # put down some text
    pg.typewrite('Hello pyautogui!')

    # maximize and close window
    pg.hotkey('win', 'up')
    pg.hotkey('alt', 'f4')

    # cancel to save
    pg.press('n')

