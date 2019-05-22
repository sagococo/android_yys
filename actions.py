import datetime
import os
import time

from PIL import Image


def tap(x, y):
    cmd = 'adb shell input tap {} {}'.format(x, y)
    os.system(cmd)


def to_right():
    cmd = 'adb shell input swipe 900 500 100 500'
    os.system(cmd)


def to_left():
    cmd = 'adb shell input swipe 100 500 900 500'
    os.system(cmd)


def get_screenshot():
    cwd = os.getcwd()

    screenshot = 'adb shell /system/bin/screencap -p /sdcard/screenshot.png'
    print('开始截图 {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    os.system(screenshot)
    print('完成截图 {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    pull = 'adb pull /sdcard/screenshot.png {}/screenshot.png'.format(cwd)
    print('开始传输 {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    os.system(pull)
    print('完成传输 {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    print('开始旋转 {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    Image.open('screenshot.png').rotate(90, expand=True).save('screenshot.png')
    print('完成旋转 {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
