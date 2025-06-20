class Song:
    def __init__ (self, lyrics):
        self.lyrics = lyrics
    
    def sing(self):
        for line in self.lyrics:
            print(line)
    

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing()