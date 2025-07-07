
window.onFontChange = fontName => {
    const fontFamily = `ZLabsBitmap${fontName}, serif`
    document.getElementById('title').style.fontFamily = fontFamily
    document.getElementById('input-box').style.fontFamily = fontFamily
}
