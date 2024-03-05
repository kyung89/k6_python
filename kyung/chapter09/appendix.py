def get_data():
    return 1,2,3

_,a,b = get_data() # 첫번째 값을 무시하겠다: _ 사용

a = [1,2,3]
b = [11,22,33]
mylist = [*a, *b] # 병합

print(mylist)
print()

c = ['a', 'b']
z = zip(a,c) # a 는 3개, c 는 2개, zip 결과는 2개가 된다
print(list(z))
print()

# getter, setter 를 정의하는데 decorator 사용
class Shape:

    def __init__(self, base, height):
        self.__base = base
        self.height = height

    @property # decorator for getter
    def get_base(self):
        return self.__base
    
    @property
    def get_height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.height = height