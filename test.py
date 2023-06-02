import streamlit as st
import pandas as pd

st.header("I am a Demo")
st.subheader("this is a sub title of Demo")
st.text("I am Richard.")


st.sidebar.header("筛选条件") # 侧边栏标题
st.sidebar.selectbox("Pillars",["QPC","CFS","IDG","IE","REL","H&S","Env","PD"],0) #下拉选择框（非空单选）
st.sidebar.multiselect("Areas",["Bearings","Seals-OS","APS","Tape Solutions","Life Sciences"]) # 多选框
st.sidebar.number_input("最近天数：",1,365, 7) #数字框输入
st.sidebar.radio("排序：",("日期","版本号"),horizontal=True) # 单选框 （horizontal指定了布局，Ture为横向布局，默认为False，竖向布局）

#  饼状图实现
from pyecharts.charts import Pie

pie = Pie() #定义饼状图
pie.add("",
        [ ("正常次数",8),
          ("缺失次数",3),
          ("异常次数",2)],
          center = ["35%","50%"],
          radius = ["40%","75%"], )
pie.set_colors(["rgba(60,179,113)","rgba(205,159,0)","rgba(255,69,0)"])

import streamlit_echarts as ste

ste.st_pyecharts(pie)

# from pyecharts.charts import Bar
# from config import opt

# bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
# bar.add_xaxis(["explorer_time","ie_time","notepad_time"])
# bar.add_yaxis("noClient(9次)",["0.7","1.4","0.4"],gap="5%")
# ste.st_pyecharts(bar)

