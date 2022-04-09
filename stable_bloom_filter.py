class stable_bloom_filter(object):
    
    def __init__(N,Mx,K):
        '''
        N: Number of Cells in the bloom filter
        Mx: Maximum value a cell can hold
        K: Number of Hash Functions
        
        Initialises a stable bloom filter
        '''
        
        self.N=N
        self.Mx=Mx
        self.K=K
        
        #calculating other parameters.
        self.P=5
        
    def is_duplicate(item):
        '''
        item: input item
        
        returns if the input item is already contained within the filter
        '''
        pass
    
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
    
    def get_hashes():
        '''
        item: input item
        
        returns K hashes derived from k independent hash functions
        '''
        pass