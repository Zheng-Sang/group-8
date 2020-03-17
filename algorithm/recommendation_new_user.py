from recommendation_spend_behavior import Spend_behavior_Prediction
from sklearn import  datasets
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd
import os
import numpy as np
from sklearn.cluster import KMeans

class new_user:
    def __init__(self, id, age, location, product):
        self.age = age
        self.location = location
        self.user_id = id
        self.product_list = product

def cluster(x1,x2,types_num,types,colors,shapes):
    X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)  
    kmeans_model = KMeans(n_clusters=types_num).fit(X) 
    x1_result=[]; x2_result=[]
    for i in range(types_num):
        temp=[]; temp1=[]
        x1_result.append(temp)
        x2_result.append(temp1)
    for i, l in enumerate(kmeans_model.labels_):  
        x1_result[l].append(x1[i])
        x2_result[l].append(x2[i])
        # plt.scatter(x1[i], x2[i], c=colors[l],marker=shapes[l])
    # for i in range(len(list(kmeans_model.cluster_centers_))): 
    #     plt.scatter(list(list(kmeans_model.cluster_centers_)[i])[0],list(list(kmeans_model.cluster_centers_)[i])[1],c=colors[i],marker=shapes[i],label=types[i])

    plt.legend()
    return kmeans_model,x1_result,x2_result

def recommendation_new_user(id, age, location, all_age, all_location, all_product):
    # colors = ['b', 'g', 'r', 'y'] 
    # shapes = ['o', 's', 'D', 'o'] 
    # labels=['A','B','C','D'] 
    model, age_group, location_group = cluster(all_age, all_location, 6,  labels, colors, shapes)
    index = 0
    product_list = []
    result = []
    t1 = []
    for i in range(len(age_group)):
        if age in age_group[i]:
            if age_group[i].index(age) == location_group[i].index(location):
                #find the group
                index = age_group[i].index(age)
                for j in range(len(age_group[i])):
                    if j == index:
                        continue
                    tuple = (age_group[i][j], location_group[i][j])
                    if tuple not in t1:
                    ##sql check product
                        product = []
                        product_list.extend(product)
                        # tuple = (age_group[i][j], location_group[i][j])
                        t1.append(tuple)
                dict = {}
                for key in product_list:
                    dict[key] = dict.get(key, 0) + 1
                # print(dict)
                result_dict = {}
                result_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
                result_dict = result_dict[:50]
                result = list(result_dict.keys())
                # sort_product = sorted(result, key = product[1],reverse = True)
                
                return result
