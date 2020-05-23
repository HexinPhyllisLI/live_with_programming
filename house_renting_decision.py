class Property:
    
    def __init__ (self,price,ct,wt,m,rm,aw):
        #weight=30,30,10,10,5,5,5,5
              # Integer
        self._price = price 
        self._commute = ct# Integer
        self._walk_time = wt      # Integer
        self._mood = m    # Character string
        self._rmate = rm      # Integer
        self._avarage_wc = aw     # Integer
           # Character string
        
    # Your __str__ method goes here:
    def choice(self):
        ct=self._commute      # Integer
        p=self._price     # Integer
        wt=self._walk_time       # Integer
        m=self._mood   
        rm=self._rmate     # Integer
        aw=self._avarage_wc   # Integer
        #ac=self._add_cost  
        w=[30,30,10,5,10,5,10]
        pri=[11111,22222,33333]#modify here with the price with target house
        x=(((sum(pri)/3-p)/((sum(pri)/3)))*w[0]+(30-ct)*w[1]-wt*w[2]+rm*w[3]+m*w[4]+aw*w[5])/sum(w)
        return x

    
# Your client code goes here:#价格、通勤时间、步行时间、心情（空间、绿化、运动光亮、俩桌子）、舍友、人均厕所、额外成本
my_property = Property(1111111,30,0,60+20-10-5,100,100)

print(Property.choice(my_property))