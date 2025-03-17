import requests
import json

def fetch_word_data(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {word}")
        return None

def select_example_sentence(definitions):
    selected_sentences = []
    for i, definition in enumerate(definitions):
        print(f"\nDefinition {i + 1}: {definition['definition']}")
        if 'example' in definition:
            print(f"Example: {definition['example']}")
        else:
            print("No example available.")
        
    for i, definition in enumerate(definitions):
        if 'example' in definition:
            choice = input(f"Select this example for definition {i + 1}? (y/n): ").strip().lower()
            if choice == 'y':
                selected_sentences.append(definition['example'])
            else:
                selected_sentences.append(None)
        else:
            selected_sentences.append(None)
    return selected_sentences

def process_vocab_list(vocab_list):
    selected_examples = {}
    for word in vocab_list:
        print(f"\nFetching data for: {word}")
        word_data = fetch_word_data(word)
        if word_data:
            for entry in word_data:
                for meaning in entry.get('meanings', []):
                    print(f"\nPart of Speech: {meaning['partOfSpeech']}")
                    selected_sentences = select_example_sentence(meaning['definitions'])
                    selected_examples[word] = selected_sentences
                    print(f"Selected sentences for {word}: {selected_sentences}")
    return selected_examples

def read_vocab_list(filepath):
    with open(filepath, 'r') as file:
        vocab_list = [line.strip() for line in file.readlines()]
    return vocab_list

def save_selected_examples(selected_examples, filepath):
    with open(filepath, 'w') as file:
        json.dump(selected_examples, file, indent=4)
    print(f"Selected examples saved to {filepath}")

if __name__ == "__main__":
    vocab_list = read_vocab_list("/Users/carson/Desktop/nerd-emoji/nerd-emoji/scripts/vocablist.md")
    selected_examples = process_vocab_list(vocab_list)
    save_selected_examples(selected_examples, "/Users/carson/Desktop/nerd-emoji/nerd-emoji/scripts/selected_examples.json")