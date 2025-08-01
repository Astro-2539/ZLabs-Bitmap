import math
import shutil
import zipfile

from fontTools.ttLib import TTFont
from kbitfont import KbitFont
from pixel_font_builder import FontBuilder, WeightName, SerifStyle, SlantStyle, WidthStyle, Glyph

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


def main():
    if path_define.build_dir.exists():
        shutil.rmtree(path_define.build_dir)
    path_define.outputs_dir.mkdir(parents=True)
    path_define.releases_dir.mkdir(parents=True)

    shutil.copy(path_define.src_dir.joinpath('ZLabsBitmapCN.kbitx'), path_define.data_dir)
    for region in ['HC', 'JP']:
        advanced_merge_kbitx_files(path_define.src_dir.joinpath(f'ZLabsBitmapCN.kbitx'),
                                   path_define.src_dir.joinpath(f'ZLabsBitmap{region}_diff.kbitx'),
                                   path_define.src_dir.joinpath(f'flags_{region}.txt'),
                                   path_define.data_dir.joinpath(f'ZLabsBitmap{region}.kbitx'))
        merge_kbitx_files(path_define.src_dir.joinpath(f'ZLabsBitmapCN.kbitx'),
                          path_define.src_dir.joinpath(f'ZLabsBitmap{region}_diff.kbitx'),
                          path_define.data_dir.joinpath(f'ZLabsBitmap{region}_fallback.kbitx'))


    for language_flavor in options.language_flavors:
        kbit_font = KbitFont.load_kbitx(path_define.data_dir.joinpath(f'ZLabsBitmap{language_flavor}.kbitx'))


        builder = FontBuilder()
        builder.font_metric.font_size = kbit_font.props.em_height
        builder.font_metric.horizontal_layout.ascent = kbit_font.props.line_ascent
        builder.font_metric.horizontal_layout.descent = -kbit_font.props.line_descent
        builder.font_metric.horizontal_layout.line_gap = 1
        builder.font_metric.vertical_layout.ascent = math.ceil(kbit_font.props.line_height / 2)
        builder.font_metric.vertical_layout.descent = -math.floor(kbit_font.props.line_height / 2)
        builder.font_metric.x_height = kbit_font.props.x_height
        builder.font_metric.cap_height = kbit_font.props.cap_height

        builder.meta_info.version = kbit_font.names.version
        builder.meta_info.weight_name = WeightName.REGULAR
        builder.meta_info.serif_style = SerifStyle.SERIF
        builder.meta_info.slant_style = SlantStyle.NORMAL
        builder.meta_info.width_style = WidthStyle.MONOSPACED
        builder.meta_info.manufacturer = kbit_font.names.manufacturer
        builder.meta_info.designer = kbit_font.names.designer
        builder.meta_info.description = kbit_font.names.description
        builder.meta_info.copyright_info = kbit_font.names.copyright
        builder.meta_info.license_info = kbit_font.names.license_description
        builder.meta_info.vendor_url = kbit_font.names.vendor_url
        builder.meta_info.designer_url = kbit_font.names.designer_url
        builder.meta_info.license_url = kbit_font.names.license_url
        builder.meta_info.sample_text = kbit_font.names.sample_text

        if language_flavor == 'HC_fallback' or language_flavor == 'JP_fallback':
            builder.meta_info.family_name = kbit_font.names.family + ' Fallback'
        else:
            builder.meta_info.family_name = kbit_font.names.family


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

        otf_font = builder.to_otf_builder().font
        fix_mono_mode(otf_font)

        otf_font.save(path_define.outputs_dir.joinpath(f'ZLabsBitmap{language_flavor.upper()}.otf'))
        print(f'Create {language_flavor} otf')

        otf_font.flavor = 'woff'
        otf_font.save(path_define.outputs_dir.joinpath(f'ZLabsBitmap{language_flavor.upper()}.otf.woff'))
        print(f'Create {language_flavor} otf.woff')

        otf_font.flavor = 'woff2'
        otf_font.save(path_define.outputs_dir.joinpath(f'ZLabsBitmap{language_flavor.upper()}.otf.woff2'))
        print(f'Create {language_flavor} otf.woff2')

        ttf_font = builder.to_ttf_builder().font
        fix_mono_mode(ttf_font)

        ttf_font.save(path_define.outputs_dir.joinpath(f'ZLabsBitmap{language_flavor.upper()}.ttf'))
        print(f'Create {language_flavor} ttf')

        ttf_font.flavor = 'woff'
        ttf_font.save(path_define.outputs_dir.joinpath(f'ZLabsBitmap{language_flavor.upper()}.ttf.woff'))
        print(f'Create {language_flavor} ttf.woff')

        ttf_font.flavor = 'woff2'
        ttf_font.save(path_define.outputs_dir.joinpath(f'ZLabsBitmap{language_flavor.upper()}.ttf.woff2'))
        print(f'Create {language_flavor} ttf.woff2')

    for font_format in options.font_formats:
        with zipfile.ZipFile(path_define.releases_dir.joinpath(f'ZLabsBitmap-{font_format}.zip'), 'w') as file:
            file.write(path_define.project_root_dir.joinpath('LICENSE-OFL'), 'LICENSE')
            for font_file_path in path_define.outputs_dir.iterdir():
                if font_file_path.name.endswith(f'.{font_format}'):
                    file.write(font_file_path, font_file_path.name)
        print(f'Create {font_format} zip')


if __name__ == '__main__':
    main()
