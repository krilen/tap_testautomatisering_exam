@combo
Feature: Kontrollera ordningen på mina böcker sidan

# US20
# som en användare
# vill jag säkerställa att listan med böcler på med mina böcker sida är i samma ordning som böckerna i katalogen
# så att ordningen inte påverkas av i vilken orning jag markerade böckerna i katalogen.

    Scenario: Säkerställ att ordningen på sidan mina böcker är baserad på ordningen från katalog sidan
        Given att jag befinner mig på webbsidan Läslistan och sidan lägg till bok
        When man skriver in titel och författare till en bok: "Mody Dick", "Herman Melville"
        And klickar man på lägg till ny bok knappen
        When går till mina böcker sidan
        Then när man kommer till mina böcker sidan informeras man om att här kommer dina favoritböcker listas
        When går till katalogsidan
        When klickar på markeringsknappen för bokraden, "L"
        When markerar böcker i en speciell ordning: "5,2,4,0"
        When går till mina böcker sidan
        Then när man kommer till mina böcker sidan informeras man inte längre om att här kommer favoritböcker att listas
        And ordningen på böckerna är den som i katalogen med "Mody Dick" som sist

