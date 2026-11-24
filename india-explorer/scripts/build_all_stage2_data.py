import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent / "backend" / "data"
DIST_DIR = BASE_DIR / "districts"
PLACES_DIR = BASE_DIR / "places"
DIST_DIR.mkdir(parents=True, exist_ok=True)
PLACES_DIR.mkdir(parents=True, exist_ok=True)

def save_json(file_path: Path, data: list):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(data)} records to {file_path.name}")

# ==========================================
# 2. TAMIL NADU (38 Districts + Temples/Places)
# ==========================================
tn_districts = [
  {"id": "ariyalur", "name": "Ariyalur", "type": "district", "parent": "tamil-nadu", "path": "Ariyalur, Tamil Nadu, India",
   "summary": "Limestone and fossil rich region, home to Rajendra Chola's imperial capital Gangaikonda Cholapuram.",
   "profile": {"Headquarters": "Ariyalur", "Language": "Tamil", "Food": "Varagu rice delicacies", "Crafts": "Limestone cement, Cashew processing"},
   "area": "1,949 km²", "population": "754,894 (2011 Census)", "points": ["Houses Gangaikonda Cholapuram UNESCO World Heritage Chola temple built in 1035 CE", "Famous for Mesozoic marine fossil beds"],
   "wiki": "https://en.wikipedia.org/wiki/Ariyalur_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "chengalpattu", "name": "Chengalpattu", "type": "district", "parent": "tamil-nadu", "path": "Chengalpattu, Tamil Nadu, India",
   "summary": "Coastal historic district boasting Mamallapuram UNESCO rock monuments and tech SEZs.",
   "profile": {"Headquarters": "Chengalpattu", "Language": "Tamil", "Food": "Chettinad snacks, Seafood", "Crafts": "Granite stone sculptures of Mamallapuram"},
   "area": "2,945 km²", "population": "2,556,244 (2011 Census)", "points": ["7th-century Pallava dynasty shore temples and rock-cut rathas at Mahabalipuram", "Automotive manufacturing corridor of Chennai"],
   "wiki": "https://en.wikipedia.org/wiki/Chengalpattu_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "chennai", "name": "Chennai", "type": "district", "parent": "tamil-nadu", "path": "Chennai, Tamil Nadu, India",
   "summary": "Gateway to South India, historic capital featuring Fort St. George, Marina Beach, and Carnatic music.",
   "profile": {"Headquarters": "Chennai", "Language": "Tamil, English", "Food": "Idli Sambhar, Filter Coffee, Murukku Sandwich", "Crafts": "Bronze idols, Leather goods"},
   "area": "426 km²", "population": "7,088,403 (2011 Census)", "points": ["Marina Beach is the second-longest urban natural beach in the world (13 km)", "Kapaleeshwarar Temple in Mylapore represents classical 7th-century Dravidian Shaivism"],
   "wiki": "https://en.wikipedia.org/wiki/Chennai_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "coimbatore", "name": "Coimbatore", "type": "district", "parent": "tamil-nadu", "path": "Coimbatore, Tamil Nadu, India",
   "summary": "The Manchester of South India, engineering capital on the Noyyal river renowned for textiles and pumps.",
   "profile": {"Headquarters": "Coimbatore", "Language": "Tamil", "Food": "Kovai Biryani, Pallipalayam chicken, Annapoorna Sambar", "Crafts": "Wet grinders, Cotton yarn, Precision engineering"},
   "area": "4,723 km²", "population": "3,458,045 (2011 Census)", "points": ["Major manufacturing center producing 50% of India's water pumps and motors", "Home to Marudhamalai Murugan temple and Adiyogi Shiva bust"],
   "wiki": "https://en.wikipedia.org/wiki/Coimbatore_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "cuddalore", "name": "Cuddalore", "type": "district", "parent": "tamil-nadu", "path": "Cuddalore, Tamil Nadu, India",
   "summary": "Coastal maritime district famed for Silver Beach, Chidambaram Nataraja Temple, and Neyveli lignite.",
   "profile": {"Headquarters": "Cuddalore", "Language": "Tamil", "Food": "Seafood curries, Cashew halwa", "Crafts": "Cashew nut processing, Ceramic pottery of Panruti"},
   "area": "3,703 km²", "population": "2,605,914 (2011 Census)", "points": ["Nataraja Temple at Chidambaram is the center of the cosmos in Hindu cosmic dance philosophy", "Neyveli Lignite Corporation operates major open-cast mines and thermal plants"],
   "wiki": "https://en.wikipedia.org/wiki/Cuddalore_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "dharmapuri", "name": "Dharmapuri", "type": "district", "parent": "tamil-nadu", "path": "Dharmapuri, Tamil Nadu, India",
   "summary": "Agricultural territory along the Kaveri river celebrated for Hogenakkal Falls and mango orchards.",
   "profile": {"Headquarters": "Dharmapuri", "Language": "Tamil", "Food": "Ragi kali, Mango dishes", "Crafts": "Sericulture, Bamboo basketry"},
   "area": "4,498 km²", "population": "1,506,843 (2011 Census)", "points": ["Hogenakkal Falls known as the 'Niagara of India' features carbonatite rocks", "One of the leading mango and sericulture producers in Tamil Nadu"],
   "wiki": "https://en.wikipedia.org/wiki/Dharmapuri_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "dindigul", "name": "Dindigul", "type": "district", "parent": "tamil-nadu", "path": "Dindigul, Tamil Nadu, India",
   "summary": "Fortress city celebrated for GI-tagged handcrafted brass locks, Dindigul Thalappakatti biryani, and Kodaikanal.",
   "profile": {"Headquarters": "Dindigul", "Language": "Tamil", "Food": "Dindigul Seeraga Samba Biryani", "Crafts": "GI-tagged Dindigul handmade iron/brass locks"},
   "area": "6,267 km²", "population": "2,159,775 (2011 Census)", "points": ["Dindigul Rock Fort constructed in the 17th century by Nayakas of Madurai", "Includes hill station Kodaikanal ('Princess of Hill Stations') in Palani Hills"],
   "wiki": "https://en.wikipedia.org/wiki/Dindigul_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "erode", "name": "Erode", "type": "district", "parent": "tamil-nadu", "path": "Erode, Tamil Nadu, India",
   "summary": "The Turmeric City (Manjal Maanagaram), premier textile market and Bhavanisagar dam region on the Bhavani River.",
   "profile": {"Headquarters": "Erode", "Language": "Tamil", "Food": "Kongu Nadu mutton chukka, Ragi kali", "Crafts": "GI-tagged Erode Turmeric, Bhavani Jamakkalam carpets"},
   "area": "5,722 km²", "population": "2,251,744 (2011 Census)", "points": ["Major turmeric trading terminal in India with GI certification for Erode turmeric", "Birthplace of rationalist social reformer Periyar E. V. Ramasamy and mathematician Ramanujan"],
   "wiki": "https://en.wikipedia.org/wiki/Erode_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kanchipuram", "name": "Kanchipuram", "type": "district", "parent": "tamil-nadu", "path": "Kanchipuram, Tamil Nadu, India",
   "summary": "The City of Thousand Temples and Silk, ancient capital of the Pallava dynasty and center of Vedantic philosophy.",
   "profile": {"Headquarters": "Kanchipuram", "Language": "Tamil", "Food": "Kanchipuram Idli (spiced steamed in Mandharai leaf)", "Crafts": "GI-tagged Kanchipuram pure mulberry silk sarees with heavy zari"},
   "area": "1,704 km²", "population": "1,166,401 (2011 Census)", "points": ["Capital of the Pallava Empire from 4th to 9th century CE", "Home to Kailasanathar Temple, Ekambareswarar Temple, and Varadharaja Perumal Temple"],
   "wiki": "https://en.wikipedia.org/wiki/Kanchipuram_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kanyakumari", "name": "Kanyakumari", "type": "district", "parent": "tamil-nadu", "path": "Kanyakumari, Tamil Nadu, India",
   "summary": "Southernmost tip of the Indian mainland (Cape Comorin), confluence of Arabian Sea, Indian Ocean, and Bay of Bengal.",
   "profile": {"Headquarters": "Nagercoil", "Language": "Tamil, Malayalam", "Food": "Nanjil Nadu fish curry, Pazham pori, Ulundhu kali", "Crafts": "Sea shell crafts, Banana fibre weaving"},
   "area": "1,672 km²", "population": "1,870,374 (2011 Census)", "points": ["Features Vivekananda Rock Memorial and 133-foot stone statue of Tamil poet-philosopher Thiruvalluvar", "Unique geographical site where one can witness both sunrise and sunset over the ocean"],
   "wiki": "https://en.wikipedia.org/wiki/Kanyakumari_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "karur", "name": "Karur", "type": "district", "parent": "tamil-nadu", "path": "Karur, Tamil Nadu, India",
   "summary": "Textile export hub on the Amaravathi and Kaveri rivers, ancient Chera inland capital vanji.",
   "profile": {"Headquarters": "Karur", "Language": "Tamil", "Food": "Karur biryani, Kaveri fish curry", "Crafts": "Home textiles (bed linen, towels, table mats)"},
   "area": "2,896 km²", "population": "1,064,493 (2011 Census)", "points": ["Major global export cluster for home textiles to USA and Europe", "Pasupatheeswarar Temple showcases early Chola stone architecture"],
   "wiki": "https://en.wikipedia.org/wiki/Karur_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "krishnagiri", "name": "Krishnagiri", "type": "district", "parent": "tamil-nadu", "path": "Krishnagiri, Tamil Nadu, India",
   "summary": "Mango capital and electronic hardware manufacturing hub bordering Karnataka, featuring historic Krishnagiri Fort.",
   "profile": {"Headquarters": "Krishnagiri", "Language": "Tamil, Telugu, Kannada", "Food": "Mango pulp, Ragi kali", "Crafts": "Mango processing, Granite monuments"},
   "area": "5,143 km²", "population": "1,879,809 (2011 Census)", "points": ["Produces over 300,000 tonnes of mangoes annually, exporting mango pulp worldwide", "Hosur industrial estate hosts major electric vehicle and auto manufacturers"],
   "wiki": "https://en.wikipedia.org/wiki/Krishnagiri_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "madurai", "name": "Madurai", "type": "district", "parent": "tamil-nadu", "path": "Madurai, Tamil Nadu, India",
   "summary": "The Athens of the East and Temple City on the Vaigai river, celebrated for Meenakshi Sundareswarar Temple.",
   "profile": {"Headquarters": "Madurai", "Language": "Tamil", "Food": "Jigarthanda, Kari Dosa, Madurai Idli, Bun Parotta", "Crafts": "Madurai Sungudi sarees, Jasmine (Malli) flower cultivation"},
   "area": "3,741 km²", "population": "3,038,252 (2011 Census)", "points": ["Ancient capital of the Pandya dynasty and site of all three historic Tamil Sangams", "Meenakshi Amman Temple features 14 majestic soaring gopurams with over 33,000 sculptures"],
   "wiki": "https://en.wikipedia.org/wiki/Madurai_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "nagapattinam", "name": "Nagapattinam", "type": "district", "parent": "tamil-nadu", "path": "Nagapattinam, Tamil Nadu, India",
   "summary": "Coastal seaport district on the Bay of Bengal, spiritual center of Velankanni Basilica and Nagore Dargah.",
   "profile": {"Headquarters": "Nagapattinam", "Language": "Tamil", "Food": "Coastal fish curries, Nandu (crab) roast", "Crafts": "Marine fishing, Salt manufacturing"},
   "area": "1,397 km²", "population": "697,069 (2011 Census)", "points": ["Chola medieval international port linking Sri Lanka, Java, and China", "Basilica of Our Lady of Good Health at Velankanni is called the 'Lourdes of the East'"],
   "wiki": "https://en.wikipedia.org/wiki/Nagapattinam_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "namakkal", "name": "Namakkal", "type": "district", "parent": "tamil-nadu", "path": "Namakkal, Tamil Nadu, India",
   "summary": "Egg City and Transport City of South India, built around the single monolithic rock fort of Namakkal Anjaneyar.",
   "profile": {"Headquarters": "Namakkal", "Language": "Tamil", "Food": "Egg curry specialties, Kongu dishes", "Crafts": "Poultry farming, Lorry body building"},
   "area": "3,368 km²", "population": "1,726,601 (2011 Census)", "points": ["Produces over 30 million eggs daily, catering to national mid-day meal schemes", "Namakkal Anjaneyar Temple features an 18-foot open-air monolithic idol of Lord Hanuman"],
   "wiki": "https://en.wikipedia.org/wiki/Namakkal_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "nilgiris", "name": "The Nilgiris", "type": "district", "parent": "tamil-nadu", "path": "The Nilgiris, Tamil Nadu, India",
   "summary": "Blue Mountains of the Western Ghats, celebrated for Nilgiri Orthodox black tea, Ooty hill station, and Toda tribes.",
   "profile": {"Headquarters": "Udhagamandalam (Ooty)", "Language": "Tamil, Badaga, Toda, Kota, English", "Food": "Nilgiri tea, Homemade chocolates, Varkey pastry", "Crafts": "GI-tagged Toda tribal geometric embroidery, Nilgiri tea processing"},
   "area": "2,565 km²", "population": "735,394 (2011 Census)", "points": ["Nilgiri Mountain Railway (built 1908) is a UNESCO World Heritage rack-and-pinion steam railway", "Doddabetta peak rises to 2,637 m as the highest summit in the Nilgiris"],
   "wiki": "https://en.wikipedia.org/wiki/Nilgiris_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "ramanathapuram", "name": "Ramanathapuram", "type": "district", "parent": "tamil-nadu", "path": "Ramanathapuram, Tamil Nadu, India",
   "summary": "Island district containing sacred Rameswaram Jyotirlinga, Pamban sea bridge, and birthplace of Dr. A. P. J. Abdul Kalam.",
   "profile": {"Headquarters": "Ramanathapuram", "Language": "Tamil", "Food": "Rameswaram fish curry, Palmyra sweets", "Crafts": "Chank shell carving, Palm leaf basketry"},
   "area": "4,104 km²", "population": "1,353,445 (2011 Census)", "points": ["Ramanathaswamy Temple features the longest corridor in any Hindu temple (1,220 m) with 1,212 pillars", "Pamban Bridge constructed in 1914 was India's first cantilever sea bridge"],
   "wiki": "https://en.wikipedia.org/wiki/Ramanathapuram_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "salem", "name": "Salem", "type": "district", "parent": "tamil-nadu", "path": "Salem, Tamil Nadu, India",
   "summary": "The Steel and Mango City surrounded by hills, famed for Salem Steel Plant, Malgova mangoes, and sago production.",
   "profile": {"Headquarters": "Salem", "Language": "Tamil", "Food": "Salem Thattu Vadai Set, Malgova mango", "Crafts": "Sago (Sabudana) processing, Silk and venpattu handlooms"},
   "area": "5,245 km²", "population": "3,482,056 (2011 Census)", "points": ["Supplies over 70% of India's sago and tapioca starch through SAGOSERVE", "Yercaud hill station sits amidst coffee and orange groves in the Shevaroy Hills"],
   "wiki": "https://en.wikipedia.org/wiki/Salem_district,_India", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "thanjavur", "name": "Thanjavur", "type": "district", "parent": "tamil-nadu", "path": "Thanjavur, Tamil Nadu, India",
   "summary": "Rice Bowl of Tamil Nadu on the Kaveri delta, capital of the Chola Empire, home to Brihadisvara Temple.",
   "profile": {"Headquarters": "Thanjavur", "Language": "Tamil", "Food": "Thanjavur Ashoka halwa, Kaveri meals", "Crafts": "GI-tagged Thanjavur gold leaf paintings, Thanjavur Bobblehead dancing dolls, Art plates"},
   "area": "3,411 km²", "population": "2,405,890 (2011 Census)", "points": ["Brihadisvara Temple built in 1010 CE by Emperor Rajaraja Chola I, UNESCO World Heritage site", "Saraswathi Mahal Library founded in the 16th century preserves rare palm-leaf manuscripts"],
   "wiki": "https://en.wikipedia.org/wiki/Thanjavur_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "tiruchirappalli", "name": "Tiruchirappalli", "type": "district", "parent": "tamil-nadu", "path": "Tiruchirappalli, Tamil Nadu, India",
   "summary": "Historic delta city on the Kaveri river, renowned for the Rockfort Temple and the colossal Sri Ranganathaswamy Temple at Srirangam.",
   "profile": {"Headquarters": "Tiruchirappalli", "Language": "Tamil", "Food": "Trichy Halwa, Banana leaf meals", "Crafts": "Synthetic diamond cutting, BHEL boiler manufacturing"},
   "area": "4,403 km²", "population": "2,722,290 (2011 Census)", "points": ["Sri Ranganathaswamy Temple in Srirangam is the largest functioning Hindu temple complex in the world (156 acres)", "Rockfort Temple sits perched atop an ancient 3.8-billion-year-old quartz rock formation"],
   "wiki": "https://en.wikipedia.org/wiki/Tiruchirappalli_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "tirunelveli", "name": "Tirunelveli", "type": "district", "parent": "tamil-nadu", "path": "Tirunelveli, Tamil Nadu, India",
   "summary": "City of Halwa on the perennial Thamirabarani River, famed for Nellaiappar Temple and Courtallam waterfalls.",
   "profile": {"Headquarters": "Tirunelveli", "Language": "Tamil", "Food": "GI-tagged Tirunelveli wheat Halwa, Sodhi kuzhambu", "Crafts": "Pattamadai pai (reed mats), Brass lamps"},
   "area": "3,914 km²", "population": "1,665,253 (2011 Census)", "points": ["Nellaiappar Temple built in 7th century CE features famous musical stone pillars", "Thamirabarani is the only perennial river flowing entirely within Tamil Nadu"],
   "wiki": "https://en.wikipedia.org/wiki/Tirunelveli_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "tiruvannamalai", "name": "Tiruvannamalai", "type": "district", "parent": "tamil-nadu", "path": "Tiruvannamalai, Tamil Nadu, India",
   "summary": "Spiritual center of Agni (Fire) element, famed for Annamalaiyar Temple, Giri Valam circumambulation, and Ramana Maharshi ashram.",
   "profile": {"Headquarters": "Tiruvannamalai", "Language": "Tamil", "Food": "Makkan Peda of Arani, Millet porridge", "Crafts": "Arani silk sarees, Brass idols"},
   "area": "6,188 km²", "population": "2,464,875 (2011 Census)", "points": ["Annamalaiyar Temple is one of the Pancha Bhoota Stalas representing the element Fire", "Millions participate in monthly 14 km Giri Valam walk barefoot around Mount Arunachala"],
   "wiki": "https://en.wikipedia.org/wiki/Tiruvannamalai_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "vellore", "name": "Vellore", "type": "district", "parent": "tamil-nadu", "path": "Vellore, Tamil Nadu, India",
   "summary": "Fort city and medical hub on the Palar river, celebrated for Vellore Sepoy Mutiny of 1806 and CMC Hospital.",
   "profile": {"Headquarters": "Vellore", "Language": "Tamil", "Food": "Ambur Dum Biryani, Vellore Boti curry", "Crafts": "Leather tanning and footwear exports"},
   "area": "2,036 km²", "population": "1,614,242 (2011 Census)", "points": ["Vellore Fort (built 16th century by Vijayanagara rulers) features double granite moat walls", "Vellore Mutiny on 10 July 1806 was the earliest major military uprising against British rule"],
   "wiki": "https://en.wikipedia.org/wiki/Vellore_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},
]

save_json(DIST_DIR / "tamil-nadu.json", tn_districts)

tn_places = [
  {"id": "brihadisvara-temple-thanjavur", "name": "Brihadisvara Temple (Peruvudaiyar Kovil), Thanjavur", "type": "place", "parent": "thanjavur",
   "path": "Brihadisvara Temple, Thanjavur, Tamil Nadu, India",
   "summary": "Great Living Chola Temple built entirely of granite, celebrating over 1,000 years of Dravidian architectural mastery.",
   "points": [
     "Commissioned by Emperor Rajaraja Chola I, completed in 1010 CE to celebrate his imperial victories",
     "Chola dynasty; designated a UNESCO World Heritage Site in 1987",
     "Dedicated to Lord Shiva (Peruvudaiyar); features a 66-meter Vimana tower built without binding mortar",
     "The capstone (Kumbam) weighing approximately 80 tonnes was hoisted to the summit using a 6-km inclined earthen ramp"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Brihadisvara_Temple", "source": "Archaeological Survey of India, UNESCO, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "meenakshi-amman-temple-madurai", "name": "Meenakshi Sundareswarar Temple, Madurai", "type": "place", "parent": "madurai",
   "path": "Meenakshi Amman Temple, Madurai, Tamil Nadu, India",
   "summary": "Historic heart of Madurai on the Vaigai river, acclaimed for 14 polychrome gopurams and Hall of Thousand Pillars.",
   "points": [
     "Originally established during ancient Sangam era; current monumental structure rebuilt by King Vishwanatha Nayak and expanded by Thirumalai Nayak in 16th–17th century",
     "Pandya and Madurai Nayak dynasties",
     "Dedicated to Goddess Meenakshi (manifestation of Parvati) and her consort Sundareswarar (Shiva)",
     "Encompasses the Hall of Thousand Pillars (Aayiram Kaal Mandapam) displaying 985 exquisitely sculpted granite pillars"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Meenakshi_Temple", "source": "Madurai Temple Board, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "ramanathaswamy-temple-rameswaram", "name": "Ramanathaswamy Temple, Rameswaram", "type": "place", "parent": "ramanathapuram",
   "path": "Ramanathaswamy Temple, Ramanathapuram, Tamil Nadu, India",
   "summary": "Sacred Jyotirlinga island temple on Pamban Island, revered for the world's longest pillared temple corridors and 22 theerthams.",
   "points": [
     "Expanded significantly in the 12th century CE by Sri Lankan King Parakramabahu I and Sethupathi rulers of Ramanathapuram in the 17th century",
     "Pandya, Jaffna, and Sethupathi dynasties",
     "One of the 12 holy Jyotirlingas; according to the Ramayana, Lord Rama consecrated this Shiva Lingam before crossing to Lanka",
     "Renowned for its outer corridor measuring 1,220 meters in perimeter with 1,212 intricately carved sandstone pillars"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Ramanathaswamy_Temple", "source": "Hindu Religious & Charitable Endowments, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "shore-temple-mahabalipuram", "name": "Shore Temple, Mahabalipuram", "type": "place", "parent": "chengalpattu",
   "path": "Shore Temple, Chengalpattu, Tamil Nadu, India",
   "summary": "8th-century structural stone temple overlooking the Bay of Bengal, iconic Pallava monument on the UNESCO list.",
   "points": [
     "Constructed between 700 and 728 CE by King Narasimhavarman II (Rajasimha) of the Pallava dynasty",
     "Pallava dynasty; inscribed on the UNESCO World Heritage list in 1984",
     "One of the earliest structural stone temples of Southern India, combining shrines for Lord Shiva and reclining Vishnu",
     "Withstood severe coastal weathering and the December 2004 Indian Ocean tsunami due to resilient granite block masonry"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Shore_Temple", "source": "Archaeological Survey of India, UNESCO, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "sri-ranganathaswamy-temple-srirangam", "name": "Sri Ranganathaswamy Temple, Srirangam", "type": "place", "parent": "tiruchirappalli",
   "path": "Sri Ranganathaswamy Temple, Tiruchirappalli, Tamil Nadu, India",
   "summary": "The foremost of the 108 Divya Desams, sprawling across 156 acres enclosed by seven concentric walled prakaras.",
   "points": [
     "Epigraphic records date from 10th century Chola period; heavily patronized and fortified by Pandya, Hoysala, and Vijayanagara emperors",
     "Chola, Pandya, Hoysala, and Vijayanagara dynasties",
     "Dedicated to Ranganatha, a reclining form of Lord Vishnu, situated on an island formed by rivers Kaveri and Kollidam",
     "Features 21 magnificent gopurams, including the southern Rajagopuram rising 73 meters (239 ft), the second tallest in Asia"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Ranganathaswamy_Temple,_Srirangam", "source": "Archaeological Survey of India, UNESCO Tentative List, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kapaleeshwarar-temple-chennai", "name": "Kapaleeshwarar Temple, Mylapore", "type": "place", "parent": "chennai",
   "path": "Kapaleeshwarar Temple, Chennai, Tamil Nadu, India",
   "summary": "Classical Dravidian Shaivite temple in Mylapore featuring a vibrant 37-meter rainbow gopuram and sacred temple tank.",
   "points": [
     "Original 7th-century Pallava coastal shrine praised by Nayanars; relocated and reconstructed in present location by Vijayanagara Tuluva kings in the 16th century",
     "Pallava and Vijayanagara dynasties",
     "Dedicated to Lord Shiva (Kapaleeshwarar) and Goddess Parvati (Karpagambal, 'Goddess of the Wish-Yielding Tree')",
     "Legend records Goddess Parvati worshipped Lord Shiva in the form of a peacock (Mayil), giving Mylapore its name"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Kapaleeshwarar_Temple", "source": "HR&CE Tamil Nadu, Wikipedia", "updated": "2024-11", "model": ""},
]

save_json(PLACES_DIR / "tamil-nadu.json", tn_places)

print("Tamil Nadu Data generated.")
