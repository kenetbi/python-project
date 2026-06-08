def translator(language):
    translations = {
    'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
    'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
    'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }

    def translate_word(word):
        if word in translations[language]:
            return translations[language][word]
        else:
            return "Not Available"
        
    return translate_word


translate_to_spanish = translator('spanish')
print(translate_to_spanish('goodbye'))

translate_to_spanish = translator('french')
print(translate_to_spanish('goodbye'))

translate_to_spanish = translator('italian')
print(translate_to_spanish('goodbye'))

