import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)
file = open('data.bin', 'wb')
file.write(packed)

file.close()
