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
        line = self.book[self.bookmark]
        if 'cmd' in line:
            self.bookmark += 1
            print(line)
            cmd = line.pop('cmd')
            print(line)
            cmd(**line)
            self.check()
        else:
            if line['lambda']():
                self.bookmark += 1
                self.check()
            else:
                print('lambda function', line, line['lambda']())



    def run(self, new_book: list[dict[any]]):
        self.book = new_book
        self.bookmark = 0
        self.check()
