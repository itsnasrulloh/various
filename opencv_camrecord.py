# Recording Video 
# from a webcam or IP camera
# by @itsnasrulloh

import cv2

# cap = VideoCapture(0) captures first web camera, change it to: cap = cv2.VideoCapture(rtsp://username:password@ipaddress:rtspPort)
# to capture certain IP camera. default IP address for cameras is: 192.168.1.64
cap = cv2.VideoCapture(0) 

w = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH) # width of cap
h = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)  # height of cap
framerate = cap.get(cv2.CAP_PROP_FPS)  # framerate of cam
filename = "webcam.avi"  # output file will be saved as filename

# Writer writes output video to a file with certain name, frame rate and resolution. Resolution should be same as of the input
writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'MP42'), framerate, (w, h)) #  The Writer

# Main loop
while True:
    ret, frame = cap.read()
    if ret:
      cv2.imshow('frame',frame) # show the frame
      video.write(frame) # write the frame into output file
      if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' on keyboard to stop
          break

cap.release() # release the camera
cv2.destroyAllWindows() # destroy all the windows created






