import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent / "backend" / "data"
DIST_DIR = BASE_DIR / "districts"
PLACES_DIR = BASE_DIR / "places"

def write_data(folder: Path, filename: str, data: list):
    path = folder / f"{filename}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Generated {path.name}: {len(data)} items")

# ==========================================
# 5. MAHARASHTRA (Districts & Temples/Places)
# ==========================================
mh_districts = [
  {"id": "ahmednagar", "name": "Ahilyanagar (Ahmednagar)", "type": "district", "parent": "maharashtra", "path": "Ahilyanagar, Maharashtra, India",
   "summary": "Historic fortress district, sugar cooperative capital, home to Shirdi Sai Baba Temple and Shani Shingnapur.",
   "profile": {"Headquarters": "Ahilyanagar", "Language": "Marathi", "Food": "Jowar bhakri, Pithla, Shirdi Prasad laddu", "Crafts": "Sugar manufacturing, Handloom weaving"},
   "area": "17,048 km²", "population": "4,543,159 (2011 Census)", "points": ["Shirdi is the sacred spiritual sanctuary of 19th-century saint Sai Baba", "Ahmednagar Fort was constructed in 1490 CE by Malik Ahmad Nizam Shah I"],
   "wiki": "https://en.wikipedia.org/wiki/Ahmednagar_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "chhatrapati-sambhajinagar", "name": "Chhatrapati Sambhajinagar (Aurangabad)", "type": "district", "parent": "maharashtra", "path": "Chhatrapati Sambhajinagar, Maharashtra, India",
   "summary": "Tourism Capital of Maharashtra, world-renowned gateway to Ajanta and Ellora UNESCO rock cave temples.",
   "profile": {"Headquarters": "Chhatrapati Sambhajinagar", "Language": "Marathi, Urdu", "Food": "Naan Qalia, Tahari", "Crafts": "GI-tagged Paithani silk sarees, Himroo shawls, Bidriware"},
   "area": "10,107 km²", "population": "3,701,282 (2011 Census)", "points": ["Ellora Cave 16 (Kailasa Temple) is the largest monolithic rock-cut structure on Earth", "Bibi Ka Maqbara constructed in 1660 CE is known as the 'Taj of the Deccan'"],
   "wiki": "https://en.wikipedia.org/wiki/Aurangabad_district,_Maharashtra", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kolhapur", "name": "Kolhapur", "type": "district", "parent": "maharashtra", "path": "Kolhapur, Maharashtra, India",
   "summary": "Historic royal Maratha capital on the Panchganga River, famed for Mahalakshmi Temple, wrestling, and leather footwear.",
   "profile": {"Headquarters": "Kolhapur", "Language": "Marathi", "Food": "Kolhapuri Tambda Rassa, Pandhra Rassa, Kolhapuri Misal", "Crafts": "GI-tagged Kolhapuri chappals (leather sandals), Kolhapuri Saaj jewelry"},
   "area": "7,685 km²", "population": "3,876,001 (2011 Census)", "points": ["Mahalakshmi (Ambabai) Temple is an ancient 7th-century Chalukyan Shakti shrine", "Revered center of traditional Indian Kushti wrestling at historic talims"],
   "wiki": "https://en.wikipedia.org/wiki/Kolhapur_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "mumbai-city", "name": "Mumbai City", "type": "district", "parent": "maharashtra", "path": "Mumbai City, Maharashtra, India",
   "summary": "Financial and entertainment capital of India, island city of Gateway of India, Dalal Street, and Bollywood.",
   "profile": {"Headquarters": "Mumbai", "Language": "Marathi, Hindi, English", "Food": "Vada Pav, Pav Bhaji, Bombay Duck, Bhel Puri", "Crafts": "Commercial publishing, Diamond polishing"},
   "area": "157 km²", "population": "3,085,411 (2011 Census)", "points": ["Gateway of India erected in 1924 overlooking the Arabian Sea", "Victorian Gothic and Art Deco Ensembles of Mumbai inscribed as UNESCO World Heritage Site in 2018"],
   "wiki": "https://en.wikipedia.org/wiki/Mumbai_City_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "mumbai-suburban", "name": "Mumbai Suburban", "type": "district", "parent": "maharashtra", "path": "Mumbai Suburban, Maharashtra, India",
   "summary": "Metropolitan suburban territory housing Sanjay Gandhi National Park, Kanheri Buddhist Caves, and film studios.",
   "profile": {"Headquarters": "Bandra", "Language": "Marathi, Hindi, English", "Food": "Street chaat, Frankie", "Crafts": "Film production, IT services"},
   "area": "446 km²", "population": "9,356,962 (2011 Census)", "points": ["Sanjay Gandhi National Park is one of the world's few major protected forests inside city limits", "Kanheri Caves feature 109 rock-cut Buddhist chaityas and viharas (1st century BCE–10th century CE)"],
   "wiki": "https://en.wikipedia.org/wiki/Mumbai_Suburban_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "nagpur", "name": "Nagpur", "type": "district", "parent": "maharashtra", "path": "Nagpur, Maharashtra, India",
   "summary": "Orange City and Winter Capital of Maharashtra, geographical center of India marked by the Zero Mile Stone.",
   "profile": {"Headquarters": "Nagpur", "Language": "Marathi, Hindi", "Food": "Tarri Poha, Saoji Mutton, Nagpur Orange barfi", "Crafts": "Nagpur Mandarin orange processing"},
   "area": "9,892 km²", "population": "4,653,570 (2011 Census)", "points": ["Zero Mile Stone erected by British Great Trigonometrical Survey of India in 1907", "Deekshabhoomi is where Dr. B. R. Ambedkar embraced Buddhism with 600,000 followers on 14 October 1956"],
   "wiki": "https://en.wikipedia.org/wiki/Nagpur_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "nashik", "name": "Nashik", "type": "district", "parent": "maharashtra", "path": "Nashik, Maharashtra, India",
   "summary": "Wine Capital of India on the Godavari river, sacred Kumbh Mela city, home to Trimbakeshwar Jyotirlinga.",
   "profile": {"Headquarters": "Nashik", "Language": "Marathi", "Food": "Misal Pav, Poha, Table grapes, Wine", "Crafts": "GI-tagged Nashik Valley Wine, Silver jewellery"},
   "area": "15,530 km²", "population": "6,107,187 (2011 Census)", "points": ["Trimbakeshwar Temple houses one of the 12 sacred Jyotirlingas with three-faced lingam (Brahma, Vishnu, Shiva)", "Hosts the monumental Simhastha Kumbh Mela once every 12 years along the Ramkund ghats"],
   "wiki": "https://en.wikipedia.org/wiki/Nashik_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "pune", "name": "Pune", "type": "district", "parent": "maharashtra", "path": "Pune, Maharashtra, India",
   "summary": "Oxford of the East and cultural capital of Maharashtra, seat of the Peshwas, automotive and IT metropolis.",
   "profile": {"Headquarters": "Pune", "Language": "Marathi, English", "Food": "Puneri Misal, Bhakarwadi, Pithla Bhakri", "Crafts": "Bakharwadi savories, Automobile engineering"},
   "area": "15,643 km²", "population": "9,429,408 (2011 Census)", "points": ["Shaniwar Wada was the historic seven-story fortified palace seat of the Maratha Peshwas built in 1732 CE", "Aga Khan Palace served as prison for Mahatma Gandhi and Kasturba Gandhi during the Quit India movement"],
   "wiki": "https://en.wikipedia.org/wiki/Pune_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "solapur", "name": "Solapur", "type": "district", "parent": "maharashtra", "path": "Solapur, Maharashtra, India",
   "summary": "Textile and pilgrimage center, home to Siddheshwar Temple and sacred Vithoba sanctuary at Pandharpur.",
   "profile": {"Headquarters": "Solapur", "Language": "Marathi, Kannada, Telugu", "Food": "Shenga Chutney, Jowar Bhakri", "Crafts": "GI-tagged Solapur Chaddar (jacquard bedsheets) and Terry Towels"},
   "area": "14,895 km²", "population": "4,317,756 (2011 Census)", "points": ["Pandharpur Vithoba Temple is the spiritual focal point of Maharashtra's historic Varkari Bhakti movement", "Largest producer of jacquard bedsheets and terry towels in India"],
   "wiki": "https://en.wikipedia.org/wiki/Solapur_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},
]

write_data(DIST_DIR, "maharashtra", mh_districts)

mh_places = [
  {"id": "kailasa-temple-ellora", "name": "Kailasa Temple (Cave 16), Ellora", "type": "place", "parent": "chhatrapati-sambhajinagar",
   "path": "Kailasa Temple, Chhatrapati Sambhajinagar, Maharashtra, India",
   "summary": "World's largest monolithic rock-cut monument, chiseled vertically top-down from a single basalt cliff face.",
   "points": [
     "Commissioned in the 8th century CE (c. 756–773 CE) by Rashtrakuta King Krishna I",
     "Rashtrakuta dynasty; central highlight of the UNESCO World Heritage Ellora Caves inscribed in 1983",
     "Dedicated to Lord Shiva as his Himalayan abode Mount Kailash; carved from 200,000 tonnes of solid basalt rock",
     "Excavated entirely using top-down quarrying technique without scaffolding, featuring intricate multi-story elephant and Ramayana relief friezes"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Kailash_Temple,_Ellora", "source": "Archaeological Survey of India, UNESCO, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "trimbakeshwar-shiva-temple", "name": "Trimbakeshwar Shiva Temple, Nashik", "type": "place", "parent": "nashik",
   "path": "Trimbakeshwar Temple, Nashik, Maharashtra, India",
   "summary": "Ancient Jyotirlinga sanctuary located at the source of the holy Godavari river at the foot of Brahmagiri mountain.",
   "points": [
     "Present monumental black basalt temple constructed by Maratha ruler Peshwa Balaji Baji Rao (Nana Saheb) between 1755 and 1786 CE",
     "Maratha Peshwa dynasty",
     "One of the 12 sacred Jyotirlingas; unique for housing a three-faced lingam representing Brahma, Vishnu, and Shiva",
     "Adorned with a jeweled crown (Trimbakeshwar Crown) studded with diamonds, emeralds, and rubies dating back to the Pandavas"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Trimbakeshwar_Shiva_Temple", "source": "Trimbakeshwar Devasthan, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "siddhivinayak-temple-mumbai", "name": "Shree Siddhivinayak Temple, Prabhadevi", "type": "place", "parent": "mumbai-city",
   "path": "Siddhivinayak Temple, Mumbai City, Maharashtra, India",
   "summary": "Two-century-old premier Ganesha sanctuary in central Mumbai, renowned for gold-plated inner sanctum.",
   "points": [
     "Originally constructed on 19 November 1801 by contractor Laxman Vithu and funded by rich agri woman Deubai Patil",
     "Patronized by Maratha and Peshwa nobility; modern multi-tier gold-domed structure consecrated in 1993",
     "Dedicated to Lord Ganesha (Siddhivinayak - 'granter of wishes'); carved from a single 2.5-foot black stone with right-turned trunk (Navasacha Ganapati)",
     "Visited by over 200,000 devotees every Tuesday including leaders of business, politics, and the film industry"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Siddhivinayak_Temple,_Mumbai", "source": "Shree Siddhivinayak Ganapati Temple Trust, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "shirdi-sai-baba-temple", "name": "Sai Baba Temple, Shirdi", "type": "place", "parent": "ahmednagar",
   "path": "Sai Baba Temple, Ahilyanagar, Maharashtra, India",
   "summary": "Global pilgrimage shrine honoring 19th-century saint Sai Baba, preaching universal harmony and devotion.",
   "points": [
     "Samadhi Mandir construction began in 1915 CE by wealthy disciple Gopalrao Booty; saint's mortal remains consecrated in October 1918",
     "Dedicated to the venerated ascetic Sadguru Sai Baba of Shirdi, who taught 'Sabka Malik Ek' (One God Governs All)",
     "Features a life-size pure Italian white marble statue of Sai Baba seated on an Italian marble throne sculpted by Balaji Vasant Talim in 1954",
     "Attracts upwards of 25,000 to 100,000 devotees every day from all religious backgrounds worldwide"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Shirdi", "source": "Shri Saibaba Sansthan Trust, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "mahalakshmi-temple-kolhapur", "name": "Shri Ambabai (Mahalakshmi) Temple, Kolhapur", "type": "place", "parent": "kolhapur",
   "path": "Mahalakshmi Temple, Kolhapur, Maharashtra, India",
   "summary": "7th-century Chalukyan architectural marvel and major Shakti Peetha where solar rays illuminate the deity twice yearly.",
   "points": [
     "Constructed in the 7th century CE by King Karandev of the Chalukya dynasty; further embellished by Shilahara and Yadava kings in 11th century",
     "Chalukya, Shilahara, and Maratha dynasties",
     "Dedicated to Goddess Mahalakshmi (locally called Ambabai), the supreme Shakti granting both spiritual liberation and worldly prosperity",
     "Acclaimed for the architectural marvel of Kiranotsav (Festival of Sun Rays), where natural setting sunbeams fall directly on the deity's feet and face in January and November"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Mahalakshmi_Temple,_Kolhapur", "source": "Paschim Maharashtra Devasthan Samiti, Wikipedia", "updated": "2024-11", "model": ""},
]

write_data(PLACES_DIR, "maharashtra", mh_places)

# ==========================================
# 6. UTTAR PRADESH (Key Districts & Temples)
# ==========================================
up_districts = [
  {"id": "agra", "name": "Agra", "type": "district", "parent": "uttar-pradesh", "path": "Agra, Uttar Pradesh, India",
   "summary": "Imperial Mughal capital on the Yamuna river, internationally famous for the Taj Mahal, Agra Fort, and marble inlay.",
   "profile": {"Headquarters": "Agra", "Language": "Hindi, Urdu, Braj Bhasha", "Food": "Agra Petha, Bedai Aloo, Mughlai curries", "Crafts": "Pietra dura marble inlay, Leather footwear"},
   "area": "4,027 km²", "population": "4,418,797 (2011 Census)", "points": ["Home to three UNESCO World Heritage Sites: Taj Mahal, Agra Fort, and Fatehpur Sikri", "Capital of the Mughal Empire under emperors Akbar, Jahangir, and Shah Jahan"],
   "wiki": "https://en.wikipedia.org/wiki/Agra_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "ayodhya", "name": "Ayodhya", "type": "district", "parent": "uttar-pradesh", "path": "Ayodhya, Uttar Pradesh, India",
   "summary": "Ancient sacred city on the holy Saryu river, legendary capital of the Ikshvaku dynasty and birthplace of Lord Rama.",
   "profile": {"Headquarters": "Ayodhya", "Language": "Hindi, Awadhi", "Food": "Laddus, Ramdana laddoos", "Crafts": "Wood carving, Religious souvenirs"},
   "area": "2,522 km²", "population": "2,470,996 (2011 Census)", "points": ["Birthplace of Lord Rama described in the epic Ramayana; capital of ancient Kosala Kingdom", "Home to the newly consecrated grand Ram Mandir and historic Hanuman Garhi temple"],
   "wiki": "https://en.wikipedia.org/wiki/Ayodhya_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "lucknow", "name": "Lucknow", "type": "district", "parent": "uttar-pradesh", "path": "Lucknow, Uttar Pradesh, India",
   "summary": "The City of Nawabs and capital of Uttar Pradesh, famed for refined Tehzeeb manners, Awadhi cuisine, and Chikankari embroidery.",
   "profile": {"Headquarters": "Lucknow", "Language": "Hindi, Urdu, Awadhi", "Food": "Awadhi Dum Biryani, Galouti Kebab, Sheermal", "Crafts": "GI-tagged Chikankari white embroidery, Zardozi gold embroidery"},
   "area": "2,528 km²", "population": "4,589,838 (2011 Census)", "points": ["Capital of the Nawabs of Awadh who built the Bara Imambara and Rumi Darwaza in the 18th century", "Bara Imambara features the world's largest unsupported vaulted hall (Bhulbhulaiya maze)"],
   "wiki": "https://en.wikipedia.org/wiki/Lucknow_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "mathura", "name": "Mathura", "type": "district", "parent": "uttar-pradesh", "path": "Mathura, Uttar Pradesh, India",
   "summary": "Sacred Braj Bhumi on the Yamuna river, revered birthplace of Lord Krishna, and ancient seat of Mathura Kushan art.",
   "profile": {"Headquarters": "Mathura", "Language": "Hindi, Braj Bhasha", "Food": "Mathura Peda, Makhan Mishri, Kachori", "Crafts": "Sanjhi paper stenciling art, Deity dresses"},
   "area": "3,340 km²", "population": "2,547,184 (2011 Census)", "points": ["Birthplace of Lord Krishna at Shri Krishna Janmabhoomi complex", "Major cultural capital of Kushan Empire (1st–3rd century CE) where early red sandstone Buddha and Hindu sculptures evolved"],
   "wiki": "https://en.wikipedia.org/wiki/Mathura_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "varanasi", "name": "Varanasi (Kashi)", "type": "district", "parent": "uttar-pradesh", "path": "Varanasi, Uttar Pradesh, India",
   "summary": "Spiritual Capital of India, sacred holy city on the Ganges with 84 bathing ghats and Kashi Vishwanath Jyotirlinga.",
   "profile": {"Headquarters": "Varanasi", "Language": "Hindi, Bhojpuri", "Food": "Banarasi Paan, Malaiyo, Tamatar Chaat, Kachori Jalebi", "Crafts": "GI-tagged Banarasi silk brocade sarees, Pink Meenakari enamel, Wooden toys"},
   "area": "1,535 km²", "population": "3,676,841 (2011 Census)", "points": ["One of the world's oldest continuously inhabited sacred cities, dating back to 2nd millennium BCE", "Includes Sarnath, where Gautama Buddha delivered his first sermon (Dharmachakra Pravartana) in 528 BCE"],
   "wiki": "https://en.wikipedia.org/wiki/Varanasi_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},
]

write_data(DIST_DIR, "uttar-pradesh", up_districts)

up_places = [
  {"id": "kashi-vishwanath-temple", "name": "Kashi Vishwanath Temple, Varanasi", "type": "place", "parent": "varanasi",
   "path": "Kashi Vishwanath Temple, Varanasi, Uttar Pradesh, India",
   "summary": "Holiest Jyotirlinga of Lord Shiva on the sacred western bank of River Ganges, center of Kashi Vishwanath Dham.",
   "points": [
     "Ancient shrine destroyed and rebuilt several times; current sanctum erected in 1780 CE by Queen Ahilyabai Holkar of Indore",
     "Maratha Holkar dynasty, with gold spires gifted in 1835 by Maharaja Ranjit Singh of the Sikh Empire",
     "Dedicated to Lord Vishveshwara (Shiva), the Lord of the Universe; one of the 12 supreme Jyotirlingas",
     "Expanded in 2021 into the grand Kashi Vishwanath Corridor connecting the temple directly to the sacred Ganga ghats"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Kashi_Vishwanath_Temple", "source": "Shri Kashi Vishwanath Special Area Development Board, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "taj-mahal", "name": "Taj Mahal, Agra", "type": "place", "parent": "agra",
   "path": "Taj Mahal, Agra, Uttar Pradesh, India",
   "summary": "Ivory-white marble mausoleum on the south bank of the Yamuna River, universal masterpiece of world heritage.",
   "points": [
     "Commissioned in 1632 CE by Mughal Emperor Shah Jahan to house the tomb of his favorite consort Mumtaz Mahal; completed c. 1653 CE",
     "Mughal dynasty; principal architect Ustad Ahmad Lahori; inscribed as a UNESCO World Heritage Site in 1983",
     "Constructed of pure white Makrana marble inlaid with 28 varieties of semi-precious gemstones in intricate Pietra Dura motifs",
     "Stands in a 42-acre complex featuring four 40-meter minarets, red sandstone mosque, and Charbagh Mughal formal gardens"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Taj_Mahal", "source": "Archaeological Survey of India, UNESCO, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "ram-janmabhoomi-mandir", "name": "Ram Janmabhoomi Mandir, Ayodhya", "type": "place", "parent": "ayodhya",
   "path": "Ram Mandir, Ayodhya, Uttar Pradesh, India",
   "summary": "Grand Nagara-style Hindu temple complex marking the sacred birthplace of Lord Rama on the banks of Saryu River.",
   "points": [
     "Designed in classical Gujara-Chalukya style by master temple architect Chandrakant Sompura; consecrated on 22 January 2024",
     "Constructed under the supervision of Shri Ram Janmbhoomi Teerth Kshetra trust",
     "Dedicated to Ram Lalla Virajman (infant Lord Rama), carved from 3-billion-year-old black Krishna shila stone by sculptor Arun Yogiraj",
     "Built entirely with carved pink Bansi Paharpur sandstone from Rajasthan without using structural steel or iron"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Ram_Mandir", "source": "Shri Ram Janmbhoomi Teerth Kshetra, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "krishna-janmabhoomi-temple", "name": "Shri Krishna Janmabhoomi Complex, Mathura", "type": "place", "parent": "mathura",
   "path": "Krishna Janmabhoomi, Mathura, Uttar Pradesh, India",
   "summary": "Sacred prison cell (Garbha Griha) where Lord Krishna was born to Devaki and Vasudeva during the reign of King Kamsa.",
   "points": [
     "Earliest stone temple built by great-grandson Vajranabha; grand temple erected in 1150 CE by Jajja; present complex restored by industrialist Jugal Kishore Birla in 1965",
     "Gupta, Chandela, and modern public trusts",
     "Marks the exact prison cell underground chamber where Krishna took birth to destroy demon king Kamsa",
     "Excavations yielded 6th-century BCE punch-marked coins, terracotta figurines, and Kushan stone sculptures"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Krishna_Janmasthan_Temple_Complex", "source": "Mathura Heritage Trust, ASI, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "sarnath-dhamek-stupa", "name": "Dhamek Stupa & Lion Capital, Sarnath", "type": "place", "parent": "varanasi",
   "path": "Sarnath Dhamek Stupa, Varanasi, Uttar Pradesh, India",
   "summary": "Sacred Buddhist park where Gautama Buddha preached his first sermon, and origin of the National Emblem of India.",
   "points": [
     "Originally established by Mauryan Emperor Ashoka in 249 BCE; massive current stone stupa built in 500 CE during the Gupta Empire",
     "Maurya and Gupta dynasties",
     "Marks the Deer Park (Rishipatana) where Buddha revealed the Four Noble Truths and Eightfold Path (Dhammacakkappavattana Sutta)",
     "Ashoka erected the famous polished sandstone Lion Capital here, adopted as the official National Emblem of the Republic of India"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Dhamek_Stupa", "source": "Archaeological Survey of India, UNESCO Tentative, Wikipedia", "updated": "2024-11", "model": ""},
]

write_data(PLACES_DIR, "uttar-pradesh", up_places)

print("Maharashtra and Uttar Pradesh data generated successfully.")
