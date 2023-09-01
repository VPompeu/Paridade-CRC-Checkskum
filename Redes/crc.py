import zlib

# Define uma função chamada calculate_crc32 que recebe dados como entrada.
def calculate_crc32(data):
    crc32_value = zlib.crc32(data)  # Calcula o valor CRC32 dos dados usando a função da biblioteca zlib.
    return crc32_value & 0xFFFFFFFF  # Retorna o valor CRC32, garantindo que ele seja um número positivo de 32 bits.

# Solicita ao usuário que digite um número binário como uma string e armazena a entrada na variável user_input.
user_input = input("Digite um número binário: ")

# Verifica se a entrada do usuário é um número binário válido.
if not all(bit in '01' for bit in user_input):
    print("Entrada inválida. Certifique-se de que você digitou um número binário válido.")
else:
    # Converte a entrada do usuário em uma sequência de bytes usando a codificação UTF-8.
    data = int(user_input, 2).to_bytes((len(user_input) + 7) // 8, byteorder='big')

    # Calcula o valor CRC32 para os dados convertidos e armazena o resultado na variável crc32_result.
    crc32_result = calculate_crc32(data)

    # Imprime o resultado do valor CRC32 formatado como hexadecimal com 8 caracteres.
    print(f"CRC32: {crc32_result:08X}")
    