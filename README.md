# MIJN PROJECTVOORSTEL


## 1. Het doel mijn van project

Mijn project wordt een fantasiegame, die zich afspeelt in de middeleeuwen. Voor de game wil ik ideeën ophalen uit DND-achtige games, zoals de combat en de klassensetting. De game wilde ik eerst als een visual novel creëren. Daarna kwam ik op het idee (na overleg op dinsdag) om de game in 2D-setting te maken, met een wereldmap waarbij naar andere kamers gemanoeuvreerd kan worden. Wel wil ik ook de optie openhouden voor een 3D-setting, in een live-omgeving binnen een wereld. De game wil ik op de PC toegankelijk maken, om meer ruimte te hebben voor de interface van de game. Ook wil ik een combatsysteem opzetten. De verhaallijn heb ik in richtlijnen opgezet en zal ik verder uitleggen bij de vragen over mijn project. 

---

## 2. Het formaat

### 2.1 Het probleem 

Mijn project heeft als doel DND-achtige games toegankelijker te maken voor een breder publiek, omdat DND-achtige games normaliter een kleinere (niche) doelgroep heeft. DND-achtige games hebben vaak een systeem dat door het grote publiek wat moeilijker wordt ervaren, en games zoals Baldur's Gate 3 hebben het makkelijker en aantrekkelijker gemaakt voor de gemiddelde gamer of zelfs de gemiddelde internet-gebruiker om complexere games te spelen.

### 2.2 Het doelgroep

Dit project is vooral gericht op jongvolwassenen, die familiar zijn met het internet, en daarmee dus ook (een lichte vorm van) gamen. Het is niet specifiek gericht op DND-fanaten of reguliere gamers, aangezien ik  wil proberen de game voor een breder publiek aantrekkelijk & toegankelijk te maken. 

### 2.3 De setting

De setting van de game is op de PC én laptop. Dit wil ik, omdat veel vergelijkbare, uitgebreide games zoals de Witcher of Baldur's Gate alleen toegankelijk op de PC zijn. Het probleem dat daarbij komt kijken, is dat game PC's vaak vanaf €1000,- starten. De prijs loopt ook steeds verder op, naarmate je een een betere grafische kaart wil (voor het runnen van de games überhaupt) of meer opslagruimte. Games zoals de Sims maken daarom ook veel winst. De games worden opzettelijk steeds simpeler gemaakt, opdat de games op laptops (met doorgaans een zwakke grafische kaart) te spelen zijn. Hierdoor hebben ze ook toegang tot een bredere publiek, doordat hun games zo toegankelijk worden gemaakt. Daarnaast is een interface op PC en/of laptop beter dan een interface op de telefoon, omdat er meer beweegruimte is voor het spelen van de game.

### 2.4 Wat doet mijn oplossing beter?

Zoals in 2.3 eigenlijk al vermeld is, zijn de meeste DND-achtige fantasy games alleen toegankelijk op de PC en niet op de normale laptop met een zwakke grafische kaart. Mijn doel met mijn game is dit soort games meer toegankelijk te maken voor een bredere doelgroep door deze DND-achtige games simplistischer te maken. Voor een persoon die nog nooit een game heeft gespeeld, moet mijn game begrijpelijk en toegankelijk zijn. Dit in tegenstelling tot veel games in de fantasieachtige thema, die vaak (naar mijn mening) soms te complex worden gecreëerd. Voor de gewone gamer is het makkelijk te begrijpen, maar niet voor iemand die niet familiair is met games. Door de complexiteit kan hij of zij namelijk ook sneller afhaken. 

---

## 3. De schets

Ik heb voor mijn voorbeeld van de gameplay één van de potentiële hoofdkarakters getekend op mijn iPad met ibisPaint X. Vervolgens heb ik als achtergond een online wallpaper van The Legend of Zelda gebruikt en geplakt achter mijn schets, en heb ik een beslissingsmenu toegevoegd. Voor de uiteindelijke game zal ik niet zomaar afbeeldingen van het internet halen, dan zal ik de achtergronden tekenen. Omdat ik nog niet zeker ben of ik de game in 2D of 3D ga uitvoeren, heb ik een 2D voorbeeld (cutscene) geschetst. 
![Example gameplay](./Project/Example_gameplay.PNG)

De combat wil ik op de manier van Baldur's Gate 3 of Pokemon uitvoeren, de gameplay van BG3 ziet er als volgt uit:
![Example gameplay](./Project/Flophouse.png)

