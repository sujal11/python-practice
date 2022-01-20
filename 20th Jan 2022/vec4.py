class Vector:
    def __init__(self, vec):
        self.vec=vec

    def __str__(self):
      return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"    

    def __add__(self,vec3):
        newList= []
        for i in range(len(self.vec)):
          newList.append(self.vec[i]+vec3.vec[i])
        return Vector(newList)

    def __mul__(self,vec4):
        newList2=[]
        for i in range(len(self.vec)):
            newList2.append(self.vec[i]*vec4.vec[i])
        return Vector(newList2)        

v1= Vector([1,2,3])
v2= Vector([4,5,6])
print(v1+v2)
print(v1*v2)