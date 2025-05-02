# Exam uppgift för Testautomatisering och testverktyg

## Vad som har testats

Jag har testet websidan "https://tap-ht24-testverktyg.github.io/exam-template/" och dess funktioner.

---

## Köra testet: 'behave'

För att köra testet måtet först alla dependencies för python installeras

```
pip install -r requirements.txt
```

Därefter kan testet köras genom 'behave' kommandot

```
'behave' - körs i "tests/" mappen.
```

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
'behave --tags=online -k' - körs i "tests/" mappen. Kör endast scenarion taggad med '@online' och visa inga andra scenarion
```

---

## Övrigt

### Sidor

User stories som används för Behave: [User Stories >>](/STORIES.md)  
Examens uppgiften som skall lösas: [Exam uppgift >>](/UPPGIFT.md)
