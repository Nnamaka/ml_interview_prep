# Hashtable class written in python
# other class methods for thte hashtable are implemented as well

class HashTable:
    def __init__(self, length=4) -> None:
        self.array = [None] * length

        # 'ball' , 'table' 
        # hash( 'ball' ) ==> 1
        # hash( 'table' ) ==> 1
        # key and key2 are the same

        # [ [], [('ball', value), ('table', value), (key2, value)]  ]
    