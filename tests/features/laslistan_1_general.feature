Feature: Webbsidan Läslistan

    Background: Är på webbsidan
        Given att jag befinner mig på webbsidan Läslistan

# US01
# som en användare  
# vill jag säkerställa att webbsidan rubrik och title stämmer  
# så jag är säker på att jag är på rätt ställe

    Scenario: Bekräfta titel och rubrik på webbsidan
        Then bör jag se att titeln på webbsidan är "Läslistan"
        And att webbsidan har en rubrik med texten "Läslistan"

# US02

    Scenario: Bekräfta antal navigeringsknappar på webbsidan
        Then bör jag kunna se att det finns "3" st navigationsknappar på webbsidan

# US03

    Scenario: Bekräfta namn och testid på navigeringsknappar på webbsidan
        Then bör jag kunna se att det är rätt namn och testid på vardera navigationsknapp på webbsidan
            | namn          | testid    | count |
            | Katalog       | catalog   | 1     |
            | Lägg till bok | add-book  | 1     |
            | Mina böcker   | favorites | 1     |
            | Katalog       | favorites | 0     |

# US04

    Scenario Outline: Bekräfta att man kommer till rätt sida vid navigering
        When när jag klickar på en navigeringsknapp med ett specifikt test-id: "<testid>"
        Then bör jag se att den aktuella navigeringknappen, "<testid>", blivit deaktiverad
        And självaste innehållet för sidan har ett div element med en speciell class: "<divclass>"

        Examples:
            | testid    | divclass   |
            | catalog   | .catalog   |
            | add-book  | .form      |
            | favorites | .favorites |

