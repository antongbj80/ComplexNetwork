import pandas as pd

# 读取包含原油价格和黄金价格数据的Excel文件
df = pd.read_excel('scaled_with_date(0,10).xlsx')
print(df)

# 自定义相关系数计算公式
def correlation(x, y, method):
    corr = x.corr(y, method=method)
    return corr

# 创建一个空的DataFrame，用于保存不同相关系数的结果
df_corr = pd.DataFrame()

# 计算并保存不同相关系数的结果,滑动窗口=20
for i in range(len(df)-20):
    corr_list = []
    for method in ['pearson', 'spearman', 'kendall']:
        corr = correlation(df['Brent'].iloc[i:i+20], df['USD_gold'].iloc[i:i+20], method)
        corr_list.append(corr)
    df_corr[i] = corr_list

# 将DataFrame转置，使日期作为索引
df_corr = df_corr.T

# 为每种相关系数设置不同的列名
df_corr.columns = ['Pearson', 'Spearman', 'Kendall']
print(df_corr)

# 保存结果到Excel表格
df_corr.to_excel('correlation_results.xlsx')
