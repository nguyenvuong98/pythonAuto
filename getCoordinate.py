import pyautogui as pg
import time
from action import click_pg

execScript = False


def fightVsStrong(name):
    resFightBtn = pg.locateCenterOnScreen('images/fight.png', confidence=0.8)
    
    click_pg(name, resFightBtn.x, resFightBtn.y)
    
    time.sleep(1)
    resFight = pg.locateCenterOnScreen('images/fightButton.png', confidence=0.8)
    click_pg(name, resFight.x, resFight.y)

    time.sleep(3)
    resIgnore = pg.locateCenterOnScreen('images/ignore.png', confidence=0.8)
    click_pg(name, resIgnore.x, resIgnore.y)

    time.sleep(2)
    resBack = pg.locateCenterOnScreen('images/backBtn.png', confidence=0.8)
    click_pg(name, resBack.x, resBack.y)

    time.sleep(1)
