from Hausaufgaben.Hausaufgabe_6.Aufgabe_6_3.MonsterCard import MonsterCard


def monsterDeck():
    MONSTER_DATA = [
        {"title": "Astrales Echo", "image": "Astrales Echo.png",
         "subtitle": "Eine schimmernde, halbtransparente, humanoide Erscheinung, die bei ihrem Erscheinen die Schwerkraft in der Nähe verzerrt. Es ist schwach im direkten Kampf, aber seine psychischen Angriffe sind verheerend.",
         "stats": (30, 50, 5, 10, 0)},

        {"title": "Schiefer-Haut-Wächter", "image": "Schiefer-Haut-Wächter.png",
         "subtitle": "Ein massiver, langsamer Golem mit einer Haut aus dunklem Schiefergestein. Er ist extrem gepanzert und widerstandsfähig, besitzt aber keine offensiven Waffen außer seiner schieren Masse.",
         "stats": (150, 5, 80, 10, 50)},

        {"title": "Toxischer Schleicher", "image": "Toxischer Schleicher.png",
         "subtitle": "Ein kleines, kriechendes Insekt, das sich von verrottender Materie ernährt. Es ist schnell und hinterlässt eine Spur aus ätzendem, toxischem Schleim.",
         "stats": (20, 5, 5, 40, 0)},

        {"title": "Sonnenschlund-Raptor", "image": "Sonnenschlund-Raptor.png",
         "subtitle": "Ein vogelähnliches, angriffslustiges Raubtier, dessen Schnabel bei Gefahr glüht und kleine Feuerbälle speien kann. Es ist mittelschwer stark und unglaublich schnell.",
         "stats": (70, 60, 30, 40, 10)},

        {"title": "Chronos-Parasit", "image": "Chronos-Parasit.png",
         "subtitle": "Ein mikroskopisch kleiner Organismus, der in die Gelenke von Opfern eindringt und deren Bewegungen für Sekundenbruchteile verlangsamt oder beschleunigt. Nicht gefährlich, aber extrem störend.",
         "stats": (5, 0, 0, 0, 0)},

        {"title": "Klagender Nebelfürst", "image": "Klagender Nebelfürst.png",
         "subtitle": "Eine große schattenhafte Gestalt, die in dichtem, eiskaltem Nebel gehüllt ist. Es greift nur selten physisch an; seine Hauptwaffe ist ein schwächer machender, lähmender Schrei.",
         "stats": (60, 10, 10, 5, 0)},

        {"title": "Dampf-Gnom", "image": "Dampf-Gnom.png",
         "subtitle": "Ein kleiner mechanischer Diener mit einer Messinghülle. Es ist nicht zum Kampf gebaut, aber es kann heißen, gepanzerten Dampf ausstoßen, um Angreifer kurzzeitig zu blenden.",
         "stats": (25, 0, 5, 0, 10)},

        {"title": "Titanen-Wurzel-Kraken", "image": "Titanen-Wurzel-Kraken.png",
         "subtitle": "Eine enorm große Kreatur, die wie ein Bündel aus verdrehten, dicken Baumwurzeln aussieht. Sie ist extrem stark und nutzt Ranken, um Gegner zu zermalmen.",
         "stats": (200, 70, 50, 90, 30)},

        {"title": "Der Gold-Gefräßige", "image": "Der Gold-Gefräßige.png",
         "subtitle": "Ein flinker, kleiner Kobold mit einer Haut, die Münzen ähnelt. Er ist schwach, aber extrem diebisch und versucht, alle metallischen Gegenstände zu stehlen.",
         "stats": (10, 5, 5, 5, 0)},

        {"title": "Kybernetischer Gladiator (Einheit 7)", "image": "Kybernetischer Gladiator (Einheit 7).png",
         "subtitle": "Eine große, schwerfällige, gepanzerte Kampfmaschine mit einem Plasmawerfer als Arm. Konzipiert als reiner Frontkämpfer; sehr stark und widerstandsfähig.",
         "stats": (120, 80, 70, 70, 40)},

        {"title": "Obsidian-Flügel-Fledermaus", "image": "Obsidian-Flügel-Fledermaus.png",
         "subtitle": "Eine mittelgroße, angriffslustige Fledermaus mit Klingen-scharfen Obsidian-Flügeln. Sie ist schnell und kann tiefe Schnittwunden verursachen.",
         "stats": (45, 40, 10, 30, 5)},

        {"title": "Der Stille Jäger", "image": "Der Stille Jäger.png",
         "subtitle": "Eine humanoide Gestalt, die sich perfekt an ihre Umgebung anpasst. Sie ist körperlich durchschnittlich, aber ihre Fähigkeit zur Tarnung und ihre lautlose Annäherung machen sie gefährlich.",
         "stats": (75, 35, 35, 35, 15)},

        {"title": "Gedanken-Spinner", "image": "Gedanken-Spinner.png",
         "subtitle": "Eine kleine, spinnenartige Kreatur, die unsichtbare Netze aus mentaler Energie webt. Körperlich schwach, aber kann Opfer in illusionäre Alpträume fangen.",
         "stats": (15, 5, 5, 15, 0)},

        {"title": "Ätherischer Phönix", "image": "Ätherischer Phönix.png",
         "subtitle": "Ein leuchtender Vogel aus reinem Feuer und Licht. Er ist stark und kann nur durch spezielle, magische Mittel dauerhaft besiegt werden, da er sich selbst regenerieren kann.",
         "stats": (90, 50, 20, 60, 10)},

        {"title": "Rost-Koloss", "image": "Rost-Koloss.png",
         "subtitle": "Ein großer Haufen aus Schrott und verrostetem Metall, der sich selbst zu einer humanöden Form zusammengeschweißt hat. Sehr langsam, aber extrem gepanzert und besitzt massive Schlagkraft.",
         "stats": (180, 60, 90, 80, 60)},

        {"title": "Die singende Sirene (der Tiefe)", "image": "Die singende Sirene (der Tiefe).png",
         "subtitle": "Eine schöne, aber bösartige Meerjungfrau. Sie ist körperlich schwach, aber ihr hypnotischer Gesang ist verführerisch und kann Opfer in den Tod locken.",
         "stats": (40, 5, 5, 10, 0)},

        {"title": "Der Zorn der Leere", "image": "Der Zorn der Leere.png",
         "subtitle": "Eine formlose, amöbenartige Masse, die alles verschlingt, was sie berührt. Sie ist weder stark noch schwach, sondern existiert nur, um zu konsumieren.",
         "stats": (100, 50, 50, 50, 50)},

        {"title": "Kristallscherbe", "image": "Kristallscherbe.png",
         "subtitle": "Eine kleine, aber messerscharfe Kreatur aus lebendigem, zerbrochenem Kristall. Sie ist schnell und ihre Berührung verursacht tiefe Schnittwunden; aber leicht zu zerbrechen.",
         "stats": (15, 25, 5, 20, 0)},

        {"title": "Bio-Mechanischer Saboteur", "image": "Bio-Mechanischer Saboteur.png",
         "subtitle": "Ein mittelschwerer Roboter, der sich als Mensch verkleiden kann. Er ist stark genug für einen schnellen Nahkampf und mit versteckten Betäubungswaffen ausgestattet.",
         "stats": (80, 45, 40, 45, 20)},

        {"title": "Albtraum-Kojote", "image": "Albtraum-Kojote.png",
         "subtitle": "Ein hundeartiges, angriffslustiges Raubtier mit glühenden Augen. Es ist schnell und kann die größten Ängste seiner Opfer als Illusionen manifestieren, während es physisch angreift.",
         "stats": (65, 55, 20, 35, 5)},
    ]

    monsterDeck = {}
    basePath = "/Users/lno/Library/Mobile Documents/iCloud~md~obsidian/Documents/lennart/Uni/3.Semester/Modellierung-und-Programmierung-interaktiver-Systeme/Hausaufgaben/Aufgabe_5/Aufgabe_5_3/!Media/"

    for data in MONSTER_DATA:
        imgPath = basePath + data["image"]
        # pixmap = QPixmap(imgPath)
        healthPoints, attackValue, defenseValue, damageValue, armor = data["stats"]
        card = MonsterCard(
            key=None,
            title=data["title"],
            subtitle=data["subtitle"],
            healthPoints=healthPoints,
            attackValue=attackValue,
            defenseValue=defenseValue,
            damageValue=damageValue,
            armorValue=armor,
            pixmap=None
        )
        monsterDeck[card.getKey()] = card

        # if pixmap.isNull():
        #     print(f"WARNING: Image for '{data['title']}' could not be loaded under: '{imgPath}'.")

    print(f"{len(monsterDeck)} monster card are loaded.\n")

    i = 1
    for monster in monsterDeck:
        print(f"{i}. {monsterDeck[monster].getTitle()}")
        i += 1


    return monsterDeck

if __name__ == "__main__":
    monsterDeck()
