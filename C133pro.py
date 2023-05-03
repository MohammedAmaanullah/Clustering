from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X = []
for index, planet_mass in enumerate(planet_masses):
  temp_list = [planet_radiuses[index],planet_mass]
  X.append(temp_list)
wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i,init='k-means++',random_state = 42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)
plt.figure(figsize=(10,5))
sns.lineplot(x = range(1,11),y = wcss,marker = 'o', color = 'red' )
plt.title('elbow_method')
plt.xlabel('number of clusters')
plt.ylabel('wcss')
plt.show()

planet_masses = []
planet_radiuses = []
planet_types = []
for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_types.append(planet_data[6])
fig = px.scatter(x=planet_radiuses, y = planet_masses, color = planet_types)
fig.show()  