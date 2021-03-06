import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import csv


# Get the KDE values for the tree data 
tree_path = '/Volumes/USB20FD/Spring2017/Visualization/Project/Project_Data/2015_Street_Tree_Census_-_Tree_Data.csv'

tree_df = pd.read_csv(tree_path, usecols=['latitude', 'longitude'])
tree_latitudes = tree_df.latitude.tolist()
tree_longitudes = tree_df.longitude.tolist()

xmint, xmaxt = min(tree_latitudes), max(tree_latitudes)
ymint, ymaxt = min(tree_longitudes), max(tree_longitudes)

X_tree, Y_tree = np.mgrid[xmint:xmaxt:50j, ymint:ymaxt:50j]
positionst = np.vstack([X_tree.ravel(), Y_tree.ravel()])
valuest = np.vstack([tree_latitudes, tree_longitudes])
kernelt = stats.gaussian_kde(valuest)
Z_tree = np.reshape(kernelt(positionst).T, X_tree.shape)

'''
fig = plt.figure()
fig.set_size_inches(30, fig.get_figwidth(), forward=True)
ax = fig.add_subplot(111)
ax.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r,extent=[xmin, xmax, ymin, ymax])
ax.plot(latitudes, longitudes, 'k.', markersize=2)
ax.set_xlabel("Latitude")
ax.set_ylabel("Longitude")
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
ax.set_title("KDE of Tree Data")
plt.show()
'''

# Get the KDE values for the air Quality Complaints
air_path = '/Volumes/USB20FD/Spring2017/Visualization/Project/Project_Data/Air_Quality_Complaints.csv'
sr = range(1, 222)
fieldsa = ['Latitude', 'Longitude', 'Incident Zip']
air_df = pd.read_csv(air_path, usecols=fieldsa, skiprows=list(sr), nrows=207)
air_latitudes = air_df.Latitude.tolist()
air_longitudes = air_df.Longitude.tolist()

xmina, xmaxa = min(air_latitudes), max(air_latitudes)
ymina, ymaxa = min(air_longitudes), max(air_longitudes)


X_air, Y_air = np.mgrid[xmina:xmaxa:50j, ymina:ymaxa:50j]
X_air[np.isnan(X_air)] = 0
Y_air[np.isnan(Y_air)] = 0
positionsa = np.vstack([X_air.ravel(), Y_air.ravel()])
positionsa[np.isnan(positionsa)] = 0
valuesa = np.vstack([air_latitudes, air_longitudes])
valuesa[np.isnan(valuesa)] = 0
kernela = stats.gaussian_kde(valuesa)
Z_air = np.reshape(kernela(positionsa).T, X_air.shape)


X_tree = X_tree.flatten()
Y_tree = Y_tree.flatten()
X_air = X_air.flatten()
Y_air = Y_air.flatten()
Z_tree = Z_tree.flatten()
Z_air = Z_air.flatten()
row = []

# Write KDE values to csv
with open("/Volumes/USB20FD/Spring2017/Visualization/Project/Project_Data/kde.csv", "w", newline ='') as fi:
	writer = csv.writer(fi, delimiter=",")
	for u, v, w, x, y, z in zip(X_tree, Y_tree, X_air, Y_air, Z_tree, Z_air):
		row.append([u, v, w, x, y, z])
	writer.writerows(row)
