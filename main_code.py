import csv
import pandas as pd
import statistics as stats
import random
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()

mean=stats.mean(data)
std_dev=stats.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = stats.mean(dataset)
    return mean

meanList=[]

for i in range(0,1000):
  mean_sample=random_set_of_mean(100)
  meanList.append(mean_sample)

mean_list=stats.mean(meanList)
std_dev_list=stats.stdev(meanList)

first_std_deviation_start, first_std_deviation_end = mean-std_dev, mean+std_dev
second_std_deviation_start, second_std_deviation_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_dev), mean+(3*std_dev)

df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = stats.mean(data)
fig=ff.create_distplot([meanList],["Math_score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


print("MEAN : - ",mean_list)
print("STANDARD DEVIATION : - ",std_dev_list)
print("Mean is :- ",mean)
print("Standard deviation is :- ",std_dev)
print("std 1 :-- ",first_std_deviation_start, first_std_deviation_end)
print("std 2 :-- ",second_std_deviation_start, second_std_deviation_end)
print("std 3 :-- ",third_std_deviation_start,third_std_deviation_end)