# Jackson J.
# 11/18/19
# Exercise 40 and it is continuing the lesson about creating a class


class Song(object):
    # This is the class creation "Song"
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade_song = Song(["They rally around tha family",
                             "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade_song.sing_me_a_song()
