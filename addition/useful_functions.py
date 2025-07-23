import re


def fix_text_hyphens(text):
    text = re.sub(r'-\s*\n\s*', '-', text)
    text = re.sub(r'—\s*\n\s*', '—', text)
    text = re.sub(r'–\s*\n\s*', '–', text)

    text = re.sub(
        r'(?<!\n)\n(?!\n|$)',
        lambda m: ' ' if not re.search(r'^\w+$', text[:m.start()].split('\n')[-1]) else '\n',
        text
    )

    return text


def highlight_important(text):
    text = re.sub(
        r'(\d{1,2}[./-]\d{1,2}[./-]\d{2,4})',
        r'<b>\1</b>',
        text
    )

    text = re.sub(
        r'(\d+[\.,]?\d*\s*[₽рРpP$€£¥])',
        r'<b>\1</b>',
        text
    )

    text = re.sub(
        r'(?<!\w)(\d+[\.,]?\d*)(?!\w)',
        r'<b>\1</b>',
        text
    )

    return text


# def correct_text(text):
#     try:
#         detected_lang = detect(text)
#         lang = detected_lang.split("-")[-1]
#     except:
#         lang = "en"
#
#     spell = Speller( lang )
#
#     tokens = re.findall(r'(\w+|\s+|[^\w\s])', text)
#     corrected_tokens = []
#
#     for token in tokens:
#         if not token.strip():
#             corrected_tokens.append(token)
#             continue
#
#         if not token.isalpha():
#             corrected_tokens.append(token)
#             continue
#         corrected_word = spell(token)
#         if token.isupper():
#             corrected_word = corrected_word.upper()
#         elif token[0].isupper():
#             corrected_word = corrected_word.capitalize()
#
#         corrected_tokens.append(corrected_word)
#
#     return ''.join(corrected_tokens)