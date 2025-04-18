![Title](https://github.com/user-attachments/assets/73d855e7-76af-42ce-bd8e-da862a5aae51)
# Z Labs Bitmap
「Z Labs Bitmap」是一款仿 [GNU Unifont](https://www.unifoundry.com/unifont/index.html) 风格的小型像素字体。这套字体在 11 * 12 的像素空间（实际占用 12 * 12 像素）中，尽可能还原了 Unifont 字体的特色。

本字体遵循中国大陆标准规范字形，西文字体按等宽规格设计，同时字体被设置为具有“等宽”属性，可在某些对字体属性有要求的软件中使用。

> **注意：** 此字体目前处于字形调整阶段。尽管此字体已经实现了对简体中文必要字符（GB/T 2312）的全面支持，但仍需对部分字形进行调整。目前的发布候选版本不代表最终版品质。

> **提示：** 本字体为开源项目，采用 OFL 许可证授权，您可以免费商用此字体（详见「授权」一节）。

## 字体示例
（由于字形大规模调整，此处示例待更新）
中文示例：
![Sample-2](https://github.com/user-attachments/assets/a6a15eea-adb1-49a5-b8bc-24d10546c1de)

日文示例（目前对日文的支持十分有限）：
![Sample-1](https://github.com/user-attachments/assets/2ff7acd3-24b3-4860-ab90-323494221366)



## 字体覆盖范围
| 字符  | 目前支持情况  | 计划支持情况  |
| :------------: | :------------: | :------------: |
|  简体中文 | 目前支持 GB/T 2312 中规定的所有汉字（共6763个），以及《通用规范汉字表》*¹中的部分汉字（6880个）。目前制作完成的字符可满足大多数简体中文用字需求。| 计划支持《通用规范汉字表》*¹中规定的所有汉字。  |
| 繁体中文和日语汉字*²  |  目前仅制作了少量的繁体中文汉字和日语汉字。 |  未来可能会实现对繁体中文和日语的基本支持。 |
| 扩展区汉字支持 | 除《通用规范汉字表》规定的汉字之外，本字体额外收录了部分扩展区汉字，这些汉字包括地名生僻字（𧒽、𮀎等）、具有独特字形的汉字（𡆢、𦒹、𫯮、𠛸等）、部分类推简化字（𫛸、𮖱、𮹝等）。有关本字体收录的具体扩展区汉字，详见[此处](https://github.com/Astro-2539/ZLabs-Bitmap/blob/main/docs/Plane2Characters.md)。 | 未来视情况添加更多字符。 |
| 平假名和片假名  |  支持（含半角片假名） | -  |
| 拉丁字母  |  支持半角与全角两种格式的英文字母。同时也制作了大写字母的其他形式（🅰🅱等）。 | 未来会增加对其他拉丁字母的支持。  |
| 其他西文字母  |  支持西里尔字母与希腊字母（按半角规格制作）。 | -  |
|  数字 | 包含半角数字和全角数字及 3 种格式的数字序号。  |  - |
| Emoji 符号  | 支持以下字符：♿⛔✅❎㊗️㊙️🆎🆑🆕🆖🆗🆘🆚🈚️🈯️🈲️🈴️🈵️🈶️🈷️️🈸️🈹️🈺️🉐️🉑️🏧💹🔟🔠🔡🔢🚫🚾 （仅支持纯色样式）。 | -  |
| 标点及其他符号 | 目前仅支持少量的标点及其他字符。 | 未来会增加更多字符。 |

> **注：**
>
> 1.《通用规范汉字表》中的部分简体汉字位于第二平面（如“𤩽”、“𬞟”、“𬱖”、“𩽾”、“𩾌”等），较难输入，而这些汉字的繁体大多位于基本平面，更易输入。本字体也一并为这些汉字制作了繁体支持。
>
> 2.对于繁体中文汉字和日语汉字，本字体仍然按照中国大陆字形标准进行制作，且由于作者精力有限，暂不会推出其他地区字形变体。因此非简体中文使用者应慎重考虑选用本字体。

字体对中文字符的具体支持情况如下：

<img width="640" alt="CJK_Coverage" src="https://github.com/user-attachments/assets/85eeca20-bfae-4bc3-ac37-47847c8b6f8f" />




本字体在 Unicode 私有区定义了部分字符，详见[此处](https://github.com/Astro-2539/ZLabs-Bitmap/blob/main/docs/PUA.md)。




## 字体授权
Z Labs Bitmap 遵循 [SIL Open Font License 1.1](https://openfontlicense.org/open-font-license-official-text/) 许可协议。您可以将此字体用于包含商用与嵌入式使用在内的多种用途，而无须取得字体作者的授权。

再分发此字体时，您应当注明 OFL 授权协议的原文或链接。

根据 OFL 协议，如使用此字体制作衍生字体，那么衍生字体也必须同样遵循 OFL 协议。您不得单独售卖此字体。

作者保留字体名称「Z工坊 / Z Labs」。

如使用过程中出现任何问题或有任何建议，您可以添加 issue 进行反馈。
