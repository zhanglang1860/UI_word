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
from docxtpl.richtext import R

from generate_words.generate_check_tower_word_dict import *
from generate_words.generate_windspeed_word_dict import *


# for key, value in dict.items():
#     aKey = key
#     aValue = value
#     temp.append(aKey)
#     temp.append(aValue)
#     dictList.append(temp)
#     aKey = ""
#     aValue = ""
class Generate_docx:

    """1. 重构Dict"""

    def method_to_dict(self, df):
        # print(df)
        table_name=df.name
        df_level1 = df.xs(table_name).dropna(how="all",axis=1)
        print("df = df.xs(df.name).dropna(how=all,axis=1) ")
        print(df_level1)
        table_list = []
        context = {}
        cft_name_vaule = df_level1.iloc[0, 0]
        if df.name.endswith("words"):
            context = df_level1.to_dict()

        elif table_name.endswith("nocols"):
            tbl_contents = []

            cft_name_vaule = df_level1.index[0]
            col_labels_list = df_level1.iloc[0, :].values.tolist()
            col_labels = dict({"col_labels": col_labels_list})

            choose_df = df_level1.iloc[1:, :].astype(float).round(3)
            choose_df = choose_df.fillna("--")
            print("asdasdasdasd")
            print(choose_df)
            for i in range(0, choose_df.shape[0]):
                index_labels = dict({"index_labels": choose_df.index[i]})
                value_labels = dict(
                    {"value_labels": choose_df.iloc[i, :].values.tolist()}
                )

                single_context = dict(index_labels, **value_labels)
                tbl_contents.append(single_context)

            tbl_contents_dict = dict({"tbl_contents": tbl_contents})
            dict_cft = dict({"cft_name": cft_name_vaule})
            context = dict(
                dict_cft,
                **col_labels,
                **tbl_contents_dict,
            )
            print("contextttt")
            print(context)
            # table_list = df.xs(df.name).dropna(how="all", axis=1).T.to_dict(orient="list")
            # print("iiiiiiiiiiiiii")
            # print(table_list)
            # dict_cft = dict({"cft_name": cft_name_vaule})
            # # dict_metadata = dict({"metadata": [table_list]})
            # context = dict(
            #     dict_cft,
            #     **table_list,
            # )
        else:
            df = df.xs(df.name).dropna(how="all", axis=1).to_dict()
            for key in df.keys():
                table_list.append(df[key])
            dict_cft = dict({"cft_name": cft_name_vaule})
            dict_metadata = dict({"metadata": table_list})

            context = dict(
                dict_cft,
                **dict_metadata,
            )
        return context

    def load_dict(self, path, sheetname):
        context_tables, context_words, context_nocols = {}, {}, {}
        df = pd.read_excel(path, index_col=[1, 2], sheet_name=sheetname).round(3)
        print(" # df = df.loc[:, ~df.columns.str.startswith(Unnamed)]")
        print(df)
        # df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
        df = df.drop(columns=["Unnamed: 0"])
        df = df.dropna(how="all", axis=0)

        # context = (
        #     df.groupby(level=0).apply(lambda df: df.xs(df.name).to_dict(orient="list")).to_dict()
        # )
        final_table_list = []

        context = df.groupby(level=0).apply(self.method_to_dict).to_dict()
        print(context)
        print("context.keys()")
        print(context.keys())
        for key in context.keys():
            if "table" in key:
                final_table_list.append(context[key])
                context_tables = dict({sheetname + "_tables": final_table_list})
            elif "nocols" in key:
                final_table_list.append(context[key])
                context_nocols = dict({sheetname + "_nocols": final_table_list})

            else:
                context_words = dict({sheetname + "_words": context[key]})
        print("context_table")
        print(context_tables)
        print("context_word")
        print(context_words)
        print("context_nocols")
        print(context_nocols)
        return context_tables, context_words, context_nocols

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
            context_tables, context_words, context_nocols = self.load_dict(
                load_data_path, sheetnames[i]
            )
            if sheetnames[i] == "风数据总结":
                tower_check_word_dict = get_tower_check_word_dict(context_words)
                # tower_density_title_dict = get_tower_density_title_dict(context_words)
                # tower_density_word_dict = get_tower_density_word_dict(context_words)
                dict_dict = dict(
                    tower_check_word_dict,
                    # **tower_density_title_dict,
                    # **tower_density_word_dict,
                )
                # print(dict_dict)
            elif sheetnames[i] == "平均风速及风功率密度":

                windspeed_word_dict = get_windspeed_word_dict(context_words)
                dict_dict = dict(windspeed_word_dict)

            # elif sheetnames[i] == "风速合理性检验":

            #     windspeed_word_dict = get_windspeed_word_dict(context)
            #     dict_dict = dict(windspeed_word_dict)

            dict_dict_final = dict(
                dict_dict_final, **context_tables, **context_nocols, **dict_dict
            )
            print(dict_dict_final)
        self.create_doc(dict_dict_final, read_templates_path, input, save_path, output)


if __name__ == "__main__":
    # 这两个参数的默认设置都是False
    pd.set_option("display.unicode.ambiguous_as_wide", True)
    pd.set_option("display.unicode.east_asian_width", True)

    read_templates_path = os.path.abspath(os.path.join(os.getcwd(), "./templates"))
    save_path = os.path.abspath(os.path.join(os.getcwd(), "./templates"))
    result_sheet_names = [
        "风数据总结",
        "风速合理性检验",
        "风向合理性检验",
        "气压合理性检验",
        "相关性检验参考表",
        "风速相关性检验",
        "风向相关性检验",
        "风速趋势检验",
        "气温趋势检验",
        "气压趋势检验",
        "测风塔完整率",
        "相关性统计表",
        "平均风速表",
        "逐时平均风速表",
        "逐月平均风速表", 
        "风切变指数表",  
                
    ]
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
