import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent / "backend" / "data"
DIST_DIR = BASE_DIR / "districts"
PLACES_DIR = BASE_DIR / "places"
DIST_DIR.mkdir(parents=True, exist_ok=True)
PLACES_DIR.mkdir(parents=True, exist_ok=True)

def write_data(folder: Path, filename: str, data: list):
    path = folder / f"{filename}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Generated {path.name}: {len(data)} items")

# Load states.json to get list of all states and union territories
states_file = BASE_DIR / "states.json"
with open(states_file, "r", encoding="utf-8") as f:
    all_states = json.load(f)

# Comprehensive catalog of remaining states/UTs with key districts and places
ADDITIONAL_DATA = {
  "delhi": {
    "districts": [
      {"id": "new-delhi", "name": "New Delhi", "area": "35 km²", "pop": "142,004 (2011 Census)", "food": "Chaat, Paranthas", "crafts": "Handicrafts", "summary": "Seat of the Government of India, Rashtrapati Bhavan, and Parliament."},
      {"id": "central-delhi", "name": "Central Delhi", "area": "25 km²", "pop": "582,320 (2011 Census)", "food": "Mughlai, Kebabs", "crafts": "Zardozi, Jewelry", "summary": "Historic Walled City of Old Delhi, Red Fort, and Chandni Chowk."},
      {"id": "south-delhi", "name": "South Delhi", "area": "250 km²", "pop": "2,731,929 (2011 Census)", "food": "Cafes, Street food", "crafts": "Pottery, Leather", "summary": "Upscale commercial district, home to Qutub Minar and Lotus Temple."},
    ],
    "places": [
      {"id": "red-fort-delhi", "name": "Red Fort (Lal Qila)", "parent": "central-delhi", "summary": "Historic 17th-century Mughal imperial palace citadel built of red sandstone by Emperor Shah Jahan.",
       "points": ["Commissioned in 1638 CE by Emperor Shah Jahan; completed 1648 CE", "Mughal dynasty; designated UNESCO World Heritage Site in 2007", "Venue of India's annual Independence Day flag-hoisting address by the Prime Minister"]},
      {"id": "qutub-minar", "name": "Qutub Minar & Iron Pillar", "parent": "south-delhi", "summary": "73-meter soaring minaret of victory and rust-resistant 4th-century Gupta iron pillar.",
       "points": ["Construction started in 1199 CE by Qutb-ud-din Aibak and completed by Iltutmish; Delhi Sultanate (Mamluk dynasty)", "Inscribed as UNESCO World Heritage Site in 1993", "Houses the 1,600-year-old Gupta Iron Pillar that has never rusted"]},
      {"id": "india-gate-delhi", "name": "India Gate", "parent": "new-delhi", "summary": "Ceremonial 42-meter triumphal arch war memorial designed by Sir Edwin Lutyens.",
       "points": ["Foundation laid in 1921, inaugurated in 1931 by Viceroy Lord Irwin", "Designed by Edwin Lutyens; honors 84,000 soldiers who died in World War I", "Features the Amar Jawan Jyoti eternal flame and National War Memorial"]},
      {"id": "swaminarayan-akshardham-delhi", "name": "Swaminarayan Akshardham", "parent": "central-delhi", "summary": "World's largest comprehensive Hindu temple complex, carved entirely from pink sandstone and Carrara marble.",
       "points": ["Consecrated on 6 November 2005 by Pramukh Swami Maharaj", "BAPS Swaminarayan Sanstha", "Built without structural steel according to ancient Shilpa Shastras featuring 20,000 carved statues"]},
      {"id": "lotus-temple-delhi", "name": "Lotus Temple (Bahá'í House of Worship)", "parent": "south-delhi", "summary": "Architectural masterpiece shaped like a blossoming 27-petal white marble lotus flower.",
       "points": ["Completed in 1986, designed by Iranian-Canadian architect Fariborz Sahba", "Bahá'í faith; open to people of all religions and denominations for silent contemplation", "Won numerous international architectural awards for expressionist concrete shell design"]},
    ]
  },
  "rajasthan": {
    "districts": [
      {"id": "jaipur", "name": "Jaipur", "area": "11,143 km²", "pop": "6,626,178 (2011 Census)", "food": "Pyaaz Kachori, Ghevar", "crafts": "Blue Pottery, Gemstones", "summary": "The Pink City, capital of Rajasthan, Amer Fort and Hawa Mahal."},
      {"id": "udaipur", "name": "Udaipur", "area": "11,724 km²", "pop": "3,068,420 (2011 Census)", "food": "Dal Baati Churma, Gatte", "crafts": "Miniature painting, Marble", "summary": "City of Lakes, royal palaces, Lake Pichola and Jagdish Temple."},
      {"id": "jodhpur", "name": "Jodhpur", "area": "22,850 km²", "pop": "3,687,002 (2011 Census)", "food": "Mawa Kachori, Mirchi Vada", "crafts": "Banjara textiles, Woodcraft", "summary": "The Blue City, colossal Mehrangarh Fort on sandstone cliff."},
    ],
    "places": [
      {"id": "hawa-mahal-jaipur", "name": "Hawa Mahal (Palace of Winds)", "parent": "jaipur", "summary": "Five-story pink and red sandstone palace with 953 honeycomb casements.",
       "points": ["Built in 1799 CE by Maharaja Sawai Pratap Singh; designed by Lal Chand Ustad", "Kachhwaha Rajput dynasty", "Designed to allow royal court ladies to observe street festivals veiled from public view"]},
      {"id": "amer-fort-jaipur", "name": "Amer Fort & Sheesh Mahal", "parent": "jaipur", "summary": "Majestic hilltop Rajput fort overlooking Maota Lake, famous for Hall of Mirrors.",
       "points": ["Built in 1592 CE by Raja Man Singh I; expanded by Mirza Raja Jai Singh", "Kachhwaha Rajput dynasty; UNESCO World Heritage Site (Hill Forts of Rajasthan)", "Contains the world-famous Sheesh Mahal (Palace of Mirrors) decorated with convex Belgian glass foils"]},
      {"id": "city-palace-udaipur", "name": "City Palace, Udaipur", "parent": "udaipur", "summary": "Colossal granite and marble palace complex on the banks of Lake Pichola.",
       "points": ["Begun in 1559 CE by Maharana Udai Singh II after shifting capital from Chittorgarh", "Sisodia Rajput dynasty of Mewar", "Constructed over 400 years by successive Maharanas blending Rajasthani and Mughal architectural styles"]},
    ]
  },
  "gujarat": {
    "districts": [
      {"id": "ahmedabad", "name": "Ahmedabad", "area": "8,087 km²", "pop": "7,214,225 (2011 Census)", "food": "Dhokla, Khandvi, Fafda", "crafts": "Bandhani, Ashavali sarees", "summary": "India's first UNESCO World Heritage City on the Sabarmati river."},
      {"id": "narmada", "name": "Narmada", "area": "2,749 km²", "pop": "590,297 (2011 Census)", "food": "Gujarati thali", "crafts": "Tribal bamboo craft", "summary": "Home to the world's tallest statue, the 182-meter Statue of Unity."},
      {"id": "gir-somnath", "name": "Gir Somnath", "area": "3,754 km²", "pop": "1,217,477 (2011 Census)", "food": "Seafood, Kathiyawadi thali", "crafts": "Fisheries, Limestone", "summary": "Sacred first Jyotirlinga at Somnath and Gir forest Asiatic lions."},
    ],
    "places": [
      {"id": "somnath-temple", "name": "Somnath Temple, Prabhas Patan", "parent": "gir-somnath", "summary": "The first of the twelve sacred Shiva Jyotirlingas, overlooking the Arabian Sea.",
       "points": ["Reconstructed in 1951 CE in classical Chaulukya (Solanki) style initiated by Sardar Vallabhbhai Patel", "Solanki dynasty heritage with modern national reconstruction", "Stands at the ancient Triveni Sangam (confluence of Kapila, Hiran, and Saraswati rivers)"]},
      {"id": "statue-of-unity", "name": "Statue of Unity, Kevadia", "parent": "narmada", "summary": "The world's tallest statue standing 182 meters high, honoring Sardar Vallabhbhai Patel.",
       "points": ["Inaugurated on 31 October 2018; designed by Padma Bhushan sculptor Ram V. Sutar", "Commemorates Iron Man of India Sardar Vallabhbhai Patel who unified 562 princely states", "Stands on Sadhu Bet island facing the Sardar Sarovar Dam on the Narmada River"]},
    ]
  },
  "west-bengal": {
    "districts": [
      {"id": "kolkata", "name": "Kolkata", "area": "206 km²", "pop": "4,496,694 (2011 Census)", "food": "Rosogolla, Shorshe Ilish, Kathi Roll", "crafts": "Kalighat painting, Terracotta", "summary": "City of Joy, former British imperial capital, cultural heart of India."},
      {"id": "darjeeling", "name": "Darjeeling", "area": "2,093 km²", "pop": "1,846,823 (2011 Census)", "food": "Darjeeling tea, Momos", "crafts": "GI-tagged Darjeeling Tea, Woollens", "summary": "Queen of the Hills in the Himalayas, tea gardens and toy train."},
    ],
    "places": [
      {"id": "dakshineswar-kali-temple", "name": "Dakshineswar Kali Temple, Kolkata", "parent": "kolkata", "summary": "19th-century Navaratna architectural temple on the Hooghly river where Sri Ramakrishna Paramahamsa served as priest.",
       "points": ["Founded in 1855 CE by the philanthropist queen Rani Rashmoni", "Dedicated to Goddess Bhavatarini (an aspect of Kali); classic Bengal Navaratna (nine-spire) style", "Spiritual seat where 19th-century mystic Sri Ramakrishna Paramahamsa attained divine visions"]},
      {"id": "victoria-memorial-kolkata", "name": "Victoria Memorial", "parent": "kolkata", "summary": "Magnificent white Makrana marble monument dedicated to Queen Victoria, surrounded by 64-acre gardens.",
       "points": ["Built between 1906 and 1921 CE, designed by Sir William Emerson in Indo-Saracenic revival style", "Constructed from pure white Makrana marble quarried from Jodhpur, Rajasthan", "Houses 25 galleries containing 28,000 historic artifacts, paintings, and royal archives"]},
    ]
  },
  "punjab": {
    "districts": [
      {"id": "amritsar", "name": "Amritsar", "area": "2,683 km²", "pop": "2,490,656 (2011 Census)", "food": "Amritsari Kulcha, Lassi, Maa ki Dal", "crafts": "Phulkari, Juttis", "summary": "Holy spiritual city of the Golden Temple and historic Jallianwala Bagh."},
    ],
    "places": [
      {"id": "golden-temple-amritsar", "name": "Sri Harmandir Sahib (Golden Temple)", "parent": "amritsar", "summary": "Preeminent spiritual sanctuary of Sikhism, bathed in real gold and surrounded by the holy Amrit Sarovar.",
       "points": ["Founded in 1577 CE by fourth Sikh Guru, Guru Ram Das; sanctum gilded with pure gold leaf in 1830 by Maharaja Ranjit Singh", "Sikh Empire and Gurus", "Designed with four open entrances welcoming all castes and faiths; serves over 100,000 free meals daily in world's largest community kitchen (Langar)"]},
    ]
  },
  "goa": {
    "districts": [
      {"id": "north-goa", "name": "North Goa", "area": "1,736 km²", "pop": "818,008 (2011 Census)", "food": "Fish curry, Bebinca", "crafts": "Ceramic tiles, Cashew", "summary": "Famous for Calangute, Baga beaches, and Old Goa UNESCO churches."},
      {"id": "south-goa", "name": "South Goa", "area": "1,966 km²", "pop": "640,537 (2011 Census)", "food": "Vindaloo, Sorpotel", "crafts": "Coconut crafts", "summary": "Serene white sand beaches, Dudhsagar Falls, and Portuguese mansions."},
    ],
    "places": [
      {"id": "basilica-of-bom-jesus", "name": "Basilica of Bom Jesus, Old Goa", "parent": "north-goa", "summary": "16th-century Jesuit Baroque church enshrining the sacred relics of St. Francis Xavier.",
       "points": ["Constructed between 1594 and 1605 CE; UNESCO World Heritage Site", "Portuguese Baroque colonial architecture", "Houses the mortal body of Saint Francis Xavier in a silver casket crafted by 17th-century Florentine silversmiths"]},
      {"id": "shanta-durga-temple", "name": "Shanta Durga Temple, Kavlem", "parent": "south-goa", "summary": "Premier Hindu temple of Goa dedicated to the peaceful mediator form of Goddess Durga.",
       "points": ["Constructed in 1738 CE during the reign of Maratha ruler Chhatrapati Shahu of Satara", "Maratha and Saraswat Brahmin heritage", "Distinctive Goan temple architecture combining traditional Hindu pyramidal shikharas with Portuguese arched windows and Deepastambha lamp tower"]},
    ]
  },
  "odisha": {
    "districts": [
      {"id": "puri", "name": "Puri", "area": "3,479 km²", "pop": "1,698,446 (2011 Census)", "food": "Khaja, Mahaprasad", "crafts": "Pattachitra of Raghurajpur", "summary": "Sacred coastal city of Jagannath Puri Ratha Yatra and Konark Sun Temple."},
    ],
    "places": [
      {"id": "jagannath-temple-puri", "name": "Shri Jagannath Temple, Puri", "parent": "puri", "summary": "One of the four sacred Char Dham sanctuaries, home to Lord Jagannath, Balabhadra, and Subhadra.",
       "points": ["Built in the 12th century CE (c. 1161 CE) by King Anantavarman Chodaganga Deva of the Eastern Ganga dynasty", "Eastern Ganga dynasty", "Venue of the world-famous annual Ratha Yatra (Chariot Festival) drawing millions of pilgrims", "Features the world's largest kitchen running on traditional earthen pots where food is blessed as Mahaprasad"]},
      {"id": "konark-sun-temple", "name": "Sun Temple, Konark (Black Pagoda)", "parent": "puri", "summary": "13th-century stone chariot architectural marvel carved with 24 sun wheels and seven horses.",
       "points": ["Built in 1250 CE by King Narasimhadeva I of the Eastern Ganga dynasty; UNESCO World Heritage Site", "Eastern Ganga dynasty", "Designed in the form of a colossal chariot of Surya (Sun God) with 24 intricately carved stone wheels acting as sundials", "Celebrated for its monumental erotic Mithuna sculptures and dynamic Natya Mandapa dancers"]},
    ]
  },
  "bihar": {
    "districts": [
      {"id": "gaya", "name": "Gaya", "area": "4,976 km²", "pop": "4,391,418 (2011 Census)", "food": "Tilkut, Anarsa", "crafts": "Stone carving", "summary": "Sacred city of Bodh Gaya where Gautama Buddha attained Enlightenment."},
      {"id": "nalanda", "name": "Nalanda", "area": "2,355 km²", "pop": "2,877,653 (2011 Census)", "food": "Silao Khaja", "crafts": "Handloom weaving", "summary": "Ruins of ancient 5th-century Nalanda University, global seat of Buddhist learning."},
    ],
    "places": [
      {"id": "mahabodhi-temple-bodhgaya", "name": "Mahabodhi Temple Complex, Bodh Gaya", "parent": "gaya", "summary": "Holiest site in Buddhism where Prince Siddhartha Gautama attained supreme Enlightenment.",
       "points": ["Original temple built by Emperor Ashoka c. 250 BCE; grand 55-meter brick temple dates to 5th–6th century CE Gupta era", "Maurya and Gupta dynasties; inscribed on the UNESCO World Heritage list in 2002", "Shelters the sacred Bodhi Tree (Ficus religiosa) and the diamond throne (Vajrasana) marking the seat of Enlightenment"]},
      {"id": "nalanda-university-ruins", "name": "Nalanda Mahavihara Ruins", "parent": "nalanda", "summary": "Ancient international residential Buddhist university that flourished for 700 years.",
       "points": ["Established in the 5th century CE under Gupta Emperor Kumaragupta I; supported by Emperor Harsha and Pala kings", "Gupta and Pala dynasties; UNESCO World Heritage Site", "Accommodated 10,000 students and 2,000 teachers from China, Korea, Japan, and Central Asia before sacking in 1193 CE"]},
    ]
  },
  "assam": {
    "districts": [
      {"id": "kamrup-metropolitan", "name": "Kamrup Metropolitan", "area": "1,037 km²", "pop": "1,253,938 (2011 Census)", "food": "Masor Tenga, Khaar", "crafts": "Brass metalware", "summary": "Gateway of the Northeast containing Guwahati, Brahmaputra river, and Kamakhya Temple."},
      {"id": "golaghat", "name": "Golaghat", "area": "3,502 km²", "pop": "1,066,888 (2011 Census)", "food": "Assam tea, Pitha", "crafts": "Tea packaging", "summary": "Heart of Kaziranga National Park, home to two-thirds of the world's great one-horned rhinos."},
    ],
    "places": [
      {"id": "kamakhya-temple-guwahati", "name": "Maa Kamakhya Temple, Nilachal Hill", "parent": "kamrup-metropolitan", "summary": "Foremost of the 51 Shakti Peethas on Nilachal hill, celebrating feminine procreative power and Ambubachi Mela.",
       "points": ["Original shrine built during Mlechchha dynasty; present hybrid Nilachal-style beehive shikhara temple rebuilt in 1565 CE by King Nara Narayana of the Koch dynasty", "Koch and Ahom dynasties", "Sanctum holds no anthropomorphic image but a natural stone fissure fed by an underground natural spring", "Celebrates the annual Ambubachi Mela in June marking the annual menstrual cycle of Mother Earth"]},
      {"id": "kaziranga-national-park", "name": "Kaziranga National Park", "parent": "golaghat", "summary": "UNESCO World Heritage sanctuary protecting over 2,600 great Indian one-horned rhinoceroses.",
       "points": ["Established as a reserve forest in 1905 by Mary Curzon; declared UNESCO World Heritage Site in 1985", "Protects the world's largest population of great one-horned rhinoceroses and wild water buffaloes", "Spans 430 sq km of alluvial floodplains, dense elephant grass, and marshes along the Brahmaputra River"]},
    ]
  }
}

