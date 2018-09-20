def to_str(bytes_or_str):
    '''Takes a str or bytes and always returns a str.'''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_bytes(bytes_or_str):
    '''takes a str or bytes and always returns bytes.'''
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

'''example of a helper function'''
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

'''know how to slice'''
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four:', a[-4:])
print('Middle two', a[3:-3])
assert a[:5] == a[0:5] # leave out the zero index to reduce visual noise
assert a[5:] == a[5:len(a)] #leave out the final index becouse it's reduntant
