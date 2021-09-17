#! python3
# -*- encoding: utf-8 -*-
"""
@File    :   check_tower.py
@Time    :   2021/08/16 14:55:44
@Author  :   ZhangYicheng 
@Version :   1.0
@Contact :   zhangyicheng1986@outlook.com
"""

import pandas as pd
# 检验是否有气温气压数据
from numpy.lib.shape_base import column_stack
import sys


sys.path.append(r"L:\Onedrive - Microsoft 365\工作\联合动力（新）\1. 代码\UI_word\core\wind")
from wind.method.temp_press_method import density_value_hight_cal, temp_press_cal


def get_tower_check_words(data, data_base_information, index):

    tower_pd = pd.DataFrame()
    start_date = ""
    end_date = ""
    pick_temp = data.columns.str.startswith("Temperature") & (
        ~data.columns.str.endswith("SD")
        & ~data.columns.str.endswith("Max")
        & ~data.columns.str.endswith("Min")
    )

    pick_pres = data.columns.str.startswith("Pressure") & (
        ~data.columns.str.endswith("SD")
        & ~data.columns.str.endswith("Max")
        & ~data.columns.str.endswith("Min")
    )

    """# 编号"""
    code_name = data_base_information[
        data_base_information.index == ("测风塔基本信息", "编号")
    ].iloc[:, index][0]
    """# 气温数据 / 气压数据（检查是否有气温气压数据）"""
    pick_temp_data = data.loc[:, pick_temp]
    pick_pres_data = data.loc[:, pick_pres]

    if pick_temp.sum() == 0:
        temp_data = 0
        temp_prec = 0
    else:
        if pick_temp_data.notnull().any()[0]:
            temp_data = 1
            """完整率"""
            temp_prec = (
                100
                - (
                    pick_temp_data.isnull().sum()
                    / pick_temp_data.isnull().count()
                    * 100
                ).round(2)[0]
            )
            str_temp_prec = str(temp_prec) + "%"
            """气温气压数据是否有缺失"""
            if temp_prec < 90:
                check_use = 0
                """
                [summary]主要用来查找最大的缺失时段
                    1.pick_pres_data.isnull().astype(int) 先判断是否为空值[0，非空值][1,空值]
                    2.pick_pres_data.notnull().astype(int).cumsum().iloc[:, 0] 把不是空值的做累加计算
                    3.max_miss_index = pick_pres_data["cumsum"].value_counts().index[0] 取出最大空值所对应的index
                    4.miss_num = pick_pres_data["cumsum"].value_counts().iloc[0] 连续多少个空值
                    5.start_date = pick_pres_data.index[max_miss_index]
                    end_date = pick_pres_data.index[max_miss_index + miss_num] 取出来对应的时间
                """
                # print(pick_pres_data.notnull().astype(int).cumsum())
                # pick_pres_data["isnull"] = pick_pres_data.isnull().astype(int)
                # res=pick_pres_data['isnull'].groupby(pick_pres_data['cumsum']).sum()

                pick_pres_data["cumsum"] = (
                    pick_pres_data.notnull().astype(int).cumsum().iloc[:, 0]
                )
                max_miss_index = pick_pres_data["cumsum"].value_counts().index[0]
                miss_num = pick_pres_data["cumsum"].value_counts().iloc[0]

                start_date = pick_pres_data.index[max_miss_index]
                end_date = pick_pres_data.index[max_miss_index + miss_num]
            else:
                check_use = 1

        else:
            temp_data = 0
            temp_prec = 0
    if pick_pres.sum() == 0:
        pres_data = 0
        pres_prec = 0
    else:
        if pick_pres_data.notnull().any()[0]:
            pres_data = 1
            """完整率"""
            pres_prec = (
                100
                - (
                    pick_pres_data.isnull().sum()
                    / pick_pres_data.isnull().count()
                    * 100
                ).round(2)[0]
            )
            str_pres_prec = str(pres_prec) + "%"
        else:
            pres_data = 0
            pres_prec = 0

    """
     生成Excel 结构的 pd

    """

    tower_pd["编号"] = [code_name]
    tower_pd["气温数据"] = [temp_data]

    tower_pd["气压数据"] = [pres_data]
    tower_pd["缺失日期"] = [str(start_date) + "-" + str(end_date)]
    tower_pd["完整率"] = str_temp_prec
    tower_pd["是否计入计算空气密度"] = [check_use]
    tower_pd = tower_pd.T
    return tower_pd


