class Outer:
    x = 10

    class Inner:
        y = 20

        def m1(self):
            print(Outer().x, "............", self.y)


Outer().Inner().m1()
'''

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

'''
