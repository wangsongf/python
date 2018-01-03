import pandas as pd # 引用套件並縮寫為 pd

groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]  
num = [46, 8, 12, 12, 6, 58]

dict = {"groups": groups,  
        "num": num
        }


select_df = pd.DataFrame(dict)

select_df.sort_index(axis = 0, ascending = True) # 透過索引值做排序，axis 可以指定第幾欄，ascending 用於設定升冪或降密
print(select_df)