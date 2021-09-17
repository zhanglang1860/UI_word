#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   generate_windspeed_word_dict.py
@Time    :   2021/08/18 17:06:41
@Author  :   ZhangYicheng 
@Version :   1.0
@Contact :   zhangyicheng1986@outlook.com
'''

def get_windspeed_word_dict(context):
    # print(context)
    words = []
    superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    density_unit="W/m2".translate(superscript)
  
    for each_dict in context["平均风速及风功率密度_table"]:
      
        word_str = "对%s测风塔数据进行统计，%s测风塔%sm高度的年平均风速为%sm/s，（折算到标准空气密度下为%sm/s)，风功率密度分别为%s%s；" % (
            each_dict["编号"],
            each_dict["编号"],
            each_dict["轮毂高度"],
            each_dict["年平均风速"],
            each_dict["标况下年平均风速"],
            each_dict["风功率密度"],
            density_unit,

           
        )
        words.append(word_str)
      
    res_dict = dict({"各测风塔平均风速及风功率密度描述": words})
    return res_dict
    