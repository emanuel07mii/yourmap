yourmap
===========

### esse pacote tem a finalidade de fazer marcações em um mapa e retorna um html para vizualização

## Instalação
    pip install yourmap

## Exemplo de Uso
#### Importando pacote
    >>> import yourmap

#### Criando mapa
    >>> myMap = yourmap.Map(-7.0840, -41.4704, 17.67)

#### Marcando um ponto no mapa
    >>> myMap.to_point('Praça de Picos', 'Você está aqui', 'blue')

#### Marcando um circulo em um ponto
    >>> myMap.mark_circle(50)

#### Visualizando mapa pelo navegador
    >>> myMap.open_map('mapacentroPicos.html')

## Saída para o código acima:

![Imagem de Saida.](https://raw.githubusercontent.com/emanuel07mii/yourmap/master/imgs/mapEX.png)
