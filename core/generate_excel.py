#! python3
# -*- encoding: utf-8 -*-
"""
@File    :   generate_excel.py
@Time    :   2021/08/16 13:55:32
@Author  :   ZhangYicheng 
@Version :   1.0
@Contact :   zhangyicheng1986@outlook.com
"""
import os
import re
import sys

import pandas as pd

sys.path.append(r"L:\Onedrive - Microsoft 365\工作\联合动力（新）\1. 代码\UI_word\core")
from wind.generate_check_tower_excel import (get_tower_check_words,
                                             get_tower_density_table)


class Generate_excel:

    """1. 读取TXT"""

    def file_load(self, file_path, filename):
        """
        file_load [summary]该方法把原有的TXT文件进行重构，并生成pd格式。

        [extended_summary]

        Args:
            file_path ([type]): [windog生成TXT路径]
            filename ([type]): [windog生成TXT名字]
            cftname ([type]): [windog生成cft名字]

        Returns:
            [type]: [pd]
        """
        # 首先确定载入数据的截取自然年的时间段，并以该时间段的原始文件TXT，作为分析的基础。（windographer 记得导出所有的选项）
        o_data = pd.read_csv(
            os.path.join(file_path, filename),
            header=8,
            sep="\t",
        )
        # 删除未命名的列
        o_data = o_data.drop(
            o_data.loc[:, o_data.columns.str.startswith("Unnamed")], axis=1
        )
        # 整合每列的列名
        col_names = []
        for col_name in o_data.columns:
            col_name = re.sub(u"\\s\[.*?]", "", col_name)
            col_names.append(col_name)
        o_data.columns = col_names
        # print(o_data.columns)
        # 初始化时间
        o_data["Date/Time"] = pd.to_datetime(o_data["Date/Time"])
        o_data = o_data.set_index(["Date/Time"])
        # month_data = o_data.groupby(o_data.index.month).mean().round(3)
        # print(month_data)

        return o_data

    """2. 生成Word_excel
        运行相应的get excel 模板
        例如：
        word_excel = generate_check_tower_excel.get_excel(o_data) 
    """

    """3. 生成excel"""

    def create_excel(self, data, save_path, output, result_sheet_names):
        """
        create_excel 生成word文档

        Args:
            data ([字典类型]): [对应字段的描述语句]
            save_path ([type]): [保存路径]
            output ([type]): [输出文件名]
            result_sheet_names ([type]): [excel sheet_names]
        """
        from openpyxl import Workbook
        from styleframe import StyleFrame, Styler, utils

        # writer = pd.ExcelWriter(os.path.join(save_path, "%s.xlsx") % output)
        # data.to_excel(excel_writer=writer, sheet_name=sheet_name)
        # writer.save()
        # writer.close()

        book1 = Workbook()
        writer1 = StyleFrame.ExcelWriter(
            (os.path.join(save_path, "%s.xlsx") % output),
            # engine="openpyxl",
        )

        writer1.book = book1

        for i in range(len(data)):

            sf = data[i].reset_index()
            sf.iloc[:, 0] = sf.iloc[:, 0].mask(sf.iloc[:, 0].shift(1) == sf.iloc[:, 0])
            sf = StyleFrame(sf)

            print(sf)

            # sf.apply_headers_style(
            #     style_index_header=True,
            #     styler_obj=Styler(bg_color=utils.colors.red, bold=True, font_size=10),
            # )
            # sf.apply_column_style(
            #     cols_to_style="cft0号",
            #     styler_obj=Styler(bg_color=utils.colors.green),
            #     style_header=True,
            # )
            sf.to_excel(
                writer1,
                sheet_name=result_sheet_names[i],
                index=True,
                best_fit=sf.columns.to_list(),
            )

        book1.remove(book1["Sheet"])

        writer1.save()
        writer1.close()

    """综合，汇总"""
    """
    读取TXT，并生成excel。这里包含3个步骤
        1. 根据TXT，重构data
        2. 对应生成 word_excel
        2. 根据word_excel 最终生成excel文档
    """

    def generate_excel_method(
        self,
        chapters_fucns,
        read_txt_path,
        save_path,
        output,
        chapters_fucns_names,
        result_sheet_names,
    ):
        chapters_combine = []
        for chapter_fucns in chapters_fucns:
            chapters_num = 0
            fuc_num = 0
            chapter_combine = pd.DataFrame()
            data_base_information = pd.read_excel(
                os.path.join(read_txt_path, "base_information.xlsx"), index_col=[0, 1]
            )
       
            file_names = data_base_information[
                data_base_information.index == ("风电场基本信息", "文件")
            ].values[0]
            # print(file_names)
            for func in chapter_fucns:
                column_names = []
                level0_names = []

                towers_pd = pd.DataFrame()

                for index, file_name in enumerate(file_names):

                    generate_excel_data = Generate_excel()
                    excel_data = generate_excel_data.file_load(read_txt_path, file_name)
                    tower_pd = func(excel_data, data_base_information, index)
                    towers_pd = pd.concat([towers_pd, tower_pd], axis=1)
                    column_name = "cft" + str(index) + "号"
                    column_names.append(column_name)

                towers_pd.columns = column_names
                # towers_pd['类型']='风数据总结'

                for i in range(0, len(towers_pd.index)):
                    level0_names.append(chapters_fucns_names[chapters_num][fuc_num])
                arrays = [level0_names, towers_pd.index]
                towers_pd.index = pd.MultiIndex.from_arrays(arrays, names=("类型", "种类"))

                chapter_combine = pd.concat([chapter_combine, towers_pd])

                fuc_num = fuc_num + 1
            chapters_combine.append(chapter_combine)
            chapters_num = chapters_num + 1
        self.create_excel(chapters_combine, save_path, output, result_sheet_names)


if __name__ == "__main__":
    # 这两个参数的默认设置都是False
    pd.set_option("display.unicode.ambiguous_as_wide", True)
    pd.set_option("display.unicode.east_asian_width", True)
    read_txt_path = os.path.abspath(os.path.join(os.getcwd(), "./templates"))
    save_path = os.path.abspath(os.path.join(os.getcwd(), "./templates"))
    chapters_fucns, chapters_fucns_names = [], []

    chapter_fucns = [get_tower_check_words, get_tower_density_table]
    chapters_fucns.append(chapter_fucns)
    chapter_fucns_names = ["风数据总结_words", "风数据总结_table"]
    chapters_fucns_names.append(chapter_fucns_names)
    result_sheet_names = ["风数据总结"]

    data_excel = Generate_excel()
    data_excel.generate_excel_method(
        chapters_fucns,
        read_txt_path,
        save_path,
        "data_excel",
        chapters_fucns_names,
        result_sheet_names,
    )
