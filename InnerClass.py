class Outer:
    x = 10

    class Inner:
        y = 20

        def m1(self):
            print(Outer().x, "............", self.y)


Outer().Inner().m1()
