# Pong

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Luiza Morais Braga
- Victhor Gabriel Freire de Oliveira
- Maria Fernanda Melo e Reis

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo.
  - `config.py`: constantes do jogo (cores, tamanhos, velocidades e FPS).
  - `funcoes.py`: regras puras do jogo (rebatidas, limites do campo e colisão).
  - `jogo.py`: loop principal, eventos e renderização, menus e lógica de pontuação.
  - `dados.py`: leitura e gravação de recorde/ranking (preparado para o placar da próxima entrega).
  - `sprites.py`: organização dos elementos do jogo (preparado para a próxima entrega).
- `tests/`: testes unitários com pytest.
- `docs/`: documentação do projeto, incluindo a proposta inicial.
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking), preparados para o placar da próxima entrega.

> Os arquivos `src/dados.py`, `src/sprites.py` e a pasta `data/` (com `ranking.txt` e `recorde.txt`) já fazem parte da estrutura, mas ainda não são usados ativamente. A próxima entrega deve incluir o ranking persistente, gravando e lendo os resultados das partidas nesses arquivos.

## Descrição do jogo

Pong é uma releitura do clássico jogo de "tênis de mesa" para dois jogadores. Cada jogador controla uma raquete em um dos lados da tela e a bola se move pelo campo, ricocheteando nas bordas e nas raquetes. O campo tem uma linha central e um círculo ao centro, no estilo de uma quadra.

Nesta versão o jogo conta com seleção de modo (Melhor de 3 ou Melhor de 5), placar em tempo real, condição de vitória e tela de resultado final.

## Objetivo do jogador

Rebater a bola e fazer o adversário falhar. Cada vez que a bola passa pelo lado do adversário, você marca um ponto. Vence quem atingir o limite de pontos primeiro, conforme o modo de jogo escolhido.

## Regras do jogo

- A partida é para dois jogadores, cada um controlando uma raquete.
- O jogador escolhe o modo antes de iniciar: Melhor de 3 (primeiro a 2 pontos) ou Melhor de 5 (primeiro a 3 pontos).
- A raquete só se movimenta na vertical e não pode sair dos limites da tela.
- A bola se movimenta automaticamente e ricocheteia ao tocar nas bordas superior e inferior.
- Quando a bola encosta em uma raquete, ela é rebatida na direção contrária.
- Se a bola passar pela lateral esquerda, o jogador 2 marca ponto. Se passar pela lateral direita, o jogador 1 marca ponto.
- Após cada ponto, a bola retorna ao centro e o jogo recomeça após uma breve pausa.
- Quem atingir o limite de pontos do modo escolhido vence a partida.

## Controles

Jogador 1 (raquete da esquerda):

- `W`: mover para cima
- `S`: mover para baixo

Jogador 2 (raquete da direita):

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo

Geral:

- `ESC`: sair do jogo

## Como executar o projeto

1. Clonar o repositório:

```bash
git clone https://github.com/ICEI-PUC-Minas-PPL-CDIA/IntroAlgs_pygame_template
cd IntroAlgs_pygame_template
```

2. Instalar as dependências:

```bash
pip install -r requirements.txt
```

3. Executar o jogo:

```bash
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Decisões técnicas

- As regras do jogo foram separadas do loop principal em `src/funcoes.py`. Como o jogo roda em um laço infinito, manter as regras em funções puras permite testá-las sem abrir a janela do jogo.
- As constantes ficaram centralizadas em `src/config.py` para facilitar ajustes de velocidade, tamanho e cores.
- A lógica de pontuação e controle de vitórias foi implementada diretamente no loop principal em `src/jogo.py`, usando variáveis simples de contagem.
- O modo de jogo é selecionado antes da partida e define o limite de pontos necessários para vencer.
- A próxima entrega deve incluir o ranking persistente com leitura e escrita de arquivos na pasta `data/`.
