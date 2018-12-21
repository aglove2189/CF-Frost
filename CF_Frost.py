# -*- coding: utf-8 -*-
import random


def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0


def generate_amex():
    """
    Generates a random American Express credit card number
    that satisfies a Luhn check.
    """
    nums = [3, random.choice([4, 7])] + [random.randint(1, 9) for x in range(12)]
    for i in range(10):
        candidate = "".join(map(str, nums)) + str(i)
        if luhn(candidate):
            return candidate


def amex_card():
    ll = [
        "╔════════════════════╗",
        "║  AMERICAN EXPRESS  ║",
        "║                    ║",
        "║                    ║",
        "║   {}  ║".format(generate_amex()),
        "║                    ║",
        "╚════════════════════╝",
    ]

    for l in ll:
        print(l)


if __name__ == "__main__":
    amex_card()
