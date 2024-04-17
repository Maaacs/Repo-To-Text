# Repo-To-Text


## Visão Geral
O repositório Repo-To-Text contém dois scripts Python projetados para recuperar e formatar o conteúdo e a estrutura de repositórios: um para repositórios do GitHub (`repo-to-text.py`) e outro para repositórios locais (`local-repo-to-text.py`).

## Arquivos no Repositório
- **repo-to-text.py**: Busca e formata o conteúdo de um repositório do GitHub.
- **local-repo-to-text.py**: Busca e formata o conteúdo de um diretório local como um repositório.

## `repo-to-text.py`
Este script é utilizado para extrair e formatar os conteúdos de um repositório do GitHub.

### Funcionalidades
- Analisa URLs de repositórios do GitHub para identificar o proprietário e o nome do repositório.
- Busca o conteúdo do repositório usando a API do GitHub (requer um token de acesso pessoal).
- Gera uma representação textual estruturada do repositório incluindo o arquivo README, estrutura de diretórios e conteúdo de arquivos significativos (como `.py`, `.md`, etc.).
- Ignora certos caminhos de diretório (como `.github`).

### Uso
Para usar este script, você precisa fornecer uma URL de repositório do GitHub e um token de acesso pessoal (para autenticação com a API do GitHub). O script produz um arquivo de texto formatado contendo os conteúdos do repositório.

```bash
python repo-to-text.py
```
**Variáveis de Ambiente:**
- `github_url`: A URL completa do repositório do GitHub.
- `token`: Seu token de acesso pessoal do GitHub para acesso à API.

**Saída:**
- Gera um arquivo de texto nomeado `<nome-do-repo>-formatted-prompt.txt` contendo as informações estruturadas do repositório.

## `local-repo-to-text.py`
Este script formata os conteúdos de um diretório de repositório local.

### Funcionalidades
- Constrói uma árvore de diretórios baseada em texto do diretório local especificado.
- Inclui os conteúdos de cada arquivo dentro da estrutura do diretório na saída.
- Pula diretórios e arquivos comuns não relevantes (como `node_modules`, `.git`, etc.).

### Uso
O script deve ser executado a partir da linha de comando, com o caminho para o diretório do repositório local como argumento.

```bash
python local-repo-to-text.py /caminho/para/repositorio/local
```
**Parâmetros:**
- `/caminho/para/repositorio/local`: O caminho para o diretório do repositório local.

**Saída:**
- Produz um arquivo chamado `local-repo-formatted.txt` contendo a estrutura do diretório e os conteúdos dos arquivos.

Para instalar os pacotes Python necessários, execute:
```bash
pip install requests
```
