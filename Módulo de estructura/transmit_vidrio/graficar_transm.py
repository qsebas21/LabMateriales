import matplotlib.pyplot as plt
import pandas as pd
import os

headers = ['Longitud de onda (nm)', 'Transmitancia (%)']

#for filename in os.listdir(os.getcwd()):
#    root, ext = os.path.splitext(filename)
#    if ext == '.ttt':
#        df = pd.read_csv(filename, sep=';', names=headers)
#        plt.plot(df['Longitud de onda (nm)'], df['Transmitancia (%)'])
#        plt.xlabel(headers[0])
#        plt.ylabel(headers[1])
#        plt.ylim(0,110)
#        plt.title(root)
#        plt.savefig(root+'.png')
#        plt.show()

df1 = pd.read_csv('vidrio_solo.ttt', sep=';', names=headers)
df2 = pd.read_csv('vidrio_con_capa.ttt', sep=';', names=headers)
plt.plot(df1['Longitud de onda (nm)'], df1['Transmitancia (%)'])
plt.plot(df2['Longitud de onda (nm)'], df2['Transmitancia (%)'])
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.ylim(0,110)
plt.title('Transmitancia del vidrio solo y con capa conductora')
datos = ['Vidrio solo', 'Vidrio con capa conductora']
plt.legend(labels=datos, markerscale=12)
plt.savefig('vidrio.pdf')
#plt.show()
