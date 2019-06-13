import scipy.io
import pandas as pd
from scipy.io import loadmat
mat = scipy.io.loadmat('cars_meta.mat')
mat = {k:v for k, v in mat.items() if k[0] != '_'}
data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})
data.to_csv('cars_meta.csv')

# annots = loadmat('cars_train_annos.mat')
# data = [[row.flat[0] for row in line] for line in annots['annotations'][0]]
# columns = ['bbox_x1', 'bbox_y1', 'bbox_x2', 'bbox_y2', 'class', 'fname']
# df_train = pd.DataFrame(data, columns=columns)
# df_train.to_csv('df_train.csv')
