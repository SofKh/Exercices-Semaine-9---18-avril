import math

from pkg_resources import declare_namespace


class Fraction:
    def __init__(self, num, den):
        self.numerateur = int(num)
        self.denominateur = int(den)
        self.reduire()
    
    def reduire(self):
        self.numerateur = self.numerateur / pgcf()
        self.denominateur = self.denominateur / pgcf()
    
    def pgcd(self):
        if self.numerateur > self.denominateur:
            smaller = self.denominateur
        else:
            smaller = self.numerateur
        for i in range(1, smaller+1):
            if((self.numerateur % i == 0) and (self.denominateur % i == 0)):
                pgcd = i
        return pgcd



        """def choix_user(self):
            self.numerateur = int(input("Rentrez un numerateur: "))
            self.denominateur = int(input("Rentrez un denominateur: "))"""

    # ADDITION
    def __add__(self, other):
        return Fraction(self.numerateur*other.den + other.num*self.denominateur, self.denominateur * other.den)
    
    # SOUSTRACTION
    def __sub__(self, other):
        return Fraction(self.numerateur*other.den - other.num*self.denominateur, self.denominateur * other.den)
    
    # MULTIPLICATION
    def __mul__(self, other):
        return Fraction(self.numerateur*other.num, self.denominateur*other.den)
    
    # DIVISION
    def __truediv__(self, other):
        return Fraction(self.numerateur*other.den, self.denominateur*other.num)
    
    # EGALITE
    def __eq__(self, other):
        if (self.numerateur == other.num and self.denominateur == other.den):
            return "Les fractions sont egales"
        else:
            return "Les fractions ne sont pas egales"
    
    # STRING
    def __str__(self, other):
        return f"{self.numerateur}/{self.denominateur}"


    


    

