from pandas import json_normalize
import pandas as pd

# data = pd.read_json('./xapp.json')


# 读取JSON文件
data = pd.read_json('./xapp.json')

# 提取
urls = data['value'].apply(lambda x: x.get('url', 'No URL Found'))
titles = data['value'].apply(lambda x: x.get('title', 'No Title Found'))
status = data['value'].apply(lambda x: x.get('httpFlow', {}).get('exchanges', [{}])[0].get('response', {}).get('status', 'No Status Found'))
ip=data['value'].apply(lambda x: x.get('httpFlow', {}).get('exchanges', [{}])[0].get('response', {}).get('ip', 'No Status Found'))
tag=data['value'].apply(lambda x: x.get('fingerprints', [{}])[0].get('product', {}).get('name', 'No Status Found'))
fofa=data['value'].apply(lambda x: x.get('fingerprints', [{}])[0].get('extra', {}).get('fofa', 'No Status Found'))
length=data['value'].apply(lambda x: x.get('httpFlow', {}).get('exchanges', [{}])[0].get('response', {}).get('header',{}).get('Content-Length', 'No Status Found'))

# 将urls和titles组合成一个新的DataFrame
output_df = pd.DataFrame({'URL': urls, 'Title': titles, "Status": status,"IP": ip,"tag":tag,"FoFa": fofa,"length": length})

# 设置打印选项，使DataFrame输出更美观
pd.set_option('display.max_colwidth', None)  # 不限制列宽
pd.set_option('display.width', 1000)         # 设置显示宽度
pd.set_option('display.unicode.east_asian_width', True)  # 正确显示中文字符宽度

# 打印DataFrame
print(output_df)

output_df.to_csv('./output.csv', index=False, encoding='utf-8-sig')


