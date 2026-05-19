import xml.etree.ElementTree as ET

def read_g_elements(file_path):
    """读取.kbitx文件中的所有g元素，并以u属性为键存储到字典中"""
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    g_dict = {}
    for g in root.findall('g'):
        u = g.get('u')
        if u is not None:
            try:
                u_value = int(u)
                if (13312 <= u_value <= 40959) or (u_value >=131072): # 仅基本区无补充，范围为19968-40869
                    d_value = g.get('d', '')  # 获取d属性，如果不存在则为空字符串
                    g_dict[u_value] = d_value
            except ValueError:
                continue  # 忽略无法转换为整数的u属性
    return g_dict

def compare_files(file_a, file_b, output_file):
    """比较两个文件中的g元素，并输出结果"""
    g_a = read_g_elements(file_a)
    g_b = read_g_elements(file_b)

    results = []

    for u_value, d_a in g_a.items():
        d_b = g_b.get(u_value)
        if d_b is not None and d_a == d_b:
            uni_code = format(u_value, 'X')  # 转换为大写十六进制
            ## 输出 Unicode 及对应字符
            # char = chr(u_value)
            # results.append(f"{uni_code} {char}")
            ## 仅输出 Unicode
            results.append(f"{uni_code}")

    # 按 Unicode 排序
    results.sort()

    # 写入结果到文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in results:
            f.write(line + '\n')

    print(f"比较完成，共找到 {len(results)} 个重复项，结果已保存到 {output_file}")

# 示例使用方式
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 4:
        print("用法: python kbitx_compare.py <file_a.kbitx> <file_b.kbitx> <output.txt>")
    else:
        file_a = sys.argv[1]
        file_b = sys.argv[2]
        output_file = sys.argv[3]
        compare_files(file_a, file_b, output_file)