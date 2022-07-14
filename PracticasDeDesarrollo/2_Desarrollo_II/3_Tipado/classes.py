from dataclasses import dataclass


class A:
    def __init__(self, a: int, b: str, c: float):
        self.a = a
        self.b = b
        self.c = c


ia = A(a=1, b=1, c="asdad")


@dataclass
class B:
    a: int
    b: str
    c: float


ib = B(a=1, b=1, c="asdwqe")

print(f"ia: {ia}")
print(f"ib: {ib}")
