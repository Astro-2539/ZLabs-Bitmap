# 用法：python advanced_merge_kbitx.py A.kbitx B.kbitx hex_list.txt merged_output.kbitx

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
            u_value = elem.attrib['u']
            g_dict[u_value] = elem
    return g_dict

def read_hex_values(txt_file):
    """读取.txt文件中的十六进制Unicode值，返回集合"""
    hex_values = set()
    with open(txt_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                hex_values.add(line.upper())
    return hex_values

def merge_g_elements_advanced(root_a, root_b, hex_values):
    """根据规则高级合并g元素到B文件的根中"""
    existing_gs = get_g_elements_with_u(root_b)

    for elem in root_a:
        if elem.tag != 'g' or 'u' not in elem.attrib:
            continue

        u_str = elem.attrib['u']
        try:
            u_int = int(u_str)
        except ValueError:
            continue  # 跳过非整数u值

        # 规则(1)
        if u_int < 13312 or (u_int > 40959 and u_int < 131072):
            if u_str not in existing_gs:
                root_b.append(elem)
            continue

        # 规则(2)
        u_hex = format(u_int, 'X').upper()
        if u_hex in hex_values:
            if u_str not in existing_gs:
                root_b.append(elem)

def write_kbitx(root, output_path):
    """将合并后的根元素写入新的.kbitx文件"""
    tree = ET.ElementTree(root)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

def advanced_merge_kbitx_files(file_a, file_b, hex_file, output_file):
    """
    主函数：高级合并两个.kbitx文件
    - file_a: 源文件A
    - file_b: 源文件B
    - hex_file: 十六进制Unicode值文件
    - output_file: 合并后的输出文件
    """
    # 读取文件
    root_a = read_kbitx(file_a)
    root_b = read_kbitx(file_b)
    hex_values = read_hex_values(hex_file)

    # 高级合并<g>元素
    merge_g_elements_advanced(root_a, root_b, hex_values)

    # 写入结果文件
    write_kbitx(root_b, output_file)

# 示例用法
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("用法: python advanced_merge_kbitx.py <file_a.kbitx> <file_b.kbitx> <hex_list.txt> <output.kbitx>")
    else:
        file_a = sys.argv[1]
        file_b = sys.argv[2]
        hex_file = sys.argv[3]
        output_file = sys.argv[4]
        advanced_merge_kbitx_files(file_a, file_b, hex_file, output_file)