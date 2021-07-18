"""
Just in case if binary is confusing

block_0 = block_read() # 1234567890
read(1) # 1
read(3) # 234
read(5) # 56789
read(3) # Out of range
"""

class Read():
    prev_read_pos = 1

    def __init__(self, block):
        self.block = block

    def block_read(self, n):
        current_read_pos = 0
        block_str = str(self.block)
        while self.prev_read_pos < len(block_str):
            if n == 1:
                print(block_str[self.prev_read_pos-1])
                self.prev_read_pos+=n
                break
            else:
                print("prev",self.prev_read_pos)
                current_read_pos = self.prev_read_pos + n
                print(block_str[self.prev_read_pos-1:current_read_pos-1])
                self.prev_read_pos += n
                break
        else:
            print("Out of range")

checking = Read(12)
checking.block_read(1)
checking.block_read(3)
checking.block_read(5)
checking.block_read(3)
#print(checking.)









