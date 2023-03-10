# movie = ['2001: A Space Odyssey', 'Ad Astra', 'Alien', 'Alien 3', 'Alien vs. Predator', 'Alien vs. Predator: Requiem',
#          'Alien: Covenant', 'Alien: Resurrection', 'Aliens', 'Alita: Battle Angel', 'Arrival', 'Avatar',
#          'Back to the Future', 'Back to the Future Part II', 'Back to the Future Part III', 'Blade', 'Blade II',
#          'Blade Runner', 'Blade Runner 2049', 'Blade Runner 2049: 2036: Nexus Dawn', 'Blade Runner 2049: Nexus Dawn',
#          'Blade Runner 2049: Nowhere to Run', 'Blade Runner 2049: The Replicant Pursuit',
#          'Blade Runner: Black Out 2022', 'Blade Runner: The Final Cut', 'Blade: Trinity',
#          'Close Encounters of the Third Kind', 'Cloud Atlas', 'Dark City', 'Dawn of the Planet of the Apes',
#          'District 9', 'Doctor Strange', 'Doctor Who: Revolution of the Daleks', 'Doctor Who: Spyfall',
#          'Doctor Who: The Day of the Doctor', 'Doctor Who: The Movie', 'Doctor Who: The Return of Doctor Mysterio',
#          'Doctor Who: The Time of the Doctor', 'Doctor Who: The Timeless Children',
#          'Doctor Who: The Woman Who Fell to Earth', 'Doctor Who: Twice Upon a Time', 'E.T. the Extra-Terrestrial',
#          'Edge of Tomorrow', 'Elysium', 'Equilibrium', 'Escape from LA', 'Escape from New York', 'Ex Machina',
#          'Gemini Man', 'Ghost in the Shell', 'Gravity', 'Harry Potter and the Chamber of Secrets',
#          'Harry Potter and the Deathly Hallows: Part 1', 'Harry Potter and the Deathly Hallows: Part 2',
#          'Harry Potter and the Goblet of Fire', 'Harry Potter and the Half-Blood Prince',
#          'Harry Potter and the Order of Phoenix', "Harry Potter and the Philosopher's Stone",
#          'Harry Potter and the Prisoner of Azkaban', 'Her', 'I Am Legend', 'Inception', 'Independence Day',
#          'Independence Day: Resurgence', 'Interstellar', 'Interstellar 2', 'Jurassic Park', 'Jurassic World', 'Life',
#          'Limitless', 'Logan', 'Lucy', 'Mad Max: Fury Road', 'Metropolis', 'Minority Report', 'Mortal Engines',
#          'Oblivion', 'Pacific Rim', 'Pitch Black', 'Planet of the Apes', 'Predator', 'Predator 2', 'Prometheus',
#          'Ready Player One', 'Return of the Jedi', 'Rise of the Planet of the Apes', 'RoboCop',
#          'Rogue One: A Star Wars Story', 'Serenity', 'Solaris', 'Solo: A Star Wars Story', 'Soylent Green', 'Star Trek',
#          'Star Trek Beyond', 'Star Trek II: The Wrath of Khan', 'Star Trek III: The Search for Spock',
#          'Star Trek IV: The Voyage Home', 'Star Trek Into Darkness', 'Star Trek V: The Final Frontier',
#          'Star Trek VI: The Undiscovered Country', 'Star Trek: First Contact', 'Star Trek: Generations',
#          'Star Trek: Insurrection', 'Star Trek: Nemesis', 'Star Trek: The Motion Picture',
#          'Star Wars: Episode I - The Phantom Menace', 'Star Wars: Episode II - Attack of the Clones',
#          'Star Wars: Episode III - Revenge of the Sith', 'Star Wars: Episode IV - A New Hope',
#          'Star Wars: Episode IX - The Rise of Skywalker', 'Star Wars: Episode VII - The Force Awakens',
#          'Star Wars: Episode VIII - The Last Jedi', 'Star Wars: Rebels', 'Star Wars: Resistance',
#          'Star Wars: The Clone Wars', 'Stargate', 'Starman', 'Sunshine', 'Terminator 2: Judgment Day',
#          'Terminator 3: Rise of the Machines', 'Terminator Genisys', 'Terminator Salvation', 'The 5th Wave',
#          'The Adjustment Bureau', 'The Andromeda Strain', 'The Book of Eli', 'The Chronicles of Narnia: Prince Caspian',
#          'The Chronicles of Narnia: The Horse and His Boy',
#          'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe',
#          "The Chronicles of Narnia: The Magician's Nephew", 'The Chronicles of Narnia: The Silver Chair',
#          'The Chronicles of Narnia: The Voyage of the Dawn Treader', 'The Chronicles of Riddick',
#          'The Chronicles of Riddick: Dark Fury', 'The Day the Earth Stood Still', 'The Empire Strikes Back',
#          'The Fifth Element', "The Hitchhiker's Guide to the Galaxy", 'The Hobbit: An Unexpected Journey',
#          'The Hobbit: The Battle of the Five Armies', 'The Hobbit: The Battle of the Five Armies - Extended Edition',
#          'The Hobbit: The Desolation of Smaug', 'The Hobbit: The Desolation of Smaug - Extended Edition',
#          'The Hobbit: The Unexpected Journey - Extended Edition', 'The Hunger Games', 'The Hunger Games: Catching Fire',
#          'The Island', 'The Lord of the Rings: The Fellowship of the Ring',
#          'The Lord of the Rings: The Fellowship of the Ring - Extended Edition',
#          'The Lord of the Rings: The Return of the King',
#          'The Lord of the Rings: The Return of the King - Extended Edition', 'The Lord of the Rings: The Two Towers',
#          'The Lord of the Rings: The Two Towers - Extended Edition', 'The Mandalorian', 'The Martian', 'The Matrix',
#          'The Matrix 4', 'The Matrix Reloaded', 'The Matrix Resurrections', 'The Matrix Revolutions', 'The Omega Man',
#          'The Prestige', 'The Signal', 'The Terminator', 'The Terminator: Dark Fate', 'The Thing',
#          'The Thirteenth Floor', 'The Time Machine', 'The War of the Worlds', 'They Live', 'Thor', 'Thor: Ragnarok',
#          'Thor: The Dark World', 'Total Recall', 'Tron', 'Tron: Legacy', 'War for the Planet of the Apes',
#          'War of the Worlds', 'Westworld']

