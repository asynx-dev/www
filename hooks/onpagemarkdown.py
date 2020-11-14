def onpagemarkdown(*args, **kwargs):

    if "axlang" in kwargs["page"].meta:
        print(kwargs["page"].meta["axlang"])
        kwargs["page"].title += " [" + kwargs["page"].meta["axlang"].upper() + "]"
        return kwargs["page"].markdown.replace('# ','# ' + "[" + kwargs["page"].meta["axlang"].upper() + "] ", 1)
