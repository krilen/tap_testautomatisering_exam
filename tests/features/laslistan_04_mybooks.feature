@mybooks
Feature: Mina böcker

    Background: Är på webbsidan och sidan "Mina böcker"
        Given att man befinner sig på webbsidan Lässidan och sidan mina böcker

# US15
# som en användare
# vill jag att det skall vara tomt på mina böcker sidan från början
# så att jag får lägga till de böcker som jag vill.

    Scenario: Kommer till mina böcker sidan utan några favoritböcker listade
        Then när man kommer till mina böcker sidan informeras man om att här kommer dina favoritböcker listas
