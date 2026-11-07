def main() -> None:
    total = 0

    for number in range(21, 100):
        if number % 3 == 0:
            total += number

    print(f"Сумма: {total}")


if __name__ == "__main__":
    main()