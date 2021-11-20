import yourmap

# Criando mapa -7.0834098,-41.470758,17.67
myMap = seemap.Map(-7.0840, -41.4704, 17.67)

# Marcando um ponto no mapa
myMap.to_point('Praça de Picos', 'Você está aqui', 'blue')

# Marcando um circulo em um ponto
myMap.mark_circle(50)

# Visualizando mapa pelo navegador
myMap.open_map('mapacentroPicos.html')
