class Man:

    def __init__(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


# class Woman:
#
#     def __init__(self, name):
#         self.name = name
#
#     def marry(self, man):
#         return [self.name, man.name]

a = Man("john")
a.set_age(20)
print(a.get_age())
