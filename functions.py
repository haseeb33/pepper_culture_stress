#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:58:34 2021

@author: khan
"""
import matplotlib.pyplot as plt
import numpy as np
from operator import add
import graphviz

def update_column(df, col):
    labels = list(df[col].unique())
    labels_dict = {}
    for idx, val in enumerate(labels):
        labels_dict[val] = idx+1
    if col=='programming':
        labels_dict = {'none': 0,'months': 1,'1-3 years': 2,'3-5 years': 3,
                       '5-10 years': 4,'more than 10 years': 5}
    df[col] = df[col].apply(lambda x: labels_dict[x])
    return labels_dict

def age_bar_graph(df):
    ages = sorted(df.age.unique())
    df_age_sort = df.sort_values(by=['age'])
    
    dont_mind = [0 for i in range(len(ages))]
    mind_little = [0 for i in range(len(ages))]
    mind_lot = [0 for i in range(len(ages))]
    
    for index, row in df_age_sort.iterrows():
        if row['pepper_review'] == 'not mind':
            dont_mind[ages.index(row['age'])]+=1
        elif row['pepper_review'] == 'mind a little':
            mind_little[ages.index(row['age'])]+=1
        elif row['pepper_review'] == 'mind a lot':
            mind_lot[ages.index(row['age'])]+=1
        else:
            None
    
    ind = np.arange(len(ages)); width = 0.55      
    
    p1 = plt.bar(ind, dont_mind, width)
    p2 = plt.bar(ind, mind_little, width, bottom=dont_mind)
    p3 = plt.bar(ind, mind_lot, width, bottom=list(map(add, dont_mind, mind_little)))
    
    plt.ylabel('Number of teachers')
    plt.xlabel('Age of teachers')
    plt.title('Culture stress by Age')
    plt.xticks(ind, ages, fontsize=5)
    #plt.yticks(np.arange(0, 17, 1))
    plt.legend((p1[0], p2[0], p3[0]), ('Absent', 'Negligible', 'Acute'))
    
    plt.savefig('age_acceptance_rate.pdf')
    plt.show()
    
def overall_age_bar_graph(df):
    ages = ['25-30', '31-35', '36-40', '41-45', '46-50', '51-55', '56-60', '61-65']
    ages_num = [[25,26,27,28,29,30], [31,32,33,34,35], [36,37,38,39,40], [41,42,43,44,45],
                [46,47,48,49,50], [51,52,53,54,55], [56,57,58,59,60], [61,62,63,64,65]]
    df_age_sort = df.sort_values(by=['age'])
    
    dont_mind = [0 for i in range(len(ages))]
    mind_little = [0 for i in range(len(ages))]
    mind_lot = [0 for i in range(len(ages))]
    
    for index, row in df_age_sort.iterrows():
        idx = [i for i, val in enumerate(ages_num) for j in val if j==row['age']][0]    
        if row['pepper_review'] == 'not mind':
            dont_mind[idx]+=1
        elif row['pepper_review'] == 'mind a little':
            mind_little[idx]+=1
        elif row['pepper_review'] == 'mind a lot':
            mind_lot[idx]+=1
        else:
            None
     
    ind = np.arange(len(ages)); width = 0.55      
    
    p1 = plt.bar(ind, dont_mind, width)
    p2 = plt.bar(ind, mind_little, width, bottom=dont_mind)
    p3 = plt.bar(ind, mind_lot, width, bottom=list(map(add, dont_mind, mind_little)))
    
    plt.ylabel('Number of teachers')
    plt.xlabel('Age of teachers')
    plt.title('Culture stress by Age range')
    plt.xticks(ind, ages)
    #plt.yticks(np.arange(0, 28, 4))
    plt.legend((p1[0], p2[0], p3[0]), ('Absent', 'Negligible', 'Acute'))
    
    plt.savefig('overall_age_acceptance_rate.pdf')
    plt.show()
    return dont_mind, mind_little, mind_lot
    
def programming_bar_graph(df):
    programming_dict = {'none':0, 'months':1, '1-3 years':2, '3-5 years':3, 
                        '5-10 years':4, 'more than 10 years':5}
    programming_list = ['none', 'months', '1-3 years', '3-5 years', 
                        '5-10 years', 'more than 10 years']
    
    df['programming'] = df['programming'].apply(lambda x: programming_dict[x])
    
    experience = sorted(df.programming.unique())
    df_experience_sort = df.sort_values(by=['programming'])
    
    dont_mind = [0 for i in range(len(experience))]
    mind_little = [0 for i in range(len(experience))]
    mind_lot = [0 for i in range(len(experience))]
    
    for index, row in df_experience_sort.iterrows():
        if row['pepper_review'] == 'not mind':
            dont_mind[experience.index(row['programming'])]+=1
        elif row['pepper_review'] == 'mind a little':
            mind_little[experience.index(row['programming'])]+=1
        elif row['pepper_review'] == 'mind a lot':
            mind_lot[experience.index(row['programming'])]+=1
        else:
            None
            
    ind = np.arange(len(experience)); width = 0.55      
    
    p1 = plt.bar(ind, dont_mind, width)
    p2 = plt.bar(ind, mind_little, width, bottom=dont_mind)
    p3 = plt.bar(ind, mind_lot, width, bottom=list(map(add, dont_mind, mind_little)))
    
    plt.ylabel('Number of teachers')
    plt.xlabel('Coding Literacy of teachers')
    plt.title('Culture stress by Coding Literacy')
    plt.xticks(ind, programming_list, fontsize=6)
    #plt.yticks(np.arange(0, 31, 5))
    plt.legend((p1[0], p2[0], p3[0]), ('Absent', 'Negligible', 'Acute'))
    
    plt.savefig('programming_acceptance_rate.pdf')
    plt.show()
    
def education_level_graph(df):
    programming_dict = {'2 years college':0, 'university':1, 'master':2}
    
    programming_list = ['2 years college', 'university', 'master']
    
    df['education_level'] = df['education_level'].apply(lambda x: programming_dict[x])
    
    experience = sorted(df.education_level.unique())
    df_experience_sort = df.sort_values(by=['education_level'])
    
    dont_mind = [0 for i in range(len(experience))]
    mind_little = [0 for i in range(len(experience))]
    mind_lot = [0 for i in range(len(experience))]
    
    for index, row in df_experience_sort.iterrows():
        if row['pepper_review'] == 'not mind':
            dont_mind[experience.index(row['education_level'])]+=1
        elif row['pepper_review'] == 'mind a little':
            mind_little[experience.index(row['education_level'])]+=1
        elif row['pepper_review'] == 'mind a lot':
            mind_lot[experience.index(row['education_level'])]+=1
        else:
            None
            
    ind = np.arange(len(experience)); width = 0.55      
    
    p1 = plt.bar(ind, dont_mind, width)
    p2 = plt.bar(ind, mind_little, width, bottom=dont_mind)
    p3 = plt.bar(ind, mind_lot, width, bottom=list(map(add, dont_mind, mind_little)))
    
    plt.ylabel('Number of teachers')
    plt.xlabel('Education level of teachers')
    plt.title('Culture stress by Education level')
    plt.xticks(ind, programming_list, fontsize=6)
    #plt.yticks(np.arange(0, 31, 5))
    plt.legend((p1[0], p2[0], p3[0]), ('Absent', 'Negligible', 'Acute'))
    
    plt.savefig('education_level.pdf')
    plt.show()
    
def study_background(df):
    degree_list = list(df.background.unique())
    degree_dict = {}
    for idx, val in enumerate(degree_list):
        degree_dict[val] = idx+1
    
    df['background'] = df['background'].apply(lambda x: degree_dict[x])
    
    experience = sorted(df.background.unique())
    df_experience_sort = df.sort_values(by=['background'])
    
    dont_mind = [0 for i in range(len(experience))]
    mind_little = [0 for i in range(len(experience))]
    mind_lot = [0 for i in range(len(experience))]
    
    for index, row in df_experience_sort.iterrows():
        if row['pepper_review'] == 'not mind':
            dont_mind[experience.index(row['background'])]+=1
        elif row['pepper_review'] == 'mind a little':
            mind_little[experience.index(row['background'])]+=1
        elif row['pepper_review'] == 'mind a lot':
            mind_lot[experience.index(row['background'])]+=1
        else:
            None
            
    ind = np.arange(len(experience)); width = 0.55      
    
    p1 = plt.bar(ind, dont_mind, width)
    p2 = plt.bar(ind, mind_little, width, bottom=dont_mind)
    p3 = plt.bar(ind, mind_lot, width, bottom=list(map(add, dont_mind, mind_little)))
    
    plt.ylabel('Number of teachers')
    plt.xlabel('Speciality of teachers')
    plt.title('Culture stress by Speciality')
    plt.xticks(ind, degree_list, rotation=50, fontsize=5)
    #plt.yticks(np.arange(0, 31, 5))
    plt.legend((p1[0], p2[0], p3[0]), ('Absent', 'Negligible', 'Acute'))
    
    plt.savefig('speciality.pdf', bbox_inches='tight')
    plt.show()
    
def generate_tree_graph(model): #only for decision tree model
    dot_data = tree.export_graphviz(model, out_file=None, feature_names=['age', 'programming', 'background'], 
                                    class_names=['Absent', 'Negligible', 'Acute'], filled=True, 
                                    rounded=True, special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render("dummy_tree")
