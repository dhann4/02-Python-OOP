class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{}, dengan health: {}".format(self.name, self.health))

'''class Hero_Intellegent(Hero):
    def __init__(self, name):
        self.name = name
        self.health = 100

class Hero_Strength(Hero):
    def __init__(self, name):
        self.name = name
        self.health = 200
        
di sebut dengan pengulangan karena di dalan Class
Hero Intellegent dan Strength ada self.name dan self.health

di dalam pemrograman tidak boleh melakukan pengulangan seperti ini.
Daripada menggunakan sistem yang di atas, lebih baik menggunakan sistem seperti yang di bawah
'''

class Hero_Intellegent(Hero):
    def __init__(self, name):
        '''Hero.__init__(self, name, 100)
            atau bisa juga dengan menggunakan super seperti di bawah ini'''
        super().__init__(name, 100)
        '''
        kita bisa memanggil function showInfo di sini dengan cara :
        '''
        super().showInfo()

        '''
        nah, berbeda dengan Hero.__init__(self, name, 100)
        super() artinya Super Class / Class Utama yaitu Hero
        sedangkan .__init__() artinya method init yang ada di dalam Super Class Hero
        jadi jika super().__init__() artinya mengambil method init yang ada di dalam Super Class
        lalu, jika Hero.__init__(self, name, 100) ada self nya
        di super tidak ada self nya karena self sudah ada di dalam Super Class
        jadi hanya memakai super().__init__(name, 100) atau nama dan health nya saja.
        '''

class Hero_Strength(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 200)
        super().__init__(name, 200)
        super().showInfo()

'''
kesimpulan nya adalah, setiap kali membuat Hero di dalam Sub Class Her Intellegent maka default darah/health nya adalah 100
begitu juga dengan Hero Strength default darah/health untuk semua Hero yang ada di dalam Sub Class Hero Strength adalah 200
'''

lina = Hero_Intellegent('lina')
axe = Hero_Strength('axe')

