# coding=utf-8
"""
Ambience based music and background
"""
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import playsound

FILE = 'data/3.csv'
DF1 = pd.read_csv(FILE)
LIGHT = DF1[['LIGHT (lux)', 'Time since start in ms ']]
# light.hist(column='LIGHT (lux)')
plt.axis('off')
SUM_TOT = 0
i = 0
TIME_FLAG = LIGHT.loc[0, 'Time since start in ms ']
ARR = []
for index, row in LIGHT.iterrows():
    SUM_TOT += LIGHT.loc[index, 'LIGHT (lux)']
    i += 1
    if (LIGHT.loc[index, 'Time since start in ms '] - TIME_FLAG) > 300000:
        AVG = SUM_TOT / i
        TIME_FLAG = LIGHT.loc[index, 'Time since start in ms ']
        ARR.append(AVG)
        i = 0
        SUM_TOT = 0
        if AVG < 500:
            print("Its Pleasant. Have a Peaceful time ")
            ImageAddress = 'data/1.jpeg'
            ImageItself = Image.open(ImageAddress)
            ImageNumpyFormat = np.asarray(ImageItself)
            plt.imshow(ImageNumpyFormat)
            plt.draw()
            plt.pause(1)  # pause how many seconds
            plt.close()
            playsound.playsound('data/1.mp3')
        elif 500 <= AVG < 1500:
            print("Its Quite Normal around here.Enjoy the moments")
            ImageAddress = 'data/2.jpeg'
            ImageItself = Image.open(ImageAddress)
            ImageNumpyFormat = np.asarray(ImageItself)
            plt.imshow(ImageNumpyFormat)
            plt.draw()
            plt.pause(1)  # pause how many seconds
            # plt.close()
            playsound.playsound('data/2.mp3')
            plt.close()

        elif AVG > 1500:
            print("Its Bright out here!!")
            ImageAddress = 'data/3.jpeg'
            ImageItself = Image.open(ImageAddress)
            ImageNumpyFormat = np.asarray(ImageItself)
            plt.imshow(ImageNumpyFormat)
            plt.draw()
            plt.pause(1)  # pause how many seconds
            plt.close()
            playsound.playsound('data/3.mp3')

AVG = pd.DataFrame()
AVG['avg'] = ARR
# print(arr)
plt.show()
