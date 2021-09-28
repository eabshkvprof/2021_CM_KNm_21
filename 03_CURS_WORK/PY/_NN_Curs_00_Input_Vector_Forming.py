# -*- coding: utf-8 -*-
"""
13.10.2020

ФОРМИРВОАНИЕ ВХОДНЫХ ВЕКТОРОВ ДЛЯ НЕЙРОСЕТИ
Берем список созданных векторов по описанию символа
Считываем вектор
и форимруем матрицу

Марица
строк столько сколько  разных входных векторов
столбцов - сколько в векторе призаков (в нашем случа 112)


"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

Dir_IN_Name = "j:/_Doc_Vol_My_/Kursi_Uchebnie/2020_2021__Осень_Когнитивное_Моделирование/3_CURS/My_Symb/Vectors/"
In_Vec_Size = 112

xTtrain_file_name_list = [
        '01_Alfa_01_.png.npy',
        '01_Alfa_02_.png.npy',
        '01_Alfa_03_.png.npy',
        '01_Alfa_04_.png.npy',
        '01_Alfa_05_.png.npy',
        '02_Beta_05_.png.npy',
        '02_Beta_04_.png.npy',
        '02_Beta_03_.png.npy',
        '02_Beta_02_.png.npy',
        '02_Beta_01_.png.npy',
        '03_Gamma_01_.png.npy',
        '03_Gamma_02_.png.npy',
        '03_Gamma_03_.png.npy',
        '03_Gamma_04_.png.npy',
        '03_Gamma_05_.png.npy',
        '10_Fi_01_.png.npy',
        '10_Fi_02_.png.npy',
        '10_Fi_03_.png.npy',
        '10_Fi_04_.png.npy',
        '10_Fi_05_.png.npy']


N_Train = len(xTtrain_file_name_list)
print('Количество тренировочных векторов',N_Train)
print('Количество признаков в векторе', In_Vec_Size )

xTrain = np.zeros((N_Train,In_Vec_Size), np.float32)

# Форимруем массив векторов признаков
for i in range (N_Train):
    In_filename = Dir_IN_Name + xTtrain_file_name_list[i]
#   print (i, In_filename)
    xTrain_vect = np.load(In_filename)
#   print (xTrain_vect)
    xTrain[i][:] = np.copy(xTrain_vect)

print ('Структура матрицы',np.shape(xTrain))

# Выводим весь массив в файл с именем "xTrain_Array"
Out_filename = Dir_IN_Name + "xTrain_Array"
np.save(Out_filename, xTrain)

Y_Vec_Size = 4
yTrain = np.zeros((N_Train,Y_Vec_Size), np.float32)
for i in range(5) :
    yTrain[i][0] = 1.0
    yTrain[i+5][1] = 1.0
    yTrain[i+10][2] = 1.0
    yTrain[i+15][3] = 1.0

print (yTrain)

Out_filename = Dir_IN_Name + "yTrain_Array"
np.save(Out_filename, yTrain)


# --------------------------------------------------------
# --------  ФОРМИРУЕМ МАССИВ ТЕСТОВЫХ ВХОДНЫХ ВЕКТОРОВ
# --------------------------------------------------------

xTest_file_name_list = [
        '01_Alfa_06_.png.npy',
        '01_Alfa_07_.png.npy',
        '02_Beta_06_.png.npy',
        '02_Beta_07_.png.npy',
        '03_Gamma_06_.png.npy',
        '03_Gamma_07_.png.npy',
        '10_Fi_06_.png.npy',
        '10_Fi_07_.png.npy']

N_Test = len(xTest_file_name_list)
xTest = np.zeros((N_Test, In_Vec_Size), np.float32)

# Форимруем массив тестовых векторов признаков
for i in range (N_Test):
    In_filename = Dir_IN_Name + xTest_file_name_list[i]
#   print (i, In_filename)
    xTest_vect = np.load(In_filename)
#   print (xTrain_vect)
    xTest[i][:] = np.copy(xTest_vect)

print ('Структура матрицы',np.shape(xTest))
Out_filename = Dir_IN_Name + "xTest_Array"
np.save(Out_filename, xTest)








