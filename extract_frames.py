import cv2
import os

frames_folder = "./data/frames/"

if not os.path.exists(frames_folder):
    os.makedirs(frames_folder)

cam = cv2.VideoCapture("./data/apple_falling.mp4")

frameno = 0
while(True):
   ret, frame = cam.read()
   if ret:
      name = f"./data/frames/{str(frameno)}.png"
      print('new frame captured...' + name)

      cv2.imwrite(name, frame)
      frameno += 1
   else:
      break

cam.release()
cv2.destroyAllWindows()