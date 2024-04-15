#归一化处理
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.read_excel('E:\AT\Postgraduate\LearningMaterials\复杂网络金融方向\黄金和原油\Data\复现用数据(中美黄金和Brent期货).xlsx',header=0,nrows=2616,usecols=[1,2,3])
date = pd.read_excel('E:\AT\Postgraduate\LearningMaterials\复杂网络金融方向\黄金和原油\Data\复现用数据(中美黄金和Brent期货).xlsx',header=0,nrows=2616,usecols=[0])
date.columns = ['Date']

#最值归一化
scaler = MinMaxScaler(feature_range=(0, 10), copy=True)
scaler.fit(data)
scaled_features = scaler.transform(data)
scaled_features = pd.DataFrame(scaled_features,columns=['ChinaGold', 'COMEXGold', 'Brent'])

#合并数据
final_df = pd.concat([date, scaled_features], axis=1)
#保存数据  
final_df.to_csv('scaled_with_date.csv', index=False)


# 
# df_MinMax.to_csv('ScalerData.csv')
