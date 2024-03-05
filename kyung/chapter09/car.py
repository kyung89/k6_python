class Car:
    """자동차 클래스"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """뜻이 분명하고 깔끔한 이름 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """자동차의 주행거리를 출력합니다"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        거리계 값을 주어진 값으로 바꿉니다.
        현재 값보다 적은 값을 할당할 수 없습니다.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")

    def increment_odometer(self, miles):
        """거리계 값을 주어진 값만큼 늘입니다."""
        self.odometer_reading += miles

