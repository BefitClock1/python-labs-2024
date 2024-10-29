class Farm:
    Animal_owner = ""
    Animal_squad_count = 0
    
    def __init__(self, location, animal_count, power_vent, farm_visiting = 0):
        #Приватні поля
        self.__location = location  
        self.__animal_count = animal_count  
        self.__power_vent = power_vent 
        self.__farm_visiting = farm_visiting  
    def default_constructor(farm):
        return farm("Unknown", 0, 0)
    def get_farm_visiting(self):
        if self.__farm_visiting.is_integer():
            print(f"кількість відвідувань{self.__farm_visiting}")
        else:
            print("відвідуваність має бути число")
    def set_farm_visiting(self, new_v):
        self.__farm_visiting += new_v

    
    def get_farm_location(self):
        print(f"Розташуваня ферми {self.__location}")
    def get_farm_animal_count(self):
        print(f"Кількість тварин {self.__animal_count}шт")
    def get_farm_power_vent(self):
        print(f"Потужність вентиляторів {self.__power_vent}Ват")
    def __str__(self):                                                                                                                                                                              #Перевизначення str
        return f"Локація ферми:{self.__location}, Кількість тварин:{self.__animal_count}, потужність вентилятора:{self.__power_vent}, відвідувань{self.__farm_visiting}"
    def __repr__(self):                                                                                                                                                                             # перевизначення repr
        return f"Farm(location='{self.__location}', animal_count={self.__animal_count}, power_vent={self.__power_vent})"
    def __del__(self):
        print("Farm deleted")
    def max_visiting(farms):
        return max(farms, key=lambda farm: farm.__farm_visiting)

def main():
    farm1 = Farm("Ukraine", 10, 50, 10)
    farm2 = Farm("USA", 20, 75, 40)
    farm3 = Farm("Gyrtogutok", 10, 20 ,20)

    
    farms = [farm1, farm2, farm3]


    
    #print(Farm1)
    #print(Farm1.get_farm_visiting())
    #Farm1.set_farm_visiting(2)
    #print(Farm1)
    #print(Farm1.get_farm_visiting())
    max_visiting_farm = Farm.max_visiting(farms)
    print("Ферма з найбільшою кількістю відвідувань:", max_visiting_farm)


main()