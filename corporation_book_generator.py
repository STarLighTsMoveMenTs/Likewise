#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corporation Partnership Book Generator
Erstellt ein 1111-seitiges Corporation Partnership & Bewerbungsbuch
basierend auf Frieden, Vergebung, Freiheit, Nächstenliebe, Hoffnung & Zuversicht
"""
import re
import random
from pathlib import Path
from datetime import datetime

# Eingabe- und Ausgabepfade
SOURCE = Path(r"/run/media/shinehealthcare/c538b800-b7eb-45d6-a563-a1ad3de6a7b3/STarLighTsMoveMenTs/SinceLightsThink/SinceLightsThink/Textdatei (1).txt")
OUTPUT = Path(r"/home/shinehealthcare/Schreibtisch/Corporation_Partnership_Book_1111.txt")

# Kernwerte (positive Transformation)
CORE_VALUES = {
    "Frieden": ["Harmonie", "Verständigung", "Kooperation", "Balance", "Stabilität"],
    "Vergebung": ["Versöhnung", "Heilung", "Neuanfang", "Gnade", "Transformation"],
    "Freiheit": ["Autonomie", "Selbstbestimmung", "Unabhängigkeit", "Wahlfreiheit", "Entfaltung"],
    "Nächstenliebe": ["Mitgefühl", "Solidarität", "Unterstützung", "Gemeinschaft", "Fürsorge"],
    "Hoffnung": ["Optimismus", "Zukunftsvision", "Inspiration", "Motivation", "Glaube"],
    "Zuversicht": ["Vertrauen", "Positivität", "Mut", "Entschlossenheit", "Stärke"]
}

def load_and_clean_text(path: Path) -> str:
    """Lädt Text und filtert negative Inhalte"""
    text = path.read_text(encoding='utf-8', errors='replace')
    
    # Negative Begriffe entfernen/transformieren
    negative_patterns = [
        (r'\bnicht\b', 'positiv'),
        (r'\bkein\b', 'vollständig'),
        (r'\bproblem\b', 'Herausforderung'),
        (r'\bfehler\b', 'Lernmöglichkeit'),
        (r'\bschlecht\b', 'verbesserungsfähig'),
        (r'\bkrieg\b', 'Friedensinitiative'),
        (r'\bhölle\b', 'transformative Erfahrung')
    ]
    
    for pattern, replacement in negative_patterns:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    return text

def extract_key_info(text: str) -> dict:
    """Extrahiert Schlüsselinformationen"""
    info = {
        'name': 'Daniel Pohl',
        'title': 'EU-UNION Expert · Disability Advocate & CEO',
        'reference': 'EX2025D1218310',
        'duns': '315676980',
        'pic': '873042778',
        'vat': '31353063511',
        'orcid': '0009-0004-0348-9769',
        'emails': re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text),
        'urls': re.findall(r'https?://[^\s)]+', text),
        'locations': ['Detmold', 'Brüssel', 'Luxemburg', 'Schweiz', 'Portugal', 'Spanien', 'Italien', 'USA', 'Irland', 'Frankreich', 'Brasilien']
    }
    return info

def generate_themes_and_chapters():
    """Generiert 3333 Themen und 4444 Kapitel"""
    themes = []
    chapters = []
    
    # Basis-Themen aus Kernwerten
    base_themes = []
    for value, aspects in CORE_VALUES.items():
        for aspect in aspects:
            for i in range(111):  # 6 * 5 * 111 = 3330
                theme = f"{value} durch {aspect} - Dimension {i+1}"
                base_themes.append(theme)
    
    # Ergänzung auf 3333
    for i in range(3):
        base_themes.append(f"Universelle Harmonie - Aspekt {i+1}")
    
    themes = base_themes
    
    # Kapitel generieren (4444)
    chapter_templates = [
        "Grundlagen von {theme}",
        "Praktische Anwendung von {theme}",
        "Internationale Perspektive auf {theme}",
        "Zukunftsvision für {theme}",
        "Implementierung von {theme}",
        "Nachhaltige {theme}",
        "Innovative Ansätze zu {theme}",
        "Ethische Dimensionen von {theme}",
        "Technologische Integration von {theme}",
        "Gesellschaftlicher Einfluss von {theme}",
        "Wissenschaftliche Grundlagen von {theme}",
        "Kulturelle Aspekte von {theme}",
        "Wirtschaftliche Dimensionen von {theme}",
        "Bildungsansätze zu {theme}"
    ]
    
    for i, theme in enumerate(themes):
        if len(chapters) < 4444:
            template = chapter_templates[i % len(chapter_templates)]
            chapters.append(template.format(theme=theme))
    
    # Ergänzung falls nötig
    while len(chapters) < 4444:
        chapters.append(f"Erweiterte Betrachtung - Kapitel {len(chapters)+1}")
    
    return themes[:3333], chapters[:4444]

def generate_application_letter(info: dict) -> str:
    """Generiert Bewerbungsschreiben"""
    return f"""
BEWERBUNGSSCHREIBEN
Corporation Partnership & Enterprise Initiative

Sehr geehrte Damen und Herren,

als {info['title']} mit der EU-Union Referenz {info['reference']} bewerbe ich mich 
um eine strategische Partnerschaft im Rahmen der "House of Lights & Tech" Initiative.

Meine Vision basiert auf den Grundpfeilern:
• Frieden als Basis für nachhaltige Kooperation
• Vergebung als Kraft für Transformation
• Freiheit als Rahmen für Innovation
• Nächstenliebe als Motivation für Gemeinschaft
• Hoffnung als Antrieb für Zukunftsgestaltung
• Zuversicht als Fundament für Erfolg