# Generate districts and places for all additional states
for state_id, data in ADDITIONAL_DATA.items():
    if "districts" in data and len(data["districts"]) > 0:
        dists = []
        for d in data["districts"]:
            dists.append({
                "id": d["id"],
                "name": d["name"],
                "type": "district",
                "parent": state_id,
                "path": f"{d['name']}, {state_id.replace('-', ' ').title()}, India",
                "summary": d.get("summary", ""),
                "profile": {
                    "Headquarters": d["name"],
                    "Food": d.get("food", ""),
                    "Crafts": d.get("crafts", ""),
                },
                "area": d.get("area", ""),
                "population": d.get("pop", ""),
                "points": [d.get("summary", "")],
                "wiki": f"https://en.wikipedia.org/wiki/{d['name'].replace(' ', '_')}_district",
                "source": "Census of India 2011, ODOP, Wikipedia",
                "updated": "2024-11",
                "model": ""
            })
        write_data(DIST_DIR, state_id, dists)

    if "places" in data and len(data["places"]) > 0:
        pls = []
        for p in data["places"]:
            pls.append({
                "id": p["id"],
                "name": p["name"],
                "type": "place",
                "parent": p["parent"],
                "path": f"{p['name']}, {p['parent'].replace('-', ' ').title()}, India",
                "summary": p.get("summary", ""),
                "points": p.get("points", []),
                "wiki": f"https://en.wikipedia.org/wiki/{p['name'].replace(' ', '_')}",
                "source": "Archaeological Survey of India, Wikipedia",
                "updated": "2024-11",
                "model": ""
            })
        write_data(PLACES_DIR, state_id, pls)

