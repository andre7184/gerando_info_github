import requests
import matplotlib.pyplot as plt
from collections import defaultdict
import os

# Substitua 'seu_usuario' pelo seu nome de usuário do GitHub
username = 'andre7184'
# Obtenha o token da variável de ambiente
token = os.getenv('GH_TOKEN')
repos_url = f'https://api.github.com/users/{username}/repos'

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
    
    # Obter commits
    commits_url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
    commits = requests.get(commits_url, headers=headers).json()
    for commit in commits:
        author = commit['commit']['author']['name']
        commits_per_repo[repo_name] += 1
        commits_per_author[author] += 1

print("Gerando gráficos...")

# Ordene as linguagens por quantidade de linhas de código
sorted_languages = dict(sorted(languages.items(), key=lambda item: item[1], reverse=True))

# Crie o gráfico de linha para linguagens
plt.figure(figsize=(10, 5))
plt.plot(list(sorted_languages.keys()), list(sorted_languages.values()), marker='o')
plt.xlabel('Linguagens')
plt.ylabel('Linhas de Código')
plt.title('Linguagens Mais Usadas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('languages_chart.png')
print("Gráfico de linguagens gerado: languages_chart.png")

# Crie o gráfico de barras para commits por repositório
plt.figure(figsize=(10, 5))
plt.bar(commits_per_repo.keys(), commits_per_repo.values())
plt.xlabel('Repositórios')
plt.ylabel('Commits')
plt.title('Commits por Repositório')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('commits_per_repo_chart.png')
print("Gráfico de commits por repositório gerado: commits_per_repo_chart.png")

# Crie o gráfico de barras para commits por autor
plt.figure(figsize=(10, 5))
plt.bar(commits_per_author.keys(), commits_per_author.values())
plt.xlabel('Autores')
plt.ylabel('Commits')
plt.title('Commits por Autor')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('commits_per_author_chart.png')
print("Gráfico de commits por autor gerado: commits_per_author_chart.png")
