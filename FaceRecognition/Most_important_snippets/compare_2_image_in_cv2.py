import cv2
import numpy
import tensorflow as tf

img_example = "data\\anchor\\334093f9-209f-11ef-94fe-f21805e91111.jpg"

# QUESTION :- Is Resized image same as Scaled down image ?

byte_img = tf.io.read_file(img_example)
img_decoded = tf.io.decode_jpeg(byte_img)
img_resized = tf.image.resize(img_decoded, (100,100) )
img_scaled_down = img_resized / 255.0


im_resz_shape  = img_resized.numpy().shape
im_scale_shape = img_scaled_down.numpy().shape
print(f'Same size and channels = { im_scale_shape == im_resz_shape} ; scaled_down = { im_scale_shape } ; resize = {im_resz_shape}')


difference = cv2.subtract(img_resized.numpy() , img_scaled_down.numpy())
b, g, r = cv2.split(difference)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("The images are completely Equal")
else:
    print("The images are different")