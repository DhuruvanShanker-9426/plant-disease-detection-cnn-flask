import numpy as np

def image_preprocessing(input_image):
    image_size=(128,128)

    input_image=input_image.resize(image_size)

    img_arr=np.array(input_image)
    img_arr=img_arr/255.0

    img_arr=np.expand_dims(img_arr, axis=0)

    return img_arr