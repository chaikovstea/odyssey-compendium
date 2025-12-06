# run_transform.py - Modeled after Variorum structure

import xml.etree.ElementTree as ET
from lxml import etree # Import lxml for transformation and pretty printing

# --- Data Preparation ---

# The raw texts provided by the user (punctuation intact)
GREEK_TEXT = """
ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ
πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν:
πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,
πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,
ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.
ἀλλ᾽ οὐδ᾽ ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ:
αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,
νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο
ἤσθιον: αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ.
τῶν ἁμόθεν γε, θεά, θύγατερ Διός, εἰπὲ καὶ ἡμῖν.
"""

LATTIMORE_TEXT = """
Tell me, Muse, of the man of many ways, who was driven
far journeys, after he had sacked Troy’s sacred citadel.
Many were they whose cities he saw, whose minds he learned of,
many the pains he suffered in his spirit on the wide sea,
struggling for his own life and the homecoming of his companions.
Even so he could not save his companions, hard though
he strove to; they were destroyed by their own wild recklessness,
fools, who devoured the oxen of Helios, the Sun God,
and he took away the day of their homecoming. From some point
here, goddess, daughter of Zeus, speak, and begin our story.
"""

WILSON_TEXT = """
Tell me about a complicated man.
Muse, tell me how he wandered and was lost
when he had wrecked the holy town of Troy, 
and where he went, and who he met, the pain
he suffered on the sea, and how he worked
to save his life and bring his men back home.
He failed, and for their own mistakes, they died. 
They are the Sun God's cattle, and the god 
kept them from home. Now goddess, child of Zeus,
tell the old story for our modern times.
Find the beginning. 
"""

TEXTS = {
    'Greek': GREEK_TEXT,
    'Lattimore': LATTIMORE_TEXT,
    'Wilson': WILSON_TEXT
}

# --- Core Tokenization Function ---

def tokenize_line(line_text):
    """Tokenizes a single line, retaining punctuation."""
    words = []
    tokens_with_punctuation = line_text.split()
    
    token_id_counter = 1
    for word in tokens_with_punctuation:
        # Token for matching is still the lowercased version of the word.
        token = word.lower() 
        words.append({
            'text': word, 
            'token_id': str(token_id_counter), 
            'token': token
        })
        token_id_counter += 1
    return words

# --- XML Generation (Variorum Style) ---

def create_full_xml():
    """Generates the Variorum-style XML, grouping versions by line."""
    
    # 1. Split all texts into lines
    version_lines = {name: text.strip().split('\n') for name, text in TEXTS.items()}
    max_lines = max(len(lines) for lines in version_lines.values())

    root = ET.Element('odyssey_variorum')
    
    # 2. Iterate by line number (the location marker)
    for line_num in range(max_lines):
        
        # Variorum Structure: <line line_id="1"> ... </line>
        line_element = ET.Element('line', line_id=str(line_num + 1))
        
        # 3. Iterate through each version for this line
        for version_name, lines in version_lines.items():
            if line_num < len(lines):
                line_text = lines[line_num]
                
                # Variorum Structure: <version name="Greek"> ... </version>
                version_element = ET.Element('version', name=version_name)
                
                # Tokenize the words in this line/version
                tokenized_words = tokenize_line(line_text)
                
                for word_data in tokenized_words:
                    word_element = ET.Element('word', 
                        token_id=word_data['token_id'], 
                        token=word_data['token']
                    )
                    word_element.text = word_data['text']
                    version_element.append(word_element)
                
                line_element.append(version_element)
        
        root.append(line_element)
        
    # Write the XML to a file
    try:
        xml_string = etree.tostring(etree.fromstring(ET.tostring(root)), 
                                    pretty_print=True, 
                                    encoding='utf-8', 
                                    xml_declaration=True).decode('utf-8')
        with open('odyssey_data_variorum.xml', 'w', encoding='utf-8') as f:
            f.write(xml_string)
        print("✅ Created odyssey_data_variorum.xml with Variorum structure.")
    except Exception as e:
        ET.ElementTree(root).write('odyssey_data_variorum.xml', encoding='utf-8', xml_declaration=True)
        print(f"⚠️ Created XML without pretty-printing: {e}")
    
    return root

# --- XSLT Execution ---

def run_xslt_transformation(xml_file, xsl_file, output_file):
    """Performs the XSLT transformation using lxml."""
    try:
        # 1. Load the XML data
        xml_doc = etree.parse(xml_file)
        
        # 2. Load the XSLT stylesheet
        xslt_doc = etree.parse(xsl_file)
        transform = etree.XSLT(xslt_doc)
        
        # 3. Perform the transformation
        result_tree = transform(xml_doc)
        
        # 4. Write the result to the output file
        with open(output_file, 'wb') as f:
            f.write(etree.tostring(result_tree, pretty_print=True))
            
        print(f"✅ Transformation complete. Output saved to **{output_file}**.")
        print("   Open this file in your browser to see the HTML table.")

    except etree.LxmlError as e:
        print(f"\n❌ An error occurred during XSLT transformation: {e}")
    except FileNotFoundError:
        print("\n❌ Error: Make sure both XML and XSL files are in the same directory.")
    except NameError:
        print("\n❌ Error: The 'lxml' library is required. Please install it: pip install lxml")

if __name__ == '__main__':
    create_full_xml()
    
    xml_data_file = 'odyssey_data_variorum.xml'
    xslt_style_file = 'odyssey_transform_variorum.xsl'
    html_output_file = 'odyssey_alignment_variorum.html'
    
    run_xslt_transformation(xml_data_file, xslt_style_file, html_output_file)