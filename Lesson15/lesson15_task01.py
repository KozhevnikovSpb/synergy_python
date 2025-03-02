# github link - https://github.com/KozhevnikovSpb/synergy_python.git

class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_Transport(self):
        print(f"Название автомобиля: {self.name}. Скорость: {self.max_speed}. Пробег: {self.mileage}")
    

def main():
    Autobus = Transport("Renault Logan", 180, 12)   
    Autobus.print_Transport()


if __name__ == "__main__":
    main()
