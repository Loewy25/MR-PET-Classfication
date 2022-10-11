#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import pandas as pd  
from datetime import *
import numpy as np


# In[6]:


ImageSize=2
size=0
ImagePath="/Users/liupeiwang/Desktop/ADNIMERGE/"
#ImagePath="/scratch/jjlee/Singularity/ADNI/bids/derivatives/"
images=[]
labels=[]
num_patient=0
file_list=[]
date_data=[]


# Get the file name

file_temp_list = os.listdir(ImagePath)
for i in file_temp_list:
    if "sub" in i:
        file_list.append(i)
        
while size < ImageSize:
    min_date=50
    tolerance=21
    print(num_patient)
    i_id=file_list[num_patient][4:7]+"_S_"+file_list[num_patient][8:12]
    df=pd.read_csv('/Users/liupeiwang/Desktop/ADNIMERGE.csv')
    file_list_date=[]
    iter_date=0
    new_ImagePath=ImagePath+file_list[size]+"/"
    file_temp_list = os.listdir(new_ImagePath)
    for i in file_temp_list:
        if "ses" in i:
            file_list_date.append(i)
    while iter_date < len(file_list_date):
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
            data_diff=abs(data_diff_ob.days)
            if data_diff < min_date:
                min_date = data_diff
                current_date = m
        if min_date <= tolerance:
            data = df[(df["PTID"] == i_id) & (df["EXAMDATE"] == current_date)]
            dx = data["DX"]
            label=dx.values.tolist()[0]
            if (label == "CN" or label == "MCI" or label == "Dementia"):
                new_ImagePath=new_ImagePath+file_list_date[iter_date]+"/pet/"
                file_temp_list = os.listdir(new_ImagePath)
                for i in file_temp_list:
                    if "trc-FDG_proc-CASU_orient-rpi_pet_on_T1w_detJ_Warped_mask_0.1.nii.gz" in i:
                        final_path=new_ImagePath+i
                        labels.append(label)
                        images.append(final_path)
                        size+=1
        iter_date+=1
    num_patient+=1
    print(images)
    print(labels)


# In[ ]:




