class pet:
    def __init__(self,name,gender,health):
        self.name=name
        self.gender=gender
        self.__health=health
    def show_info(self):
        print("The pet is a ",self.name ,"and the gender is ",self.gender,"and their health rating is ",self.__health)
    def care(self):
        print(self.name," needs care")
    def set_health(self,new_health):
        if 0<new_health<=100:
            self.__health=new_health
            print("The new health number for ",self.name," is",new_health)
        else:
            print("Health rating must be between 1-100")
class dog(pet):
      def care(self):
        print(self.name," needs a walk and some playtime")
class cat(pet):
      def care(self):
        print(self.name," needs grooming and stroking.")
class hamster(pet):
      def care(self):
        print(self.name," needs to go on the running wheel and wants food")

d=dog("Bruno the dog","male",89)
c=cat("Oreo the cat","female",67)
h=hamster("Coco the hamster","male",76)
pets=[d,c,h]
for pet in pets:
    pet.show_info()
    pet.care()
    print()
h.set_health(82)
