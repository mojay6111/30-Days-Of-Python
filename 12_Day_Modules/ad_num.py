def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total


def add_two_numbers (num1, num2):
    total = num1 + num2
    return total

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;


def generate_full_name(firstname, lastname):
      space = ' '
      fullname = firstname + space + lastname
      return fullname

def sum_two_nums (num1, num2):
    return num1 + num2
gravity = 9.81
person = {
    "firstname": "Asabeneh",
    "age": 250,
    "country": "Finland",
    "city":'Helsinki'
}