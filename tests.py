import pytest
from main import BooksCollector
class TestBooksCollector:
    @pytest.mark.parametrize(
        'name',
        [
            'Хомяк хочет убивать',
            'Что делать, если ваш кот хочет вас убить'
        ]
    )
    def test_add_new_book_add_book_with_title_no_more_than_max_value_positive_result(self, name, collector):
        collector.add_new_book(name)
        assert name in collector.books_genre

    def test_add_new_book_add_two_books_positive_result(self, collector):
        collector.add_new_book('Капитанская почка')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    #@pytest.mark.parametrize
    def test_set_book_genre_is_comedy_positive_result(self, collector):
        collector.add_new_book('Капитанская почка')
        collector.set_book_genre('Капитанская почка', 'Комедии')
        assert {'Капитанская почка' : 'Комедии'} == collector.books_genre

    def test_get_book_genre_missing_book_return_null(self, collector):
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') is None

    def test_get_books_with_specific_genre_add_book_and_genre_positive_result(self, collector):
        collector.add_new_book('Капитанская почка')
        collector.set_book_genre('Капитанская почка', 'Комедии')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert 'Капитанская почка' in collector.get_books_with_specific_genre('Комедии')

    def test_get_books_genre_book_with_new_genre_return_not_None(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Хомяк хочет убивать', 'Триллер')
        assert collector.get_books_genre() != None

    def test_get_books_for_children_horror_book_not_added_to_children_books(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert 'Что делать, если ваш кот хочет вас убить' not in collector.get_books_for_children()

    def test_add_book_in_favorites_re_adding_books_false(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_added_1_book_is_deleted_from_favorites(self, collector):
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_getting_list_of_favorites_without_adding_book(self, collector):
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.get_list_of_favorites_books()
        assert collector.favorites == []