import random

# список фильмов
films = ["Зеленая миля", "Побег из Шоушенка", "Форрест Гамп", "Список Шиндлера", "1+1", "Начало", "Престиж",
         "Интерстеллар", "Достучаться до небес", "Крестный отец", "Крестный отец 2", "Властелин колец: Братство кольца",
         "Властелин колец: Две крепости", "Властелин колец: Возвращение Короля", "Гарри Поттер и Философский камень",
         "Гарри Поттер и Тайная комната", "Гарри Поттер и Узник Азкабана", "Гарри Поттер и Кубок огня",
         "Гарри Поттер и Орден Феникса", "Гарри Поттер и Принц-полукровка", "Гарри Поттер и Дары Смерти: Часть 1",
         "Гарри Поттер и Дары Смерти: Часть 2", "Матрица", "Храброе сердце", "Титаник", "Аватар",
         "Терминатор 2: Судный день", "Назад в будущее", "Гладиатор", "Мстители", "Темный рыцарь", "Мстители: Финал",
         "Леон", "Бойцовский клуб", "Шестое чувство", "Ла-Ла Ленд", "Бегущий по лезвию", "Бэтмен начало",
         "Малышка на миллион", "В джазе только девушки", "Красавица и чудовище", "Король Лев", "Головоломка", "1+1",
         "Пятница", "Трудности перевода", "Зверополис", "Джентльмены", "Как приручить дракона", "История игрушек",
         "Люди в черном", "Сплит", "Джокер", "Звездные войны: Эпизод IV - Новая надежда",
         "Звездные войны: Эпизод V - Империя наносит ответный удар", "Звездные войны: Эпизод VI - Возвращение джедая",
         "Звездные войны: Эпизод VII - Пробуждение силы", "Звездные войны: Эпизод VIII - Последние джедаи",
         "Звездные войны: Эпизод IX - Скайуокер"]

# выбираем случайный фильм из списка
random_film = random.choice(films)

# выводим на экран название фильма
print("Случайный фильм из списка: ", random_film)



