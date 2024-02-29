# 출력할 디자인이 저장된 리스트
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 남은 게 없을 때까지 디자인을 출력합니다.
# 출력한 디자인을 completed_models 로 옮깁니다
while unprinted_designs: # 빈 리스트일때 끝난다
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)


# 완료된 디자인을 표시합니다.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
print()

#####

def print_models(unprinted_designs, completed_models):
    while unprinted_designs: # 빈 리스트일때 끝난다
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# 출력할 디자인이 저장된 리스트
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models) # 리스트가 parameter 이면  mutable
show_completed_models(completed_models)
print()

def modify_string(s): # 스트링 값을 전달받았다
    ### immutable 변수는 튜플, 스트링, 불리언  
    s = s + "world" # 변수 s 는 원래 변수가 가리키는 주소와 다르다
    print(s)

st = "hello "
modify_string(st)
print(st) # 출력 결과가 hello => 변경안됨