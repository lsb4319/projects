import folium
from branca.element import Template, MacroElement
import webbrowser, os



premier = [
    {"club": "Arsenal", "stadium": "Emirates Stadium", "lat": 51.5549, "lon": -0.1084},
    {"club": "Aston Villa", "stadium": "Villa Park", "lat": 52.5090, "lon": -1.8847},
    {"club": "Bournemouth", "stadium": "Vitality Stadium", "lat": 50.7352, "lon": -1.8383},
    {"club": "Brentford", "stadium": "Gtech Community Stadium", "lat": 51.4882, "lon": -0.2886},
    {"club": "Brighton", "stadium": "Amex Stadium", "lat": 50.8618, "lon": -0.0831},
    {"club": "Hull City", "stadium": "MKM Stadium", "lat": 53.7461, "lon": -0.3678},       # promoted
    {"club": "Chelsea", "stadium": "Stamford Bridge", "lat": 51.4816, "lon": -0.1910},
    {"club": "Crystal Palace", "stadium": "Selhurst Park", "lat": 51.3983, "lon": -0.0855},
    {"club": "Everton", "stadium": "Hill Dickinson Stadium", "lat": 53.4489, "lon": -2.9862},  # new stadium
    {"club": "Fulham", "stadium": "Craven Cottage", "lat": 51.4749, "lon": -0.2217},
    {"club": "Leeds United", "stadium": "Elland Road", "lat": 53.7774, "lon": -1.5726},  # promoted
    {"club": "Liverpool", "stadium": "Anfield", "lat": 53.4308, "lon": -2.9608},
    {"club": "Manchester City", "stadium": "Etihad Stadium", "lat": 53.4831, "lon": -2.2004},
    {"club": "Manchester United", "stadium": "Old Trafford", "lat": 53.4631, "lon": -2.2913},
    {"club": "Newcastle", "stadium": "St. James' Park", "lat": 54.9756, "lon": -1.6218},
    {"club": "Nottingham Forest", "stadium": "City Ground", "lat": 52.9400, "lon": -1.1326},
    {"club": "Sunderland", "stadium": "Stadium of Light", "lat": 54.9146, "lon": -1.3883},  # promoted
    {"club": "Tottenham", "stadium": "Tottenham Hotspur Stadium", "lat": 51.6044, "lon": -0.0665},
    {"club": "Coventry City", "stadium": "Coventry Building Society Arena", "lat": 52.4481, "lon": -1.4956},
    {"club": "Ipswich Town", "stadium": "Portman Road", "lat": 52.055, "lon": 1.14528},
]

championship = [
   {"club": "Birmingham City",          "stadium": "St Andrew's",                       "lat": 52.4758, "lon": -1.8683},
   {"club": "Blackburn Rovers",         "stadium": "Ewood Park",                        "lat": 53.7286, "lon": -2.4892},
   {"club": "Bolton Wanderers",         "stadium": "Toughsheet Community Stadium",      "lat": 53.5805, "lon": -2.5357},
   {"club": "Bristol City",             "stadium": "Ashton Gate",                       "lat": 51.4400, "lon": -2.6206},
   {"club": "Burnley",                  "stadium": "Turf Moor",                         "lat": 53.7890, "lon": -2.2300},
   {"club": "Cardiff City",             "stadium": "Cardiff City Stadium",              "lat": 51.4728, "lon": -3.2031},
   {"club": "Charlton Athletic",        "stadium": "The Valley",                        "lat": 51.4865, "lon":  0.0364},
   {"club": "Derby County",             "stadium": "Pride Park Stadium",                "lat": 52.9150, "lon": -1.4470},
   {"club": "Lincoln City",             "stadium": "Sincil Bank (LNER Stadium)",        "lat": 53.2182, "lon": -0.5403},
   {"club": "Middlesbrough",            "stadium": "Riverside Stadium",                 "lat": 54.5783, "lon": -1.2169},
   {"club": "Millwall",                 "stadium": "The Den",                           "lat": 51.4860, "lon": -0.0507},
   {"club": "Norwich City",             "stadium": "Carrow Road",                       "lat": 52.6220, "lon":  1.3091},
   {"club": "Portsmouth",               "stadium": "Fratton Park",                      "lat": 50.7963, "lon": -1.0639},
   {"club": "Preston North End",        "stadium": "Deepdale",                          "lat": 53.7722, "lon": -2.6883},
   {"club": "Queens Park Rangers",      "stadium": "Loftus Road",                       "lat": 51.5093, "lon": -0.2320},
   {"club": "Sheffield United",         "stadium": "Bramall Lane",                      "lat": 53.3703, "lon": -1.4709},
   {"club": "Southampton",              "stadium": "St Mary's Stadium",                 "lat": 50.9058, "lon": -1.3911},
   {"club": "Stoke City",               "stadium": "bet365 Stadium",                    "lat": 52.9883, "lon": -2.1756},
   {"club": "Swansea City",             "stadium": "Swansea.com Stadium",               "lat": 51.6422, "lon": -3.9347},
   {"club": "Wrexham",                  "stadium": "Racecourse Ground (SToK Cae Ras)",  "lat": 53.0506, "lon": -2.9931},
   {"club": "West Ham United",          "stadium": "London Stadium",                    "lat": 51.5386, "lon": -0.0166},
   {"club": "Wolverhampton Wanderers",  "stadium": "Molineux Stadium",                  "lat": 52.5903, "lon": -2.1303},
]

