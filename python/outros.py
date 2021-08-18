# Construa uma função que recebe duas listas como parâmetros:
# - nomes: uma lista de textos que não pode conter elementos vazios (um texto vazio).
# - conectivos: outra lista de textos que não pode conter elementos vazios (um texto vazio).
# A função recebe ainda dois números inteiros maiores do que 0, tamanho (T) e quantidade (Q). 

# A função deve então gerar uma lista com Q nomes compostos gerados a partir da intercalação de T nomes e conectivos, nesta ordem.

# Por exemplo, considere nomes = ["julio", "melo", "marcio", "aguiar"] e conectivos = ["de", "da", "_"]. Para quantidade igual a 3 e tamanho igual a 5, a função retornaria: ["julio de melo _ aguiar", "melo _ marcio de melo", "aguiar de julio da melo"]. Veja que um nome não pode terminar com um conectivo. Assim, se o tamanho T for igual a 4, um nome válido seria "julio _ melo melo", mas não "julio _ melo de". Logo, neste caso você deve sortear dois nomes ao invés de intercalar.

# Após isso, construa um programa que lê do usuário duas listas com nomes e conectivos, e usa o retorno da função para imprimir os nomes gerados como nos exemplos que seguem. Veja que não deve ser usado print dentro da função, mas você pode usar a função desenvolvida na Questão 1 para facilitar a leitura das listas.

# Dica: Para sortear aleatoriamente os nomes use o bloco junto com o bloco "in list get random" ou os blocos "random integer" e "in list get #" para pegar um elemento aleatóriamente das listas.

# Exemplo 1
# Digite a quantidade de nomes que deseja incluir na Lista 1: 4
# Digite um nome: julio
# Digite um nome: melo
# Digite um nome: marcio
# Digite um nome: aguiar
# Digite a quantidade de conectivos que deseja incluir na Lista 2: 3
# Digite um conectivo: de
# Digite um conectivo: da
# Digite um conectivo: _
# Digite o tamanho de cada nome formado: 5
# Digite a quantidade de nomes a serem formados: 3
# Os nomes formados sao:
# julio de melo _ aguiar
# melo _ marcio de melo
# aguiar de julio da melo           

# Exemplo 2
# Digite a quantidade de nomes que deseja incluir na Lista 1: 4
# Digite um nome: julio
# Digite um nome: melo
# Digite um nome: marcio
# Digite um nome: aguiar
# Digite a quantidade de conectivos que deseja incluir na Lista 2: 3
# Digite um conectivo: de
# Digite um conectivo: da
# Digite um conectivo: _
# Digite o tamanho de cada nome formado: 4
# Digite a quantidade de nomes a serem formados: 3
# Os nomes formados sao
# julio de melo aguiar
# melo _ marcio melo
# aguiar de julio melo