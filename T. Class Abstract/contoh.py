from abc import ABC, abstractmethod

class Button(ABC):

    def __init__(self, set_link):
        self.link = set_link # adalah setter

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):

    def click(self):
        print("Go to: {}".format(self.link)) # adalah getter

    '''
    bisa bolak balik asal urutan super class nya selalu di atas, contoh :
    
    awal nya seperti ini
    @Button.link.setter berada di posisi atas, jika si @link.getter di posisi atas masih bisa juga asalkan
    ada si @Button. ini
    
     @Button.link.setter
    def link(self, input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link
    '''

    @Button.link.getter
    def link(self):
        return self.__link

    @link.setter
    def link(self, input):
        self.__link = input


tombol1 = PushButton("www.contoh-class-abstract.com")
tombol1.click()

'''
dan akhir nya selesai juga (THE END)... Hore:v "prok...prok...prok!!"

selanjutnya setelah menguasai Object Oriented Programming (OOP)
next step nya adalah :

Object Oriented Design (OOD)
'''
