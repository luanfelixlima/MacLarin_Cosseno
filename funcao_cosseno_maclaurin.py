def maclaurin_cosseno(x, precisao_desejada):
    import math
    import numpy as np
    from decimal import Decimal

    f = Decimal(0)
    k = 0
    n = 0

    while True:
        if abs(k) % 2 == 0:
            f += ((-1) ** n) * (Decimal(x) ** (2 * n)) / math.factorial(2 * n)
            n += 1

        r = (1 / math.factorial(k + 1)) * math.pow(np.abs(x), k + 1)
        if r <= precisao_desejada:
            break

        k += 1

    return f, k
