import math
import shutil

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._n_a_m_e import NameRecord
from kbitfont import KbitFont
from pixel_font_builder import FontBuilder, WeightName, SerifStyle, SlantStyle, WidthStyle, Glyph
from datetime import date

import path_define, options
from kbitx_marge_selected import advanced_merge_kbitx_files
from kbitx_marge_fallback import merge_kbitx_files

def fix_mono_mode(font: TTFont):
    font['post'].isFixedPitch = 1
    font['OS/2'].panose.bFamilyType = 2 
    font['OS/2'].panose.bProportion = 9 # 修改字体的 Panose 属性，使其能够被识别为等宽字体
    font['OS/2'].xAvgCharWidth = 600    # 修复 Panose 属性引起的字宽问题
    font['OS/2'].achVendID = "ZLAB"
    font['OS/2'].ulCodePageRange1 = 0b1100000000101100000000000001101
    font['OS/2'].ulCodePageRange2 = 0b10000110101010000000000000000    # 为字体添加微软编码页属性，防止某些程序不识别

def font_name_table_set(font: TTFont, region: str):
    info_CHS = {
        0: '© 2023-2026 Astro_2539. 本字体保留字体名称「Z工坊」「Z Labs」。',
        1: 'Z工坊像素黑体 12px',
        2: 'Regular',
        8: 'Z Labs Design',
        13: '本字体软件采用OFL-1.1开源字体许可证授权。欲知详情，请访问：https://openfontlicense.org/。\n本字体所有副本均免费分发，若您通过付费途径获取本字体软件，请立即举报并差评！',
        19: '像素之光点亮文字之美 The luster of pixels lights up the beauty of words.'
    }
    info_CHT = {
        0: '© 2023-2026 Astro_2539. 本字型檔保留字體名稱「Z工坊」「Z Labs」。',
        1: 'Z工坊像素黑體 12px',
        2: 'Regular',
        8: 'Z Labs Design',
        13: '本字型檔採用OFL-1.1開源字型許可證授權。欲知詳情，請訪問：https://openfontlicense.org/。\n本字型檔所有副本均免費分發，若您通過付費途徑獲取本字型檔，請立即舉報並差評！',
        19: '像素之光點亮文字之美 The luster of pixels lights up the beauty of words.'
    }
    if region == 'HC_fallback':
        region = 'HC FB'
    elif region == 'JP_fallback':
        region = 'JP FB'
    info_CHS[1] += ' M ' + region
    info_CHT[1] += ' M ' + region
    info_CHS[4] = info_CHS[1] + ' Regular'
    info_CHT[4] = info_CHT[1] + ' Regular'

    name_table = font['name']

    for name_id, new_content in info_CHS.items():
        new_record = NameRecord()
        new_record.nameID = name_id
        new_record.platformID = 3
        new_record.platEncID = 1
        new_record.langID = 0x804
        new_record.string = new_content.encode('utf-16-be')
        name_table.names.append(new_record)

    for name_id, new_content in info_CHT.items():
        new_record = NameRecord()
        new_record.nameID = name_id
        new_record.platformID = 3
        new_record.platEncID = 1
        new_record.langID = 0x404
        new_record.string = new_content.encode('utf-16-be')
        name_table.names.append(new_record)


