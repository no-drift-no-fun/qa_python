from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
    #     # создаем экземпляр (объект) класса BooksCollector
    #     collector = BooksCollector()
    #
    #     # добавляем две книги
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    #
    #     # проверяем, что добавилось именно две
    #     # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #     assert len(collector.get_books_rating()) == 2
    #
    # # напиши свои тесты ниже
    # # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('book', ['Гордость и предубеждение и зомби', '', '12345678910123456789101234567891012345678910' ] )
    def test_add_new_book_add_book_with_incorrect_name(self, book):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        amount_before = len(collector.books_genre)
        collector.add_new_book(book)
        amount_after = len(collector.books_genre)
        assert amount_before == amount_after

    def test_set_book_genre_add_gender(self):
        collector = BooksCollector()
        collector.add_new_book('Собачье сердце')
        collector.set_book_genre('Собачье сердце', 'Комедии')
        assert collector.books_genre == {'Собачье сердце': 'Комедии'}

    def test_get_book_genre_comedy(self):
        collector = BooksCollector()
        collector.add_new_book('Собачье сердце')
        collector.set_book_genre('Собачье сердце', 'Комедии')
        assert collector.get_book_genre('Собачье сердце') == 'Комедии'

    def test_get_books_with_specific_genre_return_comedy(self):
        collector = BooksCollector()
        collector.add_new_book('Собачье сердце')
        collector.set_book_genre('Собачье сердце', 'Комедии')
        collector.add_new_book('Приключения Шерлока Холмса и Доктора Ватсона')
        collector.set_book_genre('Приключения Шерлока Холмса и Доктора Ватсона', 'Детектив')
        collector.add_new_book('Чебурашка')
        collector.set_book_genre('Чебурашка', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Чебурашка']

    def test_get_books_genre_return_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Собачье сердце')
        assert collector.get_books_genre() == {'Собачье сердце': ''}

    def test_get_books_for_children_return_cartoon(self):
        collector = BooksCollector()
        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужас')
        collector.add_new_book('Приключения Шерлока Холмса и Доктора Ватсона')
        collector.set_book_genre('Приключения Шерлока Холмса и Доктора Ватсона', 'Детектив')
        collector.add_new_book('Чебурашка')
        collector.set_book_genre('Чебурашка', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Чебурашка']

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Собачье сердце')
        collector.add_book_in_favorites('Собачье сердце')
        assert collector.favorites == ['Собачье сердце']

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Собачье сердце')
        collector.add_book_in_favorites('Собачье сердце')
        collector.add_new_book('Приключения Шерлока Холмса и Доктора Ватсона')
        collector.add_book_in_favorites('Приключения Шерлока Холмса и Доктора Ватсона')
        collector.delete_book_from_favorites('Приключения Шерлока Холмса и Доктора Ватсона')
        assert collector.favorites == ['Собачье сердце']

    def test_get_list_of_favorites_books_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Собачье сердце')
        collector.add_book_in_favorites('Собачье сердце')
        assert collector.get_list_of_favorites_books() == collector.favorites






