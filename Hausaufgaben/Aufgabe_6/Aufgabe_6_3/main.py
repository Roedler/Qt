from BasicCard import BasicCard

def firstBasicCard():
    cardName = "Astrales Echo"
    cardSubtitle = "Eine schimmernde, halbtransparente, humanoide Erscheinung, die bei ihrem Erscheinen die Schwerkraft in der Nähe verzerrt. Es ist schwach im direkten Kampf, aber seine psychischen Angriffe sind verheerend."

    card = BasicCard(cardName, cardSubtitle)

    print(f"{card.toString()}")

if __name__ == "__main__":
    firstBasicCard()