Qualifikationen:
- EU-UNION Expert (Referenz: {info['reference']})
- D-U-N-S®: {info['duns']}
- PIC: {info['pic']}
- ORCID: {info['orcid']}

Projektumfang:
Das "House of Lights & Tech" Zentrum vereint Forschung, Bildung und soziale Innovation
auf internationaler Ebene mit Standorten in Europa, Amerika und weiteren Kontinenten.

Mit freundlichen Grüßen,
{info['name']}
{info['emails'][0] if info['emails'] else 'kontakt@example.com'}
"""

def generate_book_content(themes: list, chapters: list, info: dict, source_text: str) -> str:
    """Generiert das komplette Buchcontent"""
    
    content = []
    
    # Titelseite
    content.append("=" * 80)
    content.append("CORPORATION PARTNERSHIP BOOK")
    content.append("House of Lights & Tech Initiative")
    content.append("1111 Seiten • 3333 Themen • 4444 Kapitel")
    content.append(f"Autor: {info['name']}")
    content.append(f"EU-Union Referenz: {info['reference']}")
    content.append(f"Datum: {datetime.now().strftime('%d. %B %Y')}")
    content.append("=" * 80)
    content.append("")
    
    # Copyright-Hinweise
    content.append("COPYRIGHT & REGISTRIERUNG")
    content.append("-" * 40)
    content.append(f"© 2025 {info['name']}")
    content.append("Alle Rechte vorbehalten.")
    content.append("Registriert unter EU-Union Referenz: " + info['reference'])
    content.append("D-U-N-S®: " + info['duns'])
    content.append("ORCID: " + info['orcid'])
    content.append("")
    content.append("Diese Publikation ist urheberrechtlich geschützt.")
    content.append("Vervielfältigung nur mit ausdrücklicher Genehmigung.")
    content.append("Corporation Partnership Request - Offizielles Dokument")
    content.append("")
    
    # Bewerbungsschreiben
    content.append("BEWERBUNGSSCHREIBEN")
    content.append("-" * 40)
    content.extend(generate_application_letter(info).split('\n'))
    content.append("")
    
    # Inhaltsverzeichnis
    content.append("INHALTSVERZEICHNIS")
    content.append("-" * 40)
    content.append("Seite 1-50: Grundlagen und Vision")
    content.append("Seite 51-100: Bewerbungsunterlagen")
    content.append("Seite 101-200: Kernwerte-Analyse")
    
    page_counter = 201
    for i, theme in enumerate(themes):
        if i < 50:  # Erste 50 Themen im Inhaltsverzeichnis
            content.append(f"Seite {page_counter}: {theme}")
            page_counter += 1
    
    content.append("...")
    content.append(f"Seite 1111: Zusammenfassung und Ausblick")
    content.append("")
    
    # Hauptinhalt - 1 Seite pro Thema/Kapitel
    for page_num in range(1, 1112):  # 1111 Seiten
        content.append(f"SEITE {page_num}")
        content.append("=" * 20)
        
        if page_num <= len(themes):
            theme = themes[page_num - 1]
            content.append(f"THEMA: {theme}")
            content.append("")
            
            # Kernwerte-basierter Inhalt
            for value in CORE_VALUES:
                if value.lower() in theme.lower():
                    content.append(f"Im Kontext von {value} entwickeln wir innovative Ansätze")
                    content.append(f"für nachhaltige Partnerschaft und Kooperation.")
                    break
            else:
                content.append("Dieses Thema verbindet alle Kernwerte unserer Initiative")
                content.append("und schafft Synergien für positive Transformation.")
        
        if page_num <= len(chapters):
            chapter = chapters[page_num - 1]
            content.append(f"KAPITEL: {chapter}")
            content.append("")
            content.append("Innovative Lösungsansätze durch:")
            content.append("• Interdisziplinäre Zusammenarbeit")
            content.append("• Technologische Integration")
            content.append("• Nachhaltige Entwicklung")
            content.append("• Internationale Kooperation")
        
        content.append("")
        content.append("House of Lights & Tech - Zentrum für Innovation und Partnerschaft")
        content.append(f"EU-Union Referenz: {info['reference']}")
        content.append("")
        content.append("-" * 60)
        content.append("")
    
    # Anhang mit Originaltext (transformiert)
    content.append("ANHANG: URSPRUNGSTEXT (TRANSFORMIERT)")
    content.append("=" * 50)
    content.extend(source_text.split('\n'))
    
    return '\n'.join(content)

def main():
    """Hauptfunktion"""
    print("Generiere Corporation Partnership Book...")
    
    # Text laden und reinigen
    source_text = load_and_clean_text(SOURCE)
    
    # Informationen extrahieren
    info = extract_key_info(source_text)
    
    # Themen und Kapitel generieren
    themes, chapters = generate_themes_and_chapters()
    
    print(f"Generiert: {len(themes)} Themen, {len(chapters)} Kapitel")
    
    # Buchinhalt generieren
    book_content = generate_book_content(themes, chapters, info, source_text)
    
    # Speichern
    OUTPUT.write_text(book_content, encoding='utf-8')
    
    print(f"Corporation Partnership Book gespeichert: {OUTPUT}")
    print(f"Umfang: 1111 Seiten, {len(themes)} Themen, {len(chapters)} Kapitel")
    print("Schriftgröße: 13pt (Hinweis für Formatierung)")

if __name__ == '__main__':
    main()