#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:28:03 2021

@author: khan
"""

import pandas as pd
import functions
from sklearn.ensemble import RandomForestClassifier
import time 

df = pd.read_excel("Data-book_3p.xlsx")
df.columns = ['age', 'education_level', 'background','programming', 'pepper_review']
new_df = df.copy()

labels = functions.update_column(df, 'pepper_review')
programming = functions.update_column(df, 'programming')
background = functions.update_column(df, 'background')

X = df[['age', 'background', 'programming']].values.tolist() 
y = df['pepper_review'].values.tolist()
#y = [2 if i==3 else i for i in y]

model = RandomForestClassifier(max_depth=5, random_state=0) #Performed best 80.59% 
#if combine(mind little, and mind a lot) then accuracy is 88.8% 
model.fit(X,y)

#available_peppers = int(input("Please input the number of available peppers and press Enter: "))
available_teachers = int(input("Please input the number of available teachers and press Enter: "))

a_t = []; X_test = []
print("\nPlease input teacher's info as follow(comma seperated):")
time.sleep(1)
print("\nName, Age, Education_level, Speciality, Code_literacy")
time.sleep(1)
print("\nFor code literacy Please select one of following:")
print("none: 0, \nmonths: 1, \n1-3 years': 2, \n3-5 years': 3, \n5-10 years': 4, \nmore than 10 years': 5")
time.sleep(1)

for i in range(available_teachers):
    name, age, edu_level, sp, code_l = input("Teacher "+ str(i+1) + ": ").split(",")
    name = name.strip(); age = age.strip(); edu_level = edu_level.strip(); sp = sp.strip(); code_l = code_l.strip();
    a_t.append([name, age, edu_level, sp, code_l])
    X_test.append([int(age), background[sp], int(code_l)])

predictions = model.predict(X_test)
print("\n\n")
assign = 0
for idx, v in enumerate(predictions):
    if v == 1:
        assign+=1
        if X_test[idx][2] == 0:
            print("1 pepper can be assigned to "+ a_t[idx][0])
        elif X_test[idx][2] in [1,2,3]:
            print("2 peppers can be assigned to "+ a_t[idx][0])
        elif X_test[idx][2] in [4,5]:
            print("3 peppers can be assigned to "+ a_t[idx][0])

if assign == 0:
    print("No suitable teacher found")
    






