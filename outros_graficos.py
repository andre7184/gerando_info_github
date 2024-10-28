import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo para o gráfico de barras empilhadas
languages = ['Python', 'JavaScript', 'HTML', 'CSS']
data = [100, 80, 60, 40]  # Quantidade de linhas de código para cada linguagem em todos os repositórios

# Calcular a porcentagem de cada linguagem
total = sum(data)
percentages = [d / total * 100 for d in data]

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(10, 1))  # Altura ajustada para 50px (1 polegada)

# Gera a barra empilhada horizontal
bottom = 0
for i in range(len(languages)):
    ax.barh(0, percentages[i], left=bottom, color=['#3572A5', '#F1E05A', '#E34C26', '#563D7C'][i], label=f'{languages[i]} ({percentages[i]:.2f}%)')
    bottom += percentages[i]

# Configurações adicionais do gráfico
ax.set_xlabel('Porcentagem')
ax.set_title('Distribuição de Linguagens em Todos os Repositórios')
ax.set_yticks([])  # Remove os ticks do eixo y
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=len(languages))  # Legenda abaixo do gráfico

# Salva o gráfico como um arquivo PNG
plt.tight_layout()
plt.savefig('stacked_horizontal_bar_chart_with_percentages_small.png')

# Exibe o gráfico
plt.show()
