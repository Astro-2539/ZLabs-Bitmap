# Source 文件夹

该文件夹存储字体源文件与共通字形表。

有关字体的生成原理，请参阅`tools`文件夹下的自述文件。

**如需对字体进行二次创作，请修改此文件夹中的文件。**

### ZLabsBitmapCN.kbitx

该文件为中国大陆变体字形（CN）的源工程文件，亦是其他变体字形的基础文件。

该文件存储了系列字体的所有西文字符、符号及所有的陆标汉字字符。

### ZLabsBitmapHC_diff.kbitx / ZLabsBitmapJP_diff.kbitx

该文件为中国香港变体字形（HC）/日本变体字形（JP）的源工程文件之一。

该文件**仅存储**与中国大陆字形有差异的汉字及符号，不能单独生成字体。

需要配合`ZLabsBitmapCN.kbitx`及`flags_HC.txt`/`flags_JP.txt`以生成完整字体。

### flags_HC.txt / flags_JP.txt

该文件为中国香港变体字形（HC）/日本变体字形（JP）的源工程文件之一。

该文件为港标/日标字形与陆标字形的共通字形表，存储了与陆标相同字形的 Unicode 值。

字体构建过程将使用这些文件。
