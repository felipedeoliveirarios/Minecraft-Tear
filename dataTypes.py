import struct as s

class s_byte:
  data = False
  
  def __init__(self, integer : int):
    # Faz a coerção do valor para a faixa válida do byte
    if integer < -127:
      integer = -127
    elif integer > 128:
      integer = 128
    
    self.data = integer.to_bytes(1, 'sys.byteorder', True)
