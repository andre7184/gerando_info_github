import requests
import matplotlib.pyplot as plt
from collections import defaultdict
import os

# Obtenha o token da variável de ambiente
token = os.getenv('GH_TOKEN')
repos_url = 'https://api.github.com/user/repos'
cores = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Gray', 'Cyan', 'Magenta', 'Lime', 'Maroon', 'Navy', 'Olive', 'Teal', 'Silver', 'Gold']

# Cabeçalhos para autenticação
headers = {
    'Authorization': f'token {token}'
}

print("Obtendo lista de repositórios...")
repos = requests.get(repos_url, headers=headers).json()

languages = {}
commits_per_repo = defaultdict(int)
commits_per_author = defaultdict(int)

# Obtenha a quantidade de código em cada linguagem e estatísticas de commits para cada repositório
for repo in repos:
    repo_name = repo['name']
    print(f"Processando repositório: {repo_name}")
    
    # Obter linguagens
    languages_url = repo['languages_url']
    repo_languages = requests.get(languages_url, headers=headers).json()
    for language, lines in repo_languages.items():
        if language in languages:
            languages[language] += lines
        else:
            languages[language] = lines
    

print("Gerando gráficos...")

# Ordene as linguagens por quantidade de linhas de código
sorted_languages = dict(sorted(languages.items(), key=lambda item: item[1], reverse=True))
nome_languages = list(sorted_languages.keys())
line_linguages = list(sorted_languages.values())
total = sum(line_linguages)
percentages = [d / total * 100 for d in line_linguages]

fig, ax = plt.subplots(figsize=(6.8, 2.1))
bottom = 0
for i in range(len(languages)):
    ax.barh(0, percentages[i], left=bottom, color=cores[i], label=f'{nome_languages[i]} ({percentages[i]:.2f}%)')
    bottom += percentages[i]
ax.set_title('Linguagens dos Repositórios')
ax.set_yticks([])
ax.set_xticks([])
ax.grid(False)
ax.set_xlabel('')
for spine in ax.spines.values():
    spine.set_visible(False)
handles, labels = ax.get_legend_handles_labels()
ncol = 3
ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.475, -0.3), ncol=ncol)
plt.tight_layout()
plt.savefig('languages_chart.png')
plt.show()
print("Gráfico de linguagens gerado: languages_chart.png")

