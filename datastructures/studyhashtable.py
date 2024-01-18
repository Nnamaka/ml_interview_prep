# Hashtable class written in python
# other class methods for the hashtable are implemented as well
# ------------------------------------------------------------
# A video may be released on youtube explaining how to code Hashtables 
# with python

# subsequent videos on coding other datastructures will be released too
# my youtube channel : https://www.youtube.com/channel/UCiiY1pXCt0Msao1AFlydAbQ
# The channel focuses on software engineering and machine learning engineering.
# nothing much
# copyright 2024

class HashTable:
    def __init__(self, length=4) -> None:
        self.array = [None] * length

        # 'ball' , 'table' 
        # hash( 'ball' ) ==> 1
        # hash( 'table' ) ==> 1
        # key and key2 are the same

        # [ [], [('ball', value), ('table', value), (key2, value)]  ]
    