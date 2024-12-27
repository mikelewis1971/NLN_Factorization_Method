import math
from typing import List, Set
from concurrent.futures import ThreadPoolExecutor, as_completed


def decimal_to_binary(n: int) -> str:
    """
    Converts a decimal number to its binary representation without the '0b' prefix.
    """
    return bin(n)[2:]


def binary_to_decimal(b: str) -> int:
    """
    Converts a binary string to its decimal equivalent.
    """
    return int(b, 2)


def circular_shift_left(b: str, k: int) -> str:
    """
    Performs a circular left shift on the binary string by k positions.
    """
    k = k % len(b)  # Normalize shift amount
    return b[k:] + b[:k]


def circular_shift_right(b: str, k: int) -> str:
    """
    Performs a circular right shift on the binary string by k positions.
    """
    k = k % len(b)  # Normalize shift amount
    return b[-k:] + b[:-k]


def shave_bits(b: str, num_bits: int) -> List[str]:
    """
    Removes the specified number of leading bits from the binary string.
    Returns a list of shaved binary strings.
    """
    shaved = []
    for i in range(1, num_bits + 1):
        shaved_version = b[i:]
        if shaved_version:  # Ensure it's not empty
            shaved.append(shaved_version)
    return shaved


def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def process_shift(n: int, binary_n: str, direction: str, k: int) -> Set[int]:
    """
    Performs a circular shift operation and checks if the shifted number is a factor.
    If so, returns the factor.
    """
    if direction == 'left':
        shifted = circular_shift_left(binary_n, k)
    elif direction == 'right':
        shifted = circular_shift_right(binary_n, k)
    else:
        raise ValueError("Invalid shift direction. Choose 'left' or 'right'.")

    shifted_decimal = binary_to_decimal(shifted)

    # Avoid trivial factors
    if shifted_decimal == 0 or shifted_decimal == n:
        return set()

    if n % shifted_decimal == 0:
        return {shifted_decimal}
    return set()


def process_shave(n: int, binary_shifted: str, num_bits: int) -> Set[int]:
    """
    Performs shave operations on a shifted binary string and checks for factors.
    If a shaved number is a factor, returns the factor.
    """
    shaved_binaries = shave_bits(binary_shifted, num_bits)
    factors = set()
    for shaved in shaved_binaries:
        shaved_decimal = binary_to_decimal(shaved)
        if shaved_decimal == 0:
            continue
        if n % shaved_decimal == 0:
            factors.add(shaved_decimal)
    return factors


def shift_and_shave(n: int, depth: int = 0, visited: Set[int] = None) -> Set[int]:
    """
    Recursively applies shift-and-shave operations to find all factors of n.
    Utilizes parallel processing for shift operations.
    """
    if visited is None:
        visited = set()
    factors_found = set()

    if n in visited:
        return factors_found
    visited.add(n)

    binary_n = decimal_to_binary(n)
    num_bits = len(binary_n)

    # Define shift parameters
    shift_directions = ['left', 'right']
    shift_positions = range(1, num_bits)  # Shift by 1 to (num_bits -1) positions

    # Use ThreadPoolExecutor for parallel shift operations
    with ThreadPoolExecutor() as executor:
        future_to_shift = {
            executor.submit(process_shift, n, binary_n, direction, k): (direction, k)
            for direction in shift_directions
            for k in shift_positions
        }

        for future in as_completed(future_to_shift):
            shift_direction, shift_k = future_to_shift[future]
            try:
                shifted_factors = future.result()
                if shifted_factors:
                    factors_found.update(shifted_factors)
            except Exception as exc:
                print(f"Shift {shift_direction} by {shift_k} generated an exception: {exc}")

    # Process shave operations on shifted numbers
    with ThreadPoolExecutor() as executor:
        future_to_shave = {
            executor.submit(process_shave, n, decimal_to_binary(factor), len(decimal_to_binary(factor)) - 1): factor
            for factor in factors_found
        }

        for future in as_completed(future_to_shave):
            factor = future_to_shave[future]
            try:
                shaved_factors = future.result()
                for shaved_factor in shaved_factors:
                    if is_prime(shaved_factor):
                        factors_found.add(shaved_factor)
                    else:
                        # Recursive decomposition
                        factors_found.update(shift_and_shave(shaved_factor, depth + 1, visited))
            except Exception as exc:
                print(f"Shave on factor {factor} generated an exception: {exc}")

    return factors_found



def factorize(n: int) -> List[int]:
    """
    Returns the list of prime factors of n using the shift-and-shave method.
    """
    if n <= 1:
        return []
    factors = shift_and_shave(n)
    # Include n itself if it's prime
    if is_prime(n):
        factors.add(n)
    # Return sorted list of unique prime factors
    return sorted(factors)


if __name__ == "__main__":
    number = 10376
    print(f"Factoring {number} using shift-and-shave method:")
    prime_factors = factorize(number)
    print(f"Prime Factors: {prime_factors}")


    def debug_shift_and_shave(n: int):
        """
        Debugging function to trace the steps of the shift-and-shave process.
        """
        visited = set()
        binary_n = decimal_to_binary(n)
        num_bits = len(binary_n)
        shift_directions = ['left', 'right']
        shift_positions = range(1, num_bits)

        print(f"Debugging shift-and-shave for number: {n} (binary: {binary_n})")

        # Shift operations
        for direction in shift_directions:
            for k in shift_positions:
                if direction == 'left':
                    shifted = circular_shift_left(binary_n, k)
                else:
                    shifted = circular_shift_right(binary_n, k)
                shifted_decimal = binary_to_decimal(shifted)
                print(f"Shift {direction} by {k}: {shifted} -> {shifted_decimal}")
                if shifted_decimal != 0 and shifted_decimal != n and n % shifted_decimal == 0:
                    print(f"Found factor from shift: {shifted_decimal}")

        # Shave operations
        for k in range(1, num_bits):
            shaved_binaries = shave_bits(binary_n, k)
            for shaved in shaved_binaries:
                shaved_decimal = binary_to_decimal(shaved)
                print(f"Shave {k} bits: {shaved} -> {shaved_decimal}")
                if shaved_decimal != 0 and n % shaved_decimal == 0:
                    print(f"Found factor from shave: {shaved_decimal}")


    # Debug the factorization of 9106
    debug_shift_and_shave(number)


    def streamlined_factorize(n: int) -> List[int]:
        """
        Streamlined factorization focusing on efficiency and direct decomposition into prime factors.
        """
        factors = []
        stack = [n]

        while stack:
            current = stack.pop()
            if is_prime(current):
                factors.append(current)
            else:
                # Try to find a factor
                found_factor = None
                for i in range(2, int(math.sqrt(current)) + 1):
                    if current % i == 0:
                        found_factor = i
                        break

                if found_factor:
                    stack.append(found_factor)
                    stack.append(current // found_factor)
                else:
                    # If no factors are found, treat it as prime
                    factors.append(current)

        return sorted(factors)


    # Test the streamlined factorization
    streamlined_factors = streamlined_factorize(number)
    print(streamlined_factors)
