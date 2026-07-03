class cricket:
    def __init__(self,player_name,score):
        self.__player_name=player_name
        self.__score=score
    def info(self):
        print("The runs he has scored is", self.__score)
    def play(self):
        print("The cricket player name is ",self.__player_name)
    def set_score(self,new_score):
        if new_score >=0:
            self.__score=new_score
        else:
            print("The score cannot be negative")
    
class football:
    def __init__(self,player_name,score):
        self.__player_name=player_name
        self.__score=score
    def info(self):
        print("The goals he has scored is", self.__score)
    def play(self):
        print("The football player name is ",self.__player_name)
    def set_score(self,new_score):
        if new_score >=0:
            self.__score=new_score
        else:
            print("The score cannot be negative")

c=cricket("Virat",167)
f=football("Ronaldo",3)

for i in (c,f):
    i.info()
    i.play()
    print()
    i.set_score(5)
