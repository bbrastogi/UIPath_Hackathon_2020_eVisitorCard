import os, cv2

def take_photo():

    camera = cv2.VideoCapture(0)
    face_detected = False

    while True:
        return_value,image = camera.read() # Capture frame-by-frame
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow ('Take Photo', gray)

        if cv2.waitKey(1) & 0xFF==13: 
            cv2.imwrite('visitor_photo.jpg',gray)
            break

    # When everything done, release the capture
    camera.release()
    cv2.destroyAllWindows()
    return os.getcwd()