Vanuit een keuzemenu heb je verschillende aanvallen per klasse. Ik vind dit keuzemenu verwarrend, zelf zou ik de keuzemenu één geheel maken zonder onderscheiding tussen bonus-aanvallen en normale aanvallen zoals hier het geval is; de bonus aanval kun je weergeven als nieuwe actie, nadat de gebruiker alle normale aanvallen al heeft uitgevoerd. Of ik een character creation scherm wil maken weet ik nog niet zeker, maar dat lijkt me zeker wel leuk. Wat ik wel zeker wil, is dat de gebruiker de keuze heeft om zijn of haar klasse te kiezen voor hun karakter. Wat ook een interessant idee is een combinatie van 2D & 3D te doen. 2D voor de cutscenes, waarbij een keuze wordt gemaakt & 3D voor de uiteindelijke gameplay. 

---

## 4. Features

### 4.1 De lijst

1. Loginpagina 
2. Character creation scherm
3. Klassenkeuze
4. Cutscenes met keuzemenu
5. Combatsysteem en -gameplay
6. Verhaallijn 
7. Eindes a.h.v. keuzes
8. Een live-omgeving

### 4.2 Onmisbare features

1. Loginpagina: anders kun je je progress in de game kwijtraken
2. Cutscenes met keuzemenu: de keuzes is de hoofdzakelijke gameplay
3. Verhaallijn: zonder een verhaallijn is er simpelweg geen richting in de game (door het keuzesysteem)
4. Eindes a.h.v. keuzes: dat is waar de gebruiker naartoe werkt

### 4.3 Optionele features

1. Character creation scherm: is leuk, maar optioneel en essentieel voor gameplay
2. Klassenkeuze: is een interessante toevoeging aan het combatsysteem in de game, maar het combatsysteem is optioneel en niet noodzakelijk
3. Combatsysteem en -gameplay: maakt de game interactiever, maar is geen vereiste

### 4.4 Prioritizeren

1. Combatsysteem en -gameplay: interactief, en maakt de game leuker
2. Klassenkeuze: leuke toevoeging, niet essentieel
3. Character creation scherm: leuk voor individuele game-ervaring, maar ook niet heel essentieel

---

## 5. Requirements


### 5.1 Gegevensbronnen

#### 5.1.1 In-game assets:
1. Indien 2D: schetsen van karakters, achtergronden, keuzeboxen
2. Indien 3D: 3D modellen, animaties
3. Geluidseffecten

#### 5.1.2 Data:
1. JSON/CSV voor klassen en combatsysteem
2. JSON/Ink/Yarn Spinner voor cuscenes
3. Accounts, en game-saves (op een Cloud-systeem)

### 5.2 Externe componenten

#### 5.2.1 2D:
1. Front-end: HTML (JavaScript), CSS
2. Back-end: Flask (Python), Jinja2 (templates)
3. Data-opslag: Flask, SQLite
4. Cutscenes: InkJS/JSON
5. Audio: Web Audio API
6. Tooling: GitHub

#### 5.2.2 3D:
1. Rendering: Three.js (WebGL)
2. Loaders: GLTFLoader (voor modellen), OrbitControls (camera)
3. Assets: GLFT/GLB modellen (JSON)
4. Back-end: zelfde als 2D

#### 5.2.3 2D en 3D:
1. UI-library: CSS
2. Design: ibisPaint (2D), Blender (3D)

---

## 6. Inhoud van de gameplay

Als laatst heb ik de verhaallijn deels opgezet voor de gameplay. [OC] ben jij, de gebruiker van de game.

>In een koninkrijk vol welvaart heerst een machtige koning, samen met zijn vrouw en dochter. De koning organiseert heimelijk een experiment op mensen die naar zijn bal komen.
Niemand weet hier niets van, tot op een dag waarop de koning weer een bal organiseert, waarbij een adellijke [Own Character (OC)] te gast is. [OC] is bevriend met de dochter van de koning, de prinses, en merkt op dat zij zich teruggetrokken gedraagt op het bal. De prinses kijkt met argwaan naar haar vader en loopt naar de kelder. Al een tijd heeft de prinses in de gaten dat haar moeder, zonder eigen wil, alles doet wat de koning van haar eist. Niet alleen haar moeder vertoont dit soort gedrag, maar ook mensen die een bal van de koning hebben bijgewoond. Soms kwamen die mensen ook nooit meer terug. Zij loopt naar de kamer van haar vader toe en vindt een geheime doorgang naar een kelder. [OC] volgt de prinses, om te achterhalen wat haar dwars zit, en ziet haar voor de opening van de geheime kelder. Op dat moment komt de koning de kamer binnen en vertelt haar niet naar de kelder te lopen. De prinses kijkt vragend [OC] aan: wat kiest [OC] om te zeggen? (1) "Loop niet naar de kamer toe, Prinses!" (2) "Luister niet naar je vader, Prinses."