def main():
    # 获取当前日期
    date_now = date.today()
    date_now_f = date_now.strftime("%Y%m%d")

    # 初始化导出文件夹
    if path_define.build_dir.exists():
        shutil.rmtree(path_define.build_dir)
    path_define.outputs_dir.mkdir(parents=True)
    path_define.releases_dir.mkdir(parents=True)

    # 将src文件夹中的CN字形文件复制到data文件夹中
    shutil.copy(path_define.src_dir.joinpath('ZLabsPixel_12px_M_CN.kbitx'), path_define.data_dir)

    # 合并字形，生成对应标准字形的完整版本
    for region in ['HC', 'JP']:
        advanced_merge_kbitx_files(path_define.src_dir.joinpath(f'ZLabsPixel_12px_M_CN.kbitx'),
                                   path_define.src_dir.joinpath(f'ZLabsPixel_12px_M_{region}_diff.kbitx'),
                                   path_define.src_dir.joinpath(f'flags_{region}.txt'),
                                   path_define.data_dir.joinpath(f'ZLabsPixel_12px_M_{region}.kbitx'))
        merge_kbitx_files(path_define.src_dir.joinpath(f'ZLabsPixel_12px_M_CN.kbitx'),
                          path_define.src_dir.joinpath(f'ZLabsPixel_12px_M_{region}_diff.kbitx'),
                          path_define.data_dir.joinpath(f'ZLabsPixel_12px_M_{region}_fallback.kbitx'))

    # 生成字体
    for language_flavor in options.language_flavors:
        kbit_font = KbitFont.load_kbitx(path_define.data_dir.joinpath(f'ZLabsPixel_12px_M_{language_flavor}.kbitx'))


        builder = FontBuilder()
        builder.font_metric.font_size = kbit_font.props.em_height
        builder.font_metric.horizontal_layout.ascent = kbit_font.props.line_ascent
        builder.font_metric.horizontal_layout.descent = -kbit_font.props.line_descent
        builder.font_metric.horizontal_layout.line_gap = 1
        builder.font_metric.vertical_layout.ascent = math.ceil(kbit_font.props.line_height / 2)
        builder.font_metric.vertical_layout.descent = -math.floor(kbit_font.props.line_height / 2)
        builder.font_metric.x_height = kbit_font.props.x_height
        builder.font_metric.cap_height = kbit_font.props.cap_height

        builder.meta_info.version = f"Build_{date_now_f}"
        builder.meta_info.weight_name = WeightName.REGULAR
        builder.meta_info.serif_style = SerifStyle.SERIF
        builder.meta_info.slant_style = SlantStyle.NORMAL
        builder.meta_info.width_style = WidthStyle.MONOSPACED
        builder.meta_info.manufacturer = 'Z Labs Design'
        builder.meta_info.designer = kbit_font.names.designer
        builder.meta_info.description = kbit_font.names.description
        builder.meta_info.copyright_info = kbit_font.names.copyright
        builder.meta_info.license_info = kbit_font.names.license_description
        builder.meta_info.vendor_url = kbit_font.names.vendor_url
        builder.meta_info.designer_url = kbit_font.names.designer_url
        builder.meta_info.license_url = kbit_font.names.license_url
        builder.meta_info.sample_text = kbit_font.names.sample_text

        if language_flavor == 'HC_fallback' or language_flavor == 'JP_fallback':
            builder.meta_info.family_name = kbit_font.names.family + ' FB'
        else:
            builder.meta_info.family_name = kbit_font.names.family

        # 设置像素点转换分辨率
        builder.opentype_config.px_to_units = 100

        k_glyph_notdef = kbit_font.named_glyphs['.notdef']
        builder.glyphs.append(Glyph(
            name='.notdef',
            horizontal_offset=(k_glyph_notdef.x, k_glyph_notdef.y - k_glyph_notdef.height),
            advance_width=k_glyph_notdef.advance,
            vertical_offset=(k_glyph_notdef.width // 2, kbit_font.props.em_ascent - k_glyph_notdef.y),
            advance_height=kbit_font.props.em_height,
            bitmap=[[0 if color <= 127 else 1 for color in bitmap_row] for bitmap_row in k_glyph_notdef.bitmap],
        ))

        for code_point, k_glyph in sorted(kbit_font.characters.items()):
            glyph_name = f'{code_point:04X}'
            builder.character_mapping[code_point] = glyph_name
            builder.glyphs.append(Glyph(
                name=glyph_name,
                horizontal_offset=(k_glyph.x, k_glyph.y - k_glyph.height),
                advance_width=k_glyph.advance,
                vertical_offset=(k_glyph.width // 2, kbit_font.props.em_ascent - k_glyph.y),
                advance_height=kbit_font.props.em_height,
                bitmap=[[0 if color <= 127 else 1 for color in bitmap_row] for bitmap_row in k_glyph.bitmap],
            ))

        # otf_font = builder.to_otf_builder().font
        # fix_mono_mode(otf_font)
        #
        # otf_font.save(path_define.outputs_dir.joinpath(f'ZLabsBitmap_12px_{language_flavor.upper()}.otf'))
        # print(f'Create {language_flavor} otf')
        #
        # otf_font.flavor = 'woff2'
        # otf_font.save(path_define.outputs_dir.joinpath(f'ZLabsBitmap_12px_{language_flavor.upper()}.otf.woff2'))
        # print(f'Create {language_flavor} otf.woff2')

        ttf_font = builder.to_ttf_builder().font
        fix_mono_mode(ttf_font)
        font_name_table_set(ttf_font, language_flavor)

        print(f"Creating ZLabsPixel_12px_M_{language_flavor.upper()}.ttf, please wait…")
        ttf_font.save(path_define.outputs_dir.joinpath(f'ZLabsPixel_12px_M_{language_flavor.upper()}.ttf'))
        print(f'Successfully created ZLabsPixel_12px_M_{language_flavor.upper()}.ttf')

        ttf_font.flavor = 'woff2'
        print(f"Creating ZLabsPixel_12px_M_{language_flavor.upper()}.ttf.woff2, please wait…")
        ttf_font.save(path_define.outputs_dir.joinpath(f'ZLabsPixel_12px_M_{language_flavor.upper()}.ttf.woff2'))
        print(f'Successfully created ZLabsPixel_12px_M_{language_flavor.upper()}.ttf.woff2')

    # for font_format in options.font_formats:
    #     with zipfile.ZipFile(path_define.releases_dir.joinpath(f'ZLabsBitmap_12px_{font_format}.zip'), 'w') as file:
    #         file.write(path_define.project_root_dir.joinpath('LICENSE-OFL'), 'LICENSE')
    #         for font_file_path in path_define.outputs_dir.iterdir():
    #             if font_file_path.name.endswith(f'.{font_format}'):
    #                 file.write(font_file_path, font_file_path.name)
    #     print(f'Create {font_format} zip')


if __name__ == '__main__':
    main()
