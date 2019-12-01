# -*- coding:utf-8 -*-

config = {
    "COUNTRY_LIST": ["Greece", "Hungary", "Sri Lanka", "Serbia"],
    "MATCHES": ["Local Government Office", "Police"],
}

# countrys = {
#     "Greece": {
#         "COUNTRY_NAME":
#         "Greece",
#         "MATCHES": ["Local Government Office", "Police"],
#         "CITY_LIST": [
#             "Athens", "Thessaloniki", "Patras", "Larissa", "Heraklion",
#             "Volos", "Ioannina", "Trikala", "Chalcis", "Serres",
#             "Alexandroupoli", "Xanthi", "Katerini", "Kalamata", "Kavala",
#             "Chania", "Lamia", "Komotini", "Rhodes", "Agrinio"
#         ]
#     },
#     "Hungary": {
#         "COUNTRY_NAME":
#         "Hungary",
#         "MATCHES": ["Local Government Office", "Police"],
#         "CITY_LIST": [
#             "Budapest", "Debrecen", "Szeged", "Miskolc", "Pécs", "Győr",
#             "Nyíregyháza", "Kecskemét"
#         ]
#     },
#     "Sri Lanka": {
#         "COUNTRY_NAME":
#         "Sri Lanka",
#         "MATCHES": ["Local Government Office", "Police"],
#         "CITY_LIST": [
#             "Ampara", "Anuradhapura", "Badulla", "Basnahira palata",
#             "Batticaloa", "Central", "Colombo", "Eastern", "Galle", "Gampaha",
#             "Hambantota", "Jaffna", "Kalutara", "Kandy", "Kegalla",
#             "Kilinochchi", "Kurunegala", "Madhyama palata", "Mannar", "Matale",
#             "Matara", "Monaragala", "Mullaittivu", "North Central",
#             "North Western", "Northern", "Nuwara Eliya", "Other",
#             "Polonnaruwa", "Puttalam", "Ratnapura", "Sabaragamuwa", "Southern",
#             "Trincomalee", "Uva", "Vavuniya", "Western"
#         ]
#     },
#     "Serbia": {
#         "COUNTRY_NAME":
#         "Serbia",
#         "MATCHES": ["Local Government Office", "Police"],
#         "CITY_LIST": [
#             "Aleksandrovac", "Aleksinac", "Aranđelovac", "Arilje", "Azanja",
#             "Babušnica", "Badovinci", "Bagrdan", "Bajina Basta",
#             "Baljevac na Ibru", "Banja Koviljača", "Barajevo", "Barič",
#             "Batočina", "Baćevac", "Bela Crkva", "Bela Palanka", "Belanovica",
#             "Belgrade", "Beli Potok", "Beljina", "Beograd", "Biljača", "Blace",
#             "Bojnik", "Boleč", "Boljevac", "Boljevci", "Bor", "Borča",
#             "Bosilegrad", "Bozevac", "Bošnjace", "Branicevski okrug",
#             "Braničevo", "Bratmilovce", "Brestovac", "Brodarevo", "Brus",
#             "Brza Palanka", "Brzi Brod", "Bujanovac", "Bukovče", "Cajetina",
#             "Cačak", "Central Serbia", "Citluk", "Cićevac", "Crna Bara",
#             "Crna Trava", "Cuprija", "Debrc", "Departamento de La Paz",
#             "Despotovac", "Deveti maj", "Dimitrovgrad", "Divčibare",
#             "Dobanovci", "Dobra", "Doljevac", "Donja Livadica",
#             "Donji Milanovac", "Drenovac", "Drijetanj", "Dušanovac", "Futog",
#             "Glogovac", "Golubac", "Gorjani", "Gornja Toponica",
#             "Gornja Trepča", "Gornji Matejevac", "Gornji Milanovac",
#             "Grabovac", "Grdelica", "Grocka", "Guberevac", "Guncati", "Guča",
#             "Inđija", "Ivanjica", "Izvor", "Jablanica", "Jabukovac",
#             "Jagodina", "Jakovo", "Jasika", "Jordan", "Južnobacki okrug",
#             "Južnobanatski okrug", "Kaluđerica", "Kamenica", "Kasidol",
#             "Kikinda", "Kladovo", "Klenje", "Klupci", "Knić", "Knjaževac",
#             "Kobilje", "Kobišnica", "Koceljeva", "Kolari", "Kolubara",
#             "Konarevo", "Korbovo", "Korman", "Kosjerić", "Kosovas", "Kosovo",
#             "Kosovska Mitrovica", "Kostolac", "Kragujevac", "Kraljevo",
#             "Kremna", "Krepoljin", "Krnjevo", "Krupanj", "Kruševac", "Kula",
#             "Kuršumlija", "Kučevo", "Lajkovac", "Lapovo", "Lazarevac",
#             "Laznica", "Lebane", "Leskovac", "Lešnica", "Leštane",
#             "Lipnički Šor", "Ljig", "Ljubovija", "Loznica", "Lozničko Polje",
#             "Lozovik", "Lužane", "Lučane", "Lučani", "Macvanski okrug",
#             "Majdanpek", "Majur", "Mala Moštanica", "Mala Plana", "Mala Reka",
#             "Mali Zvornik", "Markovac", "Mataruška Banja", "Mačva",
#             "Medoševac", "Medveða", "Meljak", "Merošina", "Mihajlovac",
#             "Mijatovac", "Miloševac", "Mionica", "Mišar", "Mladenovac",
#             "Mokra Gora", "Moravica", "Moravicki okrug", "Mršinci",
#             "Mrčajevci", "Mudrakovac", "Mur", "Murgaš", "Negotin", "NI",
#             "Nikola Tesla", "Nis", "Nišava", "Nišavski okrug", "Niška Banja",
#             "Nova Varoš", "Novi Beograd", "Novi Pazar", "Novi Sad",
#             "Novo Selo", "Obrenovac", "Obrež", "Oraovica", "Osanica",
#             "Osečina", "Osipaonica", "Ostružnica", "Other", "Padinska Skela",
#             "Pančevo", "Paraćin", "Pcinjski okrug", "Pecka", "Petrovac", "Peć",
#             "Pečenjevce", "Pirot", "Podunavski okrug", "Pojate",
#             "Pomoravski okrug", "Popovac", "Popučke", "Postenje", "Požarevac",
#             "Požega", "Pranjani", "Predejane", "Preljina", "Preševo", "Priboj",
#             "Prijepolje", "Prizren", "Prnjavor", "Prokuplje", "Provo",
#             "Pukovac", "Rabrovac", "Rabrovo", "Radinac", "Rajince", "Ralja",
#             "Rasina", "Rasinski okrug", "Ratina", "Raška", "Raški okrug",
#             "Ražanj", "Rača", "Regjioni i Prishtinës", "Rekovac",
#             "Republika Srpska", "Resavica", "Rgotina", "Ribare", "Ribariće",
#             "Ribnica", "Ripanj", "Rožaje Municipality", "Rudna Glava",
#             "Rudnik", "Rušanj", "Sabac", "Salakovac", "Serbia",
#             "Severnobacki okrug", "Sevojno", "Sićevo", "Sjenica", "Smederevo",
#             "Smederevska Palanka", "Sokobanja", "Solotuša", "Sombor", "Sopic",
#             "Sopot", "Srbija", "Srem", "Sremska Mitrovica", "Sremčica",
#             "Stalać", "Stepojevac", "Stopanja", "Subotica", "Sumane",
#             "Surdulica", "Surčin", "Svilajnac", "Svrljig", "Toplica", "Topola",
#             "Trbušani", "Trgovište", "Trnava", "Trstenik", "Tršić", "Tutin",
#             "Ub", "Ugrinovci", "Umka", "Umčari", "Uzići", "Užice", "Valjevo",
#             "Varvarin", "Velika Drenova", "Velika Moštanica", "Velika Plana",
#             "Veliki Crljeni", "Veliki Trnovac", "Veliki Šiljegovac",
#             "Veliko Gradište", "Veliko Orašje", "Vinci", "Vinča", "Vladimirci",
#             "Vladičin Han", "Vlasina Rid", "Vlasotince", "Vojvodina", "Voluja",
#             "Vranje", "Vranjska Banja", "Vranovo", "Vrbas", "Vrnjačka Banja",
#             "Vrtište", "Vršac", "Vrčin", "Vucje", "Zabari", "Zagubica",
#             "Zaječar", "Zaklopača", "Zemun", "Zimony", "Zitkovac", "Zitorađa",
#             "Ziča", "Zlatibor", "Zlot", "Zrenjanin", "Zujince", "Zvezdan",
#             "Zvečka", "Štitar", "Šumadija"
#         ]
#     }
# }
