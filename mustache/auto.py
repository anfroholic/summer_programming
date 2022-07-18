#you suck!

"""
Archie is a super villian trying to take over tele-op
He is a slow virus that works with most of the agents
He also works in his main lair autonomous
"""

class Autonomous:
    def __init__(self, *, name='no_name'):
        self.name = name
        print(f" {name} IS MY NAME")
        self.bookmark = 0
        self.book = []

    def check(self):
        func = self.book[self.bookmark]
        returned = func()
        # if self.book[self.bookmark]() is False:
        if returned is False:  # compare
            return  # leaving
        else:
            self.bookmark += 1
            self.check()

        # if 'cmd' in page:
        #     self.bookmark += 1
        #     print(page)
        #     cmd = page.pop('cmd')
        #     print(page)
        #     cmd.__call__(**page)
        #     self.check()
        # else:
        #     if page['lambda']():
        #         self.bookmark += 1
        #         self.check()
        #     else:
        #         print('lambda function', page, page['lambda']())



    def run(self, new_book: list[dict[any]]):
        self.book = new_book
        self.bookmark = 0
        self.check()
