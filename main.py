import time
import datetime
import requests
from queue import Queue
from threading import Thread

import cv2
import pyautogui
import numpy as np


def kvadro(x, q):
    time.sleep(0.41)
    images = requests.get('http://192.168.43.23:8080/shot.jpg')
    video = np.array(bytearray(images.content), dtype=np.uint8)
    render = cv2.imdecode(video, -1)
    cv2.imwrite(f'{x}.jpg', render)
    q.put(1)
    print("kvadra", datetime.datetime.now())


def sony(c, q):
    if c == 1:
        pyautogui.click(1257, 1067)
    pyautogui.moveTo(1700, 258)
    pyautogui.mouseDown()
    time.sleep(1) 
    pyautogui.click()
    time.sleep(1)
    pyautogui.mouseUp()
    # pyautogui.click(1257, 1067)
    print("camera", datetime.datetime.now())


if __name__ == "__main__":
    q = Queue()
    for i in range(0, 1):
        p1 = Thread(target=kvadro, args=(i,q,), daemon=True)
        p2 = Thread(target=sony, args=(i, q,), daemon=True)
        p1.start()
        p2.start()
        p1.join()
        p2.join()
