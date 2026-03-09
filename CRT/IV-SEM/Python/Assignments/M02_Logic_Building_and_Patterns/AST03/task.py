def sum_of_digits(n: int) -> int:
    s = 0
    for d in str(n):
        s += int(d)
    return s

if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))
