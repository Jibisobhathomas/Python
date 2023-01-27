class Medicine:
    def __init__(self,MedicineName,batch,disease,price) :
        self.MedicineName=MedicineName
        self.batch=batch
        self.disease=disease
        self.price=price

class Solution(Medicine):
    @classmethod
    def getPriceByDisease(cls,list_med,dis):
        result = []
        for i in list_med:
            if i.disease.lower() == dis.lower():
                result.append(i.price)
        return result

n=int(input())
list_med=[]

for i in range(n):
    MedicineName = input()
    batch = input()
    disease = input()
    price = int(input())

    list_med.append(Medicine(MedicineName,batch,disease,price))
dis = input()
answer = Solution.getPriceByDisease(list_med,dis)

for i in answer:
    print(i)


























