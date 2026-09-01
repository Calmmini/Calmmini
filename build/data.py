# -*- coding: utf-8 -*-
"""Central data model for the CALMMINI webshop."""

BRAND = {
    "name": "CALMMINI",
    "tagline": "Hammamrituelen",
    "domain": "https://www.calmmini.nl",
    "email": "info@calmmini.nl",
    "city": "Amersfoort",
    "slogan": "Rust voor mij. Gewoon thuis.",
    "disclaimer": "Test het product altijd eerst op een klein stukje huid en "
                  "stop met gebruiken bij irritatie of gevoeligheid.",
}

CATEGORIES = [
    {
        "slug": "sabon-beldi",
        "name": "Sabon Beldi",
        "menu": "Sabon Beldi",
        "tagline": "Marokkaanse zwarte zeep",
        "intro": "Traditionele Marokkaanse zwarte zeep (sabon beldi) als start van het "
                 "hammamritueel. Op warme, vochtige huid gebruiken en daarna eventueel "
                 "scrubben met een kessa.",
        "tip": "Gebruik sabon beldi niet als gewone schuimende douchegel. Het is juist "
               "bedoeld als zachte voorbereiding op scrubben: warmte, inwerken, afspoelen "
               "en daarna pas exfolieren.",
        "body": [
            'Sabon beldi, ook wel savon noir of Marokkaanse zwarte zeep genoemd, is de klassieke eerste stap van het hammamritueel. Deze zachte zeep op olijfoliebasis wordt op een warme, vochtige huid aangebracht en bereidt de huid voor op de gommage met een kessa. Bij CALMMINI kies je uit naturel, nila, eucalyptus, musk en aker fassi.',
            'Onze sabon beldi is kant-en-klaar: je hoeft niets aan te maken. Breng een dunne laag aan, laat kort intrekken, spoel af en scrub daarna zacht met een kessa-handschoen. Zo haal je het meeste uit je Marokkaanse zwarte zeep, thuis in je eigen badkamer. Besteld en bezorgd in heel Nederland.',
        ],
        "faq": [
            ('Wat is sabon beldi?', 'Sabon beldi is Marokkaanse zwarte zeep (savon noir) op olijfoliebasis. Het is de traditionele eerste reinigingsstap van het hammamritueel, vlak voor het scrubben.'),
            ('Hoe gebruik je Marokkaanse zwarte zeep?', 'Breng de zeep aan op warme, vochtige huid, laat 2-5 minuten intrekken, spoel af en scrub daarna zacht met een kessa-handschoen.'),
            ('Welke variant kan ik het beste kiezen?', 'Naturel is de veelzijdige klassieker. Nila, eucalyptus, musk en aker fassi voegen elk een eigen geur- en verzorgingsaccent toe. Twijfel je? Neem gerust contact op.'),
        ],
        "seo_title": "Sabon Beldi kopen - Marokkaanse zwarte zeep | CALMMINI",
        "seo_desc": "Sabon beldi: Marokkaanse zwarte zeep op olijfoliebasis, kant-en-klaar. "
                    "Naturel, nila, eucalyptus, musk en aker fassi. De start van het hammamritueel.",
    },
    {
        "slug": "ghassoul-klei",
        "name": "Ghassoul & Klei",
        "menu": "Ghassoul & Klei",
        "tagline": "Kant-en-klare klei en ghassoul",
        "intro": "Kant-en-klare klei en ghassoul: geen poeder aanmaken, direct te gebruiken. "
                 "Voor huid en haar.",
        "tip": "Niet volledig laten uitdrogen op de huid; zorgvuldig uitspoelen.",
        "body": [
            'Ghassoul is een minerale klei uit het Marokkaanse Atlasgebergte die van oudsher in de hammam wordt gebruikt voor zowel huid als haar. Bij CALMMINI is de ghassoul en klei kant-en-klaar: geen poeder aanmaken, maar direct als masker te gebruiken. Kies uit groene klei, rode klei en ghassoul met roos of oranjebloesem.',
            'Breng de klei aan als masker op huid of haar, laat kort inwerken en spoel goed uit voordat het volledig opdroogt. Ghassoul en klei passen perfect binnen een natuurlijk, Marokkaans geinspireerd verzorgingsritueel voor thuis. Besteld en bezorgd in heel Nederland.',
        ],
        "faq": [
            ('Wat is ghassoul?', 'Ghassoul is een natuurlijke minerale klei uit Marokko voor huid en haar. Bij CALMMINI is hij kant-en-klaar, dus direct te gebruiken zonder poeder aan te maken.'),
            ('Ghassoul of klei - wat is het verschil?', 'Ghassoul (met roos of oranjebloesem) is een romige reinigingsklei voor huid en haar. Groene en rode klei zijn maskers gericht op reiniging en een frisse huid.'),
            ('Mag de klei opdrogen op de huid?', 'Laat de klei niet volledig uitdrogen. Kort laten inwerken en daarna goed uitspoelen geeft het fijnste resultaat.'),
        ],
        "seo_title": "Ghassoul & klei kopen - kant-en-klaar | CALMMINI",
        "seo_desc": "Kant-en-klare Marokkaanse ghassoul en klei voor huid en haar: groene klei, "
                    "rode klei, ghassoul met roos en oranjebloesem. Direct te gebruiken.",
    },
    {
        "slug": "hammampoeder",
        "name": "Hammampoeder",
        "menu": "Hammampoeder",
        "tagline": "Traditionele kruidenblends",
        "intro": "Traditionele hammamkruiden in poedervorm voor lichaam en haar. Aan te maken "
                 "met water tot een papje en onderdeel van een authentieke hammambeleving.",
        "tip": None,
        "body": [
            'Hammampoeder bestaat uit traditionele kruidenblends voor lichaam en haar die je met water aanmaakt tot een papje. Het is een authentiek onderdeel van de Marokkaanse hammambeleving. CALMMINI biedt een blend voor het lichaam en een blend voor hoofdhuid en haar.',
            'Maak het poeder aan met water, breng het aan op vochtige huid of nat haar, laat kort inwerken en spoel goed uit. Zo bouw je stap voor stap een natuurlijk hammamritueel op in je eigen badkamer. Besteld en bezorgd in heel Nederland.',
        ],
        "faq": [
            ('Hoe maak je hammampoeder aan?', 'Meng het poeder met water tot een papje, breng het aan op vochtige huid of nat haar, laat kort inwerken en spoel goed uit.'),
            ('Wat is het verschil tussen de lichaam- en haarblend?', 'De lichaamsblend bevat onder meer lavendel, eucalyptus en munt; de haarblend bevat kruiden als hennablad, amla en shikakai voor hoofdhuid en haar.'),
        ],
        "seo_title": "Hammampoeder kopen - hammamkruiden voor lichaam en haar | CALMMINI",
        "seo_desc": "Hammampoeder: traditionele hammamkruiden voor lichaam en haar, aan te maken "
                    "met water tot een papje. Voor een authentiek Marokkaans hammamritueel.",
    },
    {
        "slug": "verzorgingsolien",
        "name": "Verzorgingsolien",
        "menu": "Verzorgingsolien",
        "tagline": "Plantaardige olien, 100 ml",
        "intro": "Plantaardige olien voor huid, haarpunten, massage en droge zones. "
                 "Gebruik weinig: enkele druppels zijn meestal genoeg.",
        "tip": "Bewaar olien goed afgesloten, koel en uit direct zonlicht. Zo blijven geur, "
               "textuur en kwaliteit langer mooi.",
        "body": [
            'Onze verzorgingsolien zijn lichte, plantaardige olien (100 ml) voor huid, haarpunten, massage en droge zones. Ze sluiten het hammamritueel af en verzorgen de huid zonder zwaar gevoel. Kies uit saffloer-, amandel-, abrikozenpit- en aloe vera olie.',
            'Gebruik weinig: enkele druppels op een licht vochtige huid of droge plekken zijn meestal genoeg. Bewaar de olien koel, droog en uit direct zonlicht. Natuurlijke Marokkaans geinspireerde verzorging, bezorgd in heel Nederland.',
        ],
        "faq": [
            ('Waarvoor gebruik je verzorgingsolie?', 'Voor huid, haarpunten, massage en droge zones - meestal als afsluitende, verzorgende stap van het ritueel.'),
            ('Hoeveel olie heb ik nodig?', 'Weinig: enkele druppels volstaan. Breng aan op een licht vochtige huid en masseer rustig in.'),
            ('Welke olie past bij mij?', 'Saffloer en abrikozenpit zijn licht en fijn voor het gezicht; amandel is een veelzijdige allrounder; aloe vera is verzachtend voor droge of gevoelige zones.'),
        ],
        "seo_title": "Verzorgingsolien kopen - plantaardige olien 100 ml | CALMMINI",
        "seo_desc": "Plantaardige verzorgingsolien (100 ml) voor huid, haarpunten en droge zones: "
                    "saffloer-, amandel-, abrikozenpit- en aloe vera olie.",
    },
    {
        "slug": "butter-scrub",
        "name": "Butter & Scrub",
        "menu": "Butter & Scrub",
        "tagline": "Rijke verzorging en exfoliatie",
        "intro": "Rijke verzorging en zachte exfoliatie: shea butter voor droge zones en een "
                 "Mediterraanse scrub voor een gladde, verzorgde huid.",
        "tip": None,
        "body": [
            'In deze categorie combineer je rijke verzorging met zachte exfoliatie: shea butter voor intensieve verzorging van droge zones en een Mediterraanse scrub met citroenmelisse voor een gladde, verzorgde huid. Samen zorgen ze voor een zacht en verzorgd huidgevoel na het hammamritueel.',
            'Gebruik de scrub op vochtige huid en masseer zacht in; breng daarna de shea butter aan op droge plekjes, lippen of haarpunten. Natuurlijke Marokkaans geinspireerde verzorging, bezorgd in heel Nederland.',
        ],
        "faq": [
            ('Wanneer gebruik ik de scrub en wanneer de butter?', 'Scrub eerst op vochtige huid voor een gladde huid; breng daarna shea butter aan op droge zones voor intensieve verzorging.'),
            ('Waarvoor is shea butter geschikt?', 'Voor droge plekjes, lippen, ruwe zones en haarpunten - overal waar de huid extra verzorging kan gebruiken.'),
        ],
        "seo_title": "Shea butter & scrub kopen - verzorging en exfoliatie | CALMMINI",
        "seo_desc": "Shea butter voor intensieve verzorging van droge huid en een Mediterraanse "
                    "scrub met citroenmelisse voor een zachte, gladde huid.",
    },
    {
        "slug": "accessoires",
        "name": "Accessoires",
        "menu": "Accessoires",
        "tagline": "Benodigdheden voor het ritueel",
        "intro": "Handige benodigdheden voor het hammamritueel: een kessa-scrubhandschoen, "
                 "puimsteen en een mengkom voor het aanmaken van sabon, ghassoul en scrub.",
        "tip": None,
        "body": [
            'De juiste accessoires maken je hammamritueel thuis compleet. Bij CALMMINI vind je een kessa-scrubhandschoen voor de gommage, een puimsteen voor ruwe hielen en een mengkom-set om sabon, ghassoul en scrub eenvoudig aan te maken en aan te brengen.',
            'Combineer de accessoires met sabon beldi, ghassoul en scrub voor een volledig Marokkaans verzorgingsritueel. Besteld en bezorgd in heel Nederland.',
        ],
        "faq": [
            ('Wat doet een kessa-handschoen?', 'Met een kessa scrub je na het inwerken van sabon beldi dode huidcellen weg - de kenmerkende gommage-stap van de hammam.'),
            ('Waar gebruik ik de mengkom voor?', 'Voor het aanmaken en aanbrengen van sabon beldi, ghassoul en scrub, zonder geknoei op je handen.'),
        ],
        "seo_title": "Kessa, puimsteen & mengkom - hammam-accessoires | CALMMINI",
        "seo_desc": "Hammam-accessoires: kessa-scrubhandschoen, puimsteen en mengkom. "
                    "De benodigdheden om je hammamritueel thuis compleet te maken.",
    },
]

