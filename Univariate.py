class uni:
    qual=[]
    quan=[]  
    def __init__(self,dataset):
        self.dataset=dataset
    def quanqual(self):
        for colname in self.dataset.columns:
            if(self.dataset[colname].dtype=='O'):
                self.qual.append(colname)
            else:
                self.quan.append(colname)
        return self.qual,self.quan


        
    