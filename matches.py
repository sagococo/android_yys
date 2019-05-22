import cv2

def match(template, img):

    h, w = template.shape[:2]

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    return max_val, max_loc[0] + int(w/2), max_loc[1] + int(h/2)

