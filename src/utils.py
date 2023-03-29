"""Módulo de utilidades."""

def fibonacci(i: int) -> int:
    """
    Función que realiza la secuencia Fibonacci.

    Args:
    ----------
    n: int.
        Índice de la secuencia que desea hallar.

    Returns:
    ----------
    int.
        Valor de dicho índice.
    """
    assert i >= 0 and isinstance(i, int), f"{i} debe ser un entero positivo."

    if i in (0, 1):
        return i

    return fibonacci(i - 1) + fibonacci(i - 2)
