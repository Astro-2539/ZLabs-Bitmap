[简体中文](/README.md) | **English** | [日本語](/README_JP.md)

![Title](/img/title.png "Title")

# Z Labs Bitmap 12px

> [!IMPORTANT]
>
> **This article is translated by artificial intelligence. Please refer to the original text in Simplified Chinese.**
>

「Z Labs Bitmap 12px」is a 12px pixel font that supports three glyph styles: Mainland China, Hong Kong (China), and Japan. Western characters are designed in a monospaced specification.



> [!WARNING]
> 
> This font is currently in the glyph adjustment phase. Although it has achieved comprehensive support for necessary characters in Simplified Chinese, Traditional Chinese, and Japanese, some characters still need to be adjusted. The current release candidate does not represent the quality of the final version.
> 
> If you find glyph errors or other issues during use, please feedback them in Issues in a timely manner.

> [!IMPORTANT]
> 
> This is an open-source project, and the font part is licensed under the [OFL-1.1](https://openfontlicense.org/open-font-license-official-text/) license. When using this font, there is no need to purchase additional licenses from the author (including commercial use, embedded use in apps/hardware, etc.).
> 

## Font Examples

![Sample 1](/img/Sample_1.PNG "Sample 1")

![Sample 2](/img/Sample_2.PNG "Sample 2")

![Sample 3](/img/Sample_3.PNG "Sample 3")

![Periodic Table](/img/periodic-table.png "Periodic Table")

## Glyph Variants

> [!IMPORTANT]
> 
> It is crucial to select the appropriate font when localizing a project. We recommend using the CN version for Simplified Chinese, the HC version for Traditional Chinese, and the JP version for Japanese.
> 
> Since the Western text parts of the three are the same, any variant version can be used for the localization of languages such as English and French (but some symbols are drawn according to Chinese usage habits).
> 

This font has three variants: CN (Mainland China glyph standard), HC (Hong Kong, China glyph standard) and JP (Japanese glyph standard), which can meet the needs of different language environments.

![Multi-Language Varient](/img/MultiLanguage.PNG "Multi-Language Varient")


## Font Coverage

### Chinese Characters

The Chinese character support varies among different versions of the font. The production plans and specific support situations for each version variant are listed below.


#### Mainland China Variant (CN)

&nbsp;&nbsp;&nbsp;&nbsp;✅ GB/T 2312 (6763 / 6763)

&nbsp;&nbsp;&nbsp;&nbsp;✅ "General Standard Chinese Characters Table"（通用规范汉字表） (8105 / 8105)

&nbsp;&nbsp;&nbsp;&nbsp;✅ Big5 Common Chinese Characters Table (5401 / 5401)

&nbsp;&nbsp;&nbsp;&nbsp;✅ "Common National Standard Font Table"（常用国字标准字体表） (4808 / 4808)

&nbsp;&nbsp;&nbsp;&nbsp;✅ GB/T 12345 (6866 / 6866)

&nbsp;&nbsp;&nbsp;&nbsp;✅ JIS X 0208 (6355 / 6355)

&nbsp;&nbsp;&nbsp;&nbsp;ℹ️ Total Chinese characters supported: 12926

#### Hong Kong, China Variant (HC)

&nbsp;&nbsp;&nbsp;&nbsp;✅ "Common National Standard Font Table" (4808 / 4808)

&nbsp;&nbsp;&nbsp;&nbsp;✅ Big5 Common Chinese Characters Table (5401 / 5401)

&nbsp;&nbsp;&nbsp;&nbsp;✅ GB/T 12345 (6866 / 6866)

&nbsp;&nbsp;&nbsp;&nbsp;✅ JIS X 0208 (6355 / 6355)

&nbsp;&nbsp;&nbsp;&nbsp;ℹ️ Total Chinese characters supported: 9977

#### Japanese Variant (JP)

&nbsp;&nbsp;&nbsp;&nbsp;✅ JIS X 0208 (Level 1 and Level 2 characters) (6355 / 6355)

&nbsp;&nbsp;&nbsp;&nbsp;ℹ️ Total Chinese characters supported: 6364

#### Font Fallback

Due to the limited energy of the author, currently only some Chinese characters have been produced for the HC and JP versions, so you may encounter missing Chinese characters during use.

If the software supports the font fallback mechanism, you can set the `font_family` or similar properties to make the CN variant, which supports more Chinese characters, serve as the fallback font for HC/JP, so that the CN variant can display the Chinese characters that HC/JP do not yet support.

If the software does not support this mechanism, you can consider using the `Fallback` (FB) version of the corresponding variant. In this version, the Chinese characters already supported by the HC/JP variants will remain unchanged; for the Chinese characters that have been produced in the CN variant but not in HC/JP, the CN glyphs will be used to fill the corresponding code positions (regardless of whether the character is in the HC/JP production plan), so that the number of supported Chinese characters is the same as that of the CN version (glyph consistency is not guaranteed).


## Building the Font from Project Files

This font is created using [Bits'n'Picas](https://github.com/kreativekorp/bitsnpicas). Run `./tools/build.py` to generate the font.

The building process depends on the `fonttools` library, `pixel_font_builder` library, and `kbitfont` library.

For details of the building process, please refer to the readme file in the `Tools` folder.
    

## Font License

The license of this project is divided into two parts: "Fonts" and "Building Code".

### Fonts

Licensed under the [SIL Open Font License 1.1](https://openfontlicense.org/open-font-license-official-text/).

You can use this font for various purposes including commercial use and embedded use without obtaining additional licenses from the author.

When redistributing this font, you should indicate the original text or link of the OFL license agreement.

According to the OFL agreement, if derivative fonts are made using this font, the derivative fonts must also comply with the OFL agreement. You are not allowed to sell this font separately.

The author reserves the font name "Z工坊 / Z Labs".

### Building Code

Licensed under the MIT License.


## Acknowledgments

[Bits'N'Picas](https://github.com/kreativekorp/bitsnpicas) provides pixel glyph editing software.

[@狼人小林（TakWolf）](https://github.com/TakWolf) provides technical support.

## Related Resources

[字统网](https://zi.tools/) - A website covering the origin, form, pronunciation, meaning, and codes of Chinese characters