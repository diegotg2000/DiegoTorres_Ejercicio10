import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal





datos1=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2008.txt', delimiter=';', header=None, decimal=',')
datos2=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2009.txt', delimiter=';', header=None, decimal=',')
datos3=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2010.txt', delimiter=';', header=None, decimal=',')
frames=[datos1,datos2,datos3]
datos=pd.concat(frames)
datos[0]=datos[0].str[0:-8:1]
datos[1]=datos[1].str[10:]
datos[0]=datos[0]+datos[1]
datos[0]=pd.to_datetime(datos[0],format='%d/%m/%Y %H:%M:%S')
date=datos[0]
datos.set_index([0],inplace=True)





del datos[1]
del datos[3]





datos.plot(figsize=(20,7))
plt.show()
plt.savefig('precios_antes.png')





date=np.array(date)
N  = 2   
Wn = 0.0001
B, A = signal.butter(N, Wn)
trans=datos[2]




trans_filtrada = signal.filtfilt(B,A, trans)





fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(date,trans, 'b-')
plt.plot(date,trans_filtrada, 'r-',linewidth=2)
plt.ylabel(r"Precio (Dólares)")
plt.legend(['Original','Filtrado'])
plt.title("Precio")
ax1.axes.get_xaxis().set_visible(False)
ax1 = fig.add_subplot(212)
plt.plot(date,trans-trans_filtrada, 'b-')
plt.ylabel(r"Precio (Dólares)")
plt.xlabel("Fecha")
plt.legend(['Residuales'])
plt.savefig('precios.png')





plt.figure(figsize=(20,7))
ruido=trans-trans_filtrada
corr=signal.correlate(ruido,ruido,mode="full")
plt.plot(corr[len(corr)//2:])
plt.show()
plt.savefig('corre.png')






