# create class
class Player:
    def play(self):
        print("The Player is playing cricket")
        
class Batsman(Player):
    def play(self):
        print("The Batsman is batting")
        
class Bowler(Player):
    def play(self):
        print("The Bowler is bowling")
        
    
#create objects 
batsman = Batsman()
bowler = Bowler() 

# call the play method
batsman.play()
bowler.play()   