from pandas import Series,DataFrame
import pandas as pd

obj = Series([4,7,-5,3])
print(obj)
data={'state':['ohio','ohio','ohio','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002],'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data)
print(frame)