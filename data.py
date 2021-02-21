'''
Este código me ayuda a organizar en carpetas para que sea más fácil el entrenamiento
Tensorflow es capaz de encontrar los labels desde la simple división de carpetas con el nombre de cada etiqueta
'''

import os
import shutil
path_inicio_train_signs = r'C:\Users\Carlita\Desktop\Prueba\64x64_SIGNS\train_signs'
path_inicio_test_signs = r'C:\Users\Carlita\Desktop\Prueba\64x64_SIGNS\test_signs'
path_inicio_val_signs = r'C:\Users\Carlita\Desktop\Prueba\64x64_SIGNS\val_signs'
contenido_train_signs = os.listdir(path_inicio_train_signs)#Lista de archivos en el directorio
contenido_test_signs = os.listdir(path_inicio_test_signs)#Lista de archivos en el directorio
contenido_val_signs = os.listdir(path_inicio_val_signs)#Lista de archivos en el directorio
#Eliminar data repetida
#Train
for archivo in contenido_train_signs:
  if archivo[-7:-4] == '(1)':
    path_train = path_inicio_train_signs + '/' + archivo
    os.remove(path_train)

#Test
for archivo in contenido_test_signs:
  if archivo[-7:-4] == '(1)':
    path_test = path_inicio_test_signs + '/' + archivo
    os.remove(path_test)

#Validation    
for archivo in contenido_val_signs:
  if archivo[-7:-4] == '(1)':
    path_val = path_inicio_val_signs + '/' + archivo
    os.remove(path_val)

path_inicio_train_signs = r'C:\Users\Carlita\Desktop\Prueba\64x64_SIGNS\train_signs'
path_inicio_test_signs = r'C:\Users\Carlita\Desktop\Prueba\64x64_SIGNS\test_signs'
path_inicio_val_signs = r'C:\Users\Carlita\Desktop\Prueba\64x64_SIGNS\val_signs'
contenido_train_signs = os.listdir(path_inicio_train_signs)#Lista de archivos en el directorio
contenido_test_signs = os.listdir(path_inicio_test_signs)#Lista de archivos en el directorio
contenido_val_signs = os.listdir(path_inicio_val_signs)#Lista de archivos en el directorio

#Train
for archivo in contenido_train_signs:
    numero = archivo[0]
    antiguo = 'C:/Users/Carlita/Desktop/Prueba/64x64_SIGNS/train_signs/' +  archivo
    nuevo = 'C:/Users/Carlita/Desktop/Prueba/DATA/Train/' + numero + '/' + archivo
    shutil.move(antiguo, nuevo)
    
#Test
for archivo in contenido_test_signs:
    numero = archivo[0]
    antiguo = ('C:/Users/Carlita/Desktop/Prueba/64x64_SIGNS/test_signs/') +  archivo
    nuevo = 'C:/Users/Carlita/Desktop/Prueba/DATA/Test/' + numero + '/' + archivo
    shutil.move(antiguo, nuevo)


#Val
for archivo in contenido_val_signs:
    numero = archivo[0]
    antiguo = ('C:/Users/Carlita/Desktop/Prueba/64x64_SIGNS/val_signs/') +  archivo
    nuevo = 'C:/Users/Carlita/Desktop/Prueba/DATA/Val/' + numero + '/' + archivo
    shutil.move(antiguo, nuevo)