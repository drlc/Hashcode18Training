from Parser import *
from Pattern import *

def main():
   parser = Parser()
   pizza = parser.readFile('/Users/DaRaLoCa/projects/hashcode-2018/Hashcode18Training/resources/example')

   print(pizza)

   pattern1 = Pattern(2,1)
   pattern1.setPoint(0,0)
   print pattern1.isFitting(pizza)
   print pattern1.getCoordinate()

   pattern2 = Pattern(2, 1)
   pattern2.setPoint(0, 1)
   print pattern2.isFitting(pizza)
   print pattern2.isInsidePizza(pizza)

   pattern3 = Pattern(4, 1)
   pattern3.setPoint(0, 1)
   print pattern3.isInsidePizza(pizza)

   pattern4 = Pattern(2, 1)
   pattern4.setPoint(0, 2)
   print pattern4.getCoordinate()

   pattern5 = Pattern(2, 1)
   pattern5.setPoint(1, 2)
   print pattern5.getCoordinate()







if __name__ == '__main__':
   main()