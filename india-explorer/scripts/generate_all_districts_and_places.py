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

# ==========================================
# 3. KERALA (14 Districts + Famous Temples & Places)
# ==========================================
kerala_districts = [
  {"id": "alappuzha", "name": "Alappuzha", "type": "district", "parent": "kerala", "path": "Alappuzha, Kerala, India",
   "summary": "Venice of the East, world-famous for palm-lined backwaters, houseboats, and the Nehru Trophy Boat Race.",
   "profile": {"Headquarters": "Alappuzha", "Language": "Malayalam", "Food": "Karimeen Pollichathu, Duck Roast", "Crafts": "GI-tagged Coir mats and ropes"},
   "area": "1,414 km²", "population": "2,127,789 (2011 Census)", "points": ["Vembanad Lake hosts the annual Punnamada snake boat races (Vallam Kali)", "Center of India's coir processing and backwater tourism economy"],
   "wiki": "https://en.wikipedia.org/wiki/Alappuzha_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "ernakulam", "name": "Ernakulam", "type": "district", "parent": "kerala", "path": "Ernakulam, Kerala, India",
   "summary": "Commercial and financial capital of Kerala centered at Kochi, historic spice port with Chinese fishing nets.",
   "profile": {"Headquarters": "Kakkanad (Kochi)", "Language": "Malayalam, English", "Food": "Kochi seafood, Appam with stew", "Crafts": "Marine export processing, Spices"},
   "area": "3,068 km²", "population": "3,282,388 (2011 Census)", "points": ["Fort Kochi was the first European colonial settlement in India (Portuguese 1500 CE)", "Home to Cochin Shipyard, Southern Naval Command, and Kochi Metro"],
   "wiki": "https://en.wikipedia.org/wiki/Ernakulam_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "idukki", "name": "Idukki", "type": "district", "parent": "kerala", "path": "Idukki, Kerala, India",
   "summary": "Mountainous Western Ghats highland boasting Munnar tea estates, Eravikulam National Park, and Idukki Arch Dam.",
   "profile": {"Headquarters": "Painavu", "Language": "Malayalam, Tamil", "Food": "Cardamom tea, Kanthari chilli dishes", "Crafts": "GI-tagged Idukki Green Cardamom, Tea packaging"},
   "area": "4,358 km²", "population": "1,108,974 (2011 Census)", "points": ["Anamudi peak (2,695 m) is the highest summit in South India", "Idukki Dam is one of the highest double-curvature concrete arch dams in Asia"],
   "wiki": "https://en.wikipedia.org/wiki/Idukki_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kannur", "name": "Kannur", "type": "district", "parent": "kerala", "path": "Kannur, Kerala, India",
   "summary": "Land of Looms and Lores on the North Malabar coast, world-famous for ritualistic Theyyam performances and handloom.",
   "profile": {"Headquarters": "Kannur", "Language": "Malayalam", "Food": "Thalassery Biryani, Muttamala", "Crafts": "GI-tagged Cannanore handloom home furnishings"},
   "area": "2,966 km²", "population": "2,523,003 (2011 Census)", "points": ["St. Angelo Fort built in 1505 CE by the first Portuguese Viceroy Dom Francisco de Almeida", "Seat of the Arakkal kingdom, the only Muslim royal dynasty in Kerala history"],
   "wiki": "https://en.wikipedia.org/wiki/Kannur_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kasaragod", "name": "Kasaragod", "type": "district", "parent": "kerala", "path": "Kasaragod, Kerala, India",
   "summary": "Northernmost coastal district, Land of Gods and Seven Languages, famed for coastal Bekal Fort and Ananthapura Lake Temple.",
   "profile": {"Headquarters": "Kasaragod", "Language": "Malayalam, Tulu, Kannada, Beary, Konkani", "Food": "Kasaragod Kozhi curry, Pathiri", "Crafts": "Bell metal ware, Kasaragod handloom cotton sarees"},
   "area": "1,992 km²", "population": "1,307,375 (2011 Census)", "points": ["Bekal Fort built in 1650 CE by Shivappa Nayaka of Keladi, Kerala's largest historic fort", "Only lake temple in Kerala situated at Ananthapura"],
   "wiki": "https://en.wikipedia.org/wiki/Kasaragod_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kollam", "name": "Kollam", "type": "district", "parent": "kerala", "path": "Kollam, Kerala, India",
   "summary": "Cashew Capital of the World on the shores of Ashtamudi Lake, ancient seaport of Quilon described by Marco Polo.",
   "profile": {"Headquarters": "Kollam", "Language": "Malayalam", "Food": "Fish peera, Cashew fry", "Crafts": "Cashew kernel processing, Coir yarn"},
   "area": "2,491 km²", "population": "2,635,375 (2011 Census)", "points": ["Historic port of Quilon traded with Phoenicians, Romans, Arabs, and Ming dynasty China", "Gateway to the backwaters via the scenic 8-hour Kollam-Alappuzha water ferry"],
   "wiki": "https://en.wikipedia.org/wiki/Kollam_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kottayam", "name": "Kottayam", "type": "district", "parent": "kerala", "path": "Kottayam, Kerala, India",
   "summary": "City of Letters, Lakes, and Latex; India's first 100% literate municipal town, heart of natural rubber estates.",
   "profile": {"Headquarters": "Kottayam", "Language": "Malayalam", "Food": "Appam, Karimeen, Beef fry", "Crafts": "Natural rubber production, Publishing"},
   "area": "2,208 km²", "population": "1,974,551 (2011 Census)", "points": ["First town in India to achieve 100% literacy in 1989", "Kumarakom bird sanctuary on the edge of Vembanad Lake hosts migratory Siberian storks"],
   "wiki": "https://en.wikipedia.org/wiki/Kottayam_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kozhikode", "name": "Kozhikode", "type": "district", "parent": "kerala", "path": "Kozhikode, Kerala, India",
   "summary": "City of Spices and Calico, historic capital of the Samoothiri (Zamorin) where Vasco da Gama landed in 1498 CE.",
   "profile": {"Headquarters": "Kozhikode", "Language": "Malayalam", "Food": "Kozhikodan Halwa, Malabar Dum Biryani, Banana Chips", "Crafts": "Beypore wooden dhow boat building (Uru), Calico cotton"},
   "area": "2,344 km²", "population": "3,086,293 (2011 Census)", "points": ["Vasco da Gama landed at Kappad beach near Kozhikode on 20 May 1498 discovering the sea route to India", "Declared India's first UNESCO City of Literature in 2023"],
   "wiki": "https://en.wikipedia.org/wiki/Kozhikode_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "malappuram", "name": "Malappuram", "type": "district", "parent": "kerala", "path": "Malappuram, Kerala, India",
   "summary": "Hill city between Western Ghats and Arabian Sea, center of Islamic scholarship, Ayurvedic research, and football passion.",
   "profile": {"Headquarters": "Malappuram", "Language": "Malayalam, Arabic", "Food": "Alissa, Muttabaq, Pathiri", "Crafts": "Kottakkal Arya Vaidya Sala Ayurvedic medicines"},
   "area": "3,554 km²", "population": "4,112,920 (2011 Census)", "points": ["Kottakkal is world-renowned center of classical Ayurvedic healing founded in 1902 by Vaidyaratnam P. S. Varier", "Thirunavaya on Bharathappuzha was the traditional venue for the 12-yearly Mamankam festival"],
   "wiki": "https://en.wikipedia.org/wiki/Malappuram_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "palakkad", "name": "Palakkad", "type": "district", "parent": "kerala", "path": "Palakkad, Kerala, India",
   "summary": "Granary of Kerala, marked by the 30-km natural mountain pass Palakkad Gap connecting Kerala to Tamil Nadu plains.",
   "profile": {"Headquarters": "Palakkad", "Language": "Malayalam, Tamil", "Food": "Palakkad Matta rice, Ramassery Idli", "Crafts": "Bell metal ware, Bamboo crafts"},
   "area": "4,480 km²", "population": "2,809,934 (2011 Census)", "points": ["Palakkad Fort built in 1766 CE by Hyder Ali of Mysore with massive granite ramparts", "Silent Valley National Park protects one of the last undisturbed rain forests in India"],
   "wiki": "https://en.wikipedia.org/wiki/Palakkad_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "pathanamthitta", "name": "Pathanamthitta", "type": "district", "parent": "kerala", "path": "Pathanamthitta, Kerala, India",
   "summary": "Pilgrimage capital of Kerala, home to hill shrine Sabarimala in Periyar Tiger Reserve, and Aranmula metal mirrors.",
   "profile": {"Headquarters": "Pathanamthitta", "Language": "Malayalam", "Food": "Aranmula Vallasadya, Unniyappam", "Crafts": "GI-tagged Aranmula Kannadi (front-surface metal alloy mirrors)"},
   "area": "2,637 km²", "population": "1,197,412 (2011 Census)", "points": ["Sabarimala Ayyappa Temple atop the forested hills attracts over 30 million pilgrims annually", "Aranmula metal mirror is an exclusive metallurgical secret preserved by a few master artisan families"],
   "wiki": "https://en.wikipedia.org/wiki/Pathanamthitta_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "thiruvananthapuram", "name": "Thiruvananthapuram", "type": "district", "parent": "kerala", "path": "Thiruvananthapuram, Kerala, India",
   "summary": "Capital of Kerala, Ever-Green City of India, home to Padmanabhaswamy Temple, Kovalam beach, and ISRO VSSC.",
   "profile": {"Headquarters": "Thiruvananthapuram", "Language": "Malayalam, English", "Food": "Boli with Palpayasam, Kappa with Meen curry", "Crafts": "Balaramapuram cotton handlooms, Wood carving"},
   "area": "2,192 km²", "population": "3,301,427 (2011 Census)", "points": ["Padmanabhaswamy Temple houses estimated $20+ billion in consecrated gold and gemstone treasures", "Thumba Equatorial Rocket Launching Station established here in 1963 launched India's space program"],
   "wiki": "https://en.wikipedia.org/wiki/Thiruvananthapuram_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "thrissur", "name": "Thrissur", "type": "district", "parent": "kerala", "path": "Thrissur, Kerala, India",
   "summary": "Cultural Capital of Kerala, famed for the grand Thrissur Pooram festival, Vadakkunnathan Temple, and gold jewelry.",
   "profile": {"Headquarters": "Thrissur", "Language": "Malayalam", "Food": "Vellayappam, Meen Peera, Thrissur Halwa", "Crafts": "Gold jewelry manufacturing, Bell metal lamps"},
   "area": "3,032 km²", "population": "3,121,200 (2011 Census)", "points": ["Host to the annual Thrissur Pooram festival featuring 30 caparisoned elephants and Kudamattam umbrella exchanges", "Vadakkunnathan Temple won UNESCO Asia-Pacific Award of Excellence for heritage conservation"],
   "wiki": "https://en.wikipedia.org/wiki/Thrissur_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "wayanad", "name": "Wayanad", "type": "district", "parent": "kerala", "path": "Wayanad, Kerala, India",
   "summary": "Misty high plateau of the Western Ghats known for Edakkal prehistoric cave petroglyphs, tea estates, and spices.",
   "profile": {"Headquarters": "Kalpetta", "Language": "Malayalam", "Food": "Bamboo rice payasam, Wayanad pepper chicken", "Crafts": "GI-tagged Wayanad Robusta Coffee, Spices"},
   "area": "2,131 km²", "population": "817,420 (2011 Census)", "points": ["Edakkal Caves feature Neolithic human rock engravings dating back to 6000 BCE", "Banasura Sagar Dam is the largest earthen dam in India and second largest in Asia"],
   "wiki": "https://en.wikipedia.org/wiki/Wayanad_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},
]

write_data(DIST_DIR, "kerala", kerala_districts)

kerala_places = [
  {"id": "padmanabhaswamy-temple", "name": "Sree Padmanabhaswamy Temple, Thiruvananthapuram", "type": "place", "parent": "thiruvananthapuram",
   "path": "Sree Padmanabhaswamy Temple, Thiruvananthapuram, Kerala, India",
   "summary": "Ancient Divya Desam shrine dedicated to Lord Vishnu in Ananthashayanam posture, built in Chera-Dravidian architecture.",
   "points": [
     "Mentioned in Sangam epics and Bhagavata Purana; present monumental 100-foot eastern gopuram reconstructed in 1731 CE by King Marthanda Varma",
     "Travancore royal dynasty (Chera lineage)",
     "Dedicated to Lord Padmanabhaswamy (Vishnu) reclining on the five-hooded serpent Anantha",
     "Vaults contain historical offerings of gold coins, gemstone crowns, and diamond necklaces evaluated as the wealthiest religious institution in recorded history"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Padmanabhaswamy_Temple", "source": "Travancore Royal Trust, Archaeological Survey, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "vadakkunnathan-temple-thrissur", "name": "Vadakkunnathan Temple, Thrissur", "type": "place", "parent": "thrissur",
   "path": "Vadakkunnathan Temple, Thrissur, Kerala, India",
   "summary": "Millennium-old Shiva temple at the epicenter of Thekkinkadu Maidan, awarded UNESCO Asia-Pacific heritage prize.",
   "points": [
     "Traditionally founded by sage Parashurama; epigraphic evidence confirms active royal patronage under Chera dynasty in 9th century CE",
     "Chera (Kulasekhara) dynasty",
     "Dedicated to Lord Shiva (Vadakkunnathan) worshipped in the form of a 16-foot mound of consecrated ghee (Neyyabhishekam) that never melts",
     "Surrounded by massive stone walls with four gopurams; site of the annual Thrissur Pooram cultural extravaganza"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Vadakkunnathan_Temple", "source": "Cochin Devaswom Board, UNESCO, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "guruvayur-temple", "name": "Guruvayur Sri Krishna Temple, Guruvayur", "type": "place", "parent": "thrissur",
   "path": "Guruvayur Temple, Thrissur, Kerala, India",
   "summary": "The Bhuloka Vaikunta (Holy Abode of Vishnu on Earth), one of the most sacred Krishna pilgrimage centers in India.",
   "points": [
     "Historical records date to 14th century; renovated after fire in 1970; dedicated by Brihaspati (Guru) and Vayu according to legend",
     "Zamorin of Calicut and local royal dynasties",
     "Dedicated to Guruvayurappan (infant Krishna) holding conch, discus, mace, and lotus",
     "Maintains Punnathur Kotta elephant sanctuary housing over 40 consecrated temple elephants"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Guruvayur_Temple", "source": "Guruvayur Devaswom Board, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "sabarimala-temple", "name": "Sabarimala Sree Dharma Sastha Temple", "type": "place", "parent": "pathanamthitta",
   "path": "Sabarimala Temple, Pathanamthitta, Kerala, India",
   "summary": "Sacred hilltop wilderness pilgrimage dedicated to Lord Ayyappa in the dense tropical forests of Periyar Tiger Reserve.",
   "points": [
     "Consecrated according to tradition by sage Parashurama; historical structure rebuilt following fire in 1950",
     "Pandalam royal dynasty and Travancore Devaswom",
     "Dedicated to Lord Ayyappa (Dharma Sastha) observed in Naishtika Brahmacharya (celibate ascetic posture)",
     "Pilgrims observe a 41-day Vratham (vow of austerity) and climb the 18 sacred golden steps (Pathinettampadi) carrying the Irumudi kettu"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Sabarimala", "source": "Travancore Devaswom Board, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "bekal-fort", "name": "Bekal Fort", "type": "place", "parent": "kasaragod",
   "path": "Bekal Fort, Kasaragod, Kerala, India",
   "summary": "Largest preserved keyhole-shaped coastal sea fortress in Kerala projecting into the Arabian Sea.",
   "points": [
     "Constructed in 1650 CE by Shivappa Nayaka of the Keladi Nayaka dynasty; later modified by Hyder Ali and Tipu Sultan",
     "Keladi Nayaka and Kingdom of Mysore dynasties",
     "Built entirely with dark brown laterite stone blocks with sea observation ramparts and zigzag entrance",
     "Features a central observation tower providing panoramic vistas of 30 km along the Malabar coastline"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Bekal_Fort", "source": "Archaeological Survey of India, Kerala Tourism, Wikipedia", "updated": "2024-11", "model": ""},
]

write_data(PLACES_DIR, "kerala", kerala_places)

# ==========================================
# 4. ANDHRA PRADESH (26 Districts + Temples/Places)
# ==========================================
ap_districts = [
  {"id": "alluri-sitharama-raju", "name": "Alluri Sitharama Raju", "type": "district", "parent": "andhra-pradesh", "path": "Alluri Sitharama Raju, Andhra Pradesh, India",
   "summary": "Forested Eastern Ghats tribal highland, home to Araku Valley coffee and Borra Caves.",
   "profile": {"Headquarters": "Paderu", "Language": "Telugu", "Food": "Bongu Chicken (Bamboo chicken)", "Crafts": "GI-tagged Araku Valley Arabica Coffee"},
   "area": "12,251 km²", "population": "953,960 (2011 Census)", "points": ["Named after freedom fighter Alluri Sitarama Raju who led the Rampa Rebellion of 1922", "Borra Caves contain 150-million-year-old limestone stalactites and stalagmites"],
   "wiki": "https://en.wikipedia.org/wiki/Alluri_Sitharama_Raju_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "anakapalli", "name": "Anakapalli", "type": "district", "parent": "andhra-pradesh", "path": "Anakapalli, Tamil Nadu, India",
   "summary": "Second-largest jaggery trading market in India, home to Buddhist rock-cut monasteries at Bojjannakonda.",
   "profile": {"Headquarters": "Anakapalli", "Language": "Telugu", "Food": "Anakapalli jaggery sweets", "Crafts": "Etikoppaka lacquer wooden toys"},
   "area": "4,292 km²", "population": "1,726,998 (2011 Census)", "points": ["Bojjannakonda Buddhist rock-cut monolithic stupas date from 4th to 9th century CE", "GI-tagged Etikoppaka toys crafted from Ankudu wood with organic vegetable dyes"],
   "wiki": "https://en.wikipedia.org/wiki/Anakapalli_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "ananthapuramu", "name": "Ananthapuramu", "type": "district", "parent": "andhra-pradesh", "path": "Ananthapuramu, Andhra Pradesh, India",
   "summary": "Historic Rayalaseema district boasting 16th-century Lepakshi hanging pillar temple and Thimmamma Marrimanu banyan.",
   "profile": {"Headquarters": "Ananthapuramu", "Language": "Telugu", "Food": "Ragi Sankati with Natukodi Pulusu", "Crafts": "Dharmavaram handloom silk sarees"},
   "area": "10,205 km²", "population": "2,241,105 (2011 Census)", "points": ["Lepakshi Veerabhadra Temple features a monolithic Nandi and hanging stone pillar", "Thimmamma Marrimanu is one of the world's largest banyan tree canopies spreading over 4.7 acres"],
   "wiki": "https://en.wikipedia.org/wiki/Ananthapuramu_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "bapatla", "name": "Bapatla", "type": "district", "parent": "andhra-pradesh", "path": "Bapatla, Andhra Pradesh, India",
   "summary": "Coastal agricultural tract on the Bay of Bengal celebrated for Suryalanka beach and Chirala handloom textiles.",
   "profile": {"Headquarters": "Bapatla", "Language": "Telugu", "Food": "Seafood, Rice delicacies", "Crafts": "Chirala handloom cotton and silk sarees"},
   "area": "3,829 km²", "population": "1,586,918 (2011 Census)", "points": ["Chirala handloom weaving cluster famed for Kuppadam border sarees", "Bapatla hosts premier agricultural and engineering research colleges"],
   "wiki": "https://en.wikipedia.org/wiki/Bapatla_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "chittoor", "name": "Chittoor", "type": "district", "parent": "andhra-pradesh", "path": "Chittoor, Andhra Pradesh, India",
   "summary": "Borderland district in the southern tip of Andhra Pradesh, famous for Totapuri mango processing and Kanipakam temple.",
   "profile": {"Headquarters": "Chittoor", "Language": "Telugu, Tamil", "Food": "Mango pulp, Pesarattu", "Crafts": "Totapuri mango pulp processing, Jaggery"},
   "area": "6,855 km²", "population": "1,872,951 (2011 Census)", "points": ["Kanipakam Varasiddhi Vinayaka Temple features a growing self-manifested (Swayambhu) Ganesha idol", "Major center of dairy farming and milk processing in South India"],
   "wiki": "https://en.wikipedia.org/wiki/Chittoor_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "east-godavari", "name": "East Godavari", "type": "district", "parent": "andhra-pradesh", "path": "East Godavari, Andhra Pradesh, India",
   "summary": "Cultural and literary capital on the Godavari river centered at Rajamahendravaram, birthplace of Adikavi Nannaya.",
   "profile": {"Headquarters": "Rajamahendravaram", "Language": "Telugu", "Food": "Pootharekulu, Rajahmundry Rose Milk", "Crafts": "Coir products, Godavari river boats"},
   "area": "2,561 km²", "population": "1,832,332 (2011 Census)", "points": ["Sir Arthur Cotton Barrage across the Godavari irrigates over one million acres of paddy", "Adikavi Nannaya began translating the Mahabharata into Telugu here in the 11th century"],
   "wiki": "https://en.wikipedia.org/wiki/East_Godavari_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "guntur", "name": "Guntur", "type": "district", "parent": "andhra-pradesh", "path": "Guntur, Andhra Pradesh, India",
   "summary": "Spicy capital of India, housing Asia's largest chilli yard, historic Kondaveedu Fort, and tobacco export markets.",
   "profile": {"Headquarters": "Guntur", "Language": "Telugu", "Food": "Guntur Gongura Mutton, Mirchi Bajji", "Crafts": "GI-tagged Guntur Sannam Red Chillies"},
   "area": "2,443 km²", "population": "2,091,075 (2011 Census)", "points": ["Guntur Mirchi Yard is Asia's largest market for dry chillies, trading Guntur Sannam varieties", "Kondaveedu Fort was built in the 14th century by the Reddy dynasty kings"],
   "wiki": "https://en.wikipedia.org/wiki/Guntur_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "krishna", "name": "Krishna", "type": "district", "parent": "andhra-pradesh", "path": "Krishna, Andhra Pradesh, India",
   "summary": "Delta territory centered at coastal Machilipatnam, historic port of Masulipatnam and birthplace of Kuchipudi dance.",
   "profile": {"Headquarters": "Machilipatnam", "Language": "Telugu", "Food": "Bandar Laddu, Bandar Halwa", "Crafts": "GI-tagged Machilipatnam Kalamkari block printing"},
   "area": "3,775 km²", "population": "1,735,079 (2011 Census)", "points": ["Machilipatnam was major 17th-century trading port for British, French, and Dutch East India Companies", "Kuchipudi village is the origin and spiritual home of classical Indian Kuchipudi dance"],
   "wiki": "https://en.wikipedia.org/wiki/Krishna_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kurnool", "name": "Kurnool", "type": "district", "parent": "andhra-pradesh", "path": "Kurnool, Andhra Pradesh, India",
   "summary": "Gateway of Rayalaseema and first capital of Andhra State (1953–56), home to Belum Caves and Konda Reddy Fort.",
   "profile": {"Headquarters": "Kurnool", "Language": "Telugu", "Food": "Uggani Bajji, Rayalaseema Pulao", "Crafts": "Stone carving, Cotton weaving"},
   "area": "7,980 km²", "population": "2,271,686 (2011 Census)", "points": ["Served as capital of Andhra State from 1953 to 1956", "Belum Caves is the second largest natural cave system in the Indian subcontinent (3.2 km long)"],
   "wiki": "https://en.wikipedia.org/wiki/Kurnool_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "nandyal", "name": "Nandyal", "type": "district", "parent": "andhra-pradesh", "path": "Nandyal, Andhra Pradesh, India",
   "summary": "Sacred territory surrounded by nine Nandi shrines (Nava Nandulu), housing Mallikarjuna Jyotirlinga at Srisailam.",
   "profile": {"Headquarters": "Nandyal", "Language": "Telugu", "Food": "Jowar roti, Gongura pachadi", "Crafts": "Cotton handlooms, Stone sculptures"},
   "area": "9,682 km²", "population": "1,781,777 (2011 Census)", "points": ["Srisailam Mallikarjuna Temple is one of only three shrines in India that is both a Jyotirlinga and a Shakti Peetha", "Nagarjunsagar-Srisailam Tiger Reserve is the largest tiger reserve in India by area"],
   "wiki": "https://en.wikipedia.org/wiki/Nandyal_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "ntr", "name": "NTR", "type": "district", "parent": "andhra-pradesh", "path": "NTR, Andhra Pradesh, India",
   "summary": "Urban economic hub centered at Vijayawada on the Krishna river, home to Kanaka Durga Temple and Prakasam Barrage.",
   "profile": {"Headquarters": "Vijayawada", "Language": "Telugu", "Food": "Punugulu, Ulavacharu Biryani", "Crafts": "Kondapalli painted wooden toys"},
   "area": "3,316 km²", "population": "2,218,591 (2011 Census)", "points": ["Kanaka Durga Temple sits atop Indrakeeladri hill overlooking the Krishna river", "Kondapalli toys crafted from Tella Poniki softwood since 14th century"],
   "wiki": "https://en.wikipedia.org/wiki/NTR_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "tirupati", "name": "Tirupati", "type": "district", "parent": "andhra-pradesh", "path": "Tirupati, Andhra Pradesh, India",
   "summary": "Spiritual Capital of Andhra Pradesh, home to the sacred Venkateswara Temple on the Seven Hills of Tirumala.",
   "profile": {"Headquarters": "Tirupati", "Language": "Telugu", "Food": "GI-tagged Tirupati Laddu, Pulihora", "Crafts": "Wood carving, Red Sanders products, Brass lamps"},
   "area": "8,231 km²", "population": "2,196,984 (2011 Census)", "points": ["Venkateswara Temple at Tirumala attracts 60,000 to 100,000 pilgrims daily, receiving over ₹1,400 crore annually", "Includes Indian spaceport Satish Dhawan Space Centre (SDSC-SHAR) at Sriharikota barrier island"],
   "wiki": "https://en.wikipedia.org/wiki/Tirupati_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "visakhapatnam", "name": "Visakhapatnam", "type": "district", "parent": "andhra-pradesh", "path": "Visakhapatnam, Andhra Pradesh, India",
   "summary": "The City of Destiny, major natural deep-water port on the Bay of Bengal, naval base, and industrial metro.",
   "profile": {"Headquarters": "Visakhapatnam", "Language": "Telugu, English", "Food": "Vizag Seafood, Madugula Halwa", "Crafts": "Shipbuilding, Steel production"},
   "area": "1,048 km²", "population": "1,959,544 (2011 Census)", "points": ["Headquarters of the Eastern Naval Command of the Indian Navy", "Features Dolphin's Nose lighthouse, Submarine Museum (INS Kursura), and Simhachalam temple"],
   "wiki": "https://en.wikipedia.org/wiki/Visakhapatnam_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},
]

write_data(DIST_DIR, "andhra-pradesh", ap_districts)

ap_places = [
  {"id": "venkateswara-temple-tirupati", "name": "Sri Venkateswara Swamy Temple, Tirumala", "type": "place", "parent": "tirupati",
   "path": "Sri Venkateswara Temple, Tirupati, Andhra Pradesh, India",
   "summary": "The preeminent Vaishnavite shrine atop the Seshachalam Seven Hills, world's most visited Hindu temple.",
   "points": [
     "Mentioned in early Tamil Sangam literature; gopuram gilded in pure gold by King Krishnadevaraya of Vijayanagara in 1517 CE",
     "Pallava, Chola, Pandya, and Vijayanagara imperial dynasties",
     "Dedicated to Lord Venkateswara (Lord Srinivasa/Balaji), an incarnation of Vishnu who manifested to save mankind in Kali Yuga",
     "Renowned for the GI-tagged Tirupati Laddu prasadam, Ananda Nilayam golden vimana, and massive tonsure (hair donation) tradition"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Venkateswara_Temple,_Tirumala", "source": "Tirumala Tirupati Devasthanams (TTD), Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "mallikarjuna-temple-srisailam", "name": "Mallikarjuna Swamy Temple, Srisailam", "type": "place", "parent": "nandyal",
   "path": "Mallikarjuna Temple, Nandyal, Andhra Pradesh, India",
   "summary": "Ancient sanctuary atop Nallamala Hills, uniquely revered as both one of the 12 Jyotirlingas and one of the 18 Maha Shakti Peethas.",
   "points": [
     "Inscriptions date from Satavahana (2nd century CE), Ikshvaku, and Kakatiya dynasties; modern prakaram walls built by Vijayanagara King Harihara II in 1404 CE",
     "Satavahana, Kakatiya, and Vijayanagara dynasties (also visited by Chhatrapati Shivaji in 1677 CE)",
     "Dedicated to Lord Mallikarjuna (Shiva) and Goddess Bhramaramba (Shakti)",
     "Enclosed by an enormous 20-foot granite fortress wall (Prakaram) carved with 3,200 panels of elephants, warfare, and Puranic legends"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Mallikarjuna_Temple,_Srisailam", "source": "Srisailam Devasthanam, ASI, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "lepakshi-veerabhadra-temple", "name": "Veerabhadra Temple, Lepakshi", "type": "place", "parent": "ananthapuramu",
   "path": "Veerabhadra Temple, Ananthapuramu, Andhra Pradesh, India",
   "summary": "16th-century Vijayanagara architectural wonder acclaimed for the world-famous Hanging Pillar and colossal monolithic Nandi.",
   "points": [
     "Built in 1530 CE by brothers Virupanna Nayaka and Viranna, governors under Vijayanagara Emperor Achyuta Deva Raya",
     "Vijayanagara dynasty",
     "Dedicated to Veerabhadra (fierce form of Shiva); contains 70 carved stone pillars including the engineering miracle of the Hanging Pillar",
     "Houses India's largest monolithic Nandi bull carved from a single granite boulder measuring 4.5 m high and 8.2 m long"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Veerabhadra_Temple,_Lepakshi", "source": "Archaeological Survey of India, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "simhachalam-temple", "name": "Varaha Lakshmi Narasimha Temple, Simhachalam", "type": "place", "parent": "visakhapatnam",
   "path": "Simhachalam Temple, Visakhapatnam, Andhra Pradesh, India",
   "summary": "Medieval lion-hill temple dedicated to Lord Narasimha, whose idol remains covered in sandalwood paste year-round.",
   "points": [
     "Original shrine expanded by Eastern Ganga King Langula Narasimha Deva I in the 13th century CE",
     "Eastern Ganga and Gajapati dynasties",
     "Dedicated to Varaha Narasimha; the presiding deity is covered in a continuous 2-inch coat of sandalwood paste (Chandan), revealing true form only on Akshaya Tritiya",
     "Features a 16-pillared Natya Mandapa (dancing hall) and Kappam Stambham (pillar that fulfills wishes)"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Varaha_Lakshmi_Narasimha_Temple,_Simhachalam", "source": "Simhachalam Devasthanam, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kanaka-durga-temple-vijayawada", "name": "Kanaka Durga Temple, Indrakeeladri", "type": "place", "parent": "ntr",
   "path": "Kanaka Durga Temple, NTR, Andhra Pradesh, India",
   "summary": "Ancient Swayambhu Shakti temple perched atop Indrakeeladri hill overlooking the sacred Krishna River.",
   "points": [
     "Mentioned in Mahabharata and Kalika Purana; historical fortifications developed under Chalukya and Vijayanagara rulers",
     "Eastern Chalukya and Vijayanagara dynasties",
     "Dedicated to Goddess Kanaka Durga, who manifested in glittering golden hue with eight arms to slay demon Mahishasura",
     "Epicenter of the massive 10-day Dasara festival where over one million devotees participate in Teppotsavam (boat festival)"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Kanaka_Durga_Temple", "source": "Kanaka Durga Devasthanam, Wikipedia", "updated": "2024-11", "model": ""},
]

write_data(PLACES_DIR, "andhra-pradesh", ap_places)

print("Finished generating Kerala and Andhra Pradesh data.")
