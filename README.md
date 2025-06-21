![幻灯片1](https://github.com/user-attachments/assets/9537e38d-ea4f-4de2-b5cb-adc114365bd4)

# Z Labs Bitmap

「Z Labs Bitmap」是一款以 [GNU Unifont](https://www.unifoundry.com/unifont/index.html) 为灵感而制作的小型像素字体。这套字体在 11 * 12 的像素空间（实际占用 12 * 12 像素）中，借鉴了 Unifont 字体的部分特征，同时进行创造性转化而成。

字体目前已基本支持简体中文、繁体中文、日语。本字体遵循中国大陆规范字形，西文字体按等宽规格设计。

> [!WARNING]
> 
> 此字体目前处于字形调整阶段。尽管此字体已经实现了对简、繁体中文及日语必要字符的全面支持，但仍需进行调整与扩充。目前的发布候选版本不代表最终版品质。
> 
> 如果在使用过程中发现了字形错误或不和谐等问题，请及时在 Issues 中反馈。

> [!IMPORTANT]
> 
> 这是一个开源项目，采用 [OFL-1.1](https://openfontlicense.org/open-font-license-official-text/) 许可证授权。您可以免费商用此字体。
> 

## 字体示例

![幻灯片2](https://github.com/user-attachments/assets/d66931b9-2504-4960-b69c-b1b18a37a0a9)

![幻灯片3](https://github.com/user-attachments/assets/ce40b5d9-408c-4681-a7a2-98be7369a9f3)

![幻灯片4](https://github.com/user-attachments/assets/104421ff-dd29-459d-8ad9-e4388a9fa4b8)

![幻灯片5](https://github.com/user-attachments/assets/f1a4ffbb-84de-40ac-b3d1-fceab5ebfb84)

![幻灯片6](https://github.com/user-attachments/assets/9aac6348-38a8-47b7-b84c-dbd0a433a9be)


## 字体覆盖范围
| 字符  | 目前支持情况  | 计划支持情况  |
| :------------: | :------------: | :------------: |
|  简体中文 | 目前支持 GB/T 2312 中规定的所有汉字（共6763个），以及《通用规范汉字表》*¹中的部分汉字（7749个）。目前制作完成的字符可满足大多数简体中文用字需求。| 计划支持《通用规范汉字表》*¹中规定的所有汉字。  |
| 繁体中文和日语汉字*²  |  目前制作了部分繁体中文汉字和日语汉字，已覆盖 Big5 常用汉字表、 JIS X 0213 的第一级汉字和第二级汉字，可满足大多数繁体中文及日语用字需求。 |  未来会支持更多字符。 |
| 扩展区汉字支持 | 除《通用规范汉字表》规定的汉字之外，本字体额外收录了部分扩展区汉字，这些汉字包括地名生僻字（𧒽、𮀎等）、具有独特字形的汉字（𡆢、𦒹、𫯮、𠛸等）、部分类推简化字（𫛸、𮖱、𮹝等）。有关本字体收录的具体扩展区汉字，详见[此处](https://github.com/Astro-2539/ZLabs-Bitmap/blob/main/docs/Plane2Characters.md)。 | 未来视情况添加更多字符。 |
| 平假名和片假名  |  支持（含半角片假名） | -  |
| 拉丁字母  |  支持半角与全角两种格式的英文字母。同时也制作了大写字母的其他形式（🅰🅱等）。 | 未来会增加对其他拉丁字母的支持。  |
| 其他西文字母  |  支持西里尔字母与希腊字母（按半角规格制作）。 | -  |
|  数字 | 包含半角数字和全角数字及 3 种格式的数字序号。  |  - |
| Emoji 符号  | 支持以下字符：♿⛔✅❎㊗️㊙️🆎🆑🆕🆖🆗🆘🆚🈚️🈯️🈲️🈴️🈵️🈶️🈷️️🈸️🈹️🈺️🉐️🉑️🏧💹🔟🔠🔡🔢🚫🚾 （仅支持纯色样式）。 | -  |
| 标点及其他符号 | 目前支持部分的标点及其他字符。 | 未来会增加更多字符。 |

> **注：**
>
> 1.《通用规范汉字表》中的部分简体汉字位于第二平面（如“𤩽”、“𬞟”、“𬱖”、“𩽾”、“𩾌”等），较难输入，而这些汉字的繁体大多位于基本平面，更易输入。本字体也一并为这些汉字制作了繁体支持。
>
> 2.对于繁体中文汉字和日语汉字，本字体仍然按照中国大陆字形标准进行制作，且由于作者精力有限，暂不会推出其他地区字形变体。因此非简体中文使用者应慎重考虑选用本字体。

字体对中文字符的具体支持情况如下：

![CJK_Coverage](https://github.com/user-attachments/assets/6dde212a-cfb1-4189-a067-6ab2dc415697)

本字体在 Unicode 私有区定义了部分字符，详见[此处](https://github.com/Astro-2539/ZLabs-Bitmap/blob/main/docs/PUA.md)。

## 从工程文件构建字体

本字体使用 [Bits'n'Picas](https://github.com/kreativekorp/bitsnpicas) 制作。下面是如何从工程文件 [（ZLabsBitmap.kbitx）](https://github.com/Astro-2539/ZLabs-Bitmap/blob/main/ZLabsBitmap.kbitx) 构建并发布字体的过程。

过程中使用了 Bits'n'Picas （用于将工程文件转换为第一级 TTF）、FontForge（用于编辑数据并生成第二级 TTF）和[utils/fix_mono](https://github.com/Astro-2539/ZLabs-Bitmap/tree/main/utils/fix_mono)下的 `fix_mono.py`（用于修复等宽字体间距问题）。

1. 在 Bits'n'Picas 所在文件夹下运行下列命令：
```
java -jar BitsNPicas.jar convertbitmap -f ttf -o "ZLabsBitmap_nightly.ttf" "ZLabsBitmap.kbitx"
```
或打开 `BitsNPicas.jar` 通过 GUI 界面将字体导出为 PDF。
> **注意：**
>
>  通过 Bits'n'Picas 生成的 TTF 文件无法在大多数软件中使用。因此考虑通过下面的步骤对字体进行调整。注意调整的方式并不唯一。如果您愿意，您也可以通过命令行等其他方式对字体进行调整。

2. 使用 FontForge 软件打开上一步中生成的 TTF 字体。
    1. 在“PS字形名称”选项卡中，将“粗细”更改为 Regular。
    2. 在“一般”选项卡中，勾选“有垂直尺寸”选项。
    3. 在“OS/2”的“其他”选项卡中，将“OS/2版本”改为4，将“粗细类属”改为400，将“PFM字族”改为等宽体。
    4. 在“OS/2”的“尺寸”选项卡中，将“Typo Linegap”和“HHead Linegap”改为100。
       > 此步骤的目的是增加默认行间距，以避免纵向粘连问题。
    5. 在“OS/2”的“特征”选项卡中，将“比例”属性改为“单一间距。
       > 本字体制作时按照等宽规格制作。此步骤的目的是为字体声明“等宽”属性，以使得该字体可在对“等宽”属性有要求的软件中使用。
       >
       > 声明此属性后，如果直接导出，会出现字符间距异常的问题。因此，稍后将通过 `fix_mono` 解决此问题。
    6. 在“OS/2”的“字符集”选项卡中，在微软编码页中勾选“默认”。
    7. 按需求修改其他属性，并导出第二级 TTF。

3. 将上一步导出的 TTF 文件放入`utils/fonts/TTF`中，并运行 `utils/fix_mono/build.bat` 修复字符间距问题。生成的新文件会覆盖原有文件。此时的字体可正常安装使用。
    



## 字体授权
Z Labs Bitmap 遵循 [SIL Open Font License 1.1](https://openfontlicense.org/open-font-license-official-text/) 许可协议。您可以将此字体用于包含商用与嵌入式使用在内的多种用途，而无须取得字体作者的授权。

再分发此字体时，您应当注明 OFL 授权协议的原文或链接。

根据 OFL 协议，如使用此字体制作衍生字体，那么衍生字体也必须同样遵循 OFL 协议。您不得单独售卖此字体。

作者保留字体名称「Z工坊 / Z Labs」。

如使用过程中出现任何问题或有任何建议，您可以添加 issue 进行反馈。
