import xml.etree.ElementTree as ET
from xml.dom import minidom


# G1 to G54
GREEK_WORDS = [
    # 1-2: ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν:
    "ἄνδρα", "μοι", "ἔννεπε", "μοῦσα", "πολύτροπον", "ὃς", "μάλα", "πολλὰ", "πλάγχθη", "ἐπεὶ", "Τροίης", "ἱερὸν", "πτολίεθρον", "ἔπερσεν",
    # 3: πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,
    "πολλῶν", "δ'", "ἀνθρώπων", "ἴδεν", "ἄστεα", "καὶ", "νόον", "ἔγνω",
    # 4: πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,
    "πολλὰ", "δ'", "ὅ", "γ'", "ἐν", "πόντῳ", "πάθεν", "ἄλγεα", "ὃν", "κατὰ", "θυμόν",
    # 5: ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.
    "ἀρνύμενος", "ἥν", "τε", "ψυχὴν", "καὶ", "νόστον", "ἑταίρων",
    # 6-7: ἀλλ᾽ οὐδ᾽ ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ: αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,
    "ἀλλ'", "οὐδ'", "ὣς", "ἑτάρους", "ἐρρύσατο", "ἱέμενός", "περ", "αὐτῶν", "γὰρ", "σφετέρῃσιν", "ἀτασθαλίῃσιν", "ὄλοντο",
    # 8-9: νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο ἤσθιον: αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ.
    "νήπιοι", "οἳ", "κατὰ", "βοῦς", "Ὑπερίονος", "Ἠελίοιο", "ἤσθιον", "αὐτάρ", "ὁ", "τοῖσιν", "ἀφείλετο", "νόστιμον", "ἦμαρ"
] # Total: 54 tokens

# E1 to E73
ENGLISH_WORDS = [
    # 1-2: Tell me, Muse, of the man of many ways, who was driven far journeys, after he had sacked Troy’s sacred citadel.
    "Tell", "me", "Muse", "of", "the", "man", "of", "many", "ways", "who", "was", "driven", "far", "journeys", "after", "he", "had", "sacked", "Troy’s", "sacred", "citadel",
    # 3: Many were they whose cities he saw, whose minds he learned of,
    "Many", "were", "they", "whose", "cities", "he", "saw", "whose", "minds", "he", "learned", "of",
    # 4-5: many the pains he suffered in his spirit on the wide sea, struggling for his own life and the homecoming of his companions.
    "many", "the", "pains", "he", "suffered", "in", "his", "spirit", "on", "the", "wide", "sea", "struggling", "for", "his", "own", "life", "and", "the", "homecoming", "of", "his", "companions",
    # 6-7: Even so he could not save his companions, hard though he strove to; they were destroyed by their own wild recklessness,
    "Even", "so", "he", "could", "not", "save", "his", "companions", "hard", "though", "he", "strove", "to", "they", "were", "destroyed", "by", "their", "own", "wild", "recklessness",
    # 8-9: fools, who devoured the oxen of Helios, the Sun God, and he took away the day of their homecoming.
    "fools", "who", "devoured", "the", "oxen", "of", "Helios", "the", "Sun", "God", "and", "he", "took", "away", "the", "day", "of", "their", "homecoming"
] # Total: 73 tokens


