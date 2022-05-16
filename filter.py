import sys
import panflute

headers = []


def bold(doc):
    doc.replace_keyword('BOLD', panflute.Strong(panflute.Str('BOLD')))


def similarHeaders(elem, doc):
    if isinstance(elem, panflute.Header):
        txt = panflute.stringify(elem)
        if txt in headers:
            sys.stderr.write(f"Warning: Header {txt} already exists in document\n")
        else:
            headers.append(txt)


def lvlHeader(elem, doc):
    if isinstance(elem, panflute.Header):
        if elem.level <= 3:
            return panflute.Header(panflute.Str(panflute.stringify(elem).upper()), level=elem.level)


if __name__ == '__main__':
    panflute.run_filters([similarHeaders, lvlHeader], prepare=bold)
