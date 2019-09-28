from w3lib.html import remove_tags
import re
import sys
def eliminateNoiseTags(text):
    text = text.replace("\n"," ")
    text = re.sub("<\s*script[^>]*>(.*?)<\s*/\s*script>",'',text)
    # text = re.sub("<script(?:(?!\/\/)(?!\/\*)[^'\"]|\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'|\/\/.*(?:\n)|\/\*(?:(?:.|\s))*?\*\/)*?<\/script>",'',text)
    text = re.sub("<\s*style[^>]*>(.*?)<\s*/\s*style>",'',text)
    # print(text)
    
    # sys.exit()
    return text

def filter_paragraphs(raw_paragraphs):
    paragraphs = raw_paragraphs
    paragraphs = [eliminateNoiseTags(item) for item in paragraphs]
    paragraphs = [remove_tags(item).strip().replace("\r\n","").replace("\t","").replace(u'\xa0', u' ') for item in paragraphs]
    paragraphs = [item for item in paragraphs if len(item.split(' ')) > 50]
    return paragraphs

def isValidUrl(url):
    if url is None or\
        '.jpg' in url or\
        '.png' in url or\
        '.pdf' in url or \
        'sconto' in url or \
        'cookie' in url or\
        'annunci' in url or\
        'abbonamenti' in url or\
        '.gif' in url or\
        '.jpeg' in url or\
        'rugby' in url or\
        'calcio' in url or\
        'risultati' in url or\
        'basket' in url or\
        '.JPG' in url or\
        '.JPEG' in url or\
        '.PNG' in url or\
        '.swf' in url or\
        '.GIF' in url or\
        '.PDF' in url or\
        'motori' in url or\
        '@' in url or\
        'QuickChart_Image.aspx' in url or\
        'shop' in url:
        return False
    return True