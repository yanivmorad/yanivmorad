# from datetime import datetime, timedelta
#
# class DateIterator:
#     def __init__(self, start_date):
#         self.start_date = start_date
#         self.current_date = start_date
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_date.month != self.start_date.month:
#             raise StopIteration
#         current_date = self.current_date
#         self.current_date += timedelta(days=1)
#         return current_date
# start_date = datetime(2022, 12, 21,19,54)
#
#
# date_iterator = DateIterator(start_date)
#
# for date in date_iterator:
#    print(date)

class EBook:

    def __init__(self, book_path: str, words_num: int):

        self.book_path = book_path
        self.pages: dict[int: str] = {}

        with open(book_path, 'r') as fh:
            content = fh.read()

        all_words: list[str] = content.split()
        page_num = 1
        for i in range(0, len(all_words), words_num):
            page_words = all_words[i : i+words_num]
            self.pages[page_num] = " ".join(page_words)
            page_num += 1

    def get_total_pages(self):
        return len(self.pages)

    def get_page_content(self, page_num) -> str:
        if page_num not in self.pages:
            raise Exception()
        return self.pages[page_num]


if __name__ == '__main__':
    book = EBook(r"C:\Users\yc\Downloads\alice_in_wonderland (2).txt", 1000)
    # print(f"Total pages: {book.get_total_pages()}")
    # print(f"Page 10: {book.get_page_content(27)}")
    print(book.__dict__)