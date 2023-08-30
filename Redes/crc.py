def calculate_crc(data):
    polynomial = 0xEDB88320  # Polinômio divisor CRC-32
    crc = 0xFFFFFFFF

    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
    
    return crc

def main():
    data = input("Digite os dados binários: ")
    data_bytes = [int(data[i:i+8], 2) for i in range(0, len(data), 8)]
    
    crc = calculate_crc(data_bytes)
    crc_binary = format(crc, '032b')  # Formata o CRC-32 como uma string binária de 32 bits
    
    print("Dado de entrada:", data)
    print("Dado com CRC:", data + crc_binary)
    print("Valor do CRC-32:", crc_binary)

if __name__ == "__main__":
    main()
