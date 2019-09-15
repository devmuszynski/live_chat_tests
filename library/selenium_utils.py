def xpath_to_text(text, exact_match=False, tag=None):
    if exact_match:
        return f"//{tag if tag else '*'}[text()=\"{text}\"]"
    else:
        return f"//{tag if tag else '*'}[contains(text(), \"{text}\")]"


def xpath_to_href(href, exact_match=False):
    if exact_match:
        return f"//a[@href='{href}']"
    else:
        return f"//a[contains(@href, '{href}')]"
