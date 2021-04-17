import cv2

#Pass an image to change
image_default = cv2.imread("image_file.jpg") 
black_image = cv2.resize(image_default, (500, 500))
blue_image = cv2.resize(image_default, (500, 500))

#converting the image to black and blue
for i in range(500):
  for j in range(500):
    black_image[i][j] = [0, 0, 0]
    blue_image[i][j] = [0, 0, 255]

#Saving the output 
cv2.imwrite("black_image.jpg", black_image)
cv2.imwrite("blue_image.jpg", blue_image)

