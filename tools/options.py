from typing import Literal, get_args

type LanguageFlavor = Literal[
    'CN',
    'HC',
    'HC_fallback',
    'JP',
    'JP_fallback',
]
language_flavors = list[LanguageFlavor](get_args(LanguageFlavor.__value__))

type FontFormat = Literal[
    'otf',
    'otf.woff',
    'otf.woff2',
    'ttf',
    'ttf.woff',
    'ttf.woff2',
]
font_formats = list[FontFormat](get_args(FontFormat.__value__))
