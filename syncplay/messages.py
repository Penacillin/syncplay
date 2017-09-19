# coding:utf8
from syncplay import constants

from . import messages_en
from . import messages_ru
from . import messages_de

messages = {
           "en": messages_en.en,
           "ru": messages_ru.ru,
           "de": messages_de.de,
           "CURRENT": None
           }

def getLanguages():
    langList = {}
    for lang in messages:
        if lang != "CURRENT":
            langList[lang] = getMessage("LANGUAGE", lang)
    return langList

def setLanguage(lang):
    messages["CURRENT"] = lang

def getMissingStrings():
    missingStrings = ""
    for lang in messages:
        if lang != "en" and lang != "CURRENT":
            for message in messages["en"]:
                if message not in  messages[lang]:
                    missingStrings = missingStrings + "({}) Missing: {}\n".format(lang, message)
            for message in messages[lang]:
                if message not in messages["en"]:
                    missingStrings = missingStrings + "({}) Unused: {}\n".format(lang, message)

    return missingStrings

def getInitialLanguage():
    import locale
    try:
        initialLanguage = locale.getdefaultlocale()[0].split("_")[0]
        if not messages.has_key(initialLanguage):
            initialLanguage = constants.FALLBACK_INITIAL_LANGUAGE
    except:
        initialLanguage = constants.FALLBACK_INITIAL_LANGUAGE
    return initialLanguage

def isValidLanguage(language):
    return language in messages

def getMessage(type_, locale=None):
    if constants.SHOW_TOOLTIPS == False:
        if "-tooltip" in type_:
            return ""

    if not isValidLanguage(messages["CURRENT"]):
        setLanguage(getInitialLanguage())

    lang = messages["CURRENT"]
    if locale and messages.has_key(locale):
        if type_ in messages[locale]:
            return unicode(messages[locale][type_])
    if lang and lang in messages:
        if type_ in messages[lang]:
            return unicode(messages[lang][type_])
    if type_ in messages["en"]:
        return unicode(messages["en"][type_])
    else:
        raise KeyError(type_)
