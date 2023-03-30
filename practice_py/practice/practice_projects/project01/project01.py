"""
import json

# python列表转为json
data01 = [{"ZRF": "周润发", "age": 19}, {"CSY": 2, "age": 20}, {"sty": 3, "age": 23}]

data01_json = json.dumps(data01, ensure_ascii=False)
print("data01_json的类型是:{}".format(type(data01_json)))
print(data01_json)

# python字典转为json
data02 = {"HJT": "胡锦涛", "add": "中南海"}

data02_json = json.dumps(data02, ensure_ascii=False)
print("data02_json的类型是:{}".format(type(data01_json)))
print(data02_json)

# json转回python(经过上述转换已有data01_json、data02_json)
data01_py = json.loads(data01_json)

print(type(data01_py))
print(data01_py)

data02_py = json.loads(data02_json)

print(type(data02_py))
print(data02_py)
"""

# pyecharts入门
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()
line.add_xaxis(["中国", "日本", "韩国"])
line.add_yaxis("GDP", [30, 20, 10])

line.set_global_opts(
    title_opts=TitleOpts(title = "GDP图标", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

line.render()

