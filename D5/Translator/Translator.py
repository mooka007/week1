from deep_translator import GoogleTranslator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translations = {
    word: GoogleTranslator(source='fr', target='en').translate(word)
    for word in french_words
}

print(translations)