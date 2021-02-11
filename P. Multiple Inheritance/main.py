'''
Multiple Inheritance berfungsi untuk mengambil 2 buah method
dalam Super Class yang berbeda-beda.

Sebagai contoh :
'''

class A:

    def method_A(self):
        print("ini adalah method A")

class B:

    def method_B(self):
        print("ini adalah method B")

class multi(A,B):
    pass

'''
jadi si multi ini berfungsi untuk meng inherit 2 buah class,
bisa untuk mengambil method dari class A dan juga method
dari class B
'''

objek = multi()

objek.method_A()
objek.method_B()