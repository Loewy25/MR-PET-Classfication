#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd  
from datetime import *
import numpy as np


# In[2]:


def tolerance():

    size=0
    iter_date=0
    num_patient=0
    data_tolerance=[]
    file_list=[]
    df=pd.read_csv('/Users/liupeiwang/Desktop/ADNIMERGE.csv')
    ImagePath="/Users/liupeiwang/Desktop/ADNIMERGE/"
    file_temp_list = os.listdir(ImagePath)
    for i in file_temp_list:
        if "sub" in i:
            file_list.append(i)
    print(file_list)
     
    while size < len(file_list):
        iter_date=0
        i_id=file_list[num_patient][4:7]+"_S_"+file_list[num_patient][8:12]
        new_ImagePath=ImagePath+file_list[size]+"/"
        file_temp_list = os.listdir(new_ImagePath)
        file_list_date=[]
        for i in file_temp_list:
            if "ses" in i:
                file_list_date.append(i)
        print(file_list_date)
        while iter_date < len(file_list_date):
            date_tolerance=[]
            i=file_list_date[iter_date]
            year=i[4:8]
            month=i[8:10]
            day=i[10:12]
            date_data=year+"-"+month+"-"+day
            date_data=datetime.strptime(date_data, "%Y-%m-%d")
            date_admi = df[(df["PTID"] == i_id)]
            dx = date_admi["EXAMDATE"]
            date_list=dx.values.tolist()
            for m in date_list:
                date_desire=datetime.strptime(m,"%Y-%m-%d")
                data_diff_ob=date_desire-date_data
                data_diff=s=abs(data_diff_ob.days)
                date_tolerance.append(data_diff)
            date_min=min(date_tolerance)
            data_tolerance.append(date_min)
            iter_date+=1
        num_patient+=1
        size+=1
    return data_tolerance

    


# In[3]:


a=tolerance()
result = pd.value_counts(a)
result = result.to_dict()
print(result)


# In[ ]:




