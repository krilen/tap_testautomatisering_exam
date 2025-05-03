@combo
Feature: Lägg till en bok och markera och boken hamnar på mina böcker sidan

# US18
# som en användare
# vill jag kunna lägga till en bok och markera boken i katalogen
# så att hamnar på sidan med mina böcker.

    Scenario Outline: Lägg till en bok och markera boken och boken hamnar på mina böcker sidan
        Given att jag befinner mig på webbsidan Läslistan och sidan lägg till bok
        When man skriver in titel och författare till en bok: "<titel>", "<forfattare>"
        And klickar man på lägg till ny bok knappen
        When går till mina böcker sidan
        Then när man kommer till mina böcker sidan informeras man om att här kommer dina favoritböcker listas
        When går till katalogsidan
        When klickar på markeringsknappen för bokraden, "L"
        When går till mina böcker sidan
        Then när man kommer till mina böcker sidan informeras man inte längre om att här kommer favoritböcker att listas
        And kan man se att boken finns listad som en favoritbok: "<titel>"

        Examples:
            | titel         | forfattare          |
            | a             | b                   |
            | Mody Dick     | Herman Melville     |
            | Odysseus      | James Joyce         |
            | Röde Orm      | Frans. G. Bengtsson |
            | Madame Bovary | Gustave Flaubert    |
            | 1             | 2                   |


# US19
# som en användare
# vill jag kunna lägga till en bok, markera och sedan avmarkera boken i katalogen
# så att boken först hamnar på sidan och sedan tas bort från sidan med mina böcker.

    Scenario Outline: Lägg till en bok och markera boken och boken hamnar på mina böcker sidan, sedan avmarkera boken och boken förvinner från mina böcker sidan
        Given att jag befinner mig på webbsidan Läslistan och sidan lägg till bok
        When man skriver in titel och författare till en bok: "<titel>", "<forfattare>"
        And klickar man på lägg till ny bok knappen
        When går till katalogsidan
        When klickar på markeringsknappen för bokraden, "L"
        When går till mina böcker sidan
        Then när man kommer till mina böcker sidan informeras man inte längre om att här kommer favoritböcker att listas
        And kan man se att boken finns listad som en favoritbok: "<titel>"
        When går till katalogsidan
        When klickar på markeringsknappen för bokraden, "L"
        When går till mina böcker sidan
        Then när man kommer till mina böcker sidan informeras man om att här kommer dina favoritböcker listas
        And kan man se att boken inte finns listad som en favoritbok: "<titel>"
        

        Examples:
            | titel         | forfattare          |
            | a             | b                   |
            | Mody Dick     | Herman Melville     |
            | Odysseus      | James Joyce         |
            | Röde Orm      | Frans. G. Bengtsson |
            | Madame Bovary | Gustave Flaubert    |
            | 1             | 2                   |