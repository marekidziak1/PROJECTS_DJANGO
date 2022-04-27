from fractions import Fraction
from typing import Tuple, Union
#def number_str_to_float(amount_str:str) -> (any, bool):
def number_str_to_float(amount_str: str) -> Tuple[Union[str, float], bool]:
    success =False
    number_as_float = amount_str
    try:
        number_as_float = float(sum(Fraction(s) for s in f"{amount_str}".split()))
    except:
        pass
    if isinstance(number_as_float, float):
        success=True
    return number_as_float, success