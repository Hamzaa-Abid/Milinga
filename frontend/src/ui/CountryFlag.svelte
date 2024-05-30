<script context="module">
    export const countries = {AF:"Afghanistan",AL:"Albania",DZ:"Algeria",AS:"American Samoa",AD:"Andorra",AO:"Angola",AI:"Anguilla",AQ:"Antarctica",AG:"Antigua and Barbuda",AR:"Argentina",AM:"Armenia",AW:"Aruba",AU:"Australia",AT:"Austria",AZ:"Azerbaijan",BS:"Bahamas",BH:"Bahrain",BD:"Bangladesh",BB:"Barbados",BY:"Belarus",BE:"Belgium",BZ:"Belize",BJ:"Benin",BM:"Bermuda",BT:"Bhutan",BO:"Bolivia",BA:"Bosnia and Herzegovina",BW:"Botswana",BV:"Bouvet Island",BR:"Brazil",IO:"British Indian Ocean Territory",BN:"Brunei Darussalam",BG:"Bulgaria",BF:"Burkina Faso",BI:"Burundi",KH:"Cambodia",CM:"Cameroon",CA:"Canada",CV:"Cape Verde",KY:"Cayman Islands",CF:"Central African Republic",TD:"Chad",CL:"Chile",CN:"China",CX:"Christmas Island",CC:"Cocos (Keeling) Islands",CO:"Colombia",KM:"Comoros",CG:"Congo",CD:"Congo, Democratic Republic",CK:"Cook Islands",CR:"Costa Rica",CI:"Cote D'Ivoire",HR:"Croatia",CU:"Cuba",CY:"Cyprus",CZ:"Czech Republic",DK:"Denmark",DJ:"Djibouti",DM:"Dominica",DO:"Dominican Republic",EC:"Ecuador",EG:"Egypt",SV:"El Salvador",GQ:"Equatorial Guinea",ER:"Eritrea",EE:"Estonia",ET:"Ethiopia",FK:"Falkland Islands (Malvinas)",FO:"Faroe Islands",FJ:"Fiji",FI:"Finland",FR:"France",GF:"French Guiana",PF:"French Polynesia",TF:"French Southern Territories",GA:"Gabon",GM:"Gambia",GE:"Georgia",DE:"Germany",GH:"Ghana",GI:"Gibraltar",GR:"Greece",GL:"Greenland",GD:"Grenada",GP:"Guadeloupe",GU:"Guam",GT:"Guatemala",GN:"Guinea",GW:"Guinea-Bissau",GY:"Guyana",HT:"Haiti",HM:"Heard Island and Mcdonald Islands",VA:"Holy See (Vatican City State)",HN:"Honduras",HK:"Hong Kong",HU:"Hungary",IS:"Iceland",IN:"India",ID:"Indonesia",IR:"Iran, Islamic Republic of",IQ:"Iraq",IE:"Ireland",IL:"Israel",IT:"Italy",JM:"Jamaica",JP:"Japan",JO:"Jordan",KZ:"Kazakhstan",KE:"Kenya",KI:"Kiribati",KP:"North Korea",KR:"South Korea",KW:"Kuwait",KG:"Kyrgyzstan",LA:"Lao People's Democratic Republic",LV:"Latvia",LB:"Lebanon",LS:"Lesotho",LR:"Liberia",LY:"Libyan Arab Jamahiriya",LI:"Liechtenstein",LT:"Lithuania",LU:"Luxembourg",MO:"Macao",MK:"Macedonia, the Former Yugoslav Republic of",MG:"Madagascar",MW:"Malawi",MY:"Malaysia",MV:"Maldives",ML:"Mali",MT:"Malta",MH:"Marshall Islands",MQ:"Martinique",MR:"Mauritania",MU:"Mauritius",YT:"Mayotte",MX:"Mexico",FM:"Micronesia, Federated States of",MD:"Moldova, Republic of",MC:"Monaco",MN:"Mongolia",MS:"Montserrat",MA:"Morocco",MZ:"Mozambique",MM:"Myanmar",NA:"Namibia",NR:"Nauru",NP:"Nepal",NL:"Netherlands",NC:"New Caledonia",NZ:"New Zealand",NI:"Nicaragua",NE:"Niger",NG:"Nigeria",NU:"Niue",NF:"Norfolk Island",MP:"Northern Mariana Islands",NO:"Norway",OM:"Oman",PK:"Pakistan",PW:"Palau",PS:"Palestinian Territory, Occupied",PA:"Panama",PG:"Papua New Guinea",PY:"Paraguay",PE:"Peru",PH:"Philippines",PN:"Pitcairn",PL:"Poland",PT:"Portugal",PR:"Puerto Rico",QA:"Qatar",RE:"Reunion",RO:"Romania",RU:"Russian Federation",RW:"Rwanda",SH:"Saint Helena",KN:"Saint Kitts and Nevis",LC:"Saint Lucia",PM:"Saint Pierre and Miquelon",VC:"Saint Vincent and the Grenadines",WS:"Samoa",SM:"San Marino",ST:"Sao Tome and Principe",SA:"Saudi Arabia",SN:"Senegal",SC:"Seychelles",SL:"Sierra Leone",SG:"Singapore",SK:"Slovakia",SI:"Slovenia",SB:"Solomon Islands",SO:"Somalia",ZA:"South Africa",GS:"South Georgia and the South Sandwich Islands",ES:"Spain",LK:"Sri Lanka",SD:"Sudan",SR:"Suriname",SJ:"Svalbard and Jan Mayen",SZ:"Swaziland",SE:"Sweden",CH:"Switzerland",SY:"Syrian Arab Republic",TW:"Taiwan",TJ:"Tajikistan",TZ:"Tanzania, United Republic of",TH:"Thailand",TL:"Timor-Leste",TG:"Togo",TK:"Tokelau",TO:"Tonga",TT:"Trinidad and Tobago",TN:"Tunisia",TR:"Turkey",TM:"Turkmenistan",TC:"Turks and Caicos Islands",TV:"Tuvalu",UG:"Uganda",UA:"Ukraine",AE:"United Arab Emirates",GB:"United Kingdom",US:"United States of America",UM:"United States Minor Outlying Islands",UY:"Uruguay",UZ:"Uzbekistan",VU:"Vanuatu",VE:"Venezuela",VN:"Viet Nam",VG:"Virgin Islands, British",VI:"Virgin Islands, U.S.",WF:"Wallis and Futuna",EH:"Western Sahara",YE:"Yemen",ZM:"Zambia",ZW:"Zimbabwe",AX:"Åland Islands",BQ:"Bonaire, Sint Eustatius and Saba",CW:"Curaçao",GG:"Guernsey",IM:"Isle of Man",JE:"Jersey",ME:"Montenegro",BL:"Saint Barthélemy",MF:"Saint Martin (French part)",RS:"Serbia",SX:"Sint Maarten (Dutch part)",SS:"South Sudan",XK:"Kosovo"};
