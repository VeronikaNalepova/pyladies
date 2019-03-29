otazky = ["Kdo?", "Kdy?"]

val=[]
key=[]

for a in range(2):
    for i in otazky:
        odpoved =  input(i)
        val.append(odpoved)
        key.append(i)



slovník = dict([(key, val) for key in key])
print(slovník)
