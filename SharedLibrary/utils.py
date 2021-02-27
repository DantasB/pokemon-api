import re

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_all_line_breakers(text):
    clean = re.compile("\s+")
    return re.sub(clean, ' ', text)