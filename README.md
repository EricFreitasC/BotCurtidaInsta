# Instagram Automation Bot

Este bot automatiza o login no Instagram, pesquisa por um usuário, acessa a conta, curte uma foto e deixa um comentário. O bot foi projetado para ser executado em um ambiente de tela dividida, com o VSCode à direita e o Chrome à esquerda.

## Requisitos

- **Python**: 3.12 ou superior
- **Bibliotecas**: 
  - `webbrowser`
  - `pyautogui`
  - `time`

## Instalação

1. **Instale o Python** em seu sistema, se ainda não o fez.
2. **Instale a biblioteca `pyautogui`** usando o pip:

   ```bash
   pip install pyautogui
   ```

3. **Coloque a imagem** `curtido.png` no diretório do seu script Python.

## Como Usar

1. **Abra o VSCode** na lateral direita da sua tela.
2. **Abra o Chrome** na lateral esquerda da sua tela e maximize a janela.
3. **Execute o código** app.py no VSCode.

## Notas

- **Atenção**: Certifique-se de que a janela do Chrome está maximizada e posicionada à esquerda para garantir que os cliques funcionem corretamente.Caso não funcione, será necessário alterar as coordenadas da tela no código.
- **Verifique** se a imagem `curtido.png` está no diretório correto e não está corrompida.

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções! Seu feedback é sempre bem-vindo.

