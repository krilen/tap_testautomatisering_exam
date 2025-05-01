Feature: Lägg till en bok och markera och avmarkera boken i katalogen

# US17
# som en användare
# vill jag kunna lägga till en bok
# som jag sedan kan markera och avmarkera boken i katalogen.

    Scenario Outline: Lägg till en bok och markera och avmarkera boken i katalogen
        Given att jag befinner mig på webbsidan Läslistan och sidan lägg till bok
        When man skriver in titel och författare till en bok: "<titel>", "<forfattare>"
        And klickar man på lägg till ny bok knappen
        When går till katalogsidan
        Then bokrad, "L", är inte markerad
        When klickar på markeringsknappen för bokraden, "L"
        Then bokrad, "L", är markerad
        When klickar på markeringsknappen för bokraden, "L"
        Then bokrad, "L", är inte markerad

        Examples:
            | titel         | forfattare          |
            | a             | b                   |
            | Mody Dick     | Herman Melville     |
            | Odysseus      | James Joyce         |
            | Röde Orm      | Frans. G. Bengtsson |
            | Madame Bovary | Gustave Flaubert    |
            | 1             | 2                   |
