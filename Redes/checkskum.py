import sys

def checksum(data):
  """Calculates the checksum of a sequence of bytes."""
  sum = 0
  for byte in data:
    sum += byte
  return sum & 0xFFFF

def main():
  """Transfers at least 4 bytes of data using Checksum."""
  if len(sys.argv) < 2:
    print("Usage: python checksum.py <data>")
    sys.exit(1)

  data = sys.argv[1].encode()
  if len(data) < 4:
    print("Data must be at least 4 bytes long.")
    sys.exit(1)

  checksum = checksum(data)
  print("Data:", data)
  print("Checksum:", checksum)

if __name__ == "__main__":
  main()
