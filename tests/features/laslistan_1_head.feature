Feature: Webbsidan Läslistan

    Background: Är på webbsidan
        Given att jag befinner mig på webbsidan läslistan

# US01
# som en användare  
# vill jag säkerställa att webbsidan rubrik och title stämmer  
# så jag är säker på att jag är på rätt ställe


    Scenario: Bekräfta titel och rubrik på webbsidan
        Then bör jag se att titeln på webbsidan är "Läslistan"
        And att webbidan har en rubrik med texten "Läslistan"