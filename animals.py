class Animals:

    def __init__(self, name, height, legs, female):
        self.name = name
        self.height = height
        self.legs = legs
        self.female = female

    def __repr__(self):
        return f"dog: {self.name=:11}   {self.height=:5}     {self.legs=:4}     {self.female=:3}"

    def sound(self):
        print("bark!")

dog = Animals("Snoopy", "25 kg", "4", "yes")
print(dog)
dog.sound()

