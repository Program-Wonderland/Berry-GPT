import phonenumbers
from phonenumbers import carrier

Available = {'86': "China", '852': "Hong Kong", '853': 'Macao', '92': 'Pakistan'}


def check(phone):
    number = phonenumbers.parse(phone)
    if number.country_code in Available.keys():
        if carrier.name_for_number(number, 'en') == '':
            pass
        if number.country_code == Available['Taiwan']:
            return False, ""
        else:
            return True, "Welcome to Berry-GPT!"
    else:
        return False, "The Berry-GPT service is not available in your country or region"


