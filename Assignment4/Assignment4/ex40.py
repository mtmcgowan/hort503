class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Study Drills
# 1. Write some more songs using this and make sure you......

happiness_is_a_warm_gun = Song(["She's not a girl who misses much",
                                "Do do do do do do, oh yea",
                                "She's well-acquainted with the touch of the velvet hand"])



# 2. Put the lyrics in a separate variable, then pass....
lyrics = "Dead lung's command it,\nYou pour your life down the rifle's spiral"

the_rifles_spiral = Song([lyrics])

# 3. See if you can hack on this and do more things....
# Ok

# 4. Search online for "object-oriented programming" and try to overflow your brain...
# Ok