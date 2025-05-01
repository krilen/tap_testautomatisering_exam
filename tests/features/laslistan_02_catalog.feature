Feature: Katalog

    Background: Är på webbsidan och sidan "Katalog"
        Given att man befinner sig på webbsidan Lässidan och sidan katalog

# US06
# som en användare
# vill jag kunna klicka på rätt ställe på en bok rad för att välja en bok
# så att den då blir blir markerad som vald.

    Scenario: Klicka på rätt ställe för att markera en bokrad
        Then bokrad, "F", är inte markerad
        When klickar på markeringsknappen för bokraden, "F"
        #Then bokrad, "F", är markerad

# US07
# som en användare
# vill jag kunna se om en bok har blivit vald
# så att jag vet att den redan har blivit vald.


    Scenario: Kontrollera om en bokrad är markerad
        When klickar på markeringsknappen för bokraden, "L"
        Then bokrad, "L", är markerad

# US08
# som en användare
# vill jag kunna avmarkera en bok som redan är vald
# så jag vet att boken inte längre är vald.


    Scenario Outline: Om en bokrad är markerad klicka på den för att avmarkera den
        When klickar på markeringsknappen för bokraden, "<bokrad>"
        Then bokrad, "<bokrad>", är markerad
        When klickar på markeringsknappen för bokraden, "<bokrad>"
        Then bokrad, "<bokrad>", är inte markerad

        Examples:
            | bokrad |
            | F      |
            | 3      |
            | 4      |
            | L      |

# US09
# som en användare
# vill jag säkerställa att toggligen vid markering och avmarkering av böcker fungerar
# så att jag kan se att böcker kan väljas och avväljas.

    Scenario Outline: Toggling av klickning av bokrad
        When "<antal>" klickningar på markeringsknappen för bokraden, "<bokrad>"
        Then antal klickningar avgör om bokraden, "<bokrad>", blir markerad, "<markerad>", eller inte

        Examples:
            | bokrad | antal | markerad |
            | F      | 3     | 1        |
            | L      | 4     | 0        |
            | 2      | 9     | 1        |
            | 5      | 0     | 0        |