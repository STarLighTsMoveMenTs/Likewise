#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
format_nlp_form.py

Liest die angegebene Textdatei vollständig ein, extrahiert strukturierte Informationen
(Headings, Kontaktfelder, Listen, URLs, E-Mails) und schreibt ein "Formular-Dokument"
als einfache Textdatei auf den Desktop: /home/shinehealthcare/Schreibtisch/formatted_document.txt

Dieses Skript versucht, keinerlei Information zu verlieren: Am Ende wird der komplette
Rohtext angehängt.
"""
import re
from pathlib import Path

# Eingabe- und Ausgabepfade (anpassen falls nötig)
SOURCE = Path(r"/run/media/shinehealthcare/c538b800-b7eb-45d6-a563-a1ad3de6a7b3/STarLighTsMoveMenTs/SinceLightsThink/SinceLightsThink/Textdatei (1).txt")
OUTPUT = Path(r"/home/shinehealthcare/Schreibtisch/formatted_document.txt")


def load_text(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='replace')


def find_headings_and_sections(text: str):
    lines = text.splitlines()
    sections = []
    cur = {'title': 'Preamble', 'level': 0, 'lines': []}
    heading_re = re.compile(r'^(#{1,6})\s*(.*)')
    for ln in lines:
        m = heading_re.match(ln)
        if m:
            # commit previous
            sections.append(cur)
            cur = {'title': m.group(2).strip() or m.group(1), 'level': len(m.group(1)), 'lines': []}
        else:
            cur['lines'].append(ln)
    sections.append(cur)
    return sections


def extract_key_values(text: str):
    kv = {}
    # simple key: value lines
    for ln in text.splitlines():
        if ':' in ln:
            k, v = ln.split(':', 1)
            k = k.strip()
            v = v.strip()
            if re.search(r'\w', k) and v:
                # aggregate repeated keys into lists
                if k in kv:
                    if isinstance(kv[k], list):
                        kv[k].append(v)
                    else:
                        kv[k] = [kv[k], v]
                else:
                    kv[k] = v
    return kv


def extract_emails(text: str):
    return sorted(set(re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)))


def extract_urls(text: str):
    return sorted(set(re.findall(r'https?://[^\s)]+', text)))


def extract_numbered_items(text: str):
    items = []
    for ln in text.splitlines():
        if re.match(r'^(\s*\d+[\.)xX-]|\s*\d+x\s|\s*\d+\s*\.)', ln):
            items.append(ln.strip())
    return items


def build_form_document(text: str):
    sections = find_headings_and_sections(text)
    kv = extract_key_values(text)
    emails = extract_emails(text)
    urls = extract_urls(text)
    numbered = extract_numbered_items(text)

    out_lines = []
    out_lines.append('--- Formular Dokument (automatisch erzeugt) ---')
    out_lines.append('Quelle: ' + str(SOURCE))
    out_lines.append('')

    # Title - take first heading if exists
    if sections and sections[0]['title'] != 'Preamble' and sections[0]['title'].strip():
        out_lines.append('Titel: ' + sections[0]['title'])
    else:
        # try first non-empty line
        first_non_empty = next((l for l in text.splitlines() if l.strip()), '')
        out_lines.append('Titel (inferred): ' + (first_non_empty[:120]))
    out_lines.append('')

    out_lines.append('== Kontakt / Schlüsselwerte ==')
    if kv:
        for k, v in kv.items():
            if isinstance(v, list):
                out_lines.append(f'{k}:')
                for vi in v:
                    out_lines.append('  - ' + vi)
            else:
                out_lines.append(f'{k}: {v}')
    else:
        out_lines.append('(keine Key-Value-Paare erkannt)')
    out_lines.append('')

    out_lines.append('== E-Mail Adressen ==')
    if emails:
        for e in emails:
            out_lines.append('- ' + e)
    else:
        out_lines.append('(keine E-Mails erkannt)')
    out_lines.append('')

    out_lines.append('== URLs ==')
    if urls:
        for u in urls:
            out_lines.append('- ' + u)
    else:
        out_lines.append('(keine URLs erkannt)')
    out_lines.append('')

    out_lines.append('== Nummerierte / Aufzählungs-Items (extracted) ==')
    if numbered:
        for it in numbered:
            out_lines.append('- ' + it)
    else:
        out_lines.append('(keine nummerierten Items erkannt)')
    out_lines.append('')

    out_lines.append('== Strukturierte Abschnitte ==')
    for idx, s in enumerate(sections):
        title = s['title'] or f'Section {idx+1}'
        out_lines.append('\n-- ' + title + ' --')
        # compress block while preserving line breaks
        block = '\n'.join(s['lines']).strip()
        if not block:
            out_lines.append('(leer)')
        else:
            # limit line width but preserve paragraphs
            out_lines.extend(line for line in block.splitlines())
    out_lines.append('')

    out_lines.append('== Rohtext (komplett, unverändert) ==')
    out_lines.append(text)

    return '\n'.join(out_lines)


if __name__ == '__main__':
    txt = load_text(SOURCE)
    form = build_form_document(txt)
    OUTPUT.write_text(form, encoding='utf-8')
    print('Fertig — formatiertes Dokument geschrieben nach: ' + str(OUTPUT))
