# 带参脚本
# 用法：python merge_kbitx.py A.kbitx B.kbitx merged_output.kbitx
# A为全集，B为diff集

import xml.etree.ElementTree as ET

def read_kbitx(file_path):
    """读取.kbitx文件，返回根元素"""
    tree = ET.parse(file_path)
    return tree.getroot()

def get_g_elements_with_u(root):
    """从根元素中提取所有g元素，并以u属性为键建立字典"""
    g_dict = {}
    for elem in root:
        if elem.tag == 'g' and 'u' in elem.attrib:
            g_dict[elem.attrib['u']] = elem
    return g_dict

def merge_g_elements(root_b, g_list_a):
    """将A中的g元素按u属性选择性合并到B中"""
    existing_gs = get_g_elements_with_u(root_b)

    for elem in g_list_a:
        if elem.tag == 'g' and 'u' in elem.attrib:
            u_value = elem.attrib['u']
            if u_value not in existing_gs:
                root_b.append(elem)

def write_kbitx(root, output_path):
    """将合并后的根元素写入新的.kbitx文件"""
    tree = ET.ElementTree(root)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

def merge_kbitx_files(file_a, file_b, output_file):
    """
    主函数：合并两个.kbitx文件
    - file_a: 源文件A
    - file_b: 源文件B
    - output_file: 合并后的输出文件
    """
    # 读取两个文件
    root_a = read_kbitx(file_a)
    root_b = read_kbitx(file_b)

    # 提取A中的所有<g>元素
    g_elements_a = [elem for elem in root_a if elem.tag == 'g' and 'u' in elem.attrib]

    # 合并<g>元素到B
    merge_g_elements(root_b, g_elements_a)

    # 写入结果文件
    write_kbitx(root_b, output_file)

# 示例用法
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("用法: python kbitx_marge_fallback.py <file_a.kbitx> <file_b.kbitx> <output.kbitx>")
    else:
        file_a = sys.argv[1]
        file_b = sys.argv[2]
        output_file = sys.argv[3]
        merge_kbitx_files(file_a, file_b, output_file)