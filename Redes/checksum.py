def binaryToHex(binary_str):
    try:
        decimal_num = int(binary_str, 2)  # Converte a string binária para um número decimal.
        hex_checksum = hex(decimal_num)    # Converte o número decimal para hexadecimal.
        return hex_checksum[2:]            # Remove o prefixo '0x' do valor hexadecimal.
    except ValueError:
        return "Entrada inválida."

if __name__ == "__main__":
    input_binary = input("Digite um número binário: ")  # Solicita ao usuário que insira um número binário.
    hex_checksum = binaryToHex(input_binary)           # Chama a função para converter o número binário em hexadecimal.
    
    print(f"Valor hexadecimal correspondente a '{input_binary}': {hex_checksum}")
