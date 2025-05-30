from lib.models import Flower
from lib.models import Sessions, Base, engine


def seed_data():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Sessions()


    flower1 = Flower(name="Rose", color="Red", price=12.0)
    flower2 = Flower(name= "Lily, color=White", price=11.5)
    flower3 = Flower(name="Tulip", color="Yellow", price=9.0)

    session.add_all([flower1, flower2, flower3])
    session.commit()
    session.close()

    print("Seeded flowers successfully!")

if __name__ == "__main__":
    seed_data()