def P(slug, name, cat, price, blurb, ingredienten, gebruik, voordeel,
      inhoud=None, badge=None, extra_cats=None):
    return {
        "slug": slug, "name": name, "cat": cat, "price": price, "blurb": blurb,
        "ingredienten": ingredienten, "gebruik": gebruik, "voordeel": voordeel,
        "inhoud": inhoud, "badge": badge, "extra_cats": extra_cats or [],
    }

PRODUCTS = [
    # 1. Sabon Beldi
    P("sabon-beldi-naturel", "Sabon Beldi Naturel", "sabon-beldi", 8.95,
      "Traditionele zwarte zeep op basis van olijfolie en olijvenpasta, perfect als eerste stap voor het scrubben.",
      "Olijfoliebasis met olijvenpasta en plantaardige zeep.",
      "Aanbrengen op warme, vochtige huid. 2-5 minuten laten inwerken, afspoelen en daarna "
      "zacht scrubben met een kessa.",
      "Diepe reiniging, zachte huid en het voorbereiden van de huid op exfoliatie.",
      badge="Bestseller"),
    P("sabon-beldi-nila", "Sabon Beldi Nila", "sabon-beldi", 9.95,
      "Zwarte zeep met blauwe Nila-poeder voor een zachte reiniging en een stralend fris huidgevoel.",
      "Olijfoliebasis met blauwe nila-poeder.",
      "Dun aanbrengen, kort laten inwerken en zorgvuldig afspoelen.",
      "Een frisse, verzorgde uitstraling en een zachte huid na het ritueel."),
    P("sabon-beldi-eucalyptus", "Sabon Beldi Eucalyptus", "sabon-beldi", 9.95,
      "Zwarte zeep met eucalyptusolie voor een fris, schoon en verkwikkend gevoel onder de douche.",
      "Olijfoliebasis met eucalyptusolie.",
      "Aanbrengen onder de douche of tijdens een warm hammammoment; kort laten inwerken en afspoelen.",
      "Een fris, schoon en reinigend gevoel."),
    P("sabon-beldi-musk", "Sabon Beldi Musk", "sabon-beldi", 9.95,
      "Zwarte zeep met een zachte muskgeur voor een warme, verzorgende en heerlijk geurende hammamervaring.",
      "Olijfoliebasis met warme muskgeur.",
      "Aanbrengen op vochtige huid, kort laten inwerken en goed afspoelen.",
      "Reiniging met een warme geurbeleving."),
    P("sabon-beldi-aker-fassi", "Sabon Beldi Aker Fassi", "sabon-beldi", 9.95,
      "Zwarte zeep met Aker Fassi-poeder voor een warme, verzorgende hammambeleving.",
      "Olijfoliebasis met Aker Fassi-poeder.",
      "Dun aanbrengen, kort laten inwerken en goed afspoelen. Daarna eventueel een kessa gebruiken.",
      "Traditionele verzorging met een zachte glow."),

    # 2. Ghassoul & Klei
    P("groene-klei", "Groene Klei", "ghassoul-klei", 9.95,
      "Een kleimengsel met groene klei, kaolien en montmorilloniet voor een zuiverend verzorgingsmoment.",
      "Groene klei, kaolien en montmorilloniet.",
      "Als masker aanbrengen op de huid. Kort laten inwerken en goed afspoelen voordat het "
      "volledig uitdroogt.",
      "Fijn voor een huid die snel glimt, bij onzuiverheden en voor een fris, schoon gevoel.",
      badge="Bestseller"),
    P("rode-klei", "Rode Klei", "ghassoul-klei", 9.95,
      "Een verzorgende klei voor huid en lichaam, ideaal voor een diepere reiniging en een frisse uitstraling.",
      "Kant-en-klare natuurlijke rode klei.",
      "Dun aanbrengen op de huid, kort laten inwerken en zorgvuldig afspoelen.",
      "Mooi voor een doffe huid en een frisse, verzorgde glow."),
    P("ghassoul-roos", "Ghassoul Rose", "ghassoul-klei", 10.95,
      "Een romige ghassoulpasta met rozengeur die de huid mild reinigt en een zacht verzorgd gevoel geeft.",
      "Kant-en-klare Marokkaanse reinigingsklei (ghassoul) met roos.",
      "Aanbrengen op huid of haar. Kort laten inwerken en goed uitspoelen.",
      "Zachte reiniging en verzorging van huid en haar.",
      badge="Bestseller"),
    P("ghassoul-oranjebloesem", "Ghassoul Orange Blossom", "ghassoul-klei", 10.95,
      "Een zachte ghassoulpasta met oranjebloesemgeur voor een frisse, verzorgde en soepel aanvoelende huid.",
      "Kant-en-klare Marokkaanse reinigingsklei (ghassoul) met oranjebloesem.",
      "Aanbrengen als masker op huid of haar. Niet te lang laten opdrogen en goed uitspoelen.",
      "Zachte reiniging met een frisse geurbeleving."),

    # 3. Hammampoeder
    P("hammamkruiden-lichaam", "Hammamkruiden Lichaam", "hammampoeder", 12.95,
      "Traditionele kruidenblend voor het lichaam, aan te maken met water.",
      "Lavendel, eucalyptus, munt, kamille, rozenblaadjes en natuurlijke mineralen.",
      "Poeder aanmaken met water tot een papje. Aanbrengen op vochtige huid, kort laten "
      "inwerken en zorgvuldig afspoelen (lichtelijk scrubben).",
      "Een verzorgende, traditionele hammambeleving.",
      badge="Bestseller"),
    P("hammamkruiden-haar", "Hammamkruiden Haar", "hammampoeder", 12.95,
      "Traditionele kruidenblend voor hoofdhuid en haar, aan te maken met water.",
      "Hennablad, amla, shikakai, kamille en fenegriek.",
      "Poeder aanmaken met water tot een papje. Aanbrengen op nat haar of hoofdhuid, (kort) "
      "laten inwerken en goed uitspoelen.",
      "Verzorging van hoofdhuid en haar en een fris, verzorgd gevoel."),

    # 4. Verzorgingsolien
    P("saffloerolie", "Saffloerolie", "verzorgingsolien", 12.95,
      "Lichte plantaardige verzorgingsolie zonder zwaar gevoel.",
      "Lichte plantaardige verzorgingsolie.",
      "Enkele druppels aanbrengen op licht vochtige huid of droge zones en zacht inmasseren.",
      "Lichte verzorging zonder zwaar gevoel.",
      inhoud="100 ml"),
    P("amandelolie", "Amandelolie", "verzorgingsolien", 12.95,
      "Zachte allround plantaardige olie voor huid en haarpunten.",
      "Zachte allround plantaardige olie.",
      "2-3 druppels op schone huid of een kleine hoeveelheid voor massage. Ook geschikt voor haarpunten.",
      "Hydratatie, zachtheid en verzorging van droge huid.",
      inhoud="100 ml"),
    P("abrikozenpitolie", "Abrikozenpitolie", "verzorgingsolien", 12.95,
      "Zachte, lichte plantaardige olie, ook fijn voor gezicht en hals.",
      "Zachte, lichte plantaardige olie. Kan sporen van noten bevatten.",
      "Een paar druppels aanbrengen op gezicht, hals of droge plekken. Zacht inmasseren.",
      "Zachte verzorging, ook fijn voor gezicht en hals.",
      inhoud="100 ml"),
    P("aloe-vera-olie", "Aloe Vera Olie", "verzorgingsolien", 12.95,
      "Verzorgende olie voor droge of gevoelige zones.",
      "Verzorgende olie / olie-extract.",
      "Dun aanbrengen op droge of gevoelige zones en rustig inmasseren.",
      "Verzachting en verzorging van de huid.",
      inhoud="100 ml"),

    # 5. Butter & Scrub
    P("shea-butter", "Shea Butter", "butter-scrub", 11.95,
      "Rijke sheaboter voor intensieve verzorging van droge huid.",
      "Sheaboter (Butyrospermum Parkii Butter).",
      "Een kleine hoeveelheid tussen de handen verwarmen en aanbrengen op droge plekjes, "
      "lippen, ruwe zones of haarpunten.",
      "Intensieve verzorging, verzachting en bescherming van droge huid.",
      badge="Bestseller"),
    P("mediterraanse-scrub", "Mediterraanse Scrub", "butter-scrub", 11.95,
      "Scrub met verzorgende oliebasis en citroenmelisse voor een gladde huid.",
      "Scrubdeeltjes met verzorgende oliebasis en citroenmelisse.",
      "Aanbrengen op vochtige huid en zacht inmasseren. Daarna goed afspoelen.",
      "Een zachte, gladde huid en het verwijderen van dode huidcellen."),

    # 6. Accessoires
    P("kessa", "Kessa Scrubhandschoen", "accessoires", 5.95,
      "Traditionele scrubhandschoen voor de gommage na sabon beldi.",
      "Scrubhandschoen.",
      "Na sabon beldi gebruiken op warme, afgespoelde huid. Met rustige, ronddraaiende "
      "bewegingen scrubben.",
      "Verwijderen van dode huidcellen na sabon beldi."),
    P("puimsteen", "Puimsteen", "accessoires", 4.95,
      "Natuurlijke puimsteen voor de verzorging van ruwe hielen en eelt.",
      "Natuurlijke voetverzorging.",
      "Alleen op natte, weekgemaakte hielen gebruiken. Zacht bewegen, niet hard drukken.",
      "Verzorging van ruwe hielen en eelt."),
    P("mengkom", "Mengkom Set", "accessoires", 4.95,
      "Silicone schaaltje met spatel en kwast voor het aanmaken van sabon, ghassoul en scrub.",
      "Silicone schaaltje, spatel en kwast.",
      "Gebruiken bij het aanmaken en aanbrengen van sabon, ghassoul en scrub.",
      "Voorkomt geknoei op de handen en zorgt dat ingredienten egaal aangebracht worden.",
      badge="Set"),
]

