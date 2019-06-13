import scipy.io
import pandas as pd
from scipy.io import loadmat
# mat = scipy.io.loadmat('cars_train_annos.mat')
# mat = {k:v for k, v in mat.items() if k[0] != '_'}
# data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})

annots = loadmat('dataset/devkit/cars_train_annos.mat')
data = [[row.flat[0] for row in line] for line in annots['annotations'][0]]
columns = ['bbox_x1', 'bbox_y1', 'bbox_x2', 'bbox_y2', 'class', 'fname']
df_train = pd.DataFrame(data, columns=columns)
df_train = df_train[['fname', 'class']]
df_train.to_csv('dataset/df_train.csv', index=False)

