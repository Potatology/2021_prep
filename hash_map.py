class HashMap:
    # initialize 2 lists - keys and data with a particular length. 
    # Should be prime number to easier deal with collisions.
    def __init__ (self, size):
        self.size = size
        self.keys = [None] * self.size
        self.data = [None] * self.size

    # get a position of where to put the key and associated data within keys and data
    def hashFn(self, key):
        if key != None:
            return self.size % key
        else: return None

    def rehash(self, oldhashvalue):
        return (oldhashvalue + 1) % self.size

    # inser input key and data into the hash map.
    # if the key exists -> replace existing data with the input data.
    def put(self, key, data):

        def write(hash):
            self.keys[hash] = key
            self.data[hash] = data

        hashvalue = self.hashFn(key)
        # introduce new key and data to the map
        if not self.keys[hashvalue]:
            write(hashvalue)
            
        # otherwise if the hashvalue is occupied and key is different:
        # rehash the hashvalue until the keys[hashvalue] is either empty or equal the key
        # then if it's empty = just put the key and the data there
        # if the key exists = replace the data
        else:
            if self.keys[hashvalue] == key:
                self.data[hashvalue] = data
            else: 
                nextSlot = self.rehash(hashvalue)
                while self.keys[nextSlot]!= key and self.keys[nextSlot] != None:
                    nextSlot = self.rehash(hashvalue)
                    if self.keys[nextSlot] == None:
                        write(nextSlot)
                    else: self.data[nextSlot] = data
    
    # return data for a queried key
    def get(self, key):
        startSlot = self.hashFn(key)
        data, stop, found, position = None, False, False, startSlot
        while self.keys[position] != None and not found and not stop:
            if  self.keys[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.keys))
                if position == startSlot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get
    
    def __setitem__(self, key, data):
        self.put(key, data)


testHash = HashMap(11)
testHash.put(1, 12)
testHash.put(1, 13)
testHash.put(2, 14)
testHash.put(3, 15)
testHash.put(6, 12)
print(testHash.keys)
print(testHash.data)

