import cv2
img = cv2.imread(r"section-3\00-puppy.jpg")

while True:
    cv2.imshow('puppy', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()