import cv2
def qrcode_reader():
    
    camera = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    
    while True:
        return_value,image = camera.read() # Capture frame-by-frame
        data, bbox, _ = detector.detectAndDecode(image)
        
        if data: #If data has captured information from QR Code then break the loop
            return data
            break
        
        cv2.imshow("Scan QRCode", image) # Display the resulting frame
        cv2.waitKey(10)
        
    # When everything done, release the capture
    camera.release()
    cv2.destroyAllWindows()
