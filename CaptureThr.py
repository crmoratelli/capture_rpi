import cv2
import numpy as np
import threading

class CaptureThr(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None, fname=None):
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.running = False
        self.fname = fname
 
    def status(self):
        return self.running

    def finish(self):
        self.running = False

    def run(self):

        self.running = True

        # Create a VideoCapture object
        cap = cv2.VideoCapture(0)

        # Check if camera opened successfully
        if not cap.isOpened(): 
            print("Unable to read camera feed")
 
        # Default resolutions of the frame are obtained.The default resolutions are system dependent.
        # We convert the resolutions from float to integer.
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        # Define the codec and create VideoWriter object.
        out = cv2.VideoWriter(self.fname, cv2.VideoWriter_fourcc('H','2','6','4'), 15, (frame_width, frame_height))
 
        while self.running:
            ret, frame = cap.read()

            if ret: 
                # Write the frame into the file 'output.avi'
                out.write(frame)
  
            # Break the loop
            else:
                break 
 
        # When everything done, release the video capture and video write objects
        out.release()

 