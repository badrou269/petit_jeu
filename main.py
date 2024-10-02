import random

if __name__ == '__main__':
    import doctest

    doctest.testmod()
class Game:
    def __init__(self,m):
        self.m = m
        self.k= random.randint(0, m)
    def test(self,k):
        if self.k==k:
            return True
            print("Bravo, tu as gagné!")
        if self.k<k:
            return False
            print("trop petit")
        if self.k>k:
            return false
            print("trop grang")
    def play(self):
        k = int(input("Entre un nombre :"))
        while self.test(k) != True:
            if self.m ==0 :
                print("Tu as perdu !")
                break
        k = int(input("Recommence: "))






game1 = Game(6)
game1.play()




