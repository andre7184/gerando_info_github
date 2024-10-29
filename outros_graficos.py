import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo para o gráfico de barras empilhadas
languages = ['Python', 'JavaScript', 'HTML', 'CSS', 'Php', 'Shell', 'Java', 'C', 'C++', 'C#', 'SQL']
data = [65, 17, 8, 3, 2, 1.8, 1.2, 0.8, 0.5, 0.5, 0.2]  # Quantidade de linhas de código para cada linguagem em todos os repositórios
cores = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Gray', 'Cyan', 'Magenta', 'Lime', 'Maroon', 'Navy', 'Olive', 'Teal', 'Silver', 'Gold']

#ok
# Calcular a porcentagem de cada linguagem
total = sum(data)
percentages = [d / total * 100 for d in data]

# Configuração do gráfico de barras: ajustar a largura para não ficar muito estreito
fig, ax = plt.subplots(figsize=(5.5, 1)) # Aumentar a altura para dar espaço à legenda

# Gera a barra empilhada horizontal
bottom = 0
for i in range(len(languages)):
    ax.barh(0, percentages[i], left=bottom, color=cores[i], label=f'{languages[i]} ({percentages[i]:.2f}%)')
    bottom += percentages[i]

# Configurações adicionais do gráfico
ax.set_title('Linguagens em Todos os Repositórios')
ax.set_yticks([])
ax.set_xticks([])

# Remover as linhas de grade e a palavra "Porcentagem"
ax.grid(False)
ax.set_xlabel('')

# Remover a borda do gráfico
for spine in ax.spines.values():
    spine.set_visible(False)

# Dividir os nomes das linguagens em 3 colunas na legenda
handles, labels = ax.get_legend_handles_labels()
ncol = 2
ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.475, -1), ncol=ncol)  # Legenda abaixo do gráfico

# Ajustar layout para garantir que a legenda tenha espaço suficiente
plt.tight_layout()

# Salva o gráfico como um arquivo PNG
plt.savefig('stacked_horizontal_bar_chart_with_percentages_small.png')

# Exibe o gráfico
plt.show()
