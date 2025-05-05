@addbook
Feature: Lägga till böcker

    Background: Är på webbsidan och sidan "Lägg till bok"
        Given att jag befinner mig på webbsidan Läslistan och sidan lägg till bok

# US10
# som en användare
# vill jag kunna lägga till en bok
# så jag vet är möjligt att lägga till nya böcker.

    Scenario: Lägga till en bok
        Then när man kommer till lägg till bok sidan bör inte en bok kunnas läggas till
        And fälten för titel och författare skall vara tomma
        When man skriver in titel och författare till en bok
        Then skall en bok kunnas läggas till 

# US11  
# som en användare
# vill jag vara säker på att en bok läggs till på rätt sätt
# så att både en boks titel och författare läggs till.

    Scenario Outline: Kontrollera när det är möjligt att lägga till en bok
        Then när man kommer till lägg till bok sidan bör inte en bok kunnas läggas till
        When man skriver in titel och författare till en bok: "<titel>", "<forfattare>"
        Then måste både titel och författare anges för att en bok skall "<accepteras>" 

        Examples:
            | titel     | forfattare      | accepteras |
            | Mody Dick | Herman Melville | 1          |
            |           | Herman Melville | 0          |
            | Mody Dick |                 | 0          |
            |           |                 | 0          |

# US12
# som en användare
# vill jag efter att ha lagt till en bok att formuläret nollställs
# så att jag kan lägga till ytterligare en bok.

    Scenario: Lägga till en bok och nollställda fält
        Then när man kommer till lägg till bok sidan bör inte en bok kunnas läggas till
        When man skriver in titel och författare till en bok
        When klickar man på lägg till ny bok knappen
        Then fälten för titel och författare skall vara tomma

