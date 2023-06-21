import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definição do DataFrame randomizado
np.random.seed(0)
data = np.random.randn(10, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Criação do gráfico de linhas estilizado
plt.figure(figsize=(10, 6))  # Definição do tamanho da figura
plt.plot(df.index, df['A'], label='A', color='blue', linestyle='-', linewidth=2)
plt.plot(df.index, df['B'], label='B', color='red', linestyle='--', linewidth=2)
plt.plot(df.index, df['C'], label='C', color='green', linestyle='-.', linewidth=2)

# Configurações do gráfico
plt.title('Gráfico de Linhas Estilizado')
plt.xlabel('Índice')
plt.ylabel('Valores')
plt.legend()

# Exibição do gráfico
plt.show()