BLOG = [
    {
        "slug": "hammamritueel-thuis",
        "title": "Het Marokkaanse hammamritueel thuis: een complete gids",
        "excerpt": "Ontdek hoe je de rust en verzorging van de Marokkaanse hammam naar je eigen "
                   "badkamer haalt - stap voor stap.",
        "seo_title": "Hammamritueel thuis doen - complete gids | CALMMINI",
        "seo_desc": "Zo doe je een Marokkaans hammamritueel thuis: van sabon beldi en gommage tot "
                    "ghassoul, kruiden en olien. De complete stap-voor-stap gids van CALMMINI.",
        "date": "2025-11-04",
        "read": 7,
        "cat_link": "sabon-beldi",
        "product_links": ["sabon-beldi-naturel", "mediterraanse-scrub", "hammamkruiden-lichaam"],
        "body": [
            ("h2", "Wat is een hammam?"),
            ("p", "De hammam is van oudsher een centraal onderdeel van de Marokkaanse verzorgingscultuur. "
                  "Het is een plek van reiniging, rust en ontmoeting. Het bijbehorende ritueel kent een "
                  "vaste opbouw en wordt van generatie op generatie doorgegeven."),
            ("p", "Je hoeft niet naar Marokko af te reizen om deze traditie te ervaren. Met de juiste "
                  "producten breng je de sfeer en de opbouw van het hammamritueel eenvoudig naar je eigen badkamer."),
            ("h2", "De stappen van het ritueel"),
            ("h3", "1. Opwarmen"),
            ("p", "Het ritueel begint met warmte en stoom, zodat het lichaam tot rust komt en de huid zich voorbereidt."),
            ("h3", "2. Sabon beldi"),
            ("p", "Traditioneel wordt sabon beldi - Marokkaanse zwarte zeep - als eerste stap op warme, vochtige "
                  "huid aangebracht en even laten intrekken. Daarna zorgvuldig afspoelen."),
            ("h3", "3. Gommage (scrub)"),
            ("p", "Met een kessa-handschoen volgt de gommage, de scrubstap die het ritueel zo kenmerkend maakt."),
            ("h3", "4. Ghassoul en kruiden"),
            ("p", "Kant-en-klare ghassoul, klei en hammamkruiden vormen de verzorgende stappen voor haar en lichaam."),
            ("h3", "5. Olien"),
            ("p", "Tot slot worden natuurlijke olien gebruikt om het ritueel af te sluiten."),
            ("h2", "Alles voor jouw ritueel"),
            ("p", "Bij CALMMINI vind je de producten die bij elke stap van het hammamritueel horen - van sabon "
                  "beldi en scrub tot kruiden en olien."),
        ],
    },
    {
        "slug": "wat-is-ghassoul",
        "title": "Wat is ghassoul en hoe gebruik je het?",
        "excerpt": "Ghassoul is een van de bekendste producten uit de Marokkaanse hammam. We leggen uit "
                   "wat het is en hoe het in het ritueel past.",
        "seo_title": "Wat is ghassoul? Uitleg en gebruik | CALMMINI",
        "seo_desc": "Wat is ghassoul en hoe gebruik je deze Marokkaanse klei voor huid en haar? "
                    "Lees de uitleg van CALMMINI en ontdek onze kant-en-klare ghassoul en klei.",
        "date": "2025-11-11",
        "read": 5,
        "cat_link": "ghassoul-klei",
        "product_links": ["ghassoul-roos", "ghassoul-oranjebloesem", "groene-klei"],
        "body": [
            ("h2", "Ghassoul: klei uit het Atlasgebergte"),
            ("p", "Ghassoul is een minerale kleisoort die traditioneel wordt gewonnen in het Atlasgebergte in "
                  "Marokko. De klei wordt van oudsher gebruikt in de hammam, voor zowel haar als lichaam."),
            ("h2", "Hoe past ghassoul in het ritueel?"),
            ("p", "Binnen het hammamritueel wordt ghassoul gezien als een van de verzorgende stappen. Het wordt "
                  "als masker aangebracht op huid of haar, kort laten inwerken en daarna goed uitgespoeld. Laat "
                  "de klei niet volledig uitdrogen op de huid."),
            ("h2", "Kant-en-klaar bij CALMMINI"),
            ("p", "De ghassoul en klei van CALMMINI zijn kant-en-klaar: je hoeft geen poeder aan te maken en kunt "
                  "ze direct gebruiken. Ontdek onder meer groene klei, rode klei en ghassoul met roos of oranjebloesem."),
        ],
    },
    {
        "slug": "savon-noir-uitgelegd",
        "title": "Sabon beldi: de Marokkaanse zwarte zeep uitgelegd",
        "excerpt": "Sabon beldi (savon noir) hoort onlosmakelijk bij de hammam. Lees wat deze traditionele "
                   "zwarte zeep is en welke varianten er bestaan.",
        "seo_title": "Sabon beldi / savon noir uitgelegd - zwarte zeep | CALMMINI",
        "seo_desc": "Wat is sabon beldi, oftewel savon noir of Marokkaanse zwarte zeep? Ontdek de traditie, "
                    "de varianten en hoe je het gebruikt in het hammamritueel.",
        "date": "2025-11-18",
        "read": 5,
        "cat_link": "sabon-beldi",
        "product_links": ["sabon-beldi-naturel", "sabon-beldi-nila", "sabon-beldi-eucalyptus"],
        "body": [
            ("h2", "Wat is sabon beldi?"),
            ("p", "Sabon beldi, ook wel savon noir of Marokkaanse zwarte zeep genoemd, is een traditionele zeep "
                  "op olijfoliebasis die centraal staat in het hammamritueel. De zeep wordt als eerste reinigende "
                  "stap op warme, vochtige huid gebruikt."),
            ("h2", "Hoe gebruik je het?"),
            ("p", "Breng de zeep aan op warme, vochtige huid, laat kort intrekken en spoel af. Daarna volgt de "
                  "gommage met een kessa. Sabon beldi is dus geen gewone schuimende douchegel, maar een zachte "
                  "voorbereiding op het scrubben."),
            ("h2", "Varianten"),
            ("p", "Naast de naturel-variant bestaan er varianten zoals nila (met blauwe nila-poeder), eucalyptus, "
                  "musk en aker fassi, elk met een eigen plek binnen de Marokkaanse verzorgingstraditie."),
        ],
    },
    {
        "slug": "natuurlijke-marokkaanse-haarverzorging",
        "title": "Natuurlijke Marokkaanse haarverzorging: waar begin je?",
        "excerpt": "Van hammamkruiden tot olien: een introductie in natuurlijke haarverzorging volgens "
                   "Marokkaanse traditie.",
        "seo_title": "Natuurlijke Marokkaanse haarverzorging - startgids | CALMMINI",
        "seo_desc": "Begin met natuurlijke Marokkaanse haarverzorging. Ontdek hammamkruiden voor het haar, "
                    "ghassoul en verzorgingsolien in de startgids van CALMMINI.",
        "date": "2025-11-25",
        "read": 6,
        "cat_link": "hammampoeder",
        "product_links": ["hammamkruiden-haar", "ghassoul-roos", "amandelolie"],
        "body": [
            ("h2", "Haarverzorging volgens traditie"),
            ("p", "In de Marokkaanse verzorgingscultuur speelt natuurlijke haarverzorging een belangrijke rol. "
                  "Kruiden, klei en olien worden al generaties lang ingezet als onderdeel van het ritueel."),
            ("h2", "Waar begin je?"),
            ("p", "Een goede start is een combinatie van hammamkruiden voor het haar (met onder meer hennablad, "
                  "amla en shikakai), ghassoul en een lichte plantaardige olie voor de haarpunten. Zo bouw je "
                  "stap voor stap een eigen ritueel op."),
            ("h2", "Ontdek de producten"),
            ("p", "Bekijk de categorieen hammampoeder, ghassoul & klei en verzorgingsolien voor alle natuurlijke "
                  "producten van CALMMINI."),
        ],
    },
]

