**简体中文** | [English](/README_EN.md) | [日本語](/README_JP.md)

![标题](/img/title.png "Title")

# Z Labs Bitmap 12px

「Z Labs Bitmap 12px」是一款规格为 12px 的像素字体，具有中国大陆、中国香港、日本三种变体字形，西文字体按等宽规格设计。

字体目前已基本支持简体中文、繁体中文、日语。

> [!WARNING]
> 
> 我们对字体文件进行了更名。安装新版本后，由于字体名称不同，与旧版本可以共存。
>
> 更新字体后，请您手动在软件中选择更名后的新字体。

> [!WARNING]
> 
> 此字体目前处于字形调整阶段。尽管此字体已经实现了对简、繁体中文及日语必要字符的全面支持，但仍需进行调整与扩充。目前的发布候选版本不代表最终版品质。
> 
> 如果在使用过程中发现了字形错误或不和谐等问题，请及时在 Issues 中反馈。

> [!IMPORTANT]
> 
> 这是一个开源项目，字体部分采用 [OFL-1.1](https://openfontlicense.org/open-font-license-official-text/) 许可证授权。您可以免费商用此字体。
> 

## 字体示例

![示例1](/img/Sample_1.PNG "Sample 1")

![示例2](/img/Sample_2.PNG "Sample 2")

![示例3](/img/Sample_3.PNG "Sample 3")

![元素周期表](/img/periodic-table.png "元素周期表")

## 字形变体

本字体具有CN（陆标）、HC（港标）、JP（日标）三种变体，可满足不同环境下的使用需求。

![变体字形](/img/MultiLanguage.PNG "Multi-Language Varient")


## 字体覆盖范围

### 汉字

本字体不同版本变体的汉字支持情况不同。下面列出了每个版本变体的制作计划与具体支持情况。

#### 中国大陆变体字形（CN）

&nbsp;&nbsp;&nbsp;&nbsp;✅ GB/T 2312 （6763 / 6763）

&nbsp;&nbsp;&nbsp;&nbsp;✅ 《通用规范汉字表》（8105 / 8105）

&nbsp;&nbsp;&nbsp;&nbsp;✅ Big5 常用汉字表（5401 / 5401）

&nbsp;&nbsp;&nbsp;&nbsp;✅《常用国字标准字体表》（4808 / 4808）

&nbsp;&nbsp;&nbsp;&nbsp;✅ GB/T 12345（6866 / 6866）

&nbsp;&nbsp;&nbsp;&nbsp;✅《通用规范汉字表》附件 1：「规范字与繁体字、异体字对照表」中的繁体字列（2563 / 2563）

&nbsp;&nbsp;&nbsp;&nbsp;✅ JIS X 0208（6355 / 6355）

&nbsp;&nbsp;&nbsp;&nbsp;ℹ️ 共计支持汉字：12926

#### 中国香港变体字形（HC）

&nbsp;&nbsp;&nbsp;&nbsp;✅《常用国字标准字体表》（4808 / 4808）

&nbsp;&nbsp;&nbsp;&nbsp;✅ Big5 常用汉字表（5401 / 5401）

&nbsp;&nbsp;&nbsp;&nbsp;✅ GB/T 12345（6866 / 6866）

&nbsp;&nbsp;&nbsp;&nbsp;✅《通用规范汉字表》附件 1：「规范字与繁体字、异体字对照表」中的繁体字列（2563 / 2563）

&nbsp;&nbsp;&nbsp;&nbsp;✅ JIS X 0208（6355 / 6355）

&nbsp;&nbsp;&nbsp;&nbsp;ℹ️ 共计支持汉字：9977

#### 日本变体字形（JP）

&nbsp;&nbsp;&nbsp;&nbsp;✅ JIS X 0208（6355 / 6355）

&nbsp;&nbsp;&nbsp;&nbsp;ℹ️ 共计支持汉字：6364

&nbsp;&nbsp;&nbsp;&nbsp;⚠️ 鉴于日语对汉字需求较小，若无特殊情况，日标字形将不再制作新的汉字字符。

#### 字体回退

由于作者精力有限，目前 HC 版与 JP 版仅制作了部分汉字，因此在使用中可能会遇到缺失汉字的情况。

若软件支持多字体排版，可以通过设置 `font_family` 或类似属性，使支持汉字数更多的 CN 变体作为 HC/JP 的后备字体，从而让 CN 变体显示 HC/JP 暂未支持的汉字。

若软件不支持多字体，可以考虑使用对应变体的 `Fallback` （FB）版本。在这个版本中，对于 HC/JP 变体已支持的汉字，将维持原样；对于 CN 变体已经制作而 HC/JP 未制作的汉字，将使用 CN 字形填充对应的码位（无论这个字是否在 HC/JP 制作计划中），使得支持汉字的数目与 CN 版一致（不保证字形正确性）。

### 其他字符

注：三种字形变体的西文与符号部分保持一致（部分中文标点除外）。

| 字符  | 目前支持情况  | 计划支持情况  |
| :------------: | :------------: | :------------: |
| 平假名和片假名  |  支持（含半角片假名） | -  |
| 拉丁字母  |  支持半角与全角两种格式的英文字母。同时也制作了大写字母的其他形式（🅰🅱等）。 | 未来会增加对其他拉丁字母的支持。  |
| 其他西文字母  |  支持西里尔字母与希腊字母（按半角规格制作）。 | -  |
|  数字 | 包含半角数字和全角数字及 3 种格式的数字序号。  |  - |
| Emoji 符号  | 支持以下字符：♿⛔✅❎㊗️㊙️🆎🆑🆕🆖🆗🆘🆚🈚️🈯️🈲️🈴️🈵️🈶️🈷️️🈸️🈹️🈺️🉐️🉑️🏧💹🔟🔠🔡🔢🚫🚾 （仅支持纯色样式）。 | -  |
| 标点及其他符号 | 目前支持部分的标点及其他字符。 | 未来会增加更多字符。 |
| 私用区 | 本字体在 Unicode 私用区定义了部分字符，详见[此处](https://github.com/Astro-2539/ZLabs-Bitmap/blob/main/docs/PUA.md)。| -  |


## 从工程文件构建字体

本字体使用 [Bits'n'Picas](https://github.com/kreativekorp/bitsnpicas) 制作。运行 `./tools/build.py` 即可生成字体。

构建流程依赖 `fonttools` 库、`pixel_font_builder` 库和 `kbitfont` 库。

构建流程详见 `Tools` 文件夹下的自述文件。
    

## 字体授权

本项目授权分为「字体」及「构建代码」两部分。

### 字体

使用 [SIL Open Font License 1.1](https://openfontlicense.org/open-font-license-official-text/) 许可证授权。

您可以将此字体用于包含商用与嵌入式使用在内的多种用途，而无须取得字体作者的额外授权。

再分发此字体时，您应当注明 OFL 授权协议的原文或链接。

根据 OFL 协议，如使用此字体制作衍生字体，那么衍生字体也必须同样遵循 OFL 协议。您不得单独售卖此字体。

作者保留字体名称「Z工坊 / Z Labs」。

### 构建代码

使用 MIT 许可证授权。


## 鸣谢

[Bits'N'Picas](https://github.com/kreativekorp/bitsnpicas) 提供像素字形编辑软件。

[@狼人小林](https://github.com/TakWolf) 提供技术支持。

## 相关资料

[字统网](https://zi.tools/) - 漢字源、形、音、義、碼网羅站點
