import math
import sys


def main() -> None:
    x = float(input("x: "))

    eps = 1e-10
    max_terms = 1000

    n = 0
    term = 1.0
    total = term

    while abs(term) > eps:
        if n >= max_terms:
            print("Превышен предел числа членов ряда", file=sys.stderr)
            sys.exit(1)

        n += 1
        term *= x / n
        total += term

    reference = math.exp(x)

    print(f"f({x}) = {total:.10f}")
    print(f"Членов ряда: {n + 1}")
    print(f"Оценка остатка: {abs(term):.3e}")
    print(f"Эталонное значение math.exp: {reference:.10f}")
    print(f"Разность: {abs(total - reference):.3e}")


if __name__ == "__main__":
    main()