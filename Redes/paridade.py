def calculate_parity(bits):
    parity_bit = bits[-1]
    data_bits = bits[:-1]
    
    # Conte o número de unidades nos bits de dados;
    ones_count = data_bits.count('1')
    
    # Determine o bit de paridade esperado com base no tipo de paridade;
    expected_parity_bit = '1' if ones_count % 2 == 0 else '0'
    
    # Faz verificação se a paridade está correta;
    if parity_bit == expected_parity_bit:
        parity_type = "ímpar" if expected_parity_bit == '1' else "par"
        return True, parity_type
    else:
        return False, None
    # Aqui termina a verificação;
def main():
    max_bits = 100 #Determina um valor máximo de bits;
    binary_input = input(f"Digite um número binário de até {max_bits} bits (incluindo o bit de paridade): ")

    if len(binary_input) > max_bits: #Verifica se o número de bits digitados não excede o máximo de bits disponível;
        print("Número de bits excede o limite máximo.")
        return
    
    if not all(bit == '0' or bit == '1' for bit in binary_input): #Verificação para aceitar apenas números binários;
        print("Entrada inválida. Digite apenas 0s e 1s.")
        return
    
    is_incorrect, parity_type = calculate_parity(binary_input) #Verifica se a paridade esta correta de acordo com o binário inserido;

    print("\nNúmero binário digitado:", binary_input)
    print("Bit de paridade:", binary_input[-1])

    if is_incorrect:
        print(f"A paridade está errada. O bit de paridade {binary_input[-1]} corresponde a um número {parity_type}.")
    else:
        print("A paridade está correta.")

if __name__ == "__main__":
    main()