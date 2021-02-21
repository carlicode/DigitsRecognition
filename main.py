import cv2
from model import sequentialModel
from keras.preprocessing import image
import numpy as np
from PIL import Image
import time
import streamlit as st 
import os

#Modelo
model = sequentialModel()

def cargarImagen(imagen):
  img = image.load_img(imagen, target_size=(64, 64))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images)
  predict = list(classes[0]).index(float(max(classes[0])))
  return predict

def openCamera():
    camera_port = 0
    #camera = cv2.VideoCapture(camera_port)
    camera = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)
    i = 0
    font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de la letra
    while True:
        i+=1
        ret_val, img = camera.read()
        return_value, image = camera.read()
        #tomo foto y la guardo
        name = 'C:/Users/Carlita/Desktop/Prueba/images/'  + str(i) + '.jpg'
        cv2.imwrite(name, image)
        time.sleep(0.1)
        p = cargarImagen(name)
        img = cv2.flip(img, 1)
        cv2.putText(img,  
                    str(p),  
                    (50, 50),  
                    font, 1,  
                    (0, 255, 255),  
                    2,  
                    cv2.LINE_4) 

        if cv2.waitKey(1) == 27: 
            #esc para cerrar
            break  
        cv2.imshow('Modelo números con las manos', img)

    camera.release() 
    cv2.destroyAllWindows()

#openCamera()

def webPage():
    st.title("Upload + Classification Example")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("La imagen es del número")
        res = cargarImagen(data)
        st.write('%s (%.2f%%)' % (res))

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('seleciona un archivo', filenames)
    return os.path.join(folder_path, selected_filename)


if __name__ == '__main__':
    # Select a file
    if st.checkbox('Change directory'):
        folder_path = st.text_input('por favor ingresa el directorio de la imagen', '.')
    filename = file_selector(folder_path=folder_path)
    var = cargarImagen(filename)
    res = 'El número es: ' + str(var)
    st.write(res)
#C:\Users\Carlita\Desktop\Prueba\DATA\Test\0\0_IMG_5942