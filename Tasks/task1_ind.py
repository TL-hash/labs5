#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "f", "g", "m", "o"}
    b = {"b", "g", "h", "l", "u"}
    c = {"e", "f", "m"}
    d = {"e", "g", "l", "p", "q", "u", "v"}

    x = (a.intersection(c).union(b))
    print(f"x = {x}")

    bn = u.difference(b)

    y = (a.intersection(bn).union(c.difference(d)))
    print(f"y = {y}")