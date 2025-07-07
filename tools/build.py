import math
import shutil
import zipfile

from fontTools.ttLib import TTFont
from kbitfont import KbitFont
from pixel_font_builder import FontBuilder, WeightName, SerifStyle, SlantStyle, WidthStyle, Glyph

from tools import path_define, options


def fix_mono_mode(font: TTFont):
    font['OS/2'].xAvgCharWidth = 600
    font['post'].isFixedPitch = 1


def main():
    if path_define.build_dir.exists():
        shutil.rmtree(path_define.build_dir)
    path_define.outputs_dir.mkdir(parents=True)
    path_define.releases_dir.mkdir(parents=True)

    kbit_font_sc = KbitFont.load_kbitx(path_define.src_dir.joinpath('sc.kbitx'))
    for language_flavor in options.language_flavors:
        if language_flavor == 'sc':
            kbit_font = kbit_font_sc
        else:
            kbit_font = KbitFont.load_kbitx(path_define.src_dir.joinpath(f'{language_flavor}-patch.kbitx'))
            kbit_font.named_glyphs['.notdef'] = kbit_font_sc.named_glyphs['.notdef']
            characters = dict(kbit_font_sc.characters)
            characters.update(kbit_font.characters)
            kbit_font.characters = characters

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
        builder.meta_info.family_name = kbit_font.names.family
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
            file.write(path_define.project_root_dir.joinpath('LICENSE'), 'LICENSE')
            for font_file_path in path_define.outputs_dir.iterdir():
                if font_file_path.name.endswith(f'.{font_format}'):
                    file.write(font_file_path, font_file_path.name)
        print(f'Create {font_format} zip')

    if path_define.www_fonts_dir.exists():
        shutil.rmtree(path_define.www_fonts_dir)
    path_define.www_fonts_dir.mkdir(parents=True)

    for font_file_path in path_define.outputs_dir.iterdir():
        if font_file_path.name.endswith('.otf.woff2'):
            shutil.copyfile(font_file_path, path_define.www_fonts_dir.joinpath(font_file_path.name))
    print('Update www/fonts')


if __name__ == '__main__':
    main()
