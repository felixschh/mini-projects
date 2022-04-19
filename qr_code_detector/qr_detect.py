import cv2 as cv


img = cv.imread('/Users/felixschekerka/Desktop/mini-projects/qr_code_detector/qr-barcode-card.jpeg')
qr = cv.QRCodeDetector()
x, y, string = qr.detectAndDecode(img)

print(f'Your QR code contains the following Link:\n{x}')