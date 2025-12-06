import tabulate
from tabulate import tabulate

data = [
    ["ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ", "Tell me, Muse, of the man of many ways, who was driven", "Tell me about a complicated man."],
    ["πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν:", "far journeys, after he had sacked Troy’s sacred citadel.", "Muse, tell me how he wandered and was lost"], 
    ["πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,", "Many were they whose cities he saw, whose minds he learned of,", "when he had wrecked the holy town of Troy,"],
    ["πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,", "many the pains he suffered in his spirit on the wide sea,", "and where he went, and who he met, the pain"],
    ["ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων," , "struggling for his own life and the homecoming of his companions.", "he suffered on the sea, and how he worked"],
    ["ἀλλ᾽ οὐδ᾽ ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ:", "Even so he could not save his companions, hard though", "to save his life and bring his men back home."],
    ["αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,", "he strove to; they were destroyed by their own wild recklessness,", "He failed, and for their own mistakes, they died."],
    ["νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο", "fools, who devoured the oxen of Helios, the Sun God,", "They are the Sun God's cattle, and the god"],
    ["ἤσθιον: αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ", "and he took away the day of their homecoming. From some point", "kept them from home. Now goddess, child of Zeus,"],
    ["τῶν ἁμόθεν γε, θεά, θύγατερ Διός, εἰπὲ καὶ ἡμῖν.", "here, goddess, daughter of Zeus, speak, and begin our story.", "tell the old story for our modern times."],
    ["N/A", "N/A", "Find the beginning."]

   
]

headers = ["Greek", "Lattimore", "Wilson"]

print(tabulate(data, headers=headers, tablefmt="grid"))
