from django import template

register = template.Library()

@register.assignment_tag

def get_translation(LANGUAGE_CODE, highlightsArray):
    if (LANGUAGE_CODE) in highlightsArray:
        varArr = (highlightsArray[highlightsArray.index(LANGUAGE_CODE) + 1:highlightsArray.index(LANGUAGE_CODE + 'x')])
    else:
        varArr = (highlightsArray[highlightsArray.index('en') + 1:highlightsArray.index('enx')])

    return (varArr)