</script>

<script>
    import tippy from "sveltejs-tippy";

    export let flag;
</script>

<div class={flag} use:tippy={{content: countries[flag],placement:"top",}}/>

<style>
.GR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -5px;
}
.OM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -5px;
}
._commonwealth {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -37px;
}
.ID {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -37px;
}
.MW {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -5px;
}
.TH {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -37px;
}
.GB {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -69px;
}
.KE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -69px;
}
.ST {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -69px;
}
.NR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -5px;
}
.KW {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -37px;
}
.WS {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -69px;
}
.RW {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -101px;
}
.TM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -101px;
}
.JE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -101px;
}
.NI {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -101px;
}
.SG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -5px;
}
.PF {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -37px;
}
.JO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -69px;
}
.MZ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -101px;
}
.FJ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -133px;
}
.EG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -133px;
}
.IN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -133px;
}
.SH {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -133px;
}
._olympics {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -133px;
}
.TR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -5px;
}
.MU {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -37px;
}
.KH {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -69px;
}
.FK {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -101px;
}
.GW {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -133px;
}
.KM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -165px;
}
.CN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -165px;
}
.NZ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -165px;
}
.GD {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -165px;
}
.PA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -165px;
}
.NU {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -165px;
}
.LR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -5px;
}
.LK {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -37px;
}
.AW {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -69px;
}
.NC {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -101px;
}
.VC {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -133px;
}
.NO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -165px;
}
.TT {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -197px;
}
.AU {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -197px;
}
.CR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -197px;
}
.SM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -197px;
}
.LV {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -197px;
}
.IS {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -197px;
}
.NL {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -197px;
}
.TD {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -5px;
}
._british_antarctic_territory {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -37px;
}
.SN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -69px;
}
.ME {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -101px;
}
._red_cross {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -133px;
}
.BG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -165px;
}
.MM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -197px;
}
.BO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -229px;
}
.BL {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -229px;
}
.CA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -229px;
}
.CH {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -229px;
}
.HK {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -229px;
}
.GT {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -229px;
}
.LC {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -229px;
}
.SC {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -229px;
}
.TK {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -5px;
}
.YE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -37px;
}
.ET {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -69px;
}
.SA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -101px;
}
.ES {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -133px;
}
.PS {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -165px;
}
.LU {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -197px;
}
.UA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -229px;
}
.SO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -261px;
}
.GY {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -261px;
}
.CX {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -261px;
}
.UY {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -261px;
}
.KI {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -261px;
}
.PT {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -261px;
}
.GG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -261px;
}
.SI {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -261px;
}
.CL {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -261px;
}
.TG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -5px;
}
.ER {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -37px;
}
.GL {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -69px;
}
.VN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -101px;
}
.AM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -133px;
}
.YT {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -165px;
}
.FO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -197px;
}
.FI {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -229px;
}
._basque_country {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -261px;
}
.ZA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -293px;
}
.UG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -293px;
}
.SV {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -293px;
}
.MA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -293px;
}
.MV {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -293px;
}
.PE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -293px;
}
.AQ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -293px;
}
.SS {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -293px;
}
.SZ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -293px;
}
.ML {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -293px;
}
.AT {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -5px;
}
.EC {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -37px;
}
.JP {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -69px;
}
.LT {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -101px;
}
.TJ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -133px;
}
.GS {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -165px;
}
.CD {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -197px;
}
.RS {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -229px;
}
.GH {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -261px;
}
.BS {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -293px;
}
.JM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -325px;
}
.TV {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -325px;
}
.IC {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -325px;
}
.FR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -325px;
}
.LS {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -325px;
}
.GQ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -325px;
}
.GU {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -325px;
}
.TL {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -325px;
}
.MT {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -325px;
}
.EH {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -325px;
}
.SD {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -325px;
}
.IE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -5px;
}
.MS {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -37px;
}
.VG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -69px;
}
.BI {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -101px;
}
.CO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -133px;
}
.AZ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -165px;
}
.RU {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -197px;
}
.SK {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -229px;
}
.PH {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -261px;
}
.HR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -293px;
}
.SR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -325px;
}
.CY {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -357px;
}
.SB {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -357px;
}
.PK {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -357px;
}
.CW {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -357px;
}
.PG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -357px;
}
.AO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -357px;
}
.DM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -357px;
}
.UZ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -357px;
}
._mars {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -357px;
}
._united_nations {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -357px;
}
.KG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -357px;
}
.AX {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -357px;
}
.AR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -5px;
}
.MG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -37px;
}
.BZ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -69px;
}
.DO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -101px;
}
.BM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -133px;
}
.AG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -165px;
}
._wales {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -197px;
}
.MH {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -229px;
}
.MF {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -261px;
}
.TC {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -293px;
}
._nagorno_karabakh {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -325px;
}
.EE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -357px;
}
._northern_cyprus {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -389px;
}
.NG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -389px;
}
.VI {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -389px;
}
.BR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -389px;
}
.CI {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -389px;
}
.CV {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -389px;
}
.BT {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -389px;
}
._unknown {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -389px;
}
.KN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -389px;
}
.KR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -389px;
}
.AL {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -389px;
}
.DJ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -389px;
}
.PL {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -389px;
}
._gosquared {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -5px;
}
.BA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -37px;
}
.BW {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -69px;
}
.GM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -101px;
}
.MP {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -133px;
}
.VU {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -165px;
}
.SY {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -197px;
}
.WF {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -229px;
}
.MQ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -261px;
}
.BN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -293px;
}
.NP {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -325px;
}
.BY {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -357px;
}
.DK {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -389px;
}
.US {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -421px;
}
.BD {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -421px;
}
.PW {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -421px;
}
.NF {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -421px;
}
.GI {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -421px;
}
.IQ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -421px;
}
.IL {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -421px;
}
.PY {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -421px;
}
.CM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -421px;
}
.PN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -421px;
}
.FM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -421px;
}
.BB {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -421px;
}
.GE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -421px;
}
.CF {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -421px;
}
.KP {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -5px;
}
.QA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -37px;
}
.BH {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -69px;
}
.TZ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -101px;
}
.DZ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -133px;
}
.AS {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -165px;
}
.CC {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -197px;
}
.CG {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -229px;
}
.AE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -261px;
}
.GN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -293px;
}
.KY {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -325px;
}
.EU {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -357px;
}
.HU {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -389px;
}
.BE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -421px;
}
.TN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -453px;
}
.AD {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -453px;
}
.CZ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -453px;
}
._somaliland {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -453px;
}
.TW {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -453px;
}
.ZM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -453px;
}
.VE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -453px;
}
._abkhazia {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -453px;
}
.CK {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -453px;
}
.IM {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -453px;
}
.LA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -453px;
}
.HT {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -453px;
}
.GA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -453px;
}
.AI {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -453px;
}
.MR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -453px;
}
.IT {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -5px;
}
.AF {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -37px;
}
.NA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -69px;
}
._south_ossetia {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -101px;
}
.LY {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -133px;
}
.AN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -165px;
}
.BJ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -197px;
}
._nato {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -229px;
}
.HN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -261px;
}
._kosovo {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -293px;
}
.SE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -325px;
}
.NE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -357px;
}
.RO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -389px;
}
.ZW {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -421px;
}
.BF {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -453px;
}
.MO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -0 -485px;
}
.MK {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -32px -485px;
}
.SL {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -64px -485px;
}
.MX {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -96px -485px;
}
.VA {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -128px -485px;
}
.TF {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -160px -485px;
}
._scotland {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -192px -485px;
}
.KZ {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -224px -485px;
}
.CU {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -256px -485px;
}
.MY {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -288px -485px;
}
.IR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -320px -485px;
}
.PR {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -352px -485px;
}
._england {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -384px -485px;
}
.DE {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -416px -485px;
}
.MN {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -448px -485px;
}
.LB {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -480px -485px;
}
.TO {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -512px -5px;
}
.MD {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -512px -37px;
}
.LI {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -512px -69px;
}
.MC {
    width: 32px; height: 22px;
    background: url('../img/flags.png') -512px -101px;
}
</style>