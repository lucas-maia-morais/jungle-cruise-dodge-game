# jungle-cruise-dodge-game
Dodge Racing game inspired in Jungle Cruise

Requirements:
- Python 3.7
- Pygame

------------------------------------------------------------- O que está no Github

-- Diretórios

font:

Esse diretório contém fontes de letras que foram usadas para os textos do jogo, i.e. arquivos carregados com as fontes dos títulos, botões...

images:

Nesse diretório há as imagens carregadas para o jogo, imagem de fundo, obstáculos, navio do jogador...

soundtrack:

Nesse diretório há os sons utilizados no jogo, tanto de música de fundo quanto de efeitos sonoros.

packages:

Nesse diretório estão implementadas as classes do jogo e seus métodos utilizados. No arquivo elements.py há os elementos do jogo: obstáculos e o jogador. No arquivo enviroment.py há o ambiente da mecânica do jogo: geração e destruição de obstáculos, dinâmica de níveis e checagem de colisão do jogador com obstáculo. No arquivo messeges há uma implementação de mensagens que serão exibidas ao longo do jogo. Já no diretório Screen é organizado o output das telas do jogo, i.e. menu inicial, fundo do jogo, atualização do placar, música de fundo, implementação da movimentação com teclado na tela, configurações de pause e vitória do jogo. O arquivo aux.py serve apenas para algumas defnições de variáveis de cor e nomes de arquivos carregados e dicionário para os botões do jogo.

--Arquivos

Há o arquivo da apresentação final e do jogo jungle-cruise.py.

------------------------------------------------------------- Documentação Jungle Cruise

Autores: Lucas Maia, Luca Rassi e Gabriel Lucena

---Documentação

O presente documento revela detalhes de desenvolvimento e jogabilidade do jogo Jungle Cruise, desenvolvido durante a disciplina de CES-22: Programação Orientada a Objetos, durante o primeiro semestre do ano de 2022.

Introdução

Jungle Cruise é um jogo do tipo corrida de obstáculos, com ambientação em um rio e uma margem de selva, cujo objetivo é desviar dos barcos, animais e pedras durante o caminho do jogador

Descrição

O jogo se baseia em um filme de mesmo nome, lançado pela Disney, no qual a personagem protagonista busca achar uma árvore sagrada em uma floresta tropical, encontrando no seu caminho animais selvagens e inimigos que objetivam chegar nessa árvore e impedir que as personagens principais cheguem nela antes, com emboscadas, armadilhas e perseguições. No jogo, é simulada a situação de fuga dos protagonistas em um barco por um rio, tendo que desviar de objetos naturais e outros barcos inimigos. O jogo termina quando o jogador consegue chegar com o seu barco na árvore sagrada, tendo opção de continuar em uma dificuldade crescente a partir de então.

Gênero

O gênero do jogo é corrida de obstáculos/aventura.

---Design

Mecânica

A mecânica do jogo é simples, o barco tem um percurso no qual percorre, e durante esse percurso diversos objetos aparecerão diante do barco. O objetivo do jogador é desviar do objeto antes que ele bata no barco, sem encalhar nas margens do rio para isso. Durante o percurso é mostrado quantos objetos o jogador conseguiu desviar. Para aumentar a dificuldade, a velocidade do jogo aumenta conforme o jogador consegue desviar de mais obstáculos e também mais obstáculos surgem na tela por vez, a cada nível passado. Na tela é mostrado o nível atual do jogador, além do número de obstáculos desviados aparece também a pontuação do jogador, que é atribuída a cada obstáculo desviado com êxito pelo jogador. Mais pontos são atribuídos conforme o jogador desvia de obstáculos em níveis mais altos. O jogo tem um fim quando o jogador atinge o nível 3, cada nível o jogador precisa passar de 15 obstáculos. Após chegar nesse nível, o jogador tem as opções de começar novamente, voltar ao menu ou continuar jogando, nesse caso ele deve continuar desviando de obstáculos que ficam mais numerosos e mais rápidos conforme passa de mais níveis.

Iteratividade

A tela do é bem simples. A imagem inicial de fundo é uma imagem com as personagens do filme. Há um pergaminho com instruções para jogabilidade e dois botões, um para sair do jogo e um para começar. Ao começar o jogo, o jogador pode utilizar as teclas de setas no seu teclado para mover o barco na tela e desviar dos obstáculos. Há também um botão de pause durante o jogo onde o jogo é pausado e, então, o jogador tem as opções de começar o jogo novamente, continuar de onde parou ou fechar o jogo.

---Conclusão

O jogo serviu para seu propósito de praticar conceitos vistos em sala de aula relacionados à POO. Além da programação, também foi proveitoso o trabalho e desenvolvimento do projeto em equipe, usando a plataforma github para compartilhamento de progresso de forma eficiente e prática. Esperamos que os jogadores se divirtam com a jogabilidade e também com os sentimentos nostálgicos do ótimo filme que ele referencia.

