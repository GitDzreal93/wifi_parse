import os
import re
from lxml import etree
import xlwt
import collections
import pandas as pd

# 指定数据集路径
dataset_path = './Xmldata'

# 结果保存路径
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

data_cols = ['手机MAC', 'WiFi名称', 'AppId', 'SecretKey', 'ShopId']

def check_zh(word):
    '''
    判断字符串是否是简体中文，中文返回 True, 反之 False
    :param word:
    :return: BOOL
    '''
    zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zh_pattern.search(word)
    return True if match else False


def parse_xml_list(xmlfile):
    '''
    解析XML的数据，并返回一个列表
    :param xmlfile:
    :return:List
    '''
    data = []

    xml_tree = etree.parse(xmlfile)
    parse_root = xml_tree.xpath('wireless-network')
    for tag in parse_root:
        ssid_list = tag.xpath('SSID/essid/text()')
        mac_per_list = tag.xpath('wireless-client/client-mac/text()')

    ssid_s = pd.Series(ssid_list,None)
    print(ssid_list)

        # ssid_info = info.xpath('SSID/ssid/text()')[0]
        # print(ssid_info)

    # mac_list = xml_tree.xpath('//client-mac/text()')
    # ssid_list = xml_tree.xpath('//SSID/ssid/text()')
    # print(ssid_list)
    # mac_arr = np.array(mac_list)
    # ssid_arr = np.array(ssid_list)
    # print(mac_arr)
    # print(ssid_arr)
    # print(p)
    # data_arr = np.array([[mac,ssid] for mac, ssid in zip(mac,ssid)])
    # print(data_arr)

    # for info in infos:
    #     ssid_info = info.xpath('SSID/ssid/text()')
    #     if ssid_info:
    #         is_zh = check_zh(ssid_info[0])
    #         if not is_zh:
    #             mac_info = info.xpath('client-mac/text()')[0]
    #             info_list = [mac_info, ssid_info]
    #             all_info_list.append(info_list)

    # return mac, ssid


# def batchParseXmlList(xmldir):
#     '''
#     批量解析xmldata目录下的所有XML，并返回一个列表
#     :param xmldir:
#     :return: List
#     '''
#     xmlfiles = os.listdir(xmldir)
#     all_info_list = None
#
#     for xmlfile in xmlfiles:
#         xmlfile = os.path.join(xmldir,xmlfile)
#         try:
#             all_info_list = parseXmlList(xmlfile)
#         except:
#             continue
#
#     return all_info_list
#
#
# def dataWriter(all_info_list):
#     '''
#     生成目标xlsx文件
#     :param all_info_list:
#     :return: None
#     '''
#     book = xlwt.Workbook(encoding='utf-8')
#     sheet = book.add_sheet('Sheet1')
#     header = ['手机MAC', 'WiFi名称', 'AppId', 'SecretKey', 'ShopId']
#
#     for column in range(len(header)):
#         sheet.write(0, column, header[column])
#     print(all_info_list)
#     row = 1
#     for info_list in all_info_list:
#         column = 0
#         for data in info_list:
#             sheet.write(row, column, data)
#             column += 1
#         row += 1
#
#     book.save('template.xlsx')
#

if __name__ == '__main__':
    # info_list = batchParseXmlList(XMLDATA_DIR)  #遍历所有的xml文件
    info_list = parse_xml_list('E:\project\XMLParse\Xmldata\Kismet-20180303-09-38-00-1.xml') #执行单个xml文件
