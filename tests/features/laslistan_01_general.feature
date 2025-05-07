@general
Feature: Webbsidan Läslistan

    Background: Är på webbsidan
        Given att man befinner sig på webbsidan Läslistan

# US01
# som en användare
# vill jag säkerställa att webbsidans rubrik och title stämmer
# så jag är säker på att jag är på rätt ställe.

    @online
    Scenario: Bekräfta titel och rubrik på webbsidan
        Then bör man se att titeln på webbsidan är "Läslistan"
        And att webbsidan har en rubrik med texten "Läslistan"

# US02
# som en användare
# vill jag veta antalet knappar för navigation som finns på webbsidan
# så jag vet är medvetan om hur många navigerings knappar på webbsidan det skall vara.

    Scenario: Bekräfta antal navigeringsknappar på webbsidan
        Then bör man kunna se att det finns "3" st navigationsknappar på webbsidan

# US03
# som en användare
# vill jag kunna kontrollera navigationsknapparna
# så jag vet att deras namn ger rätt återkoppling till användaren.

    Scenario: Bekräfta namn och testid på navigeringsknappar på webbsidan
        Then bör man kunna se att det är rätt namn och testid på vardera navigationsknapp på webbsidan
            | namn          | testid    | count |
            | Katalog       | catalog   | 1     |
            | Lägg till bok | add-book  | 1     |
            | Mina böcker   | favorites | 1     |
            | Katalog       | favorites | 0     |

# US04
# som en användare
# vill jag säkerställa att varje navigations knapp leder till rätt sida
# så jag vet att knappen fungerar och jag kommer till rätt sida.

    Scenario Outline: Bekräfta att man kommer till rätt sida vid navigering
        When när man klickar på en navigeringsknapp med ett specifikt test-id: "<testid>"
        Then bör man se att den aktuella navigeringknappen, "<testid>", blivit deaktiverad
        And självaste innehållet för sidan har ett div element med en speciell class: "<divclass>"

        Examples:
            | testid    | divclass   |
            | catalog   | .catalog   |
            | add-book  | .form      |
            | favorites | .favorites |
