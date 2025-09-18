import csv
from collections import defaultdict

class BidirectionalTranslator:
    def __init__(self, csv_filepath, lang1='Bravanese', lang2='English'):
        """
        Initializes the Translator by loading the CSV into two dictionaries.
        """
        self.lang1_to_lang2 = defaultdict(list)
        self.lang2_to_lang1 = defaultdict(list)
        self.lang1 = lang1
        self.lang2 = lang2

        try:
            with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    word1_original = row[lang1].strip()
                    word2_original = row[lang2].strip()

                    word1_key = word1_original.lower()
                    word2_key = word2_original.lower()

                    self.lang1_to_lang2[word1_key].append(word2_original)
                    self.lang2_to_lang1[word2_key].append(word1_original)

        except FileNotFoundError:
            raise Exception("CSV file not found.")
        except KeyError:
            raise Exception("Language columns not found in the CSV.")
    
    def translate(self, input_word, direction='lang1_to_lang2'):
        """
        Translates a word in the chosen direction.
        """
        input_word_clean = input_word.strip().lower()

        if direction == 'lang1_to_lang2':
            translations = self.lang1_to_lang2.get(input_word_clean)
        elif direction == 'lang2_to_lang1':
            translations = self.lang2_to_lang1.get(input_word_clean)
        else:
            raise ValueError("Invalid direction. Use 'lang1_to_lang2' or 'lang2_to_lang1'.")

        if translations:
            return [self._prettify(word) for word in translations]
        else:
            return [f"'{input_word}' not found in the wordlist."]
    
    @staticmethod
    def _prettify(word):
        """Helper to capitalize words properly."""
        return word.capitalize()

def interactive_translation(translator):
    """
    Provides a simple user interface to translate words.
    """
    print("Welcome to the Bravanese-English Translator!")
    print("Igemaa karka qamuusi ya Chimiini na Chingerenza!")
    print("\nType 'exit' at any time to quit.")
    print("Aandika 'exit' watta we nakhsulo ku lawa.\n")

    while True:
        direction = input("Choose translation direction (1 = Bravanese → English, 2 = English → Bravanese): ").strip()
        if direction.lower() == 'exit':
            print("Waraadi!")
            break
        if direction not in ['1', '2']:
            print("Invalid option. Please enter 1 or 2.")
            continue

        word = input("Enter the word to translate: ").strip()
        if word.lower() == 'exit':
            print("Waraadi!")
            break

        if direction == '1':
            translations = translator.translate(word, direction='lang1_to_lang2')
        else:
            translations = translator.translate(word, direction='lang2_to_lang1')

        print("Translations:", ", ".join(translations))
        print("-" * 40)

if __name__ == "__main__":
    # Replace with the path to your CSV file if different
    csv_path = 'bravanese.csv'
    translator = BidirectionalTranslator(csv_path)
    interactive_translation(translator)
