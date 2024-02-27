def describe_pet(pet_name, animal_type="dog"): #default parameter
    """반려동물 정보를 표시합니다."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('sonny')
print()

def get_formatted_name(first_name, last_name, middle_name = ''):
    """실제 이름 형식"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
