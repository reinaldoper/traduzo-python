# :construction: README customizado em construção ! :construction:

## Traduzo-Aceleração python da Trybe.

- Uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para criar uma aplicação Server Side. Ou seja, o Back-end irá fornecer a camada View, para a pessoa usuária.
- A trybe disponibilizou os requisitos a serem desenvolvidos neste projeto.

![Tela](src/views/static/images/traduzo.png)

A partir deste repositório você encontra os detalhes de como estruturar o desenvolvimento do seu projeto.

<details>
  <summary>📝 Detalhes do projeto </summary>

- Implementar uma API utilizando arquitetura em camadas MVC;
- Utilizar o Docker para projetos Python;
- Aplicar conhecimentos de Orientação a Objetos no desenvolvimento WEB.
- Escrever testes para APIs para garantir a implementação dos endpoints;
- Interagir com um banco de dados não relacional MongoDB;
- Desenvolver páginas web Server Side.

</details>

<details>

## Preparando Ambiente

<details>

<summary>🐳 Subindo a aplicação</summary>

**[1]** Crie o ambiente virtual para o projeto

```bash
python3 -m venv .venv && source .venv/bin/activate
```

**[2]** Instale as dependências

```bash
python3 -m pip install -r dev-requirements.txt
```

**[3 - Opção A]** Suba o projeto pelo Docker

```bash
docker compose up translate
```

- Recomendado: Dockerfile e Docker-compose já estão prontos para uso, para subir o MongoDB e o Flask.

**[3 - Opção B]** Caso queira subir somente o banco MongoDB pelo Docker

```bash
docker compose up -d mongodb

python3 src/app.py
```
</details>
