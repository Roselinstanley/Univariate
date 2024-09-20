class univar:
    quan=[]
    qual=[]
    def __init__(self,dataset):
        self.dataset=dataset
    def quanqual(self):
        for cname in self.dataset.columns:
            if(self.dataset[cname].dtype=='O'):
                self.qual.append(cname)
            else:
                self.quan.append(cname)             
        return self.qual,self.quan
                
                
                
    
    
