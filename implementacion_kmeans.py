import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def distancia(p1, p2):
    return math.dist(p1, p2)

def cercanos(puntos, centros, k: int):
    # Se llena una k lista con listas vacias.
    clusters = [] # K listas vacías.
    for _ in range(k):
        clusters.append([])
    # Se encuentra el centro mas cercano a cada punto y se agrega a cada cluster.
    for punto in puntos:
        near_center = 0
        for i in range(1, k):
            other_center = centros[i]
            nearest_center = centros[near_center]
            if (distancia(nearest_center, punto) > distancia(other_center, punto)):
                near_center = i
        clusters[near_center].append(punto)
    return clusters


def centros(clusters):
    clusters_avg = []
    for cluster in clusters:
        xp = 0.0; yp = 0.0
        t = len(cluster)
        for point in cluster:
            (xi, yi) = point
            xp += xi; yp += yi
        avg = [xp / t, yp / t]
        clusters_avg.append(avg)
    return clusters_avg


def kmeans(puntos, k = 3, iter_n = 100):
    # Se obtienen k puntos aleatorios.
    k_indexes = []
    for _ in range(k):
        index = random.randint(0, len(puntos) - 1)
        while index in k_indexes:
            index = random.randint(0, len(puntos) - 1)
        k_indexes.append(index)
    
    # Centros.
    centross = []
    for i in k_indexes:
        centross.append(puntos[i])

    # Se actualizan estos centros 100 veces.
    clusters = cercanos(puntos, centross, k)
    for _ in range(iter_n):
        clusters = cercanos(puntos, centross, k)
        centros_avg = centros(clusters)
        for i in range(len(centros_avg)):
            centross[i] = centros_avg[i]
    return (centross, clusters)


def main():
    df = pd.read_csv("./covid19_tweets.csv")

    var = []
    for i in range(len(df['user_followers'])):
      var.append([df["user_followers"][i], df["user_friends"][i]])


    points = np.array(var)

    (centroides, clusters) = kmeans(points, k = 4, iter_n=100)

    plt.plot( [c[0] for c in clusters[0]], [c[1] for c in clusters[0]], 'r.', label='cluster 1')
    plt.plot( [c[0] for c in clusters[1]], [c[1] for c in clusters[1]], 'b.', label='cluster 2')
    plt.plot( [c[0] for c in clusters[2]], [c[1] for c in clusters[2]], 'g.', label='cluster 3')

    plt.plot( [c[0] for c in centroides], [c[1] for c in centroides],'mo',markersize=8, label='centroides')

    plt.legend(loc='best')
    plt.show()

main()
