import tkinter as tk

root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=15, width=200)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """Ok, Aqui é onde começamos a jornada na programação
('Aula 01e02 - Introdução ao Python e Entendendo Primeiros conceitos')

(Variaveis, Numeros, Matematica Basica)
(As variáveis são nomes que damos para referenciar valores ao longo do nosso programa)
(Aqui dizemos que x e y são variáveis, eles primeiro armazenaram os valores)
(e depois os usamos para calcular operçaões)

('arq02.txt','w')
(além disso mudamos o valor que y representava atribuindo a ele o valor 7.)
(podem facilitar a interpretação de um programa.)

(Uma breve observação sobre variáveis em Python)
(Variáveis servem para o programa reservar espaço na memoria para um determinado tipo de informação)
(tudo em Python são objetos, então, as variáveis Python armazenam uma referência a um objeto.)

(Como representar as variáveis)

(podem possuir caracteres numéricos.)
(não podem ter espaço entre elas)
(não podem começar com números)
(não podem ter caracteres de acentuação tais como ^, ~, !)
(não podem ter caracteres especiais como @, & nem hifens)
(determina vários métodos especiais e variáveis que usam esse padrão)
(Na tabela abaixo exemplos de nomes validos e inválidos)

(Nomes de variáveis validos e inválidos)
(area_triangulo' - 'area triangulo' #não é permitido espaço em branco)
(samuel_john ou samuel_&_john (não são validos caracteres especiais))
(_inicio total-val (não são valido hifens))
(Por fim, Python diferencia nomes de variáveis)
(com letras maiúsculas e minúsculas exemplo: AREA, Area e area são 3 variáveis diferentes)

(Operadores Aritméticos no Python)
(+ - soma\n)
(– - subtração)
(* - multiplicação)
(/ - divisão)
(// - Divisão trunca a parte fracionaria)
(% - Produz o resto da divisão)
(** - Exponenciação)

(Operadores de comparação no Python)
(abs(x) - Retorna o valor absoluto de x)
(pow(x, y) - O mesmo x**y)
(round(x, n) - Retorna um int ou float)

(Operadores de Descrição no Python)
( < - menor que)
(<= - menor ou igual a)
( > - maior que)
(>= - maior ou igual a)
(== - igual)
(!= - diferente)

(Operadores Lógicos no Python)
(and P and Q - Resulta 'True' só se P e Q forem verdade)
(or P or Q   - Resulta 'False' só se P ou Q forem falsos; se não retorna True)
(not P Se P  - Resulta 'False' se P é falso; se não retorna True)
##fim das aulas 1 e 2##
"""
T.insert(tk.END, quote)
tk.mainloop()
