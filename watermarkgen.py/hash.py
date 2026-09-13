import hmac
import hashlib

def hasher(input_array,max_x, max_y, key): #key based deterministic hashing
    input_str = "".join([str(element) for element in input_array]).encode()
    
    code = key.encode()
    hash_value = hmac.new(code,input_str, hashlib.sha256).hexdigest()
    
    position_x = (int(hash_value[8:16], 16)) % max_x #gives x integer value within boundaries of block
    position_y = (int(hash_value[:8],16)) % max_y #gives y integer value within boundaries of block

    return position_x, position_y
