import cv2

face_cascade = cv2.CascadeClassifier("face.xml")
print("model loaded successfully")

image = cv2.imread("face man.jpg")
cv2.imshow("original image", image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale image", gray_image)
face = face_cascade.detectMultiScale(
    gray_image,
    scaleFactor=1.3,
    minNeighbors=5
)

print("face coordinates", face)

for(x,y,w,h)in face:
    cv2.rectangle(
        image,
        (x,y),
        (x+w, y+h),
        (0,0,255),
        3
    )
cv2.imshow("face detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()