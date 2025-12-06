# TODO Найдите количество книг, которое можно разместить на дискете
one_symbol = 4 # Вес одного символа
symbol_in_list = one_symbol * 25 # Вес одной строки
one_page = symbol_in_list * 50 # Вес одной страницы
one_book = one_page * 100 # Вес одной книги
mb_one_book = one_book / 1024 / 1024
disk = 1.44 // mb_one_book
books = int(disk)
print("Количество книг, помещающихся на дискету:", books)
