# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Escreva aqui o nome provisório do jogo.

Exemplo:

Pong classic

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1:Victhor Gabriel Freire de Oliveira
- Nome 2:Luiza Morais Braga
- Nome 3:Maria Fernanda Melo e Reis


## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

O jogo escolhido foi a recriação do pong 

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

O jogador controla uma "raquete" retangular que em contado com a bola e jogada para o lado contrario da tela

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

Rebater a bola e fazer o adversário falhar. Cada vez que a bola passa pelo lado do adversário, o jogador marca um ponto.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: A pontuação geral começa com 0 
- Regra 2: Cada colisão com o extremo direito ou esquerdo o jogador oposto recebe um ponto e a bola recomeça no meio do campo

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

O lado que obter 5 pontos primeiro

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

Se o jogador contrario tiver ganhado os 5 pontos

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

Um retangulo simulando uma raquete para cada lado da tela 

Descrição:

que pode ser movida de baixo para cima 

## Obstáculos, inimigos ou desafios

Exemplo:

Uma competição amigavel 

Descrição:

o Desafio proposto é uma competição entre o player e a maquina ou player contra player


## Itens, alvos ou objetos de interação

Exemplo:

Uma bola na tela que em contado com a raquete é jogada de um lado ao outro

Descrição:

O alvo é a interação com da bola com o extremo da tela

## Pontuação, vidas, tempo ou progresso

Exemplo:

Os jogadores começão com a pontuação zerada que aumenta a cada ponto recebido a partir do 

Descrição:

Os jogadores começão com a pontuação zedara que a cada vez que a bola chega ao extremo desprotejido da tela contabiliza um ponto

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando:Seta para cima : move pra cima
- Tecla/comando:Seta pra baixo: move para baixo
- Tecla/comando:Tecla "W": move para cima
- Tecla/comando:Tecla "S": move para baixo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

Pretendemos pesquisar sobre utilidades gratuitas para personalizar nosso jogo

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Organização do codigo
- Dificuldade 2: criação de dificuldades no jogo 
- Dificuldade 3: Colisão entre objetos

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

A versão minima do jogo é duas raquetes que simulam um jogo de pong, uma bola que é arremessada de um lado para o outro, com 
o intuito de ser levada ao extremo do mapa para contabilizar o ponto.


## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Personalização maior do jogo 
- Melhoria 2: Menu de dificuldade 
- Melhoria 3: implementação de modo Jogador contra Jogador