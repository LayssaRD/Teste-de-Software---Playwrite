# Projeto de Automação de Formulário com Playwright

Este projeto utiliza a biblioteca Playwright para automatizar o preenchimento e envio de um formulário em uma página de exemplo. O script preenche o formulário com informações pré-definidas, valida os campos e imprime mensagens de sucesso ou erro.

## Requisitos

- Python 3.x
- Playwright para Python

## Instalação

1. Clone este repositório ou baixe os arquivos.
2. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```

3. Instale as dependências:

    ```bash
    pip install playwright
    playwright install
    ```

4. Caso queira executar o script, certifique-se de que o Playwright esteja instalado corretamente no seu sistema.

## Como Usar

1. Execute o script Python diretamente:

    ```bash
    python automacao_formulario.py
    ```

2. O script irá:

   - Acessar a página de exemplo.
   - Preencher os campos do formulário (nome, sobrenome, idade, país, e notas).
   - Submeter o formulário.
   - Verificar a resposta da submissão e imprimir mensagens sobre o sucesso ou erro.
   - Caso haja algum erro, ele tenta verificar a validade dos campos e imprime as mensagens de erro específicas.

## Funcionalidades

- Preenchimento automático dos campos `firstname`, `surname`, `age`, `country`, e `notes`.
- Submissão do formulário e verificação da resposta.
- Verificação da validade dos campos e mensagens de erro, caso existam.
- Relatório de erros específicos para os campos `firstname`, `surname`, e `age`.

## Tecnologias Utilizadas

- **Playwright**: Para automação de navegação e interação com a página web.
- **Python**: Linguagem de programação utilizada no desenvolvimento do script.

## Desenvolvido por

**Layssa Rodrigues Alves**  
Estudante de Ciência da Computação

**Contato**
📧 layssarodrigues@alunos.utfpr.edu.br 

