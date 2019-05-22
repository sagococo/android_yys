import datetime
import time

import actions
import matches
import cv2

if __name__ == '__main__':

    co = cv2.TM_CCOEFF_NORMED
    gongji = cv2.imread('gongji.png')
    jiangli = cv2.imread('jiangli.png')
    tansuo = cv2.imread('tansuo.png')
    yao = cv2.imread('yao.png')
    denglong = cv2.imread('denglong.png')
    pen = cv2.imread('pen.png')
    huode = cv2.imread('huode.png')
    dagongji = cv2.imread('dagongji.png')

    while True:
        actions.get_screenshot()
        img = cv2.imread('screenshot.png')

        print('开始比较 {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        value, x, y = matches.match(dagongji, img)
        print('完成比较 {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        if value > 0.9:
            actions.tap(x, y)
            continue

        print('开始比较 {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        value, x, y = matches.match(gongji, img)
        print('完成比较 {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        if value > 0.9:
            actions.tap(x, y)
            continue

        value, x, y = matches.match(pen, img)
        if value > 0.9:
            actions.tap(x, y)
            continue

        value, x, y = matches.match(jiangli, img)
        if value > 0.9:
            actions.tap(x, y)
            continue

        value, x, y = matches.match(huode, img)
        if value > 0.9:
            actions.tap(x + 600, y)
            continue

        value, x, y = matches.match(tansuo, img)
        if value > 0.9:
            actions.tap(x, y)
            continue
        time.sleep(2)





