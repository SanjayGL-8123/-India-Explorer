import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent / "backend" / "data"
DIST_DIR = BASE_DIR / "districts"
PLACES_DIR = BASE_DIR / "places"
DIST_DIR.mkdir(parents=True, exist_ok=True)
PLACES_DIR.mkdir(parents=True, exist_ok=True)

# Helper to write JSON files cleanly
def save_json(file_path: Path, data: list):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(data)} items to {file_path.name}")

# ==========================================
# 1. KARNATAKA DISTRICTS (All 31)
# ==========================================
karnataka_districts = [
  {"id": "bagalkote", "name": "Bagalkote", "type": "district", "parent": "karnataka", "path": "Bagalkote, Karnataka, India",
   "summary": "Historic district famed for Badami cave temples, Pattadakal UNESCO monuments, and Ilkal sarees.",
   "profile": {"Headquarters": "Bagalkote", "Language": "Kannada", "Food": "Jolada Rotti, Shenga Chutney", "Crafts": "Ilkal sarees, Guledgudda Khana fabrics"},
   "area": "6,575 km²", "population": "1,889,752 (2011 Census)",
   "points": ["Cradle of early Chalukyan rock-cut architecture at Badami, Aihole, and Pattadakal", "Prominent center of North Karnataka handloom textile clusters"],
   "wiki": "https://en.wikipedia.org/wiki/Bagalkote_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "ballari", "name": "Ballari", "type": "district", "parent": "karnataka", "path": "Ballari, Karnataka, India",
   "summary": "Mining and industrial hub known for historic Ballari Fort atop the massive monolithic rock.",
   "profile": {"Headquarters": "Ballari", "Language": "Kannada, Telugu", "Food": "Manda sweet, Bellary Biryani", "Crafts": "Jeans apparel manufacturing"},
   "area": "4,252 km²", "population": "1,400,970 (2011 Census)",
   "points": ["Ballari Fort built by Hanumappa Nayaka and later fortified by French engineers for Hyder Ali", "Major center of iron ore mining and garment production in South India"],
   "wiki": "https://en.wikipedia.org/wiki/Bellary_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "belagavi", "name": "Belagavi", "type": "district", "parent": "karnataka", "path": "Belagavi, Karnataka, India",
   "summary": "Sugar capital and commercial crossroad bordering Goa and Maharashtra, famed for Belagavi Kunda.",
   "profile": {"Headquarters": "Belagavi", "Language": "Kannada, Marathi", "Food": "Belagavi Kunda, Gokak Karadantu", "Crafts": "Brass and copper utensils, Shahapur sarees"},
   "area": "13,415 km²", "population": "4,779,661 (2011 Census)",
   "points": ["Second legislative capital of Karnataka hosting the winter assembly session at Suvarna Vidhana Soudha", "Belagavi Fort dates back to Ratta dynasty in 1204 CE"],
   "wiki": "https://en.wikipedia.org/wiki/Belagavi_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "bengaluru-rural", "name": "Bengaluru Rural", "type": "district", "parent": "karnataka", "path": "Bengaluru Rural, Karnataka, India",
   "summary": "Agricultural and poultry belt surrounding the tech metropolis, home to Kempegowda International Airport.",
   "profile": {"Headquarters": "Bengaluru", "Language": "Kannada", "Food": "Ragi Mudde, Soppina Saaru", "Crafts": "Silk worm rearing, Handloom weaving"},
   "area": "2,298 km²", "population": "990,923 (2011 Census)",
   "points": ["Encompasses Devanahalli Fort, the birthplace of 18th-century ruler Tipu Sultan", "Major floriculture, dairy, and silk cocoon production region"],
   "wiki": "https://en.wikipedia.org/wiki/Bangalore_Rural_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "bengaluru-urban", "name": "Bengaluru Urban", "type": "district", "parent": "karnataka", "path": "Bengaluru Urban, Karnataka, India",
   "summary": "Silicon Valley of India, premier center for global information technology, aerospace, and startup innovation.",
   "profile": {"Headquarters": "Bengaluru", "Language": "Kannada, English", "Food": "Benne Masala Dosa, Filter Coffee, Kesari Bath", "Crafts": "Mysore silk showroom weaving, Sandalwood products"},
   "area": "2,196 km²", "population": "9,621,551 (2011 Census)",
   "points": ["Founded in 1537 by chieftain Kempe Gowda I who built a mud fort", "Headquarters of ISRO, Infosys, Wipro, and over 400 multinational R&D tech centers"],
   "wiki": "https://en.wikipedia.org/wiki/Bangalore_Urban_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "bidar", "name": "Bidar", "type": "district", "parent": "karnataka", "path": "Bidar, Karnataka, India",
   "summary": "Crown city of Karnataka, medieval capital of Bahmani and Barid Shahi sultanates, famed for Bidriware.",
   "profile": {"Headquarters": "Bidar", "Language": "Kannada, Urdu", "Food": "Biryani, Shirmal, Chana dal halwa", "Crafts": "GI-tagged Bidriware silver inlay on blackened zinc alloy"},
   "area": "5,448 km²", "population": "1,703,300 (2011 Census)",
   "points": ["Bidar Fort built in 1428 CE by Ahmad Shah Wali Bahmani with 30 bastions", "Houses Mahmud Gawan Madrasa, 15th-century Islamic university with Persian minarets"],
   "wiki": "https://en.wikipedia.org/wiki/Bidar_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "chamarajanagar", "name": "Chamarajanagar", "type": "district", "parent": "karnataka", "path": "Chamarajanagar, Karnataka, India",
   "summary": "Southern borderland where Western and Eastern Ghats meet, famous for Bandipur Tiger Reserve and wild silk.",
   "profile": {"Headquarters": "Chamarajanagar", "Language": "Kannada", "Food": "Ragi Mudde, Country Chicken curry", "Crafts": "Raw silk production, Bamboo craft"},
   "area": "5,101 km²", "population": "1,020,791 (2011 Census)",
   "points": ["Bandipur National Park forms a key component of the Nilgiri Biosphere Reserve", "Named after Chamaraja Wadiyar IX, 18th-century Maharaja of Mysore who was born here"],
   "wiki": "https://en.wikipedia.org/wiki/Chamarajanagar_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "chikkaballapura", "name": "Chikkaballapura", "type": "district", "parent": "karnataka", "path": "Chikkaballapura, Karnataka, India",
   "summary": "Hilly terrain featuring scenic Nandi Hills, grape vineyards, and Muddenahalli, birthplace of Sir M. Visvesvaraya.",
   "profile": {"Headquarters": "Chikkaballapura", "Language": "Kannada, Telugu", "Food": "Ragi Rotti, Grape jams", "Crafts": "Mulberry silk cultivation, Incense agarbatti"},
   "area": "4,244 km²", "population": "1,255,104 (2011 Census)",
   "points": ["Nandi Hills was summer retreat of Tipu Sultan and British administrators", "Birthplace of Bharat Ratna engineer-statesman Sir M. Visvesvaraya in Muddenahalli"],
   "wiki": "https://en.wikipedia.org/wiki/Chikkaballapura_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "chikkamagaluru", "name": "Chikkamagaluru", "type": "district", "parent": "karnataka", "path": "Chikkamagaluru, Karnataka, India",
   "summary": "Cradle of Indian coffee nestled in the Western Ghats under Mullayanagiri, Karnataka's highest peak.",
   "profile": {"Headquarters": "Chikkamagaluru", "Language": "Kannada", "Food": "Akki Rotti, Halasina Hannu delicacies", "Crafts": "Coffee processing, Wood carving"},
   "area": "7,201 km²", "population": "1,137,961 (2011 Census)",
   "points": ["Sufi saint Baba Budan smuggled seven raw coffee beans from Yemen and planted them here in 1670 CE", "Mullayanagiri peak rises to 1,930 m above sea level"],
   "wiki": "https://en.wikipedia.org/wiki/Chikkamagaluru_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "chitradurga", "name": "Chitradurga", "type": "district", "parent": "karnataka", "path": "Chitradurga, Karnataka, India",
   "summary": "Historic granite fortress city celebrated for the seven-walled Chitradurga Fort and heroic legend of Onake Obavva.",
   "profile": {"Headquarters": "Chitradurga", "Language": "Kannada", "Food": "Jolada Rotti, Groundnut chutney", "Crafts": "Cotton ginning, Stone masonry"},
   "area": "8,440 km²", "population": "1,659,456 (2011 Census)",
   "points": ["Chitradurga Fort (Kallina Kote) built by Nayaka palegars features seven concentric fortification walls", "Legendary heroine Onake Obavva single-handedly defended a secret passage against invading troops"],
   "wiki": "https://en.wikipedia.org/wiki/Chitradurga_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "dakshina-kannada", "name": "Dakshina Kannada", "type": "district", "parent": "karnataka", "path": "Dakshina Kannada, Karnataka, India",
   "summary": "Coastal economic capital centered at Mangaluru, cradle of Indian private banking, Yakshagana, and coastal seafood.",
   "profile": {"Headquarters": "Mangaluru", "Language": "Tulu, Kannada, Konkani, Beary", "Food": "Neer Dosa, Kori Rotti, Mangalore Buns, Ghee Roast", "Crafts": "Cashew nut processing, Coastal boat building"},
   "area": "4,560 km²", "population": "2,089,649 (2011 Census)",
   "points": ["New Mangalore Port is Karnataka's only major sea port handling maritime container cargo", "Birthplace of major Indian commercial banks including Canara Bank, Syndicate Bank, and Corporation Bank"],
   "wiki": "https://en.wikipedia.org/wiki/Dakshina_Kannada", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "davanagere", "name": "Davanagere", "type": "district", "parent": "karnataka", "path": "Davanagere, Karnataka, India",
   "summary": "The Manchester of Karnataka, renowned for historical cotton spinning mills and crisp Davanagere Benne Dosa.",
   "profile": {"Headquarters": "Davanagere", "Language": "Kannada", "Food": "Davanagere Benne Dosa, Kara Mandakki", "Crafts": "Cotton textile weaving, Sugar processing"},
   "area": "5,924 km²", "population": "1,945,497 (2011 Census)",
   "points": ["Flourished under Haider Ali and became a premier cotton textile and trading mart on the Tungabhadra River", "Famous for GI-tagged Davanagere Benne Dosa prepared on firewood iron griddles"],
   "wiki": "https://en.wikipedia.org/wiki/Davanagere_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "dharwad", "name": "Dharwad", "type": "district", "parent": "karnataka", "path": "Dharwad, Karnataka, India",
   "summary": "Cultural hub of Hindustani classical music, literary capital of Kannada Renaissance, and home to Dharwad Peda.",
   "profile": {"Headquarters": "Dharwad", "Language": "Kannada", "Food": "Dharwad Peda, Jolada Rotti Oota", "Crafts": "Kasuti traditional embroidery, Navalur handloom"},
   "area": "4,260 km²", "population": "1,847,023 (2011 Census)",
   "points": ["Nurtured musical giants: Mallikarjun Mansur, Bhimsen Joshi, and Gangubai Hangal", "GI-tagged Dharwad Peda crafted from caramelized Dharwadi buffalo milk since the 19th century"],
   "wiki": "https://en.wikipedia.org/wiki/Dharwad_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "gadag", "name": "Gadag", "type": "district", "parent": "karnataka", "path": "Gadag, Karnataka, India",
   "summary": "Heart of Western Chalukya temple architecture, home to the historic Veeranarayana Temple and printing presses.",
   "profile": {"Headquarters": "Gadag-Betageri", "Language": "Kannada", "Food": "Girmit, Mirchi Bajji, Jolada Rotti", "Crafts": "Handloom weaving of Betageri, Wind turbine generation"},
   "area": "4,656 km²", "population": "1,064,570 (2011 Census)",
   "points": ["Kalyani Chalukyas developed the distinctive Gadag architectural style in 11th–12th century temples", "Poet Kumaravyasa composed the monumental Kannada Mahabharata (Gadugina Bharata) inside Veeranarayana Temple"],
   "wiki": "https://en.wikipedia.org/wiki/Gadag_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "hassan", "name": "Hassan", "type": "district", "parent": "karnataka", "path": "Hassan, Karnataka, India",
   "summary": "Architectural wonderland of Hoysala temples at Belur and Halebidu, and colossal monolithic Gommateshwara.",
   "profile": {"Headquarters": "Hassan", "Language": "Kannada", "Food": "Ragi Mudde, Nati Koli Saaru", "Crafts": "Soapstone stone carving, Coffee processing"},
   "area": "6,814 km²", "population": "1,776,421 (2011 Census)",
   "points": ["Hoysala sacred ensembles at Belur and Halebidu inscribed on UNESCO World Heritage list in 2023", "Shravanabelagola features 57-foot Gommateshwara monolith erected in 981 CE by Ganga minister Chavundaraya"],
   "wiki": "https://en.wikipedia.org/wiki/Hassan_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "haveri", "name": "Haveri", "type": "district", "parent": "karnataka", "path": "Haveri, Karnataka, India",
   "summary": "Agricultural hub celebrated for fiery red Byadagi chillies, cardamoms, and historic Chalukyan shrines.",
   "profile": {"Headquarters": "Haveri", "Language": "Kannada", "Food": "Byadagi chilli spiced gravies, Jolada Rotti", "Crafts": "Byadagi chilli spice trading, Cardamom garland making"},
   "area": "4,823 km²", "population": "1,597,668 (2011 Census)",
   "points": ["Byadagi chilli market is Asia's second-largest chilli market, known for deep red color and low pungency", "Birthplace of famous saint-philosophers Kanakadasa (Bada) and Sarvajna (Abalur)"],
   "wiki": "https://en.wikipedia.org/wiki/Haveri_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kalaburagi", "name": "Kalaburagi", "type": "district", "parent": "karnataka", "path": "Kalaburagi, Karnataka, India",
   "summary": "Historic medieval capital of Bahmani Sultanate, center of Sufism at Khwaja Bande Nawaz Dargah, and pulse capital.",
   "profile": {"Headquarters": "Kalaburagi", "Language": "Kannada, Urdu", "Food": "Tahari, Jolada Rotti, Shenga Chutney", "Crafts": "Red gram (Toor dal) processing, Shahabad limestone tiles"},
   "area": "10,951 km²", "population": "2,566,326 (2011 Census)",
   "points": ["Gulbarga Fort built in 1347 CE houses the unique Jama Masjid built entirely with covered domed roofs", "GI-tagged Kalaburagi Red Gram (Toor Dal) supplies major protein across southern India"],
   "wiki": "https://en.wikipedia.org/wiki/Gulbarga_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kodagu", "name": "Kodagu", "type": "district", "parent": "karnataka", "path": "Kodagu, Karnataka, India",
   "summary": "Scotland of India, misty highlands along the Western Ghats famed for Arabica coffee, pepper, and martial Kodava culture.",
   "profile": {"Headquarters": "Madikeri", "Language": "Kodava, Kannada", "Food": "Pandi Curry, Kadambuttu, Akki Rotti, Bamboo Shoot fry", "Crafts": "Coorg honey, Spices, Traditional Peeche Kathi silver daggers"},
   "area": "4,102 km²", "population": "554,519 (2011 Census)",
   "points": ["Origin of sacred river Kaveri at Talakaveri in the Brahmagiri hills", "Birthplace of Field Marshal K. M. Cariappa, first Indian Commander-in-Chief of Indian Army"],
   "wiki": "https://en.wikipedia.org/wiki/Kodagu_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "kolar", "name": "Kolar", "type": "district", "parent": "karnataka", "path": "Kolar, Karnataka, India",
   "summary": "Land of Golden Fields (KGF), silk cocoon markets, and the premier tomato wholesale trade hub of South India.",
   "profile": {"Headquarters": "Kolar", "Language": "Kannada, Telugu", "Food": "Ragi Mudde, Kolar Benne Saaru", "Crafts": "Raw silk processing, Tomato wholesale trade"},
   "area": "3,969 km²", "population": "1,536,401 (2011 Census)",
   "points": ["Kolar Gold Fields (KGF) was one of the deepest and oldest gold mines in the world, operational for over a century", "Someshwara Temple showcases ornate 14th-century Vijayanagara Dravidian architecture"],
   "wiki": "https://en.wikipedia.org/wiki/Kolar_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "koppal", "name": "Koppal", "type": "district", "parent": "karnataka", "path": "Koppal, Karnataka, India",
   "summary": "Historical gateway to Vijayanagara kingdom, internationally famous for traditional Kinhal painted wooden toys.",
   "profile": {"Headquarters": "Koppal", "Language": "Kannada", "Food": "Jolada Rotti, Sajje Rotti", "Crafts": "GI-tagged Kinhal painted woodcraft, Handloom weaving"},
   "area": "7,189 km²", "population": "1,389,920 (2011 Census)",
   "points": ["GI-tagged Kinhal toys crafted by Chitragar community using light wood and liquid gold foil since Vijayanagara times", "Mahadeva Temple at Itagi hailed as Devalaya Chakravarti (Emperor among temples) by Western Chalukyas"],
   "wiki": "https://en.wikipedia.org/wiki/Koppal_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "mandya", "name": "Mandya", "type": "district", "parent": "karnataka", "path": "Mandya, Karnataka, India",
   "summary": "Sugar Bowl of Karnataka on the fertile Kaveri basin, celebrated for Krishna Raja Sagara Dam and Maddur Vada.",
   "profile": {"Headquarters": "Mandya", "Language": "Kannada", "Food": "Maddur Vada, Ragi Mudde with Nati Koli, Jaggery", "Crafts": "Organic sugarcane jaggery processing"},
   "area": "4,961 km²", "population": "1,805,769 (2011 Census)",
   "points": ["Irrigated by the Krishna Raja Sagara (KRS) Dam constructed under Sir M. Visvesvaraya in 1932", "Historic island town of Srirangapatna served as capital of Tipu Sultan and Hyder Ali"],
   "wiki": "https://en.wikipedia.org/wiki/Mandya_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "mysuru", "name": "Mysuru", "type": "district", "parent": "karnataka", "path": "Mysuru, Karnataka, India",
   "summary": "The Heritage City of palaces, royal Wadiyar dynasty, Mysore Dasara, fragrant sandalwood, and Mysore silk.",
   "profile": {"Headquarters": "Mysuru", "Language": "Kannada", "Food": "Mysore Pak, Mysore Masala Dosa, Mylari Dosa", "Crafts": "Mysore silk sarees, Sandalwood carving, Rosewood inlay with ivory/acrylic"},
   "area": "6,854 km²", "population": "3,001,127 (2011 Census)",
   "points": ["Mysore Palace is one of India's most visited royal palaces, illuminated by 97,000 bulbs on festivals", "Dasara festival celebrated with grand Jumboo Savari elephant procession since 1610 CE"],
   "wiki": "https://en.wikipedia.org/wiki/Mysore_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "raichur", "name": "Raichur", "type": "district", "parent": "karnataka", "path": "Raichur, Karnataka, India",
   "summary": "Doab territory between Krishna and Tungabhadra rivers, famous for Raichur Thermal Power Station and Sona Masuri rice.",
   "profile": {"Headquarters": "Raichur", "Language": "Kannada", "Food": "Jolada Rotti, Sona Masuri rice delicacies", "Crafts": "Rice milling, Cotton processing"},
   "area": "8,424 km²", "population": "1,928,812 (2011 Census)",
   "points": ["Raichur Doab contested bitterly between Vijayanagara Empire and Bahmani Sultanate for its agricultural wealth", "Raichur Fort features massive stone blocks fitted without mortar in 1294 CE"],
   "wiki": "https://en.wikipedia.org/wiki/Raichur_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "ramanagara", "name": "Ramanagara", "type": "district", "parent": "karnataka", "path": "Ramanagara, Karnataka, India",
   "summary": "Silk City and Toy Town, famed for Asia's largest cocoon market, Channapatna wooden lacquer toys, and Sholay rock boulders.",
   "profile": {"Headquarters": "Ramanagara", "Language": "Kannada", "Food": "Ragi Mudde, Maddur Vada, Masala Dosa", "Crafts": "GI-tagged Channapatna wooden lacquer toys, Mulberry silk reeling"},
   "area": "3,556 km²", "population": "1,082,636 (2011 Census)",
   "points": ["Channapatna toys craft originated under patronage of Tipu Sultan who invited Persian ivory artisans", "Massive granite hillocks formed the famous cinematic setting for the film Sholay"],
   "wiki": "https://en.wikipedia.org/wiki/Ramanagara_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "shivamogga", "name": "Shivamogga", "type": "district", "parent": "karnataka", "path": "Shivamogga, Karnataka, India",
   "summary": "Gateway to Malnad, rice granary of Karnataka, home to Jog Falls, Western Ghats biodiversity, and Keladi heritage.",
   "profile": {"Headquarters": "Shivamogga", "Language": "Kannada", "Food": "Akki Rotti, Halasina Hannina Kadabu, Thambli", "Crafts": "Areca nut products, Sandalwood carving"},
   "area": "8,465 km²", "population": "1,752,753 (2011 Census)",
   "points": ["Jog Falls drops 253 m in four majestic cascades: Raja, Roarer, Rocket, and Rani", "Keladi Nayakas ruled from Ikkeri and Keladi leaving remarkable stone temples in 16th–18th century"],
   "wiki": "https://en.wikipedia.org/wiki/Shimoga_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "tumakuru", "name": "Tumakuru", "type": "district", "parent": "karnataka", "path": "Tumakuru, Karnataka, India",
   "summary": "Industrial satellite and educational hub known for Siddaganga Mutt's social service, Tatte Idli, and coconut groves.",
   "profile": {"Headquarters": "Tumakuru", "Language": "Kannada", "Food": "Kyathsandra Tatte Idli, Coconut water", "Crafts": "Coir fiber rope and matting, Handloom cotton"},
   "area": "10,597 km²", "population": "2,678,480 (2011 Census)",
   "points": ["Siddaganga Mutt founded by Shivakumar Swamiji feeds and educates over 10,000 poor students daily", "Devarayanadurga hill temples showcase Chola and Vijayanagara architecture"],
   "wiki": "https://en.wikipedia.org/wiki/Tumakuru_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "udupi", "name": "Udupi", "type": "district", "parent": "karnataka", "path": "Udupi, Karnataka, India",
   "summary": "Spiritual seaside temple town on the Arabian Sea, birthplace of Dvaita Vedanta and globally renowned Udupi vegetarian cuisine.",
   "profile": {"Headquarters": "Udupi", "Language": "Tulu, Kannada, Konkani", "Food": "Udupi Masala Dosa, Goli Baje, Patrode, Kadubu", "Crafts": "Udupi pure cotton sarees, Temple wood carvings"},
   "area": "3,582 km²", "population": "1,177,361 (2011 Census)",
   "points": ["Sri Krishna Matha founded in 13th century by philosopher Madhvacharya who established Ashta Mathas", "St. Mary's Islands feature world-renowned hexagonal columnar basaltic lava rock formations"],
   "wiki": "https://en.wikipedia.org/wiki/Udupi_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "uttara-kannada", "name": "Uttara Kannada", "type": "district", "parent": "karnataka", "path": "Uttara Kannada, Karnataka, India",
   "summary": "Dense coastal forest district boasting sacred Gokarna Atma Linga shrine, Murudeshwar beach, and Dandeli tiger reserve.",
   "profile": {"Headquarters": "Karwar", "Language": "Kannada, Konkani", "Food": "Karwar Fish Thali, Toddy palm jaggery, Cashews", "Crafts": "Sandalwood carving of Kumta, Horn and shell art"},
   "area": "10,291 km²", "population": "1,437,169 (2011 Census)",
   "points": ["Mahabaleshwar Temple at Gokarna houses the sacred Pranalinga (Atma Linga) of Lord Shiva", "Over 75% of district area covered under dense evergreen Western Ghats forests"],
   "wiki": "https://en.wikipedia.org/wiki/Uttara_Kannada", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "vijayanagara", "name": "Vijayanagara", "type": "district", "parent": "karnataka", "path": "Vijayanagara, Karnataka, India",
   "summary": "Heritage heartland created in 2021 centered at Hosapete, containing the majestic UNESCO World Heritage ruins of Hampi.",
   "profile": {"Headquarters": "Hosapete", "Language": "Kannada", "Food": "Jolada Rotti, Hampi Banana curry", "Crafts": "Stone sculpture, Terracotta, Lambani tribal embroidery"},
   "area": "5,644 km²", "population": "1,353,628 (2011 Census)",
   "points": ["Imperial capital of Vijayanagara Empire from 1336 to 1565 CE, visited by European and Persian travelers", "Encompasses Virupaksha Temple, Stone Chariot at Vittala Temple, and Lotus Mahal"],
   "wiki": "https://en.wikipedia.org/wiki/Vijayanagara_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "vijayapura", "name": "Vijayapura", "type": "district", "parent": "karnataka", "path": "Vijayapura, Karnataka, India",
   "summary": "City of domes on the Deccan plateau, historical seat of Adil Shahi dynasty boasting Gol Gumbaz and Ibrahim Rauza.",
   "profile": {"Headquarters": "Vijayapura", "Language": "Kannada, Urdu", "Food": "Jolada Rotti, Shenga Chutney, Grapes, Pomegranate", "Crafts": "Lambani embroidery, Ilkal border handlooms"},
   "area": "10,494 km²", "population": "2,177,331 (2011 Census)",
   "points": ["Gol Gumbaz (built 1656 CE) features the world's second largest dome without pillar support and an acoustic whispering gallery", "Capital of Adil Shahi Sultanate which constructed Ibrahim Rauza ('Taj Mahal of the Deccan')"],
   "wiki": "https://en.wikipedia.org/wiki/Bijapur_district,_Karnataka", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "yadgir", "name": "Yadgir", "type": "district", "parent": "karnataka", "path": "Yadgir, Karnataka, India",
   "summary": "Hill fortress district on the Bhima River, historic seat of Western Chalukyas and Rashtrakutas, and agricultural pulse center.",
   "profile": {"Headquarters": "Yadgir", "Language": "Kannada", "Food": "Jolada Rotti, Chigalli (tamarind sweet balls)", "Crafts": "Handloom weaving, Red gram processing"},
   "area": "5,270 km²", "population": "1,174,271 (2011 Census)",
   "points": ["Yadgir Fort built atop a massive hill feature by Western Chalukya and Yadava dynasties", "Carved out of Kalaburagi as an independent district in December 2009"],
   "wiki": "https://en.wikipedia.org/wiki/Yadgir_district", "source": "Census of India 2011, ODOP, Wikipedia", "updated": "2024-11", "model": ""},
]

