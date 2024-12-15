class Bird:
    def move(self):
        print("the bird is monving")

class FlyingBird(Bird):
    def fly(self):
        print("the bird is flying")
class Penguin(Bird):
    def move (self):
        print("penguin swim and walk")



penguin=Penguin()
flying_bird=FlyingBird()
penguin.move()
flying_bird.fly()
flying_bird.move()
