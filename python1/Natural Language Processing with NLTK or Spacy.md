## [[Natural Language Processing with NLTK or Spacy]]

### What is NLP with NLTK or Spacy?
Natural Language Processing (NLP) involves enabling computers to understand and process human language. NLTK and Spacy are popular Python libraries for NLP tasks, providing tools for tasks such as:

- Tokenization: Breaking text into individual words or tokens.
- Stemming: Reducing words to their root form.
- Lemmatization: Similar to stemming, but considering the word's context.
- Part-of-Speech Tagging (POS): Identifying the grammatical function of words (e.g., noun, verb).
- Named Entity Recognition (NER): Detecting and classifying specific types of entities (e.g., persons, organizations).

### How to Use NLTK or Spacy
**NLTK:**
```python
import nltk
# Load a pre-trained tokenizer
tokenizer = nltk.data.load('nltk_data/tokenizers/punkt/english.pickle')
# Tokenize some text
tokens = tokenizer.tokenize("This is a sample text to be tokenized.")
```

**Spacy:**
```python
import spacy
# Load a pre-trained NLP model
nlp = spacy.load('en_core_web_sm')
# Process some text
doc = nlp("This is a sample text to be processed.")
# Extract tokens, POS tags, and entities
for token in doc:
 print(token.text, token.pos_, token.dep_)
```

### Code Examples
**NLTK:**
```python
# Stemming using NLTK
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in ["running", "ran", "runs"]]
```

**Spacy:**
```python
# NER using Spacy
for ent in doc.ents:
 print(ent.text, ent.label_)
```

### Related Python Concepts
- [[Regular Expressions]]: Used for complex text matching and tokenization.
- [[Lists]]: Store sequences of tokens or entities.
- [[Dictionaries]]: Map words to their POS tags or lemma forms.
- [[Functions]]: Define custom NLP functions for specialized tasks.
- [[Generators]]: Yield tokens or entities one at a time for memory efficiency.
# [[Python 1 Home]]