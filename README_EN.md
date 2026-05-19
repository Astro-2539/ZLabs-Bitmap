[简体中文](/README.md) | **English** | [日本語](/README_JP.md)

> [!IMPORTANT]
> 
> This article is translated by artificial intelligence.
> 

# Z Labs Pixel 12px

![Title](/img/title_short_EN.png "Title")

> [!WARNING]
> 
> The name of this font family has been changed from "Z Labs Bitmap 12px" to "Z Labs Pixel 12px" (see [#2](https://github.com/Astro-2539/ZLabs-Bitmap/issues/2) for details).
>
> After installing the new version of the font, **you need to manually switch to the font with the new name in the software** to apply the font update. We apologize for any inconvenience caused.
> 
> If you have any questions or suggestions, please reply in this Issue.

Z Labs Pixel 12px is a pixel font with specifications of 11*12px, adopting a sans-serif font style. It has three variant glyphs for Mainland China, Hong Kong (China), and Japan, and the Western characters are designed in a monospaced specification.

The font currently basically supports daily use of Simplified Chinese, Traditional Chinese, and Japanese.

> [!WARNING]
> 
> The author is not a professional designer, so the font may have issues such as inconsistent glyph harmony and style. Please understand.
> 
> If you encounter any problems during use, please provide feedback in the Issues in a timely manner.

> [!IMPORTANT]
> 
> This is an open-source project, and the font part is licensed under the [OFL-1.1](https://openfontlicense.org/open-font-license-official-text/) license. You can use this font commercially for free.
> 

## Font Examples

![Sample 1](/img/Sample.png "Sample 1")

![Periodic Table of Elements](/img/periodic-table.png "Periodic Table of Elements")

## Glyph Variants

This font has three variants: CN (complying with Mainland China standards), HC (complying with Hong Kong (China) standards), and JP (complying with JIS X 0213:2004 standards), which can meet the usage requirements in different environments.

> [!IMPORTANT]
> 
> Due to different character usage habits in different regions, it is very important to choose an appropriate glyph variant. We recommend that you select the CN variant in the Simplified Chinese environment, the HC variant in the Traditional Chinese environment, and the JP variant in the Japanese environment.
>
> For Traditional Chinese users, if you cannot accept the Hong Kong (China) glyph standards, we recommend using other fonts.
> 

## Font Coverage

### Chinese Characters

The Chinese character support of different variants of this font varies. The production plan and specific support status of each variant are listed below.

#### Mainland China Variant Glyphs (CN)

&nbsp;&nbsp;&nbsp;&nbsp;✅ GB/T 2312 （6763 / 6763）

&nbsp;&nbsp;&nbsp;&nbsp;✅ *Table of General Standard Chinese Characters* (8105 / 8105)

&nbsp;&nbsp;&nbsp;&nbsp;✅ Big5 Common Chinese Character List (5401 / 5401)

&nbsp;&nbsp;&nbsp;&nbsp;✅ *Table of Standard Forms of Common National Characters* (4808 / 4808)

&nbsp;&nbsp;&nbsp;&nbsp;✅ GB/T 12345（6866 / 6866）

&nbsp;&nbsp;&nbsp;&nbsp;✅ The Traditional Chinese characters column in "Appendix 1: Comparison Table of Standard Characters, Traditional Characters, and Variant Characters" of *The Table of General Standard Chinese Characters* (2563 / 2563)

&nbsp;&nbsp;&nbsp;&nbsp;✅ jf7000 Priority Character Set Basic Package (6373 / 6373)

&nbsp;&nbsp;&nbsp;&nbsp;✅ JIS X 0208（6355 / 6355）

&nbsp;&nbsp;&nbsp;&nbsp;ℹ️ Total Chinese characters supported: 12994

#### Hong Kong (China) Variant Glyphs (HC)

&nbsp;&nbsp;&nbsp;&nbsp;✅ *Table of Standard Forms of Common National Characters* (4808 / 4808)

&nbsp;&nbsp;&nbsp;&nbsp;✅ Big5 Common Chinese Character List (5401 / 5401)

&nbsp;&nbsp;&nbsp;&nbsp;✅ GB/T 12345（6866 / 6866）

&nbsp;&nbsp;&nbsp;&nbsp;✅ The Traditional Chinese characters column in "Appendix 1: Comparison Table of Standard Characters, Traditional Characters, and Variant Characters" of *The Table of General Standard Chinese Characters* (2563 / 2563)

&nbsp;&nbsp;&nbsp;&nbsp;✅ jf7000 Priority Character Set Basic Package (6373 / 6373)

&nbsp;&nbsp;&nbsp;&nbsp;✅ JIS X 0208（6355 / 6355）

&nbsp;&nbsp;&nbsp;&nbsp;ℹ️ Total Chinese characters supported: 10082

#### Japanese Variant Glyphs (JP)

&nbsp;&nbsp;&nbsp;&nbsp;✅ JIS X 0208（6355 / 6355）

&nbsp;&nbsp;&nbsp;&nbsp;ℹ️ Total Chinese characters supported: 6365

&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Considering the relatively small demand for Chinese characters in Japanese, no new Chinese character glyphs will be created for the Japanese standard variant unless there are special circumstances.

#### Font Fallback

Due to the limited energy of the author, only some Chinese characters have been created for the HC and JP versions, so missing Chinese characters may be encountered during use.

If the software supports multi-font typesetting, you can set the `font_family` or similar attributes to make the CN variant, which supports more Chinese characters, serve as the fallback font for HC/JP, so that the CN variant displays Chinese characters not yet supported by HC/JP.

If the software does not support multiple fonts, you can consider using the `Fallback` (FB) version of the corresponding variant. In this version, the glyphs of Chinese characters already supported by the HC/JP variants will remain unchanged; for Chinese characters that have been created in the CN variant but not in the HC/JP variants, the CN glyphs will be used to fill the corresponding code positions (regardless of whether the character is in the HC/JP production plan), making the number of supported Chinese characters consistent with the CN version (glyph correctness is not guaranteed).

## Building the Font from Project Files

This font is created using [Bits'n'Picas](https://github.com/kreativekorp/bitsnpicas). Run `./tools/build.py` to generate the font.

The build process depends on the `fonttools` library, `pixel_font_builder` library, and `kbitfont` library.

For details of the build process, see the README file in the `Tools` folder.
    

## Font License

The license of this project is divided into two parts: "glyphs" and "build code".

### Glyphs

Licensed under the [SIL Open Font License 1.1](https://openfontlicense.org/open-font-license-official-text/).

You can use this font for various purposes including commercial and embedded use without obtaining additional authorization from the font author.

When redistributing this font, you shall indicate the original text or link of the OFL license agreement.

According to the OFL agreement, if you create a derivative font using this font, the derivative font must also comply with the OFL agreement. You are not allowed to sell this font separately.

The author reserves the font names "Z工坊" and "Z Labs".

### Build Code

Licensed under the MIT License.

## Acknowledgments

[Bits'N'Picas](https://github.com/kreativekorp/bitsnpicas) provides pixel glyph editing software.

[@TakWolf](https://github.com/TakWolf) provides technical support.

## Related Resources

[Zi.Tools](https://zi.tools/) - A website collecting the origin, form, pronunciation, meaning, and encoding of Chinese characters.

## Project Stars Statistics

[![Stargazers over time](https://starchart.cc/Astro-2539/ZLabs-Bitmap.svg?variant=adaptive)](https://starchart.cc/Astro-2539/ZLabs-Bitmap)