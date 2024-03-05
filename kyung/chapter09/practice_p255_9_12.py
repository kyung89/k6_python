# 9-12 여러 모듈
from admin_for_9_12 import Privileges, Admin

# (first_name, last_name, job, age, gender)
admin = Admin("hoin", "lee", "programmer", 29, "man")
admin.privileges.show_privileges()