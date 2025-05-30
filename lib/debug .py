from lib.database import Session
from lib.models import Flower
from lib.helpers import print_divider

session = Session()

def test_flowers():
  print_divider()
  print("Current Flowers in DB:")
  flowers = session.query(Flower).all()
  for flower in flowers:
    print(f"{flower.id}. {flower.name} ({flower.color}) -ksh {flower.price:.2f}")
print_divider()

if __name__ == "__main__":
   test_flowers()
   session.close()
  
  