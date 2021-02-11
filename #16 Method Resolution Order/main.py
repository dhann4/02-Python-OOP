# method resolution order // multiple inheritance

'''class A:

    def show_A(self):
        print("ini adalah show A")

class B:

    def show_B(self):
        print("ini adalah show B")

class C(A,B):
    pass

objek = C()
objek.show_A()
objek.show_B()'''

'''
lalu bagaimana jika method nya sama ?
contoh :
'''
class A:

    def show(self):
        print("ini adalah show A")

class B:

    def show(self):
        print("ini adalah show B")

class C(A,B):
    pass

objek = C()
objek.show()
help(objek)