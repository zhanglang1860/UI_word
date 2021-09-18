#! python3
# -*- encoding: utf-8 -*-
"""
@File    :   generate_docx.py
@Time    :   2021/08/12 13:34:58
@Author  :   ZhangYicheng 
@Version :   1.0
@Contact :   zhangyicheng1986@outlook.com
"""
import os
import re

import pandas as pd
from docxtpl import DocxTemplate, RichText

from generate_words.generate_check_tower_word_dict import *
from generate_words.generate_windspeed_word_dict import *


class Generate_docx:

    """1. 重构Dict"""

    def method_to_dict(self, df):
        table_list = []
        if df.name.endswith("words"):
            table_list = df.xs(df.name).to_dict()

        else:
            df = df.xs(df.name).dropna(how="all",axis=1).to_dict()
            for key in df.keys():
                table_list.append(df[key])

        return table_list

    def load_dict(self, path, sheetname):
        df = pd.read_excel(path, index_col=[1, 2], sheet_name=sheetname)
        print("***")
        # df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
        df = df.drop(columns=["Unnamed: 0"])
        df = df.dropna(how="all", axis=0)
        print(df)
        # context = (
        #     df.groupby(level=0).apply(lambda df: df.xs(df.name).to_dict(orient="list")).to_dict()
        # )

        context = df.groupby(level=0).apply(self.method_to_dict).to_dict()

        return context

    """2. 生成Word_Dict
        运行相应的get words 模板
        例如：
        word_dict = generate_check_tower_word.get_word(context) 
    """
    # 检验是否有气温气压数据

    """3. 生成文档"""

    def create_doc(self, Dict, read_templates_path, input, save_path, output):
        """
        create_doc 生成word文档

        Args:
            Dict ([字典类型]): [对应字段的描述语句]
            read_path ([type]): [读取模板路径]
            input ([type]): [模板名称]
            save_path ([type]): [保存路径]
            output ([type]): [输出文件名]
        """

        filename_box = [input, output]
        read_templates = os.path.join(read_templates_path, "%s.docx") % filename_box[0]
        save_path = os.path.join(save_path, "%s.docx") % filename_box[1]
        tpl = DocxTemplate(read_templates)
        tpl.render(Dict)
        tpl.save(save_path)

    """综合，汇总"""
    """
    读取excel ，并生成报告。这里包含3个步骤
        1. 根据excel，重构Dict
        2. 对应生成 word_dict
        2. 根据word_dict 最终生成word文档
    """

    def generate_word_method(
        self, load_data_path, sheetnames, read_templates_path, input, save_path, output
    ):
        dict_dict, dict_dict_final = dict(), dict()
        for i in range(0, len(sheetnames)):
            context = self.load_dict(load_data_path, sheetnames[i])
            if sheetnames[i] == "风数据总结":
                tower_check_word_dict = get_tower_check_word_dict(context)
                tower_density_title_dict = get_tower_density_title_dict(context)
                tower_density_word_dict = get_tower_density_word_dict(context)
                dict_dict = dict(
                    tower_check_word_dict,
                    **tower_density_title_dict,
                    **tower_density_word_dict
                )
                # print(dict_dict)
            elif sheetnames[i] == "平均风速及风功率密度":

                windspeed_word_dict = get_windspeed_word_dict(context)
                dict_dict = dict(windspeed_word_dict)

            # elif sheetnames[i] == "风速合理性检验":

            #     windspeed_word_dict = get_windspeed_word_dict(context)
            #     dict_dict = dict(windspeed_word_dict)

            dict_dict_final = dict(dict_dict_final, **context, **dict_dict)
            print(dict_dict_final)
        self.create_doc(dict_dict_final, read_templates_path, input, save_path, output)


if __name__ == "__main__":
    # 这两个参数的默认设置都是False
    pd.set_option("display.unicode.ambiguous_as_wide", True)
    pd.set_option("display.unicode.east_asian_width", True)

    read_templates_path = os.path.abspath(os.path.join(os.getcwd(), "./templates"))
    save_path = os.path.abspath(os.path.join(os.getcwd(), "./templates"))
    result_sheet_names = ["风数据总结", "风速合理性检验"]
    # 生成word文件
    test_word = Generate_docx()
    test_word.generate_word_method(
        os.path.join(read_templates_path, "data_excel.xlsx"),
        result_sheet_names,
        read_templates_path,
        "测风数据分析报告-templates",
        save_path,
        "res",
    )

    # context = {
    #         "风数据总结": {
    #             "cft01": {
    #                 "编号": "1488#",
    #                 "气温数据": 1,
    #                 "气压数据": 1,
    #                 "气温气压数据是否有缺失": 1,
    #                 "缺失日期": "2015/07/27 8:00-2015/11/08 10:50",
    #                 "完整率": "78.09%",
    #                 "是否计入计算空气密度": 1,
    #             },
    #             "cft02": {
    #                 "编号": "1499#",
    #                 "气温数据": 1,
    #                 "气压数据": 1,
    #                 "气温气压数据是否有缺失": 0,
    #                 "缺失日期": "",
    #                 "完整率": "98.91%",
    #                 "是否计入计算空气密度": 1,
    #             },
    #         },
    #         "风数据总结02": {
    #             "cft01": {
    #                 "编号": "1488#",
    #                 "气温数据": 1,
    #                 "气压数据": 1,
    #                 "气温气压数据是否有缺失": 1,
    #                 "缺失日期": "2015/07/27 8:00-2015/11/08 10:50",
    #                 "完整率": "78.09%",
    #                 "是否计入计算空气密度": 1,
    #             },
    #         },
    #     }
