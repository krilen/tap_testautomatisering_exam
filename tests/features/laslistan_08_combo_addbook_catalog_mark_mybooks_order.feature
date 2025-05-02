@combo
Feature: Kontrollera ordningen på mina böcker sidan

# US20
# som en användare
# vill jag säkerställa att ordningen på böckerna på mina böcker
# så att ordningen kopplas till ordningen som böckerna markerades i katalogen.

    Scenario: Säkerställ att ordningen på sidan mina böcker är baserat på ordningen markerade böcker på katalog sidan
        Given att jag befinner mig på webbsidan Läslistan och sidan lägg till bok
        When man skriver in titel och författare till en bok: "Moby Dick", "Herman Melville"
        And klickar man på lägg till ny bok knappen
        When man skriver in titel och författare till en bok: "Odysseus", "James Joyce"
        And klickar man på lägg till ny bok knappen
        When man skriver in titel och författare till en bok: "Röde Orm", "Frans. G. Bengtsson"
        And klickar man på lägg till ny bok knappen
        When man skriver in titel och författare till en bok: "Madame Bovary", "Gustave Flaubert"
        And klickar man på lägg till ny bok knappen
        When går till katalogsidan
        # Here I am 
        # 0. After creating the list below lets make it simplear to add books
        # 1. Lets mark all of the books from last to first 
        # 2. Verify the order on my books page
        # 3. REmove the second by by unmarking it
        # 4. Verify the new order
        # 5. remove another book also second (middle)
        # 6. Verify the order
        # 7. Done