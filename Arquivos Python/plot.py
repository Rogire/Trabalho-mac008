import matplotlib.pyplot as plt
import numpy as np

def plot_desloc(x, y, store, numGlib, scale=100):
    if(len(x)!=len(y)):
      raise Exception("O tamanho da lista x e da lista y devem ser iguais.")

    for i in range(len(x)):
      num_nos = len(x[i])
      x_desloc = np.copy(x[i])
      y_desloc = np.copy(y[i])

      for i in range(num_nos):
          x_d = store[i*numGlib,1]
          y_d = store[i*numGlib+1,1]

          x_desloc[i] += x_d * scale
          y_desloc[i] += y_d * scale

    # Plotar a estrutura original e deslocada
      plt.figure(figsize=(10, 6))
      plt.plot(x[i], y[i], 'ro-', label='Estrutura Original')  # Estrutura original
      plt.plot(x_desloc, y_desloc, 'bo-', label='Estrutura Deslocada')  # Estrutura deslocada

    # Configurações do gráfico
    plt.xlabel('Coordenada X (mm)', fontsize=12)
    plt.ylabel('Coordenada Y (mm)', fontsize=12)
    plt.title('Estrutura Original vs Estrutura Deslocada', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid()
    plt.show()