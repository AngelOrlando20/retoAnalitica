from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./covid19_tweets.csv")

# Relacion entre Amistades y Followers.
points = []
for i in range(len(df['user_followers'])):
  points.append([df["user_followers"][i], df["user_friends"][i]])

pnp = np.array(points)
plt.scatter(pnp[:,0],pnp[:,1])

n = 4
k_means = KMeans(n_clusters=n, max_iter=300, tol=1e+1)
k_means.fit(pnp)

centroides = k_means.cluster_centers_
etiquetas = k_means.labels_

plt.plot(pnp[etiquetas==0,0],pnp[etiquetas==0,1],'r.', label='cluster 1')
plt.plot(pnp[etiquetas==1,0],pnp[etiquetas==1,1],'b.', label='cluster 2')
plt.plot(pnp[etiquetas==2,0],pnp[etiquetas==2,1],'g.', label='cluster 3')
plt.plot(pnp[etiquetas==3,0],pnp[etiquetas==3,1],'g.', label='cluster 4')

plt.plot(centroides[:,0],centroides[:,1],'mo',markersize=8, label='centroides')

plt.legend(loc='best')
plt.show()
