import struct 
data = open('data.bin', 'rb').read()
print data
l = list(data)
packed = struct.unpack('>i4sh', data)
print packed

