#!/bin/sh
file=data/all_spiegel_sents_fixed_cats.json
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ SPIEGEL\ TV\ THEMA\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Apps\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"TESTCHANNEL\ \/\ TESTBEREICH\ ALLGEMEIN\"/\"category\":\ \"testchannel\"/g' $file
sed -ri 's/\"category\":\ \"Auto\ \/\ Fahrkultur\"/\"category\":\ \"auto\"/g' $file
sed -ri 's/\"category\":\ \"Unispiegel\ \/\ Geld\"/\"category\":\ \"unispiegel\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Reeperbahn\ Festival\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"Politik\ \/\ Deutschland\"/\"category\":\ \"politik\"/g' $file
sed -ri 's/\"category\":\ \"Eines\ Tages\ \/\ default\"/\"category\":\ \"eines_tages\"/g' $file
sed -ri 's/\"category\":\ \"KarriereSPIEGEL\ \/\ Berufsstart\"/\"category\":\ \"karrierespiegel\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ Literatur\"/\"category\":\ \"kultur\"/g' $file
sed -ri 's/\"category\":\ \"DER\ SPIEGEL\ \/\ Deutschland\"/\"category\":\ \"der_spiegel\"/g' $file
sed -ri 's/\"category\":\ \"KarriereSPIEGEL\ \/\ default\"/\"category\":\ \"karrierespiegel\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ Auf\ den\ D\\u00e4chern\"/\"category\":\ \"kultur\"/g' $file
sed -ri 's/\"category\":\ \"einestages\ \/\ Zeitzeugen\"/\"category\":\ \"einestages\"/g' $file
sed -ri 's/\"category\":\ \"Unispiegel\ \/\ WunderBAR\"/\"category\":\ \"unispiegel\"/g' $file
sed -ri 's/\"category\":\ \"SchulSPIEGEL\ \/\ Wissen\"/\"category\":\ \"schulspiegel\"/g' $file
sed -ri 's/\"category\":\ \"Politik\ \/\ Debatte\"/\"category\":\ \"politik\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ Gesellschaft\"/\"category\":\ \"kultur\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Nachtclub\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Panorama\ \/\ Zeitgeschichte\"/\"category\":\ \"panorama\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Netzpolitik\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ SPIEGEL\ THEMA\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Terra\ X\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ Fu\\u00dfball\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ Kino\"/\"category\":\ \"kultur\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ XXP\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ special\ \/\ default\"/\"category\":\ \"spiegel_special\"/g' $file
sed -ri 's/\"category\":\ \"Reise\ \/\ St\\u00e4dtereisen\"/\"category\":\ \"reise\"/g' $file
sed -ri 's/\"category\":\ \"Panorama\ \/\ Leute\"/\"category\":\ \"panorama\"/g' $file
sed -ri 's/\"category\":\ \"Spam\ \/\ default\"/\"category\":\ \"spam\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Web\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Mobil\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"Extra\ \/\ Kontakt\"/\"category\":\ \"extra\"/g' $file
sed -ri 's/\"category\":\ \"Panorama\ \/\ Justiz\"/\"category\":\ \"panorama\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Technologie\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"Wissenschaft\ \/\ Weltall\"/\"category\":\ \"wissenschaft\"/g' $file
sed -ri 's/\"category\":\ \"Wirtschaft\ \/\ einsurance\"/\"category\":\ \"wirtschaft\"/g' $file
sed -ri 's/\"category\":\ \"Wirtschaft\ \/\ Staat\ &\ Soziales\"/\"category\":\ \"wirtschaft\"/g' $file
sed -ri 's/\"category\":\ \"DER\ SPIEGEL\ \/\ Kultur\"/\"category\":\ \"der_spiegel\"/g' $file
sed -ri 's/\"category\":\ \"DER\ SPIEGEL\ \/\ Vorabmeldungen\"/\"category\":\ \"der_spiegel\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Tech\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ WM\ 2006\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"Dienste\ \/\ \\u00dcbersicht\"/\"category\":\ \"dienste\"/g' $file
sed -ri 's/\"category\":\ \"Reise\ \/\ Kurztrip\"/\"category\":\ \"reise\"/g' $file
sed -ri 's/\"category\":\ \"Extra\ \/\ default\"/\"category\":\ \"extra\"/g' $file
sed -ri 's/\"category\":\ \"SchulSPIEGEL\ \/\ default\"/\"category\":\ \"schulspiegel\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Wissen\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Unispiegel\ \/\ Job\ &\ Beruf\"/\"category\":\ \"unispiegel\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ SPIEGEL\ TV\ Digital\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Extra\ \/\ DER\ SPIEGEL\"/\"category\":\ \"extra\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ Musik\"/\"category\":\ \"kultur\"/g' $file
sed -ri 's/\"category\":\ \"Wissenschaft\ \/\ Mensch\ &\ Technik\"/\"category\":\ \"wissenschaft\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ US-Sports\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Themenabend\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Wissenschaft\ \/\ Weltraum\"/\"category\":\ \"wissenschaft\"/g' $file
sed -ri 's/\"category\":\ \"Wirtschaft\ \/\ Verbraucher\ &\ Service\"/\"category\":\ \"wirtschaft\"/g' $file
sed -ri 's/\"category\":\ \"SchulSPIEGEL\ \/\ Abi\ \-\ und\ dann\?\"/\"category\":\ \"schulspiegel\"/g' $file
sed -ri 's/\"category\":\ \"KarriereSPIEGEL\ \/\ Ausland\"/\"category\":\ \"karrierespiegel\"/g' $file
sed -ri 's/\"category\":\ \"Reise\ \/\ Aktuell\"/\"category\":\ \"reise\"/g' $file
sed -ri 's/\"category\":\ \"Entdecken\ \/\ \\u00dcbersicht\"/\"category\":\ \"entdecken\"/g' $file
sed -ri 's/\"category\":\ \"DER\ SPIEGEL\ \/\ Medien\"/\"category\":\ \"der_spiegel\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Politik\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"einestages\ \/\ default\"/\"category\":\ \"einestages\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Reportage\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"special\ Geschichte\"/\"category\":\ \"special_geschichte\"/g' $file
sed -ri 's/\"category\":\ \"Gesundheit\ \/\ Psychologie\"/\"category\":\ \"gesundheit\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ default\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ Athen\ 2004\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"Politik\ \/\ Ausland\"/\"category\":\ \"politik\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Games\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"Wirtschaft\"/\"category\":\ \"wirtschaft\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Wirtschaft\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"Dienste\ \/\ SPIEGEL\ MOBIL\"/\"category\":\ \"dienste\"/g' $file
sed -ri 's/\"category\":\ \"Wirtschaft\ \/\ Unternehmen\ &\ M\\u00e4rkte\"/\"category\":\ \"wirtschaft\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Zeitgeschichte\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"Reise\ \/\ Europa\"/\"category\":\ \"reise\"/g' $file
sed -ri 's/\"category\":\ \"SchulSPIEGEL\"/\"category\":\ \"schulspiegel\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ TV\"/\"category\":\ \"kultur\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ SPIEGEL\ Geschichte\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ K3\"/\"category\":\ \"kultur\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Spielzeug\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ Achilles\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"Panorama\"/\"category\":\ \"panorama\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Gadgets\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"Reise\ \/\ Deutschland\"/\"category\":\ \"reise\"/g' $file
sed -ri 's/\"category\":\ \"einestages\ \/\ Fundb\\u00fcro\"/\"category\":\ \"einestages\"/g' $file
sed -ri 's/\"category\":\ \"Auto\ \/\ Tests\"/\"category\":\ \"auto\"/g' $file
sed -ri 's/\"category\":\ \"digasvideoexport\"/\"category\":\ \"digasvideoexport\"/g' $file
sed -ri 's/\"category\":\ \"Auto\ \/\ Werkstatt\"/\"category\":\ \"auto\"/g' $file
sed -ri 's/\"category\":\ \"Unispiegel\ \/\ Studium\"/\"category\":\ \"unispiegel\"/g' $file
sed -ri 's/\"category\":\ \"Stil\ \/\ default\"/\"category\":\ \"stil\"/g' $file
sed -ri 's/\"category\":\ \"Wissenschaft\ \/\ Mensch\"/\"category\":\ \"wissenschaft\"/g' $file
sed -ri 's/\"category\":\ \"Panorama\ \/\ Gesellschaft\"/\"category\":\ \"panorama\"/g' $file
sed -ri 's/\"category\":\ \"Gesundheit\ \/\ Diagnose\ &\ Therapie\"/\"category\":\ \"gesundheit\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Wissenschaft\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Panamericana\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Special\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Kultur\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ Zwiebelfisch\"/\"category\":\ \"kultur\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Auto\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"Panorama\ \/\ default\"/\"category\":\ \"panorama\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Thema\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"KarriereSPIEGEL\ \/\ Berufsleben\"/\"category\":\ \"karrierespiegel\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Ausland\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"Reise\ \/\ Fernweh\"/\"category\":\ \"reise\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ dctp\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"SchulSPIEGEL\ \/\ Querweltein\"/\"category\":\ \"schulspiegel\"/g' $file
sed -ri 's/\"category\":\ \"Auto\ \/\ Aktuell\"/\"category\":\ \"auto\"/g' $file
sed -ri 's/\"category\":\ \"Wirtschaft\ \/\ default\"/\"category\":\ \"wirtschaft\"/g' $file
sed -ri 's/\"category\":\ \"DER\ SPIEGEL\ \/\ default\"/\"category\":\ \"der_spiegel\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Extra\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Wissenschaft\ \/\ Mensch\ \ Technik\"/\"category\":\ \"wissenschaft\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ Wintersport\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"Mein\ SPIEGEL\ \/\ default\"/\"category\":\ \"mein_spiegel\"/g' $file
sed -ri 's/\"category\":\ \"Gesundheit\ \/\ Schwangerschaft\ &\ Kind\"/\"category\":\ \"gesundheit\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Sport\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"Entdecken\ \/\ SPIEGEL\ MOBIL\"/\"category\":\ \"entdecken\"/g' $file
sed -ri 's/\"category\":\ \"Gesundheit\ \/\ Sex\ &\ Partnerschaft\"/\"category\":\ \"gesundheit\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ Gutenberg\"/\"category\":\ \"kultur\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Dokumentation\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Wissenschaft\ \/\ Medizin\"/\"category\":\ \"wissenschaft\"/g' $file
sed -ri 's/\"category\":\ \"Jahres-Chronik\ \/\ default\"/\"category\":\ \"jahres_chronik\"/g' $file
sed -ri 's/\"category\":\ \"Extra\ \/\ Impressum\"/\"category\":\ \"extra\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Magazin\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Unispiegel\ \/\ Job\ \ Beruf\"/\"category\":\ \"unispiegel\"/g' $file
sed -ri 's/\"category\":\ \"Wissenschaft\ \/\ Erde\"/\"category\":\ \"wissenschaft\"/g' $file
sed -ri 's/\"category\":\ \"UniSPIEGEL\ \/\ Job\ &\ Beruf\"/\"category\":\ \"unispiegel\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ WM-News\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ ZDF\ Zeit\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Gesundheit\ \/\ Ern\\u00e4hrung\ &\ Fitness\"/\"category\":\ \"gesundheit\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Netzwelt\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ SPIEGEL-ONLINE-Preview\ Tickets\"/\"category\":\ \"kultur\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ ZDF\ Zoom\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Reise\ \/\ Metropolen\"/\"category\":\ \"reise\"/g' $file
sed -ri 's/\"category\":\ \"Extra\"/\"category\":\ \"extra\"/g' $file
sed -ri 's/\"category\":\ \"einestages\ \/\ Themen\"/\"category\":\ \"einestages\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Bildung\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ Sonstiges\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"SchulSPIEGEL\ \/\ Sch\\u00fclerzeitungen\"/\"category\":\ \"schulspiegel\"/g' $file
sed -ri 's/\"category\":\ \"Netzwelt\ \/\ Netzkultur\"/\"category\":\ \"netzwelt\"/g' $file
sed -ri 's/\"category\":\ \"Wissenschaft\ \/\ Natur\"/\"category\":\ \"wissenschaft\"/g' $file
sed -ri 's/\"category\":\ \"Wissenschaft\ \/\ Technik\"/\"category\":\ \"wissenschaft\"/g' $file
sed -ri 's/\"category\":\ \"KarriereSPIEGEL\ \/\ Stellensuche\"/\"category\":\ \"karrierespiegel\"/g' $file
sed -ri 's/\"category\":\ \"UniSPIEGEL\ \/\ SchulSPIEGEL\"/\"category\":\ \"unispiegel\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ Formel\ 1\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ Frauen-WM\ 2011\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"digasthemaexport\"/\"category\":\ \"digasthemaexport\"/g' $file
sed -ri 's/\"category\":\ \"Archiv\ \/\ default\"/\"category\":\ \"archiv\"/g' $file
sed -ri 's/\"category\":\ \"Dossiers\ \/\ Gesellschaft\"/\"category\":\ \"dossiers\"/g' $file
sed -ri 's/\"category\":\ \"SchulSPIEGEL\ \/\ Leben\ U21\"/\"category\":\ \"schulspiegel\"/g' $file
sed -ri 's/\"category\":\ \"SPIEGEL\ TV\ \/\ Montagsreportage\"/\"category\":\ \"spiegel_tv\"/g' $file
sed -ri 's/\"category\":\ \"Sport\ \/\ Fu\\u00dfball-News\"/\"category\":\ \"sport\"/g' $file
sed -ri 's/\"category\":\ \"Forum\ \/\ default\"/\"category\":\ \"forum\"/g' $file
sed -ri 's/\"category\":\ \"KarriereSPIEGEL\ \/\ Games\"/\"category\":\ \"karrierespiegel\"/g' $file
sed -ri 's/\"category\":\ \"Kultur\ \/\ Bestseller\"/\"category\":\ \"kultur\"/g' $file

