# kbitx_parser.py

import xml.etree.ElementTree as ET

def parse_kbitx_file(file_path):
    # 存储符合条件的 Unicode 值
    valid_unicode_hex = []

    # 解析 XML 文件
    tree = ET.parse(file_path)
    root = tree.getroot()

    # 遍历所有 g 元素
    for elem in root.findall('g'):
        u_attr = elem.get('u')
        if u_attr is not None:
            try:
                u_value = int(u_attr)
                # 判断是否符合指定条件
                if (13312 <= u_value <= 40959) or (u_value >= 131072):
                    # 转换为大写十六进制，不带 0x 前缀
                    hex_value = format(u_value, 'X')
                    valid_unicode_hex.append(hex_value)
            except ValueError:
                # 忽略无法转换为整数的 u 属性
                continue

    return valid_unicode_hex

def write_to_txt(hex_values, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for hex_value in hex_values:
            f.write(hex_value + '\n')

if __name__ == '__main__':
    input_file = 'ZLabsBitmapJP.kbitx'     # 替换为你的 .kbitx 文件路径
    output_file = 'output_JP.txt'       # 输出文件名

    hex_values = parse_kbitx_file(input_file)
    write_to_txt(hex_values, output_file)

    print(f"共提取并保存 {len(hex_values)} 个符合条件的 Unicode 十六进制值到 {output_file}")