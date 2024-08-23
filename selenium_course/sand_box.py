class Example():

    def my_name(self):
        print("\nIn my_name func: ", id(self))
        self.name = "My name: Example class"
        print(self.name)

    def other_func(self):
        print("\nIn other_name func: ", id(self))



my_class = Example()
my_class.my_name()
my_class.other_func()