save_json(DIST_DIR / "karnataka.json", karnataka_districts)

# ==========================================
# 2. KARNATAKA PLACES (Temples & Monuments)
# ==========================================
karnataka_places = [
  {"id": "virupaksha-temple-hampi", "name": "Virupaksha Temple, Hampi", "type": "place", "parent": "vijayanagara",
   "path": "Virupaksha Temple, Vijayanagara, Karnataka, India",
   "summary": "Ancient living Shiva temple on the banks of Tungabhadra River, heart of the UNESCO World Heritage Hampi ruins.",
   "points": [
     "Originally constructed in the 7th century CE as a modest shrine; major expansion commissioned by King Krishnadevaraya in 1510 CE to commemorate his accession",
     "Vijayanagara dynasty (with earlier Chalukya and Hoysala layers)",
     "Dedicated to Lord Virupaksha, a manifestation of Lord Shiva, and his consort Pampa Devi",
     "Renowned for its 50-meter-high eastern Rajagopura and inverted pinhole shadow effect projected onto temple walls"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Virupaksha_Temple,_Hampi", "source": "Archaeological Survey of India, UNESCO, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "chennakeshava-temple-belur", "name": "Chennakeshava Temple, Belur", "type": "place", "parent": "hassan",
   "path": "Chennakeshava Temple, Hassan, Karnataka, India",
   "summary": "Masterpiece of Hoysala stone sculpture, inscribed as a UNESCO World Heritage Site in 2023.",
   "points": [
     "Commissioned in 1117 CE by Hoysala King Vishnuvardhana to commemorate victory over the Cholas at Talakad",
     "Hoysala dynasty; took 103 years and three generations of master sculptors like Dasoja to complete",
     "Dedicated to Chennakeshava (Handsome Vishnu); built entirely from soft green chloritic schist (soapstone)",
     "Celebrated for 42 Madanika (bracket dancers) figurines displaying exquisite hairstyles, instruments, and micro-filigree detailing"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Chennakeshava_Temple,_Belur", "source": "Archaeological Survey of India, UNESCO, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "hoysaleswara-temple-halebidu", "name": "Hoysaleswara Temple, Halebidu", "type": "place", "parent": "hassan",
   "path": "Hoysaleswara Temple, Hassan, Karnataka, India",
   "summary": "Twin-shrine jewel of Hoysala architecture on a star-shaped plinth, dedicated to Hoysaleswara and Shantaleswara.",
   "points": [
     "Built in 1121 CE by Ketamalla, an officer under King Vishnuvardhana of the Hoysala dynasty",
     "Hoysala dynasty; inscribed as part of Sacred Ensembles of the Hoysalas on UNESCO World Heritage list in 2023",
     "Twin Shiva temple standing on a stellate (star-shaped) platform with two large Nandi mantapas carved from monolithic stone",
     "Outer walls feature continuous horizontal friezes depicting 1,248 elephants, lions, floral scrolls, and epic Mahabharata narratives"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Hoysaleswara_Temple", "source": "Archaeological Survey of India, UNESCO, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "sri-krishna-mutt-udupi", "name": "Sri Krishna Matha, Udupi", "type": "place", "parent": "udupi",
   "path": "Sri Krishna Matha, Udupi, Karnataka, India",
   "summary": "World-famous spiritual center of Dvaita Vedanta where Lord Krishna is worshipped exclusively through a nine-hole silver window.",
   "points": [
     "Founded in the 13th century CE by Jagadguru Madhvacharya, the proponent of Tattvavada (Dvaita philosophy)",
     "Ashta Mathas (eight monastic lineages) established by Madhvacharya govern temple rituals through biennial Paryaya succession",
     "Celebrated for Kanakana Kindi (window through which devotee Kanakadasa had darshan when the idol miraculously turned to face west)",
     "Renowned for uninterrupted Annadanam (serving free wholesome meals to thousands of pilgrims daily)"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Udupi_Sri_Krishna_Matha", "source": "Udupi Temple Administration, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "chamundeshwari-temple-mysuru", "name": "Chamundeshwari Temple, Mysuru", "type": "place", "parent": "mysuru",
   "path": "Chamundeshwari Temple, Mysuru, Karnataka, India",
   "summary": "Historic hilltop temple of the patron goddess of the Kingdom of Mysore atop Chamundi Hills.",
   "points": [
     "Originally constructed in the 12th century CE by Hoysala rulers; seven-tier gopuram added by Vijayanagara rulers in 17th century and extensively renovated by Maharaja Krishnaraja Wadiyar III in 1827",
     "Hoysala, Vijayanagara, and Wadiyar dynasties",
     "Dedicated to Chamundeshwari (Durga), who slew the demon Mahishasura on this hill",
     "Connected by 1,008 stone steps featuring a colossal 16-foot monolithic Nandi bull carved in 1659 CE"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Chamundeshwari_Temple", "source": "Mysore District Heritage, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "murudeshwar-temple", "name": "Murudeshwar Temple & Raja Gopura", "type": "place", "parent": "uttara-kannada",
   "path": "Murudeshwar Temple, Uttara Kannada, Karnataka, India",
   "summary": "Coastal pilgrimage complex on the Arabian Sea headland boasting the world's second-tallest Lord Shiva statue.",
   "points": [
     "Ancient shrine of Atma Linga piece; modern 123-foot colossal Shiva statue and 20-story Rajagopura completed in 2008 by philanthropist R. N. Shetty",
     "Kadamba and Vijayanagara historical legacy with modern coastal architectural engineering",
     "Surrounded on three sides by the waters of the Arabian Sea atop Kanduka Giri hill",
     "Features a 249-foot Rajagopura equipped with a high-speed elevator taking visitors to viewing galleries on the 18th floor"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Murudeshwara", "source": "Karnataka Tourism, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "mysore-palace", "name": "Mysore Palace (Amba Vilas)", "type": "place", "parent": "mysuru",
   "path": "Mysore Palace, Mysuru, Karnataka, India",
   "summary": "Spectacular royal residence of the Wadiyar dynasty, illuminating the city with nearly 100,000 bulbs.",
   "points": [
     "Commissioned after fire destroyed old wooden palace in 1897; designed by British architect Henry Irwin and completed in 1912 CE",
     "Wadiyar dynasty of the Kingdom of Mysore",
     "Indo-Saracenic masterpiece blending Hindu, Mughal, Rajput, and Gothic architectural styles",
     "Houses the ornate Golden Throne (Chinnada Simhasana) and Durbar Hall with stained glass peacock ceiling"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Mysore_Palace", "source": "Mysore Palace Board, Government of Karnataka, Wikipedia", "updated": "2024-11", "model": ""},

  {"id": "jog-falls", "name": "Jog Falls", "type": "place", "parent": "shivamogga",
   "path": "Jog Falls, Shivamogga, Karnataka, India",
   "summary": "India's second-highest untiered plunge waterfall on the Sharavathi River dropping 253 meters in roaring cascades.",
   "points": [
     "Natural plunge waterfall fed by the Sharavathi River in the Western Ghats; first surveyed by British officers in 1840",
     "Power harnessed by the Mahatma Gandhi Hydroelectric Project commissioned in 1948",
     "Divided into four distinct cascades: Raja (unbroken drop), Roarer, Rocket (jetting stream), and Rani (graceful spray)",
     "Best witnessed during the peak monsoon season between July and October when water discharge exceeds 3,000 cubic meters per second"
   ],
   "wiki": "https://en.wikipedia.org/wiki/Jog_Falls", "source": "Karnataka Tourism, Wikipedia", "updated": "2024-11", "model": ""},
]

save_json(PLACES_DIR / "karnataka.json", karnataka_places)

print("Karnataka Stage 2 Data files successfully generated.")
