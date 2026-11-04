"""Build partitions for S(8), S(11) and S(13) from schur6-538.word and check them directly.

S(8) >= 5382:      the width-10 shifted template of Bengone et al., Table II, applied to the word.
S(11) >= 204588:   the width-380 template of Ageron et al., Table 7, Theorem 2.3, applied to the word.
S(13) >= 2045882:  the width-10 shifted template applied to the partition for S(11).

Each partition is a list c with c[n] the colour of n, for 1 <= n <= N. The check uses one
bit mask M for each colour: x, y and x + y all have the colour of M exactly when bit x of M
is set and M and M << x have the common bit x + y.
"""
import pathlib

# Bengone et al., Table II. Its row L is the same as its row M, so row M serves both.
ROW_F = ["B", "A", "P0", "P0", "B", "A", "A", "B", "P0", "P0"]
ROW_M = ["P-1", "B", "P0", "P0", "B", "A", "A", "B", "P0", "P0"]

# Ageron et al., Table 7, colours 1 to 5. Colour 6 is the special colour: all other u in 1..380.
TEMPLATE_380 = {
    1: [1, 5, 8, 11, 15, 17, 29, 33, 36, 39, 43, 57, 61, 88, 92, 106, 110, 113, 116, 120, 132, 134, 138, 141, 144,
        148, 150, 154, 157, 160, 164, 178, 182, 185, 188, 341, 344, 347, 351, 365, 369, 372, 375, 379],
    2: [2, 9, 13, 16, 20, 23, 24, 27, 28, 31, 34, 35, 38, 42, 45, 49, 53, 60, 67, 71, 78, 82, 89, 96, 100, 104, 107,
        111, 114, 115, 118, 121, 122, 125, 126, 129, 133, 136, 140, 147, 158, 162, 165, 169, 172, 176, 183, 187, 194,
        201, 328, 335, 342, 346, 353, 357, 360, 364, 367, 371],
    3: [3, 4, 12, 14, 19, 25, 30, 32, 40, 41, 47, 48, 58, 91, 101, 102, 108, 109, 117, 119, 124, 130, 135, 137, 145,
        146, 152, 153, 161, 163, 168, 179, 181, 190, 339, 348, 350, 361, 366, 368, 376, 377],
    4: [6, 7, 10, 18, 21, 22, 26, 37, 46, 50, 51, 54, 65, 70, 79, 84, 95, 98, 99, 103, 112, 123, 127, 128, 131, 139,
        142, 143, 151, 155, 156, 159, 167, 170, 171, 175, 186, 343, 354, 358, 359, 362, 370, 373, 374, 378],
    5: [44, 52, 55, 56, 59, 62, 63, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 80, 81, 83, 85, 86, 87, 90, 93, 94, 97,
        105, 189, 196, 197, 200, 203, 206, 207, 209, 214, 219, 231, 298, 310, 315, 320, 322, 323, 326, 329, 332, 333,
        340],
}


def shifted_template(g):
    """Colouring of 1..10p+2 with two more colours, from the colouring g of 1..p."""
    p = len(g) - 1
    a, b = max(g[1:]) + 1, max(g[1:]) + 2
    named = {"A": a, "B": b}
    c = [0]
    for row in range(1, p + 1):
        for label in ROW_F if row == 1 else ROW_M:
            if label == "P0":
                c.append(g[row])
            elif label == "P-1":
                c.append(g[row - 1])
            else:
                c.append(named[label])
    return c + [a, b]


def template_380(g):
    """Colouring of 1..380p+148 with five more colours, from the colouring g of 1..p."""
    p = len(g) - 1
    f = {}
    for colour, values in TEMPLATE_380.items():
        for u in values:
            if u in f:
                raise ValueError(f"{u} is in two colours of the template")
            f[u] = colour
    if min(u for u in range(1, 381) if u not in f) != 149:
        raise ValueError("the special colour must start at 149")
    top = max(g[1:])
    c = [0]
    for n in range(1, 380 * p + 148 + 1):
        row, u = (n - 1) // 380 + 1, (n - 1) % 380 + 1
        c.append(top + f[u] if u in f else g[row])
    return c


def check(c, n_expected, k_expected):
    n = len(c) - 1
    colours = sorted(set(c[1:]))
    if n != n_expected or len(colours) != k_expected:
        raise ValueError(f"wrong size or colour count: {n}, {colours}")
    masks = dict.fromkeys(colours, 0)
    for x in range(1, n + 1):
        masks[c[x]] |= 1 << x
    for x in range(1, n // 2 + 1):
        m = masks[c[x]]
        if m & (m << x) != 0:
            raise ValueError(f"monochromatic x + y = z with x = {x}")
    print(f"{k_expected} colours, 1 to {n}: no monochromatic x + y = z")


w = pathlib.Path(__file__).with_name("schur6-538.word").read_text().strip()
g6 = [0] + [int(letter) for letter in w]
check(g6, 538, 6)
check(shifted_template(g6), 5382, 8)
g11 = template_380(g6)
check(g11, 204588, 11)
check(shifted_template(g11), 2045882, 13)
