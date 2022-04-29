# jungle-cruise-dodge-game
Dodge Racing game inspired in Jungle Cruise

Requirements:
- Python 3.7
- Pygame

Para executar deve estar no dirétorio clonado:
```sh
cd path_to_cloned_directory
python jungle-cruise.py
```

------------------------------------------------------------- 
# Documentação Jungle Cruise

Autores: Lucas Maia, Luca Rassi e Gabriel Lucena

---
## Documentação

O presente documento revela detalhes de desenvolvimento e jogabilidade do jogo Jungle Cruise, desenvolvido durante a disciplina de CES-22: Programação Orientada a Objetos, durante o primeiro semestre do ano de 2022.

### Introdução

Jungle Cruise é um jogo do tipo corrida de obstáculos, com ambientação em um rio e uma margem de selva, cujo objetivo é desviar dos barcos, animais e pedras durante o caminho do jogador

### Descrição

O jogo se baseia em um filme de mesmo nome, lançado pela Disney, no qual a personagem protagonista busca achar uma árvore sagrada em uma floresta tropical, encontrando no seu caminho animais selvagens e inimigos que objetivam chegar nessa árvore e impedir que as personagens principais cheguem nela antes, com emboscadas, armadilhas e perseguições. No jogo, é simulada a situação de fuga dos protagonistas em um barco por um rio, tendo que desviar de objetos naturais e outros barcos inimigos. O jogo termina quando o jogador consegue chegar com o seu barco na árvore sagrada, tendo opção de continuar em uma dificuldade crescente a partir de então.

### Gênero

O gênero do jogo é corrida de obstáculos/aventura.

---
## Design

### Mecânica

A mecânica do jogo é simples, o barco tem um percurso no qual percorre, e durante esse percurso diversos objetos aparecerão diante do barco. O objetivo do jogador é desviar do objeto antes que ele bata no barco, sem encalhar nas margens do rio para isso. Durante o percurso é mostrado quantos objetos o jogador conseguiu desviar. Para aumentar a dificuldade, a velocidade do jogo aumenta conforme o jogador consegue desviar de mais obstáculos e também mais obstáculos surgem na tela por vez, a cada nível passado. Na tela é mostrado o nível atual do jogador, além do número de obstáculos desviados aparece também a pontuação do jogador, que é atribuída a cada obstáculo desviado com êxito pelo jogador. Mais pontos são atribuídos conforme o jogador desvia de obstáculos em níveis mais altos. O jogo tem um fim quando o jogador atinge o nível 3, cada nível o jogador precisa passar de 15 obstáculos. Após chegar nesse nível, o jogador tem as opções de começar novamente, voltar ao menu ou continuar jogando, nesse caso ele deve continuar desviando de obstáculos que ficam mais numerosos e mais rápidos conforme passa de mais níveis.

### Iteratividade

A tela do é bem simples. A imagem inicial de fundo é uma imagem com as personagens do filme. Há um pergaminho com instruções para jogabilidade e dois botões, um para sair do jogo e um para começar. Ao começar o jogo, o jogador pode utilizar as teclas de setas no seu teclado para mover o barco na tela e desviar dos obstáculos. Há também um botão de pause durante o jogo onde o jogo é pausado e, então, o jogador tem as opções de começar o jogo novamente, continuar de onde parou ou fechar o jogo.

---
## Arquivos
### Arquivos e dirétorios na diretório incicial:
- **font/**: Diretório com as fontes utilizadas no jogo
- **images/**: Diretório com as imagens utilizadas no jogo
- **packages/**: Diretório com os packages onde foram criadas as classes utilizadas no jogo. Em maior detalhes na próxima subseção.
- **soundtrack/**: Diretórios com músicas e sons utilizados no jogo
- **jungle-cruise.py**: Arquivo .py com a main para executar o jogo.

### Arquivos do diretório packages | Classes do Jogo:
- **aux.py**: Arquivo .py com a implementação de váriaveis e estruturas de dados do jogo com o intuito de reduzir a redundância no código
- **elements.py**: Arquivo .py com a implementação da classe **Elements**, responsável pela criação de elementos do jogo, bem como suas classes filhas **Player** referente ao jogador e **Obstacles** referente aos obstáculos.
- **environment.py**: Arquivo .py com a implementação da classe **Environment**, responsável pelo gerenciamento de funções e parametros relativos ao jogo, e.g. verificar colisões, aumentar nível, salvar velocidade.
- **events.py**: Arquivo .py com funções auxiliares sem classe definida para reduzir rendundância de código. Chamada events, pois em sua maioria as funções foram só de eventos, e.g. tentar fechar jogo pelo botão de quit.
- **screen.py**: Arquivo .py com a implementação da classe **Screen**, responsável pela apresentação das páginas e chamadas das funções do environment.

---
## Conclusão

O jogo serviu para seu propósito de praticar conceitos vistos em sala de aula relacionados à POO. Além da programação, também foi proveitoso o trabalho e desenvolvimento do projeto em equipe, usando a plataforma github para compartilhamento de progresso de forma eficiente e prática. Esperamos que os jogadores se divirtam com a jogabilidade e também com os sentimentos nostálgicos do ótimo filme que ele referencia.

