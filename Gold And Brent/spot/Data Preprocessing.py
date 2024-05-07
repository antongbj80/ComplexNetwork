#归一化处理
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.read_excel('E:\AT\Postgraduate\LearningMaterials\ComplexNetwork\ComplexNetwork\Gold And Brent\spot\spot_price.xlsx',header=0,usecols=[1,2])
date = pd.read_excel('E:\AT\Postgraduate\LearningMaterials\ComplexNetwork\ComplexNetwork\Gold And Brent\spot\spot_price.xlsx',header=0,usecols=[0])
date.columns = ['Date']

#最值归一化
scaler = MinMaxScaler(feature_range=(0,10), copy=True)
scaler.fit(data)
scaled_features = scaler.transform(data)
scaled_features = pd.DataFrame(scaled_features,columns=['Brent', 'USD_gold'])

#合并数据
final_df = pd.concat([date, scaled_features], axis=1)
print(final_df)
#保存数据  
final_df.to_excel('./scaled_with_date(0,10).xlsx', index=False)

