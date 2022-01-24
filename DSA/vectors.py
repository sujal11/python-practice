class C2d_vector:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
     
    def __str__(self):
        return f"2D-Vector = {self.icap}i + {self.jcap}j"

class C3d_vector(C2d_vector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.kcap=k

    def __str__(self):
        return f"3D-Vector = {self.icap}i + {self.jcap}j + {self.kcap}k"

C1=C2d_vector(3,6)
C2=C3d_vector(3,6,9)
print(C1)
print(C2)        