league_one= [
    {"club": "AFC Wimbledon",          "stadium": "Plough Lane",                 "lat": 51.4317, "lon": -0.1911},
    {"club": "Barnsley",               "stadium": "Oakwell",                     "lat": 53.5522, "lon": -1.4677},
    {"club": "Blackpool",              "stadium": "Bloomfield Road",             "lat": 53.8046, "lon": -3.0481},
    {"club": "Bradford City",          "stadium": "Valley Parade",               "lat": 53.8042, "lon": -1.7592},
    {"club": "Bromley",                "stadium": "Hayes Lane",                  "lat": 51.3942, "lon":  0.0203},
    {"club": "Burton Albion",          "stadium": "Pirelli Stadium",            "lat": 52.8217, "lon": -1.6275},
    {"club": "Cambridge United",       "stadium": "Abbey Stadium",               "lat": 52.2122, "lon":  0.1542},
    {"club": "Doncaster Rovers",       "stadium": "Eco-Power Stadium",           "lat": 53.5097, "lon": -1.1133},
    {"club": "Huddersfield Town",      "stadium": "Kirklees Stadium",            "lat": 53.6542, "lon": -1.7682},
    {"club": "Leicester City",         "stadium": "King Power Stadium",          "lat": 52.6204, "lon": -1.1422},
    {"club": "Leyton Orient",          "stadium": "Brisbane Road",               "lat": 51.5601, "lon": -0.0125},
    {"club": "Luton Town",             "stadium": "Kenilworth Road",             "lat": 51.8842, "lon": -0.4317},
    {"club": "Mansfield Town",         "stadium": "Field Mill (One Call Stadium)","lat": 53.1378, "lon": -1.2003},
    {"club": "Milton Keynes Dons",     "stadium": "Stadium MK",                  "lat": 52.0094, "lon": -0.7332},
    {"club": "Notts County",           "stadium": "Meadow Lane",                 "lat": 52.9523, "lon": -1.1357},
    {"club": "Oxford United",          "stadium": "Kassam Stadium",              "lat": 51.7164, "lon": -1.2083},
    {"club": "Peterborough United",    "stadium": "London Road Stadium",         "lat": 52.5648, "lon": -0.2403},
    {"club": "Plymouth Argyle",        "stadium": "Home Park",                   "lat": 50.3881, "lon": -4.1508},
    {"club": "Reading",                "stadium": "Madejski Stadium",            "lat": 51.4222, "lon": -0.9827},
    {"club": "Sheffield Wednesday",    "stadium": "Hillsborough Stadium",        "lat": 53.4114, "lon": -1.5006},
    {"club": "Stevenage",              "stadium": "Broadhall Way (Lamex Stadium)","lat": 51.8895, "lon": -0.1936},
    {"club": "Stockport County",       "stadium": "Edgeley Park",                "lat": 53.4045, "lon": -2.1664},
    {"club": "Wigan Athletic",         "stadium": "Brick Community Stadium",     "lat": 53.5478, "lon": -2.6539},
    {"club": "Wycombe Wanderers",      "stadium": "Adams Park",                  "lat": 51.6306, "lon": -0.8003},
]

