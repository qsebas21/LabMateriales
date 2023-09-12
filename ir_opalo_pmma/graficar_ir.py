import matplotlib.pyplot as plt
import pandas as pd

headers = ['cm(^-1)', 'T%']

#importa los datos
df_pmma = pd.read_csv('pmma.csv', names=headers)
df_op = pd.read_csv('opalo.csv', names=headers)

#grafica los datos en los mismos ejes
plt.plot(df_pmma['cm(^-1)'], df_pmma['T%'])
plt.plot(df_op['cm(^-1)'], df_op['T%'], color='red')
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.ylim(60,100)
plt.gca().invert_xaxis()
datos = ['PMMA', 'Ópalo']
plt.legend(labels=datos, markerscale=12)
plt.title('Espectroscopía IR de las esferas de PMMA y el ópalo inverso')
#plt.show()
plt.savefig('ir_pmma_opalo.pdf')
