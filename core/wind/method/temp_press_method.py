#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   temp_press_method.py
@Time    :   2021/08/27 09:10:59
@Author  :   ZhangYicheng 
@Version :   1.0
@Contact :   zhangyicheng1986@outlook.com
'''

def temp_press_cal(data,elevation):
    pick_temp = (data.columns.str.startswith("Temperature") & (
    ~data.columns.str.endswith("SD")
    & ~data.columns.str.endswith("Max")
    & ~data.columns.str.endswith("Min")
    & ~data.columns.str.endswith("TI")
    & ~data.columns.str.endswith("WPD")))|(data.columns.str.startswith("Pressure") & (
    ~data.columns.str.endswith("SD")
    & ~data.columns.str.endswith("Max")
    & ~data.columns.str.endswith("Min")
    & ~data.columns.str.endswith("TI")
    & ~data.columns.str.endswith("WPD")))
    print("ssssssssss")
    print(data.loc[:, pick_temp].columns.str.startswith("Pressure").any())
    if data.loc[:, pick_temp].columns.str.startswith("Temperature").any()==False: 
        density_value=0 
    elif data.loc[:, pick_temp].columns.str.startswith("Pressure").any()==False:
        if elevation<=3000:
            pick_press_data = 100-elevation/1000*10
        elif elevation>3000 and elevation<=5000: 
            pick_press_data = 70-elevation/1000*8
        else:  
            pick_press_data = 54-elevation/1000*6.5 
        pick_temp_data = data.loc[:, pick_temp].mean()[0].round(3)
        density_value=pick_press_data/(287.053*(273.15+pick_temp_data))*1000
    else:
        pick_temp_data = data.loc[:, pick_temp].mean()[0].round(3)
        pick_press_data = data.loc[:, pick_temp].mean()[1].round(3)

        density_value=pick_press_data/(287.053*(273.15+pick_temp_data))*1000
    return density_value.round(3)

def density_value_hight_cal(density_value,hight_low,hight_high):
    import math
    density_value_change=density_value/math.exp(-0.0001*(hight_low-hight_high))
    return density_value_change.round(3)
