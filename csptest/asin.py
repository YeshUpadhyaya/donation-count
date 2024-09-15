import docx2txt as d2t
dfile='DEN3-Adams 12 Five Star Schools-Donations-08_18_2022.docx'

asinNum=[]
doc=d2t.process(dfile)
num=0

for x in doc:
    
    x = doc[num:num+2]
    if x=='B0':
        asinNum.append(doc[num:num+10])

    num+=1

amountNum=[]
num=0
for z in doc:
    if z.isnumeric() and doc[num-1:num] == '\n':
        num2=num
        
        while doc[num2:num+1]!='\n' and doc[num2:num+1].isnumeric():
            num2+=1
            
        amountNum.append(doc[num:num2])    
    num+=1

print(amountNum)







