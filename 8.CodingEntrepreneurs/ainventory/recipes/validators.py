from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError
#!!!!
#https://docs.djangoproject.com/en/4.0/ref/validators/
import pint

valid_unit_measurements = ['pounds','lbs','ox', 'gram']

def validate_unit_of_measure(value):
    ureg= pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{e}")
    except:
        raise ValidationError(f"{value} is not valid - Unknown error")
    
    # if value not in valid_unit_measurements:
    #     raise ValidationError(f"{value} is not a valid unit of measure")
