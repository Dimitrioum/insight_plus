import cv2

cap = cv2.VideoCapture(-1)

if __name__ == '__main__':
    while 1:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('test', frame)

