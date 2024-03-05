from user_for_9_12 import User

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