# Examination

[<< ReadMe](/README.md)

## Testverktyg

_Du ska lösa uppgiften självständigt. När du tar hjälp av AI, eller diskuterar med andra studerande, ska du se till att du förstår vad koden gör._

---

## Bakgrund

"Läslistan" är en webbsida där man kan välja ut sina favoriter från en katalog med böcker, eller lägga till nya. Beställaren är en organisation som vill öka barns och ungas läsande. Nuvarande version har begränsad funktionalitet. På sikt vill man utöka webbsidan med funktioner för att dela sina listor, skapa quiz och diskutera böcker med varandra. Därför är det viktigt att det finns tester för all grundläggande funktionalitet. Detta är din uppgift!

Webbsidan som ska testas: [https://tap-ht24-testverktyg.github.io/exam-template/](https://tap-ht24-testverktyg.github.io/exam-template/)  
(För den som är intresserad av JavaScript och React finns källkoden i ett repo i kursens GitHub-organisation, alltså där alla kodexempel finns.)

Du ska ha en README.md fil i projektets rotmapp, där du berättar

- vad du har testat,
- hur man startar projektet.

Börja med att läsa igenom hela uppgiften.

## Detta ska du göra

1. Skapa ett projekt med Python, pytest, Playwright och behave. Gör ett motsvarande, publikt repo på GitHub. (Det är tillåtet att använda fler moduler.)

2. Skapa filerna README.md och STORIES.md i projektets rotmapp. (Du får använda STORIES.txt om du hellre vill det.)

3. Formulera _user stories_ för den funktionalitet som finns på webbsidan idag. Skriv ner dessa i STORIES.md.

4. Ta fram _feature-filer_ utifrån dina user stories.

5. Bygg _step-filer_ för alla _features_. Page-filer vid behov.

6. Skriv ner 1\) vad du har testat, och 2\) hur man startar projektet, i README.md. Nu kan du lämna in!

### Inlämning

Skapa en textfil "exam1_mitt_namn.txt" som innehåller länk till ditt projekt på GitHub. Ladda upp textfilen på LearnPoint. Kom ihåg, det räcker inte med att ladda upp filen, du måste klicka på knappen för att lämna in också\!

---

## För G krävs

1. Det finns user stories som täcker all funktionalitet.
2. Alla user stories har minst en feature. Alla features har minst ett scenario.
3. Det går att starta ditt projekt, efter instruktionerna du har skrivit i README.md.
4. Alla test är gröna.

## För VG krävs

5. Högre kvalitet och kod som återanvänds.
6. Du använder designmönstret Page Object.
7. Du använder Scenario Outline.
8. Dina features försöker täcka alla meningsfulla möjligheter för motsvarande user story.

Exempel på meningsfulla möjligheter: testa inte bara att det går att favoritmarkera, utan att det går att ta bort en favoritmarkering, och vad som händer om man klickar fler än två gånger.

---

## Tips

- Flera element på sidan har ett _testid_ som [du kan använda med Playwright](https://playwright.dev/docs/locators#locate-by-test-id).
- Använd _headless_ när du kommit en bit och när du lämnar in uppgiften. Det snabbar upp testandet rejält.
- Kom ihåg att testa att alla vyer gör det de ska, och att navigeringen fungerar.