league_two = [
    {"club": "Accrington Stanley",  "stadium": "Crown Ground (Wham Stadium)",        "lat": 53.7686, "lon": -2.3705},
    {"club": "Barnet",              "stadium": "The Hive Stadium",                   "lat": 51.6003, "lon": -0.2934},
    {"club": "Bristol Rovers",      "stadium": "Memorial Stadium",                   "lat": 51.4862, "lon": -2.5836},
    {"club": "Cheltenham Town",     "stadium": "Whaddon Road",                       "lat": 51.9069, "lon": -2.0608},
    {"club": "Chesterfield",        "stadium": "SMH Group Stadium",                  "lat": 53.2469, "lon": -1.4275},
    {"club": "Colchester United",   "stadium": "Colchester Community Stadium",       "lat": 51.9237, "lon":  0.8997},
    {"club": "Crawley Town",        "stadium": "Broadfield Stadium",                 "lat": 51.0976, "lon": -0.1944},
    {"club": "Crewe Alexandra",     "stadium": "Gresty Road (Mornflake Stadium)",    "lat": 53.0890, "lon": -2.4356},
    {"club": "Exeter City",         "stadium": "St James Park",                      "lat": 50.7301, "lon": -3.5215},
    {"club": "Fleetwood Town",      "stadium": "Highbury Stadium",                   "lat": 53.9181, "lon": -3.0156},
    {"club": "Gillingham",          "stadium": "Priestfield Stadium",               "lat": 51.3847, "lon":  0.5608},
    {"club": "Grimsby Town",        "stadium": "Blundell Park",                      "lat": 53.5697, "lon": -0.0461},
    {"club": "Newport County",      "stadium": "Rodney Parade",                      "lat": 51.5897, "lon": -2.9869},
    {"club": "Northampton Town",    "stadium": "Sixfields Stadium",                  "lat": 52.2353, "lon": -0.9333},
    {"club": "Oldham Athletic",     "stadium": "Boundary Park",                      "lat": 53.5556, "lon": -2.1283},
    {"club": "Port Vale",           "stadium": "Vale Park",                          "lat": 53.0503, "lon": -2.1922},
    {"club": "Rochdale",            "stadium": "Spotland Stadium (Crown Oil Arena)", "lat": 53.6209, "lon": -2.1869},
    {"club": "Rotherham United",    "stadium": "New York Stadium",                   "lat": 53.4280, "lon": -1.3620},
    {"club": "Salford City",        "stadium": "Moor Lane (Peninsula Stadium)",      "lat": 53.5125, "lon": -2.2786},
    {"club": "Shrewsbury Town",     "stadium": "New Meadow",                         "lat": 52.6883, "lon": -2.7491},
    {"club": "Swindon Town",        "stadium": "County Ground",                      "lat": 51.5644, "lon": -1.7711},
    {"club": "Tranmere Rovers",     "stadium": "Prenton Park",                       "lat": 53.3736, "lon": -3.0328},
    {"club": "Walsall",             "stadium": "Bescot Stadium",                     "lat": 52.5656, "lon": -1.9908},
    {"club": "York City",           "stadium": "York Community Stadium",             "lat": 53.9897, "lon": -1.0556},
]
m = folium.Map(location=[52.5, -1.5], zoom_start=7.25)

for s in premier:
  folium.Marker(
    location=[s["lat"], s["lon"]],
    popup=folium.Popup(f"<b>{s['club']}</b><br>{s['stadium']}", max_width=200),
    tooltip=s["club"] + " </br> " + s["stadium"] + "</br>" + " Premier",
    icon=folium.Icon(color="red", icon="futbol", prefix="fa", zIndexOffset=3),
  ).add_to(m)

for s in championship:
  folium.Marker(
    location=[s["lat"], s["lon"]],
    popup=folium.Popup(f"<b>{s['club']}</b><br>{s['stadium']}", max_width=200),
    tooltip=s["club"] + " </br> " + s["stadium"] + "</br>" + " Championship",
    icon=folium.Icon(color="blue", icon="futbol", prefix="fa", zIndexOffset=2),
  ).add_to(m)

for s in league_one:
  folium.Marker(
    location=[s["lat"], s["lon"]],
    popup=folium.Popup(f"<b>{s['club']}</b><br>{s['stadium']}", max_width=200),
    tooltip=s["club"] + " </br> " + s["stadium"] + "</br>" + " League One",
    icon=folium.Icon(color="green", icon="futbol", prefix="fa", zIndexOffset=1),
  ).add_to(m)

for s in league_two:
  folium.Marker(
    location=[s["lat"], s["lon"]],
    popup=folium.Popup(f"<b>{s['club']}</b><br>{s['stadium']}", max_width=200),
    tooltip=s["club"] + " </br> " + s["stadium"] + "</br>" + " League Two",
    icon=folium.Icon(color="orange", icon="futbol", prefix="fa", zIndexOffset=0),
  ).add_to(m)

legend_html = """
{% macro html(this, kwargs) %}
<div style="
  position: fixed;
  top: 10px;
  right: 10px;
  width: 160px;
  background: white;
  border:2px solid grey;
  z-index:9999;
  font-size:14px;
  padding: 8px;
  box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
">
  <b>League Legend</b><br>
  <i class="fa fa-map-marker" style="color:red"></i>&nbsp;Premier<br>
  <i class="fa fa-map-marker" style="color:blue"></i>&nbsp;Championship<br>
  <i class="fa fa-map-marker" style="color:green"></i>&nbsp;League One<br>
  <i class="fa fa-map-marker" style="color:orange"></i>&nbsp;League Two
</div>
{% endmacro %}
"""

template = Template(legend_html)
macro = MacroElement()
macro._template = template
m.get_root().add_child(macro)


m.save("epl_stadiums.html")
webbrowser.open("file://" + os.path.abspath("epl_stadiums.html"))