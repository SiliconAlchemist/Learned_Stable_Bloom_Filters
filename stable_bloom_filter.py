import mmh3


class stable_bloom_filter(object):
    
    def __init__(m,Mx,K):
        '''
        m: Number of Cells in the bloom filter
        Mx: Maximum value a cell can hold
        K: Number of Hash Functions
        
        Initialises a stable bloom filter
        ''' 
        self.m=m
        self.Mx=Mx
        self.K=K
        
        #calculating other parameters.
        self.P=5
        self.filter=[0]*self.m
        
    def is_duplicate(item):
        '''
        item: input item
        
        returns if the input item is already contained within the filter
        '''
        flag=True
        hashes=get_hashes()
        for i in range(self.K):
            if(hashes[i]==0):
                flag=False

        remove_random_elements()
        add_item(item)
        return flag
    
    def add_element(item):
        '''
        item: input item
        
        Adds an element to the filter by setting all the hash cells to max
        '''
        pass
    
    def remove_random_elements():
        '''
        Decrement random P cells by 1.
        '''
        pass
    
    def get_hashes(item):
        '''
        item: input item
        
        returns K hashes derived from k independent hash functions
        '''
        hashes = []
        
        for i in range(self.K):
            hash_val = mmh3.hash(item, i) % self.N
            hashes.append(hash_val)
        
        return hashes

