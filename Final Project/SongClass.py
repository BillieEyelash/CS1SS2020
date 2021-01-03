class Song:

    def __init__(self, name, artist, peakRank, weeksOnChart):
        self.name = name
        self.artist = artist
        self.peakRank = peakRank
        self.weeksOnChart = weeksOnChart

    def __str__(self):
        return self.name + ':' + self.artist + ':' + str(self.peakRank) + ':' + str(self.weeksOnChart)

    def is_collaboration(self):
        return 'featuring' in self.artist or '&' in self.artist

    def is_equal(self, other):
        return self.name == other.name and self.artist == other.artist

def test():
    BadGuy = Song('Bad Guy', 'Billie Eilish', 1, 32)
    BadGuy2 = Song('Bad Guy', 'Billie Eilish', 2, 3)
    MyStrangeAddiction = Song('My Strange Addiction', 'Billie Eilish', 0, None)
    Senorita = Song('Senorita', 'Shawn Mendez & Camila Cabello', 1, 30)
    SouthOfTheBorder = Song('South of the Border', 'Ed Sheeran featuring Camila Cabello and Cardi B', 15, 12)

    print(str(BadGuy) == 'Bad Guy:Billie Eilish:1:32')
    print(BadGuy.is_collaboration() == False)
    print(Senorita.is_collaboration() == True)
    print(SouthOfTheBorder.is_collaboration() == True)
    print(BadGuy.is_equal(BadGuy2) == True)
    print(BadGuy.is_equal(MyStrangeAddiction) == False)

test()