# G=Greek, E=English. The list uses IDs (G1, E1, etc.)
ALIGNMENT_LINKS = [
    # Lines 1-2: ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν
    ("G3", "E1"),           # ἔννεπε -> Tell
    ("G2", "E2"),           # μοι -> me
    ("G4", "E3"),           # μοῦσα -> Muse
    ("G1", "E6"),           # ἄνδρα -> man
    ("G5", "E8 E9"),        # πολύτροπον -> many ways (1-to-2)
    ("G6", "E10"),          # ὃς -> who
    ("G7 G8", "E11 E12"),    # μάλα πολλὰ -> was driven (2-to-2, simplified)
    ("G9", "E13 E14"),      # πλάγχθη -> far journeys (1-to-2)
    ("G10", "E15"),         # ἐπεὶ -> after
    ("G14", "E18"),         # ἔπερσεν -> sacked
    ("G11", "E19"),         # Τροίης -> Troy’s
    ("G12 G13", "E20 E21"), # ἱερὸν πτολίεθρον -> sacred citadel (2-to-2)
    (";E4 E5 E7 E16 E17", ""), # Structural words (of the, he had, etc.)
    
    # Line 3: πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω
    ("G15", "E22"),         # πολλῶν -> Many
    ("G17", "E24 E25"),     # ἀνθρώπων -> they cities (implied possession)
    ("G18", "E27"),         # ἴδεν -> saw
    ("G19", "E25"),         # ἄστεα -> cities
    ("G21", "E30"),         # νόον -> minds
    ("G22", "E32"),         # ἔγνω -> learned
    (";E23 E26 E28 E29 E31 E33", ""), # were, he, whose, of (structural)
    
    # Line 4: πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,
    ("G23", "E34"),         # πολλὰ -> many
    ("G27", "E44 E45"),     # πόντῳ -> wide sea (1-to-2)
    ("G28", "E37"),         # πάθεν -> suffered
    ("G29", "E36"),         # ἄλγεα -> pains
    ("G30 G31 G32", "E39 E40 E41"), # ὃν κατὰ θυμόν -> in his spirit (3-to-3)
    (";E35 E38 E42 E43", ""), # the, he, his, on (structural)

    # Line 5: ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.
    ("G33", "E46"),         # ἀρνύμενος -> struggling
    ("G35 G37", "E49 E51"), # ἥν ψυχὴν -> own life (2-to-2)
    ("G39", "E53"),         # νόστον -> homecoming
    ("G40", "E55"),         # ἑταίρων -> companions
    (";E47 E48 E50 E52 E54", ""), # for, his, and, the, of (structural)

    # Lines 6-7: ἀλλ᾽ οὐδ᾽ ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ: αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,
    ("G41 G42 G43", "E56 E57"), # ἀλλ᾽ οὐδ᾽ ὣς -> Even so (3-to-2)
    ("G45", "E60 E61"),     # ἐρρύσατο -> could not save (1-to-3)
    ("G44", "E63"),         # ἑτάρους -> companions
    ("G46 G47", "E64 E65 E66 E67"), # ἱέμενός περ -> hard though he strove (2-to-4)
    ("G50 G51", "E69 E70 E71"), # σφετέρῃσιν ἀτασθαλίῃσιν -> their own wild recklessness (2-to-3)
    ("G52", "E68"),         # ὄλοντο -> destroyed
    (";E58 E59 E62 E72", ""), # he, his, to, by (structural)

    # Lines 8-9: νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο ἤσθιον: αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ.
    ("G53", "E73"),         # νήπιοι -> fools
    ("G54", "E74"),         # οἳ -> who
    ("G57 G58", "E77 E78"), # βοῦς Ὑπερίονος Ἠελίοιο -> oxen of Helios, the Sun God (3-to-6)
    ("G59", "E76"),         # ἤσθιον -> devoured
    ("G60", "E82"),         # αὐτάρ -> and
    ("G61", "E83"),         # ὁ -> he
    ("G63", "E84 E85"),     # ἀφείλετο -> took away
    ("G64 G65", "E87 E89"), # νόστιμον ἦμαρ -> day of homecoming (2-to-3)
    (";E75 E79 E80 E81 E86 E88 E90", "") # the, the, God, took, away, the, of (structural)

# --- 3. XML Generation Function ---

def generate_alignment_xml_file(filename='lattimore_alignment_data.xml'):
    """Creates the XML structure and saves it to a file."""
    
    root = ET.Element('parallel_corpus', attrib={'source_lang': 'grc', 'target_lang': 'en_lattimore'})
    sent = ET.SubElement(root, 'sent', attrib={'id': '1_9'})
    
    # Helper function for Tokenization
    def create_token_elements(words, lang_prefix):
        s_element = ET.SubElement(sent, 's', attrib={'id': lang_prefix})
        s_element.append(ET.Comment(f"Original Token Count: {lang_prefix}{len(words)}"))
        for i, word in enumerate(words):
            token_id = f"{lang_prefix}{i+1}"
            ET.SubElement(s_element, 'w', attrib={'id': token_id}).text = word
            
    # Add Tokenized Sentences
    create_token_elements(GREEK_WORDS, 'G')
    create_token_elements(ENGLISH_WORDS, 'E')
    
    # Add Alignment Links
    link_grp = ET.SubElement(sent, 'linkGrp', attrib={'align_type': 'word'})
    for link_id, _ in ALIGNMENT_LINKS:
        ET.SubElement(link_grp, 'link', attrib={'xtarget': link_id})
        
    # Format and Save to File
    tree = ET.ElementTree(root)
    xml_string = ET.tostring(tree.getroot(), encoding='unicode')
    reparsed = minidom.parseString(xml_string)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(reparsed.toprettyxml(indent="    "))
        
    print(f"saved xml to '{filename}'")
    return filename

XML_OUTPUT_FILE = generate_alignment_xml_file()