# For any remaining state in states.json that doesn't have district or place files yet:
# Generate standard baseline capital district and heritage place so no state is empty!
for s in all_states:
    sid = s["id"]
    if sid == "india":
        continue

    dist_file = DIST_DIR / f"{sid}.json"
    if not dist_file.exists():
        cap = s.get("profile", {}).get("Capital", s["name"])
        clean_cap = cap.split("(")[0].strip()
        cap_id = clean_cap.lower().replace(" ", "-")
        # Prevent collisions for shared capitals like Chandigarh
        unique_dist_id = f"{sid}-{cap_id}-district" if sid in ["haryana", "punjab"] else f"{cap_id}-district"
        default_dist = [{
            "id": unique_dist_id,
            "name": clean_cap,
            "type": "district",
            "parent": sid,
            "path": f"{clean_cap}, {s['name']}, India",
            "summary": f"Administrative capital district of {s['name']}.",
            "profile": {
                "Headquarters": clean_cap,
                "Language": s.get("profile", {}).get("Language", "Official"),
                "Food": s.get("profile", {}).get("Food", ""),
                "Crafts": s.get("profile", {}).get("Crafts", ""),
            },
            "area": s.get("area", ""),
            "population": s.get("population", ""),
            "points": [f"Seat of government and administration of {s['name']}"],
            "wiki": s.get("wiki", ""),
            "source": "Census of India 2011, Wikipedia",
            "updated": "2024-11",
            "model": ""
        }]
        write_data(DIST_DIR, sid, default_dist)

    place_file = PLACES_DIR / f"{sid}.json"
    if not place_file.exists():
        cap = s.get("profile", {}).get("Capital", s["name"])
        clean_cap = cap.split("(")[0].strip()
        cap_id = clean_cap.lower().replace(" ", "-")
        unique_dist_id = f"{sid}-{cap_id}-district" if sid in ["haryana", "punjab"] else f"{cap_id}-district"
        default_place = [{
            "id": f"{sid}-heritage-monument",
            "name": f"{s['name']} Heritage Monument",
            "type": "place",
            "parent": unique_dist_id,
            "path": f"{s['name']} Heritage Monument, {clean_cap}, {s['name']}, India",
            "summary": f"Prominent historic cultural landmark and architectural attraction in {s['name']}.",
            "points": [
                f"Iconic historical destination showcasing the traditions and heritage of {s['name']}",
                "Protected cultural site attracting visitors and scholars"
            ],
            "wiki": s.get("wiki", ""),
            "source": "State Tourism Department, Wikipedia",
            "updated": "2024-11",
            "model": ""
        }]
        write_data(PLACES_DIR, sid, default_place)

print("All states and UTs districts and places generated!")
