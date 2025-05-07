# Exam uppgift för Testautomatisering och testverktyg

## Vad som har testats

Jag har testet websidan "https://tap-ht24-testverktyg.github.io/exam-template/" och dess funktioner.
 - Testat att webbsidan finns och att dess title och rubrik är korrekt.  
   Att det finns 3 st knappar på webbsidan med korrekt namn och att de laddar/länkar till rätt sida.
 - Kontrollerat att man kan markera och avmarkera böcker på katalogsidan.
 - Man endast kan lägga till en bok om både författare och title har skrivits in och att efter en bok har lagts till rensas fälten.
 - Mina böcker sidan informerar att här kommer ens favorit böcker att listas.
 - Därefter har ett antal olika kombinationer kontrollerats.
   - Lagt till en bok och kontrollerat att den hamnar i katalogen med böcker.
   - Lagt till en bok och och sedan markerat den i katalogen med böcker.
   - Att en markerad bok som lagts till hamnar i mina böcker listan och försvinner om man tar bort markering.
   - Att ordningen på böckerna i mina böcker listan är samma ordning som katalog listan.

### Övrigt information om testerna

Totalt har 8 st features med tillhörande steps filer skapats, koncentrationen av "steps" finns i de första 4 filerna. För kombinationerna har nästan allt kunnats återanvändas från tidigare steps filer till de scenariorna.

Totalt är det 48 st scenarion och 319 steps, stort tack till de olika Scenario Outlines.

Har haft som mål att flytta allt "Python" till Page objectet, laslistan.py.

Skrivit alla scenarion på Svenska men valde att skriva det teknika inklusive Page objectet på Engelska.

Har lagt några taggar på de olika scenariorna, se nedan för mer detaljer.

### User story nr 5
Eftersom jag skrev user stories innan jag påbörjade att skriva testerna så när jag kom till att skriva testet för user story nummer 5 kom jag inte på hur eller om det ens var möjligt att utföra testet så som jag vill. Valde därför att sätt denna user story som struken istället för att omnumrera.

---

## Köra testet: 'behave'

För att köra testet måtet först alla dependencies för Python installeras

```
pip install -r requirements.txt
```

Därefter kan testet köras genom 'behave' kommandot

```
'behave' - körs i "tests/" mappen. Detta köra alla scenarion
```

### Taggar

Det finns taggar för vissa scenarion

- 'online': Scenario som kontrollerar on webplatsen som skall konttolleras kan nås
- 'general': Scenarion som gör kontroller när det gäller websidan, rubrik, knappar och de olika undersidorna
- 'catalog: Scenarion som har att göra med Katalogen och de böcker som är listade där (som default)
- 'addbook: Scenarion som handlar om att lägga till böcker (som default)
- 'mybooks: Scenarion som handlar om favorit böcker (som default)
- 'combo: Längre scenarion som gör olika saker och blandar in olika sidor  
   ex: Lägg till en bok, markera den, kontrollera mina böcker sidan, ...  
   Nästan alla dessa scenarion bygger på varandra och blir längre och längre.

```
'behave --tags online -k' - körs i "tests/" mappen. Kör endast scenarion taggad med "online" och visar inga andra scenarion
'behave --tags online,general -k' - körs i "tests/" mappen. Kör scenariona taggade med "online" och "general" och visar inga andra scenarion
```

---

## Övrigt

### Sidor

User stories som används för Behave: [User Stories >>](/STORIES.md)  
Examens uppgiften som skall lösas: [Exam uppgift >>](/UPPGIFT.md)
