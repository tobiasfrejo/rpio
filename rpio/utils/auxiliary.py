import re

def getCustomCode(text,tag):
    pattern = r"#<!-- cc_"+tag+" START--!>(.*?)#<!-- cc_"+tag+" END--!>"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches if matches else None

def replaceCustomCode(text,tag,replacement):
    pattern = r"#<!-- cc_"+tag+" START--!>(.*?)#<!-- cc_"+tag+" END--!>"
    start_tag = "#<!-- cc_"+tag+" START--!>"
    end_tag = "#<!-- cc_" + tag + " END--!>"
    return re.sub(pattern,start_tag+replacement[0]+end_tag,text,flags=re.DOTALL)