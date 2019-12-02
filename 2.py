#!/usr/bin/python

import cv2
import time
import numpy as np
import math


def lane_slope(aoi):
    lines = cv2.HoughLines(aoi, 1, np.pi/180, 85)
    if lines is not None:
        left_x = 0
        left_y = 0
        right_x = 0
        right_y = 0
        l_c = 0
        r_c = 0
        for line in lines:
            for rho, theta in line:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                dx = float(x2 - x1)
                dy = float(y2 - y1)
                if dx == 0:
                    continue
                if 0.2 > abs(dy/dx) or 0.6 < abs(dy/dx):
                    continue
                slope = dy / dx
                if slope < 0:
                    left_x += x2 - x1
                    left_y += y2 - y1
                    l_c += 1
                else:
                    right_x += x2 - x1
                    right_y += y2 - y1
                    r_c += 1
                cv2.line(canny, (x1, y1), (x2, y2), (255, 255, 255), 8)
        left_x = left_x / float(max(l_c, 1))
        left_y = left_y / float(max(l_c, 1))
        right_x = right_x / float(max(r_c, 1))
        right_y = right_y / float(max(r_c, 1))
        return left_y / float(max(left_x, 1)) + right_y / float(max(right_x, 1))
    return 0


if __name__ == "__main__":
    cap = cv2.VideoCapture(
        '/Users/ksh/Desktop/software-project-2/class-01-KSH-code/2.avi')
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = frame
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        canny = cv2.Canny(blur, 70, 140)
        canny = canny[250:350, :]
        print(-math.degrees(math.atan(lane_slope(canny))))

        cv2.imshow("full", canny)

        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    cv2.destroyAllWindows()
