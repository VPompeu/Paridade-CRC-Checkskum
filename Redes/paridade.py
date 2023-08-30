def calculate_parity(bits):
    parity_bit = bits[-1]
    data_bits = bits[:-1]
    
    # Count the number of ones in the data bits
    ones_count = data_bits.count('1')
    
    # Determine the expected parity bit based on parity type
    expected_parity_bit = '1' if ones_count % 2 == 0 else '0'
    
    # Check if the parity is correct
    if parity_bit == expected_parity_bit:
        parity_type = "par" if expected_parity_bit == '1' else "ímpar"
        return True, parity_type
    else:
        return False, None

def main():
    max_bits = 100
    binary_input = input(f"Digite um número binário de até {max_bits} bits (incluindo o bit de paridade): ")

    if len(binary_input) > max_bits:
        print("Número de bits excede o limite máximo.")
        return
    
    if not all(bit == '0' or bit == '1' for bit in binary_input):
        print("Entrada inválida. Digite apenas 0s e 1s.")
        return
    
    is_correct, parity_type = calculate_parity(binary_input)

    print("\nNúmero binário digitado:", binary_input)
    print("Bit de paridade:", binary_input[-1])

    if is_correct:
        print(f"A paridade está correta. O bit de paridade {binary_input[-1]} corresponde a um número {parity_type}.")
    else:
        print("A paridade está incorreta.")

if __name__ == "__main__":
    main()
