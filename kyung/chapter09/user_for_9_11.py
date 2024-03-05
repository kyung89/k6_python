class User:
    def __init__(self, first_name, last_name, job, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print(f"이름은 {self.get_fullname()} 입니다.")
        print(f"직업은 {self.job} 입니다.")
        print(f"나이는 {self.age} 입니다.")
        print(f"성별은 {self.gender} 입니다.")

    def get_fullname(self):
        return (f"{self.first_name} {self.last_name}").title()
    
    def greet_user(self):
        print(f"{self.get_fullname()} 님 환영합니다.")

class Privileges:
    def __init__(self, *privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        for p in self.privileges:
            print(p)

class Admin(User):
    def __init__(self, first_name, last_name, job, age, gender):
        super().__init__(first_name, last_name, job, age, gender)
        self.privileges = Privileges("can delete post","can add post","can ban user")