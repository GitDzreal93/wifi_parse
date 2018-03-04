import os
import re
from lxml import etree
import xlwt

#xml文件目录
XMLDATA_DIR = os.path.abspath(os.path.join(os.getcwd(),'Xmldata'))


def checkZh(word):
    '''
    判断字符串是否是简体中文，中文返回 True, 反之 False
    :param word:
    :return: BOOL
    '''
    zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zh_pattern.search(word)
    if match:
        return True
    else:
        return False


def parseXmlList(xmlfile):
    '''
    解析XML的数据，并返回一个列表
    :param xmlfile:
    :return:List
    '''
    all_info_list = []
    xml_tree = etree.parse(xmlfile)
    infos = xml_tree.xpath('wireless-network')
    
    if not infos:
        raise IOError

    for info in infos:
        ssid_info = info.xpath('SSID/essid/text()')
        if ssid_info:
            is_zh = checkZh(ssid_info[0])
            if not is_zh:
                mac_infos = info.xpath('wireless-client/client-mac/text()')
                if len(mac_infos) > 0:
                	for mac_info in mac_infos:
                		info_list = [mac_info, ssid_info]
                		all_info_list.append(info_list)

    return all_info_list


def batchParseXmlList(xmldir):
    '''
    批量解析xmldata目录下的所有XML，并返回一个列表
    :param xmldir:
    :return: List
    '''
    xmlfiles = os.listdir(xmldir)
    all_info_list = None

    for xmlfile in xmlfiles:
        xmlfile = os.path.join(xmldir,xmlfile)
        try:
            all_info_list = parseXmlList(xmlfile)
        except:
            continue

    return all_info_list


def dataWriter(all_info_list):
    '''
    生成目标xlsx文件
    :param all_info_list:
    :return: None
    '''
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1')
    header = ['手机MAC', 'WiFi名称', 'AppId', 'SecretKey', 'ShopId']

    for column in range(len(header)):
        sheet.write(0, column, header[column])
    print(all_info_list)
    row = 1
    for info_list in all_info_list:
        column = 0
        for data in info_list:
            sheet.write(row, column, data)
            column += 1
        row += 1

    book.save('template.xlsx')


def dataPrinter(all_info_list):
 	# print(all_info_list)
 	print("length of infos:",len(all_info_list))
 	for info_list in all_info_list:
 		print('MAC:{0}\t wifi:{1}'.format(info_list[0],info_list[1]))



if __name__ == '__main__':
    info_list = batchParseXmlList(XMLDATA_DIR)  #遍历所有的xml文件
    # info_list = parseXmlList('E:\project\XMLParse\Xmldata\Kismet-20180303-09-38-00-1.xml') #执行单个xml文件
    # dataWriter(info_list)
    dataPrinter(info_list)
