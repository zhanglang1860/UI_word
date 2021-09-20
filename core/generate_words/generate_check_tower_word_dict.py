#! python3
# -*- encoding: utf-8 -*-
"""
@File    :   generate_check_tower_word_dict.py
@Time    :   2021/08/16 14:33:40
@Author  :   ZhangYicheng 
@Version :   1.0
@Contact :   zhangyicheng1986@outlook.com
"""
# 检验是否有气温气压数据

def get_tower_check_word_dict(context):
    words = []

    for key in context["风数据总结_words"].keys():

        if context["风数据总结_words"][key]["气温数据"] == 0:
            if context["风数据总结_words"][key]["气压数据"] == 0:
                str_check_temp_data = "无气温、气压数据"
            else:
                str_check_temp_data = "无气温、有气压数据"
        else:
            if context["风数据总结_words"][key]["气压数据"] == 0:
                str_check_temp_data = "有气温、无气压数据"
            else:
                str_check_temp_data = "有气温、气压数据"

        if context["风数据总结_words"][key]["是否计入计算空气密度"] == 0:

            word_str = (
                "%s测风塔%s记录，由于%s时段内温度及气压通道损坏，完整率%s，无法准确评估空气密度，不作为参数输入用以计算风电场空气密度。"
                % (
                    context["风数据总结_words"][key]["编号"],
                    str_check_temp_data,
                    context["风数据总结_words"][key]["缺失日期"],
                    context["风数据总结_words"][key]["完整率"],
                )
            )
            words.append(word_str)
        else:
            if (
                context["风数据总结_words"][key]["气温数据"] == 1
                and context["风数据总结_words"][key]["气压数据"] == 0
            ):
                word_str = "%s测风塔%s记录，完整率%s，压力参数采用海平面大气压向上外推得到年均气压值，故采用数据有效完整率高的%s测风塔进行空气密度的分析。" % (
                    context["风数据总结_words"][key]["编号"],
                    str_check_temp_data,
                    context["风数据总结_words"][key]["完整率"],
                    context["风数据总结_words"][key]["编号"],
                )
            elif (
                context["风数据总结_words"][key]["气温数据"] == 1
                and context["风数据总结_words"][key]["气压数据"] == 1
            ):
                word_str = "%s测风塔%s记录，完整率%s，故采用数据有效完整率高的%s测风塔进行空气密度的分析。" % (
                    context["风数据总结_words"][key]["编号"],
                    str_check_temp_data,
                    context["风数据总结_words"][key]["完整率"],
                    context["风数据总结_words"][key]["编号"],
                )
            words.append(word_str)
    # print(words)
    res_dict = dict({"各测风塔完整率描述": words})
    return res_dict


# def get_tower_density_title_dict(context):

#     turbine_height = context["风数据总结_words"][0]["轮毂高度"]
#     table_col_name = ["测风塔", "高程（m）", "10m", str(turbine_height) + "m"]
#     table_col_name_dict = dict({"tower_density_labels": table_col_name})

#     return table_col_name_dict


# def get_tower_density_word_dict(context):
#     words = []
#     average_temp = 6.67
#     average_pres = 89.67
#     superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
#     density_unit="kg/m3".translate(superscript)

#     for each_dict in context["风数据总结_table"]:

#         word_str = "本阶段收集到参考周期内%s测风塔气温数据。根据%s测风塔数据，年平均气温%s℃，依据海平面外推%s高程%sm处年平均气压%skPa，测风塔高度处空气密度为%s%s；风电场轮毂高度%sm处空气密度为%s%s。" % (
#             each_dict["编号"],
#             each_dict["编号"],
#             average_temp,
#             each_dict["编号"],
#             each_dict["海拔"],
#             average_pres,
#             each_dict["装置处的空气密度"],
#             density_unit,
#             each_dict["轮毂高度"],
#             each_dict["轮毂高度处的空气密度"],
#             density_unit,
#         )
#         words.append(word_str)
      
#     res_dict = dict({"各测风塔空气密度描述": words})
#     return res_dict
