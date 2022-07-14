def multi_call(num, alt: bool = False):
    if alt:
        return num * 5
    return num * -2


b = multi_call(23, "alt")


def multi_call_control(num: int, alt: bool = False) -> int:
    assert isinstance(num, int), f"Invalid type :{type(num)}"
    if alt:
        return num * 5
    return num * -2


# print(multi_call_control(3.5)) # Descomentar esto para que salte la excepción
