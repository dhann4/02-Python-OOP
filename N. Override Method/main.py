class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    '''def showInfo(self, tipe):
        print("{}\n\tTipe: {},\n\tHealth: {}".format(
            self.name,
            tipe,
            self.health
            )
        )
        
        jika seperti ini kepanjangan dan bisa kerepotan nanti nya,
        maka dari itu, akan menggunakan yang namanya overriding / override
        contoh :
        '''

    def showInfo(self):
        print("\nshowInfo di Super Class Hero")
        print("{}\n\tHealth: {}".format(
            self.name,
            self.health
        )
        )

class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    def showInfo(self):
        print("showInfo di Sub Class Hero intelligent")
        '''
        super().showInfo('intelligent')'

        disini tidak usah lagi memakai super, pakai saja print langsung
        contoh :
        '''
        print("{}\n\tTipe: intelligent\n\thealth {}".format(
            self.name,
            self.health
            )
        )
        '''
        artinya, menimpa function dari
            
            def showInfo(self, tipe):
                print("{}, Health: {}".format(
                    self.name,
                    self.health
                    )
                )
        
        yang ada di dalam Super Class
        '''


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)

lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

lina.showInfo()
axe.showInfo()
