import spacy

nlp = spacy.load("en_core_web_sm")

def extract_key_points(text):
    doc = nlp(text)
    summary = ""
    strengths = []
    weaknesses = []

    for sent in doc.sents:
        if "summary" in sent.text.lower():
            summary = sent.text
        elif "strength" in sent.text.lower():
            strengths.append(sent.text)
        elif "weakness" in sent.text.lower():
            weaknesses.append(sent.text)

    return {
        "summary": summary,
        "strengths": strengths,
        "weaknesses": weaknesses,
    }
