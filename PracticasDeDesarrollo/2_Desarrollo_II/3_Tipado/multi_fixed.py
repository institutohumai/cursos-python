def multi_call(num: int, alt: bool = False) -> int:
    if alt:
        return num * 5
    return num * -2


b = multi_call(23, True)