def get_tower_density_table(data, data_base_information, index):

    pick_temp = data.columns.str.startswith("Speed 100 m A") & (
        ~data.columns.str.endswith("SD")
        & ~data.columns.str.endswith("Max")
        & ~data.columns.str.endswith("Min")
        & ~data.columns.str.endswith("TI")
        & ~data.columns.str.endswith("WPD")
    )

    """# 海拔、气温气压计与轮毂高度"""
    elevation = data_base_information[
        data_base_information.index == ("测风塔基本信息", "海拔")
    ].iloc[:, index][0] 
    hight_low = data_base_information[
        data_base_information.index == ("测风塔基本信息", "测风塔温度计高度")
    ].iloc[:, index][0]
    hight_hight = data_base_information[
        data_base_information.index == ("风电场基本信息", "轮毂高度")
    ].iloc[:, index][0]

    """# 空气密度"""
    density_val = temp_press_cal(data,elevation)
    density_value_change = density_value_hight_cal(density_val, hight_low, hight_hight)
    print(density_val, density_value_change)

    tower_pd = pd.DataFrame()
    """# 编号"""
    code_name = data_base_information[
        data_base_information.index == ("测风塔基本信息", "编号")
    ].iloc[:, index][0]
    """# 海拔"""
    elevation = data_base_information[
        data_base_information.index == ("测风塔基本信息", "海拔")
    ].iloc[:, index][0]
    """# 装置处的空气密度"""
    tower_8m_density = density_val
    """# 轮毂高度处的空气密度"""
    turbine_height_density = density_value_change
    """# 轮毂高度"""
    turbine_height = data_base_information[
        data_base_information.index == ("风电场基本信息", "轮毂高度")
    ].iloc[:, index][0]

    tower_pd["编号"] = [code_name]
    tower_pd["海拔"] = [elevation]
    tower_pd["装置处的空气密度"] = [tower_8m_density]
    tower_pd["轮毂高度处的空气密度"] = [turbine_height_density]
    tower_pd["轮毂高度"] = [turbine_height]

    tower_pd = tower_pd.T
    return tower_pd


if __name__ == "__main__":
    import os
    import sys

    # sys.path.append(r"L:\Onedrive - Microsoft 365\工作\联合动力（新）\1. 代码\UI_word")
    sys.path.append("..")
    from generate_excel import *

    pd.set_option("display.unicode.ambiguous_as_wide", True)
    pd.set_option("display.unicode.east_asian_width", True)
    data_base_information = pd.read_excel(
        os.path.join(read_txt_path, "base_information.xlsx"), index_col=[0, 1]
    )

    read_txt_path = os.path.abspath(os.path.join(os.getcwd(), "./templates"))
    file_names = [
        "o_1498_20150201_20160201-Exported.txt",
        "o_1499_20150301_20160301-Exported.txt",
    ]
    cft_names = ["1498#", "1499#"]

    towers_pd = pd.DataFrame()
    column_names = []
    level0_names = []
    level0_name = ""
    for index, file_name in enumerate(file_names):

        generate_excel_data = Generate_excel()
        excel_data = generate_excel_data.file_load(read_txt_path, file_name)
        tower_pd = get_tower_check_words(excel_data, data_base_information, index)

        towers_pd = pd.concat([towers_pd, tower_pd], axis=1)

        column_name = "cft" + str(index)
        column_names.append(column_name)
        towers_pd.columns = column_names
    # towers_pd['类型']='风数据总结'
    for i in range(0, len(towers_pd.index)):
        level0_name = "风数据总结"
        level0_names.append(level0_name)
    arrays = [level0_names, towers_pd.index]
    towers_pd.index = pd.MultiIndex.from_arrays(arrays, names=("类型", "种类"))
    # towers_pd.index.name='种类'

    # towers_pd.set_index('类型',append=True,drop=True)
    print(towers_pd)
