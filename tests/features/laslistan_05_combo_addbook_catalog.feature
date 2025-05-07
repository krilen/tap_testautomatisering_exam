@combo
Feature: Lägg till bok och säkerställ att den hamnar i katalogen

# US16  
# som en användare  
# vill jag att en bok som läggs till hamnar i katalogen för böcker och får ett korrekt testid  
# så att man kan hantera böcker som läggs till på samma sätt som befintliga böcker.

    Scenario Outline: Lägg till bok och säkerställ att den hamnar i katalogen
        Given att man befinner sig på webbsidan Läslistan och sidan lägg till bok
        When man skriver in titel och författare till en bok: "<titel>", "<forfattare>"
        And klickar man på lägg till ny bok knappen
        Then när man går till katalogens sida har boken med dess titel: "<titel>" och författare: "<forfattare>" hamnat i listan med böcker
        And ett korrekt katalog testid: "<testid>" har skapats

        Examples:
            | titel         | forfattare          | testid             |
            | a             | b                   | star-a             |
            | Mody Dick     | Herman Melville     | star-Mody Dick     |
            | Odysseus      | James Joyce         | star-Odysseus      |
            | Röde Orm      | Frans. G. Bengtsson | star-Röde Orm      |
            | Madame Bovary | Gustave Flaubert    | star-Madame Bovary |
            | 1             | 2                   | star-1             |
