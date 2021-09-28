# -*- coding: utf-8 -*-
"""

ПРИВЕДЕНИЕ ИЗОБРАЖЕНИЯ В ДИАПАЗОН в 0.0 - 1.0
СОЗДАНИЕ ВХОДНОГО ВЕКТОРА

"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io


# ИМЕНА ДИРЕКТОРИЙ
Dir_IN_Name = "j:/_Doc_/"   # Здесь задаем свою дирректорию с исходными картинками
Dir_OUT_Name = "j:/_Doc_Out/" # Здесь задаем свою дирректорию для сохранения вектора изображения

# ИМЯ ОБРАБАТЫВАЕМОГО ФАЙЛА ИЗОБРАЖЕНИЯ
IM_Name = "10_Fi_07_.png"  # Определяем файл - изображение символа !!! PNG

In_filename = Dir_IN_Name + IM_Name
Out_filename = Dir_OUT_Name + IM_Name


#   ЧИТАЕМ ИЗОБРАЖЕНИЕ
IM_symb  = io.imread(In_filename)
print ('IMAGE SHAPE', IM_symb.shape, 'IMAGE SIZE', IM_symb.size)
# print (IM_symb)


#   НОРМАЛИЗАЦИЯ и ПРИВЕДЕНИЕ К 0 - 1
IM_Max = IM_symb.max()
IM_Min = IM_symb.min()
K=  1 / (IM_Max-IM_Min)
print ('IMAGE Min', IM_Min, 'IMAGE Max', IM_Max, 'K = ', K)

IM_Enh = np.float32((IM_symb - IM_Min) * K )

#  ПРОВЕРЯЕМ ПРЕДЕЛЫ
IME_Max = IM_Enh.max()
IME_Min = IM_Enh.min()
print (IM_Enh)
print ('IMAGE Min', IME_Min, 'IMAGE Max', IME_Max)

# ВЫВОД ИЗОБРАЖЕНИЯ
imgplot = plt.imshow(IM_Enh)

Vect_Size = np.int32(IM_symb.size / 3)
print (Vect_Size)

# ВЫБИРАЕМ КРАСНУЮ КОМПОНЕНТУ И ПРЕОБРАЗУЕМ В ВЕКТОР
Symb_Vect = IM_Enh[:,:,0].reshape(Vect_Size)
print ('==ЭТО ВХОДНОЙ ВЕКТОР СИМВОЛА==')
print ('РАЗМЕРНОСТЬ ВЕКТОРА=', Vect_Size )
print (Symb_Vect)

#   СОХРАНЯЕМ ВЕКТОР
np.save(Out_filename, Symb_Vect)

