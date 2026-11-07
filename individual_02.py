def main() -> None:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c

    print(f"Большее число: {maximum:.6f}")


if __name__ == "__main__":
    main()