# Real terms & conditions (from client's Algemene Voorwaarden PDF)
TERMS = [
    ("Definities",
     "In deze voorwaarden wordt verstaan onder: Klant: de natuurlijke persoon of rechtspersoon die een "
     "overeenkomst aangaat met CalmMini. Consument: een natuurlijke persoon die handelt buiten zijn bedrijfs- "
     "of beroepsactiviteit. Overeenkomst: iedere afspraak tussen CalmMini en de klant betreffende producten. "
     "Product(en): de wellnessproducten die CalmMini aanbiedt."),
    ("Offertes",
     "Alle aanbiedingen van CalmMini zijn vrijblijvend, tenzij anders aangegeven. Een offerte is geldig voor "
     "30 dagen. CalmMini kan een offerte intrekken of wijzigen tot het moment van bevestiging."),
    ("Totstandkoming van de overeenkomst",
     "De overeenkomst komt tot stand zodra de klant een bestelling bevestigt via de webshop en CalmMini deze "
     "bevestigt per e-mail. CalmMini behoudt zich het recht voor bestellingen te weigeren bij voorraadgebrek "
     "of onjuiste gegevens."),
    ("Transport, levering en invoerrechten",
     "CalmMini draagt zorg voor deugdelijke verpakking. Het risico van beschadiging gaat over bij aflevering "
     "aan de klant. Binnen Nederland gelden vaste verzendkosten. Buiten de EU zijn invoerrechten voor rekening "
     "van de klant."),
    ("Levertijd en overmacht",
     "CalmMini streeft ernaar te leveren binnen 5-10 werkdagen na bevestiging. In geval van overmacht (zoals "
     "natuurrampen of logistieke problemen) mag CalmMini de levering uitstellen. Duurt dit langer dan 30 dagen, "
     "dan mag de klant kosteloos ontbinden."),
    ("Betaling",
     "Betaling dient te geschieden binnen 14 dagen na factuurdatum. Bij overschrijding is 2% rente per maand "
     "verschuldigd plus wettelijke incassokosten."),
    ("Eigendomsvoorbehoud",
     "Producten blijven eigendom van CalmMini tot volledige betaling, inclusief bijkomende kosten. De klant mag "
     "de producten niet verpanden of doorverkopen zolang deze eigendom blijven van CalmMini."),
    ("Garantie",
     "CalmMini garandeert dat producten bij levering voldoen aan de overeenkomst. Garantie geldt 2 jaar voor "
     "consumenten. Niet geldig bij verkeerd gebruik of schade door derden. CalmMini kan kiezen voor herstel, "
     "vervanging of terugbetaling."),
    ("Aansprakelijkheid",
     "CalmMini is slechts aansprakelijk voor directe schade door opzet of grove nalatigheid. De aansprakelijkheid "
     "is beperkt tot het aankoopbedrag of \u20ac500 per gebeurtenis (welk bedrag lager is). Indirecte schade zoals "
     "winstverlies of gevolgschade is uitgesloten."),
    ("Geschillen",
     "Op overeenkomsten is Nederlands recht van toepassing. Partijen trachten geschillen eerst minnelijk op te "
     "lossen. Indien dit niet lukt, is de rechter in Amersfoort bevoegd."),
    ("Overige bepalingen",
     "Indien een bepaling ongeldig is, blijven de overige van kracht. CalmMini mag voorwaarden wijzigen; bij "
     "bestaande bestellingen gelden de voorwaarden van het moment van aankoop. De klant mag rechten niet zonder "
     "toestemming overdragen."),
]

def eur(v):
    return "\u20ac %s" % ("%.2f" % v).replace(".", ",")

def cat_by_slug(slug):
    return next(c for c in CATEGORIES if c["slug"] == slug)

def products_in_cat(slug):
    return [p for p in PRODUCTS if p["cat"] == slug or slug in p["extra_cats"]]
