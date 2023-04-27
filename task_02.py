  # Пункт A. 
  # Приведем плейлист песен в виде списка списков
  # Список my_favorite_songs содержит список названий и длительности каждого трека
  # Выведите общее время звучания трех случайных песен в формате
  # Три песни звучат ХХХ минут
my_favorite_songs =[
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
    ]      
    
    # Решение

three_songs = my_favorite_songs[3][1] + my_favorite_songs[5][1] + my_favorite_songs[8][1]
three_songs = round(three_songs,2)
print('Три песни звучат', three_songs)
    

    # Пункт B. 
    # Есть словарь песен 
    # Распечатайте общее время звучания трех случайных песен
    # Вывод: Три песни звучат ХХХ минут.

    #Решение
favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,       
  }
another_three_songs = favorite_songs_dict['Waste a Moment'] + favorite_songs_dict['Out of Touch'] + \
                      favorite_songs_dict['In This World']
another_three_songs = round(another_three_songs, 2)
print('А другие 3 песни звучат приблизительно', another_three_songs)
