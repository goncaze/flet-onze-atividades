# A flet_onze_atividades Flet app

Atividades para desenvolver usando framework Flet

01.	Tabuada de um número
Crie um programa para gerar a tabuada de um número inteiro fornecido pelo usuário:  
a.	O programa espera que o usuário informe um número (inteiro).
b.	O programa espera que o usuário selecione uma das quatro operações básicas da matemática.
c.	O programa gera a tabuada da operação selecionada e apresenta ao usuário assim que um botão chamado “Gerar tabuada” for clicado.

02.	Maior, Menor e Média 
Crie um programa que solicite ao usuário três números e apresenta o maior, o menor e a média entre eles.
a.	O programa espera que o usuário informe três números;
b.	O programa aguarda o usuário clicar em um botão denominado “Calcular”;
c.	Em seguida o programa apresenta o maior, o menor e a média entre eles.

03.	Jogo da Adivinhação 
Crie um programa que gere um número aleatório entre 1 e 100 e desafie o usuário a adivinhá-lo. 
a.	Um botão denominado “Começar” será apresentado na primeira tela do programa;
b.	Clicando no botão “Começar”, um único número aleatório será gerado uma única vez até que o usuário acerte.
c.	Além do número aleatório, o programa também apresentará uma segunda tela contendo uma caixa de texto aguardando o usuário informar seu palpite;
d.	Nesta segunda tela também haverá um botão denominado “Conferir”;
e.	Ao clicar em conferir, o programa deve testar o palpite do usuário;
f.	Se o palpite for maior que o número sorteado, o programa deverá apresentar a mensagem “Errou para cima”;
g.	Se o palpite for menor que o número sorteado, o programa deverá apresentar a mensagem “Errou para baixo”;
h.	Se o palpite for igual ao número sorteado, o programa deverá apresentar a mensagem “Muito bem, você acertou!!”;
i.	Para cada vez que o usuário errar, o programa solicitará um novo palpite.

04.	Sequência de Fibonacci
Crie um programa que gere e apresente a sequência de Fibonacci até um determinado número de termos, especificado pelo usuário. Por fim, imprima a quantidade de números pares e ímpares existentes dentro da sequência apresentada.

05.	 Juros simples
Uma empresa de consultoria financeira, denominada Start, possui muitos dados de investimento (capital, taxa de juros e tempo) e precisa que você crie um programa para calcular os juros simples de cada investimento. A empresa Start de consultoria financeira deseja que o programa também apresente o montante.

Como técnico em Desenvolvimento de Sistemas, você deve criar um programa que solicite do usuário os dados de capital, taxa de juros e tempo. Como resultado, seu código deve apresentar o juro simples.

Exemplo de entrada de dados:

C → capital = 600
i → taxa de juro ao ano = 12%
t → tempo em anos = 5

Saída de dados:

Resultado → juro simples = 360
Resultado → Montante = 960
 
 
06.	 Juros simples (avançado)
Outra empresa de consultoria financeira, a Evolution, deseja que você TDS desenvolva um programa mais avançado do que aquele feito para a concorrência. A empresa quer um programa que seja capaz de calcular ou o juro, ou a taxa de juro, ou o tempo ou o capital.

Em outras palavras, um dado sempre estará faltando e seu programa deve saber lidar com isso. Identifique o dado faltante e apresente o valor desse dado faltante como resultado.

Exemplo de entrada de dados:

C → capital = 
i → taxa de juro ao ano = 12%
t → tempo em anos = 5
j → juros = 360

Saída de dados:

Resultado → capital = 600

07.	 Juro composto
As empresas de consultoria financeira querem que você desenvolva um programa para calcular o juro composto

Exemplo de entrada de dados:

C → capital = 2000
i → taxa de juro ao mês = 10%
t → tempo em meses = 5

Saída de dados:

Resultado → Montante = 3221.02

08.	  Cafeteria de Galadriel
Uma empreendedora denominada Galadriel que é do município de Viana pretende abrir uma nova cafeteria na cidade. Galadriel pensa em ofertar um cardápio muito simples, porém, gostaria de saber de quantas formas diferentes um pedido poderá ser feito por um cliente.

OBJETIVO: Você TDS deve criar um programa que determine qual seja esse número total de possíveis pedidos diferentes.

DETALHES: No cardápio da cafeteria de Galadriel tem como prato principal o seu famoso pão de queijo recheado. Mas, o cliente poderá pedir apenas um dos tipos de recheio (doce ou salgado). Se optar pelo recheio doce poderá pedir apenas um tipo (goiabada, doce de leite, chocolate). Se optar pelo recheio salgado poderá pedir apenas um tipo (frango, carne seca, calabresa, queijo gorgonzola). Para acompanhar, é possível escolher uma bebida (café expresso, café com leite, capuccino, chocolate quente, soda italiana, água mineral).

Agora, crie um programa que calcule o total de pedidos diferentes que um cliente poderá fazer.

DICA: princípio fundamental da contagem.

09.	Aluguel de canoas de Sakura Palmares
Sakura Palmares teve a ideia de começar um negócio de aluguel de canoa para passeios nos lagos de Viana. No momento, Sakura Palmares tem apenas uma canoa, um colete salva-vidas e dois remos. O aluguel desta canoa custará 40 reais na primeira hora acrescidos de 20 reais por hora extra.

Desenvolva um programa que calcule o valor ganho pelo aluguel da canoa de Sakura Palmares solicitando do usuário apenas a quantidade de horas.

Exemplo:

Se um cliente usou a canoa por três horas:
h => horas de aluguel
g => valor ganho pelo aluguel


20*(h - 1) + 40 = g


h = 3
g = 80


DICA: equação do primeiro grau => ax + b = 80.

10.	Faxina residencial de Mandela Tokioham
Mandela Tokiohama, está abrindo uma microempresa de faxina residencial. As pessoas vão contratar seu serviço para limpar suas casas. Mandela Tokiohama pretende cobrar 100 reais na primeira hora acrescentando mais 32 reais a hora nas horas seguintes.

Desenvolva um programa que calcule o valor ganho na contratação de Mandela Tokiohama cujo serviço dure quatro horas. Solicite do usuário apenas a quantidade de horas.

Referência: Para a faxina que durou quatro horas o programa deverá retornar como resultado o valor ganho de 196 reais.

DICA: equação de primeiro grau => ax + b = 196

11.	Jogo da Forca: 
Crie um programa que implemente o jogo da forca, permitindo que um jogador tente adivinhar uma palavra secreta letra por letra. Não é necessário desenhar a forca.



To run the app:

```
flet run [app_directory]
```