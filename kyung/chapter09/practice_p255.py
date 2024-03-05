# 9-10 레스토랑 임포트하기
from restaurant import Restaurant

res = Restaurant("건강한 스무디킹", "스무디")
res.describe_restaurant()
res.open_restaurant()
print()

# 9-11 관리자 임포트하기
from user_for_9_11 import *

# (first_name, last_name, job, age, gender)
admin = Admin("hanul", "yang", "singer", 25, "woman")
admin.privileges.show_privileges()
print()

