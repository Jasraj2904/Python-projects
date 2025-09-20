setx = {'blue' , 'yellow'}
sety = {'blue' , 'green'}
seta = setx.union(sety)
setb = setx.difference(sety)
setc = setx.symmetric_difference(sety)
setz = setx.intersection(sety)
print(setz)
print(seta)
print(setb)
print(setc)