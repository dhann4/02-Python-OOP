# diamond problem

class A:

    def show(self):
        print("ini adalah Show A")

class B(A):
    pass
    # def show(self):
    #     print("ini adalah Show B")


class C(A):

    def show(self):
        print("ini adalah Show C")

class D(B,C):
    pass

objek = D()
objek.show()



