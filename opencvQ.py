import multiprocessing
import cv2
"""
one main queue (mainQ)
TWO processes 1.read
               2.show (frame processing also done here)
                
""" 
def read(mainQ):
    cap = cv2.VideoCapture(0)
 
    while True:
        _ , img = cap.read()
        if img is not None:
            mainQ.put(img)
 
def show(mainQ):
    cv2.namedWindow('test1')
    while True:
        frame1 = mainQ.get()
        frame1 = cv2.flip(frame1, 1)
        cv2.imshow('test1', frame1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
if __name__ == '__main__':
    logMessages = multiprocessing.log_to_stderr()
    logMessages.setLevel(multiprocessing.SUBDEBUG)
    mainQ = multiprocessing.Queue()
 
    read_process = multiprocessing.Process(target=read,args=(mainQ, ))
    read_process.start()
 
    show_process = multiprocessing.Process(target=show,args=(mainQ, ))
    show_process.start()
 
    read_process.join()
    show.join()


