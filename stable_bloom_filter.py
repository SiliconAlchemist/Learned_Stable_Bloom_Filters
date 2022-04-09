import mmh3
from random import sample


class stable_bloom_filter(object):
    
    def __init__(self,m,Mx,K):
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
        
    def is_duplicate(self,item):
        '''
        item: input item
        
        returns if the input item is already contained within the filter
        '''
        flag=True
        hashes=self.get_hashes(item)
        for i in range(self.K):
            if(self.filter[hashes[i]]==0):
                flag=False

        self.remove_random_elements()
        self.add_element(hashes)
        return flag
    
    def add_element(self,hashes):
        '''
        hashes: keys by K hash functions
        Adds an element to the filter by setting all the hash cells to max
        '''
        for i in range(self.K):
            self.filter[hashes[i]]=self.Mx
        
    
    def remove_random_elements(self):
        '''
        Decrement random P cells by 1.
        '''
        cell_ind=[i for i in range(self.m)]
        rem_ind=sample(cell_ind,self.P)
        for i in rem_ind:
            self.filter[i]=max(0,self.filter[i]-1)
    
    def get_hashes(self,item):
        '''
        item: input item
        
        returns K hashes derived from k independent hash functions
        '''
        hashes = []
        
        for i in range(self.K):
            hash_val = mmh3.hash(item, i) % self.m
            hashes.append(hash_val)
        
        return hashes

if __name__=="__main__":
    sbf=stable_bloom_filter(10,3,2)
    while(True):
        item=input()
        print(sbf.is_duplicate(item))