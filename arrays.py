#ATTENTION, classification is faulty and biased but as complete as I could do <3
def categorize_aircraft(muster):
    muster_upper = str(muster).upper()
    if any(keyword in muster_upper for keyword in [
        "WASSMER", "TITAN AIRCRAFT T51", "TB 10", "TIPSY NIPPER", 
        "XTREME AIR", "D4BK FASCINATION", "M18 (DROMADER)", "M20", 
        "TS-8 BIES", "Y-11", "ZLIN", "DIAMOND", "WELLER",
        "VIVID FW", "T SERIES", "TAIFUN",
        "TBM 700", "TECNAM", "140", "150", "152", "170", "172", "177", "180", "182", "185", "195",
        "205", "206", "208", "210", "23", "24", "27", "300", "330", "350", 
        "33 BONANZA", "337", "340", "35 BONANZA", "36 BONANZA", 
        "401", "407", "414",
        "50", "55", "58", "75", "82", "90 KING AIR", "A-1 HUSKY", "AA5", "ALBATROS",
        "AN-2", "YAK", "CITATION", "BARON", "CENTURION", "CARAVAN", 
        "SKYWAGON", "SUNDOWNER", 
        "STEARMAN", "SAFIR", "TRAVELER", "VELOCITY",
        "TOBAGO", "T303", "TB 20", "TB 9 ", "SPITFIRE",
        "SPORTCRUISER", "SOCATA", "SOCIETE NATIONALE DE CONSTRUCTIONS",
        "SV4B/C", "SV-4C", "STINSON 108", "CIRRUS", "SR-2",
        "SKYBOLT", "SKYVAN", "SAI - KZ VII",
        "ROCKWELL COMMANDER", "ROBIN DR400",
        "RV-7", "ROBIN - HR", "RENEGADE SPIRIT",
        "PIPER", "PZL", "PC-9", "PC-6B TURBO-PORTER", "PA-", "PA 28",
        "P68 VICTOR", "P-2", "MOONEY", "MSW AVIATION",
        "MS 893", "ME 109", "M38 MESSENGER", "M22", "M-7-420", "M SERIES",
        "LEOPOLD - KR-2/B", "LA4", "L-40 META SOKOL", "KODIAK 100",
        "JPM-01 MEDOC", "RAYTHEON", "HR 200-120 B",
        "BÜ 181 B-1", "GRUMMAN", "GS1", "GA-7 (COUGAR)",
        "G-202", "FW190", "STIEGLITZ", "UTVA 66",
        "F-8L FALCO", "CELESTINE", "PHENOM 100", "SPORTSMAN 2+2", "EXEC",
        "EAGLE", "DV-20", "DR 400-RP", "DR 315 PETIT PRINCE",
        "DR 253 REGENT", "DO-28D-6", "DHC1 CHIMPMUNK", "DE HAVILLAND - DH 89 A",
        "DA", "114B", "CESSNA 510", "COZY", "COMMANDER",
        "CAP10", "T131", "B207", "BRITTEN-NORMAN", "ISLANDER",
        "KLEMM 107", "EPIC LT", "M17", "J430", "AB  47",
        "40 DEFIANT", "20", "19 SPORTSMAN", "1,131"
        ]):
        return 'Leichtflugzeug'
    if any(keyword in muster_upper for keyword in [
        "VOGT", "MISTRAL", "VENTUS", "ASH", "ASK", "ASW", "AVIO", 
        "AVION", "SAMBURO", "SG 38", "RHÖNBUSSARD", "SCHLEICHER",
        "PHOEBUS C", "SPORTINE", "SPORTAVIA", "JUBI GMBH",
        "SLINGSBY", "SCHEMPP", "SCHEMMP", "SCHEIBE", "SUPER DIMONA TTS",
        "STEMME S6", "SHK", "SFS", "SF", "S-10, CHRYSALIS (TG-11)",
        "ROLLADEN-SCH", "RF-5", "BANJO MH", "PIK", "PICCOLO", "PHOEBUS",
        "P-220 KOALA", "ORLICAN", "NEUKOM", "NIMBUS", "MDM-1",
        "LANGE", "LS", "LAK", "L13 BLANIK", "L-SPATZ SPARROW",
        "L-33", "L-13SDL", "KESTREL", "KA7", "KA6", "K8B", "JANUS",
        "IS-28MA", "HORNET C", "HOAC AUSTRIA", "HK36", "HK-36", "HK 36",
        "H301", "H201", "H-36", "GROB", "GLASER-DIRKS", "G-109", "G-103",
        "G-102", "KRANICH II", "AV 36 CR", "ELAN",
        "DUO DISCUS", "DISCUS", "DG", "CENTAIR", "BINDER",
        "BERGFALKE", "B4-PC11", "OLYMPIA-MEISE", "B 12",
        "31B TANDEM TUTOR", "303 (MOSQUITO)"
        ]):
        return 'Segelflugzeug'
    if any(keyword in muster_upper for keyword in [
        "SPORTSTAR", "WD DALLACH", "RV7A", "TOMARK", 
        "Z-TYPE", "ZODIAC", "ZENAIR", "VIRUS", "TL", 
        "ULBI", "AT-3", "AEROPRAKT", "EUROPA", "CARAT", "ZEPHYR", 
        "CHALLENGER", "TL-96", "MCR-ULC",
        "CRI-CRI", "SKYRANGER", "SKY-WALKER II",
        "SAVAGE", "SZD", "STARK FLUGZEUGBAU - TURBULENT D-1",
        "SPACEK", "SIREN", "S-9 KAOS", "ROLAND",
        "RENEGADE 472", "REMOS", "REINSDORF", "REINHARD LEVERINGHAUS",
        "PITTS", "RANS", "PLATZER / KIEBITZ", "PIPISTREL",
        "P-2002", "OMF", "MD 3 RIDER", "NITRA",
        "MCR-01 VLA", "MCR 01", "AC-4", "LIBERTY XL-2", "LANCAIR 360",
        "LCA CADET", "LANCAIR", "BX-2 CHERRY",
        "KL 25", "KL-107", "JODEL D92", "VL-3E",
        "HB-207 ALFA", "AVAX II", "G202", "415 CD",
        "PEREGRINE SL", "FLYSYNTHESIS", "FLIGHT DESIGN", "FK",
        "VEGA ST 87", "EUROSTAR", "EUROFOX", "KR030", "EIGENBAU - RV-12",
        "WT9", "DALLACH", "C42", "CP301", "CASSUTT III M",
        "AQUILA", "C 42", "JUNGMANN", "BREEZER", "BOT SC07",
        "KR-2", "BD-5-J/V", "RV7", "200DR", "RV 9", "HB-207",
        "PIONEER 400", "AIRLONY SKYLANE", "WT-9"
        ]):
        return 'Ultraleichtflugzeug'
    if any(keyword in muster_upper for keyword in [
        "269", "280", "A 109", "AB 47", "AB 412", 
        "AS 332", "AS 350", "ECUREUIL", "SUPER PUMA", "XENON",
        "UH-12", "U-12", "TRIXY", "S-76", "R22", "R44", "MD-902",
        "MD-600N", "CABRI G2", "369", "HELICYCLE SOLAR", "GYROCOPTER",
        "GYROFLUG", "FH-1100", "ENSTROM", "CH 7", "EC", "HELICOPTER",
        "AUTO GIRO", "AUTO-GYRO", "BO105", "AUTOGYRO", "AUTOGIRO",
        "BK 117", "AUGUST SCHREMPP", "A-60+", "AEROCOPTER"
        ]):
        return 'Hubschrauber'
    if any(keyword in muster_upper for keyword in [
        "328", "737", "777", "A319", "A320", "A321", "PA200 TORNADO",
        "FALCON 2000", "AVRO RJ100"
        ]):
        return 'Verkehrsflugzeug'
    if any(keyword in muster_upper for keyword in ["UAV", "CAMCOPTER", "TRON V1"]):
        return 'Drohne'
    return 'Unbekannt'