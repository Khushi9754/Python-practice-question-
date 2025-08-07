class Demo:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        #print("my name is",self.name,"and my age is",self.age)
        

obj=Demo("khushi",22)
obj2=Demo("monika",24)
obj3=Demo("varsha",26)

l1=[obj,obj2,obj3]
#dic={0:obj,1:obj2,2:obj3}
tu=(obj,obj2,obj3)

for i in l1:
    print(i.name,i.age)

for k in tu:
   print(k.name,k.age)

#isme hum list,dic,tuple me obj de sakte hai or normal list ki tarah access kr sakte hai
