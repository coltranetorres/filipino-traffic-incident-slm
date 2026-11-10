# Error analysis

143 of 176 items have at least one wrong field (incident_type, severity, road_obstruction, language, any location field, or invalid JSON).

## Count summary

### By gold incident class

| group | errors / size |
|---|---|
| vehicle_breakdown | 19 / 22 |
| road_accident | 19 / 23 |
| road_hazard | 18 / 21 |
| flooding | 24 / 24 |
| road_closure | 15 / 23 |
| heavy_traffic | 15 / 23 |
| other | 17 / 20 |
| unknown | 16 / 20 |

### By subset tag

| group | errors / size |
|---|---|
| noisy | 22 / 26 |
| no_location | 7 / 9 |
| short | 6 / 10 |
| ambiguous | 15 / 18 |
| contradictory | 10 / 10 |

### By language

| group | errors / size |
|---|---|
| filipino | 34 / 38 |
| english | 18 / 28 |
| taglish | 91 / 110 |

## Wrong items by gold incident class

### vehicle_breakdown (19)

- `te-002` [taglish; tags: -] Sira yung makina ng bus sa Aurora, kaya mahaba ang pila ng sasakyan
  - errors: incident_type: gold=vehicle_breakdown pred=road_hazard; severity: gold=medium pred=high
  - predicted: {"incident_type":"road_hazard","location":{"road":"Aurora Boulevard","landmark":null,"direction":null},"severity":"high","road_obstruction":"unknown","language":"taglish"}
- `te-010` [taglish; tags: ambiguous] tricycle nasiraan sa gitna ng Dr. A. Santos Ave, naghihintay ng tulong
  - errors: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"Dr. A. Santos Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-017` [taglish; tags: -] naghihirap ang daloy sa Ortigas Ave Extension, naka-hazard ang van
  - errors: incident_type: gold=vehicle_breakdown pred=road_hazard
  - predicted: {"incident_type":"road_hazard","location":{"road":"Ortigas Avenue Extension","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-018` [taglish; tags: -] PUV na nasira sa may Cubao, wala namang nakaharang
  - errors: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_accident","location":{"road":null,"landmark":"Cubao","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-036` [taglish; tags: -] Tumirik ang L300 van sa kanang lane ng SLEX, hinihila na
  - errors: severity: gold=medium pred=unknown; road_obstruction: gold=partial pred=unknown; location.landmark: gold=None pred=L300 van
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"SLEX","landmark":"L300 van","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-037` [taglish; tags: -] Tumigil ang bus sa Taft Ave. southbound sa tapat ng LRT Libertad, mabagal na ang daloy
  - errors: incident_type: gold=vehicle_breakdown pred=road_accident; location.landmark: gold=LRT Libertad pred=Libertad
  - predicted: {"incident_type":"road_accident","location":{"road":"Taft Avenue","landmark":"Libertad","direction":"southbound"},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-038` [taglish; tags: ambiguous] wala nang gas ang kotse sa gitna ng Aurora, tinutulak ng mga tao
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Aurora Boulevard","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-039` [taglish; tags: -] sira ang aircon bus sa Ayala Ave tapos nakahinto pa sa bus stop
  - errors: severity: gold=low pred=medium
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Ayala Avenue","landmark":"Bus Stop","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-040` [english; tags: -] Truck stalled on the C5 flyover near Bagong Ilog, hazard on
  - errors: severity: gold=unknown pred=medium; language: gold=english pred=taglish
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"C5","landmark":"Bagong Ilog","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-041` [taglish; tags: -] umuusok ang makina ng jeep sa Mindanao Ave, nakatabi
  - errors: severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Mindanao Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-042` [taglish; tags: -] Nakatirik pa rin ang trailer truck sa NLEX Bocaue, kanang lane
  - errors: road_obstruction: gold=partial pred=unknown
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"NLEX","landmark":"Bocaue","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-043` [taglish; tags: -] dead battery daw ung SUV sa Marcos Hwy Marikina side, nakaharang pa sa lane
  - errors: road_obstruction: gold=partial pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Marcos Highway","landmark":"Marikina","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-044` [taglish; tags: -] Taxi broke down sa Roxas Blvd sb near MOA, 2 lanes blocked daw
  - errors: location.direction: gold=southbound pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Roxas Boulevard","landmark":"MOA","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-045` [taglish; tags: -] stalled ang ambulance sa Quezon Ave, pls give way
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-046` [taglish; tags: -] Nagkaproblema sa makina ang tricycle sa Katipunan, nasa gilid na
  - errors: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_accident","location":{"road":"Katipunan Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"filipino"}
- `te-048` [taglish; tags: -] Bus napagod ata, tumirik sa EDSA Boni, full stop traffic
  - errors: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"Boni","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-151` [taglish; tags: noisy] tumirik jeep sa tpat ng ust, 1 lne lng bukas
  - errors: road_obstruction: gold=partial pred=unknown; location.landmark: gold=UST pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-152` [taglish; tags: noisy] stalled truck sa cmwlth near fairview ingat
  - errors: severity: gold=unknown pred=medium; location.road: gold=Commonwealth Avenue pred=CMW
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"CMW","landmark":"Fairview","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-174` [taglish; tags: contradictory] Truck na sira sa EDSA pero tumatakbo naman ang lahat ng lane
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}

### road_accident (19)

- `te-001` [taglish; tags: -] Nabaligtad na delivery truck sa Nagtahan, kalat ang gulay sa kalsada
  - errors: incident_type: gold=road_accident pred=road_hazard; language: gold=taglish pred=filipino; location.road: gold=Nagtahan pred=None; location.landmark: gold=None pred=Nagtahan
  - predicted: {"incident_type":"road_hazard","location":{"road":null,"landmark":"Nagtahan","direction":null},"severity":"medium","road_obstruction":"unknown","language":"filipino"}
- `te-007` [filipino; tags: -] may aksidente na naman sa Kalayaan flyover, pila hanggang Buendia
  - errors: language: gold=filipino pred=taglish; location.road: gold=Kalayaan Avenue pred=Kalayaan; location.landmark: gold=Kalayaan flyover pred=Buendia
  - predicted: {"incident_type":"road_accident","location":{"road":"Kalayaan","landmark":"Buendia","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-015` [english; tags: -] Vehicular accident at Katipunan-Boni Serrano, sedan hit a post, no injuries, lane partially blocked.
  - errors: severity: gold=medium pred=low; location.road: gold=Katipunan Avenue pred=Katipunan Boulevard
  - predicted: {"incident_type":"road_accident","location":{"road":"Katipunan Boulevard","landmark":"Boni Serrano","direction":null},"severity":"low","road_obstruction":"partial","language":"english"}
- `te-025` [taglish; tags: contradictory] Minor lang daw ang banggaan sa C5 pero buong kalsada ay sarado
  - errors: incident_type: gold=road_accident pred=road_closure; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_closure","location":{"road":"C5","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"filipino"}
- `te-029` [english; tags: noisy, short] accident mc arthur hway valenzuela
  - errors: location.road: gold=McArthur Highway pred=McArthur; location.landmark: gold=Valenzuela pred=Hwy
  - predicted: {"incident_type":"road_accident","location":{"road":"McArthur","landmark":"Hwy","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"english"}
- `te-033` [taglish; tags: -] dalawang motor nagbanggaan sa Visayas Ave, nasa gilid na
  - errors: severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown
  - predicted: {"incident_type":"road_accident","location":{"road":"Visayas Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-049` [taglish; tags: -] Sumalpok ang SUV sa center island ng Commonwealth, walang nasaktan
  - errors: location.landmark: gold=None pred=Center Island
  - predicted: {"incident_type":"road_accident","location":{"road":"Commonwealth Avenue","landmark":"Center Island","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-050` [taglish; tags: -] Banggaan ng bus at jeep sa EDSA Ortigas flyover, may mga sugatan, 3 lane ang sarado
  - errors: severity: gold=high pred=medium
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"Ortigas flyover","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-051` [taglish; tags: -] Hit and run sa Shaw, isang pedestrian ang dinala sa ospital
  - errors: severity: gold=high pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"Shaw Boulevard","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-053` [taglish; tags: -] Tumaob ang tricycle sa Visayas Ave, nagtutulungan ang mga tao
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"Visayas Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-055` [taglish; tags: noisy] accdent sa edsa guadalupe, 2 trak, madaming tao
  - errors: severity: gold=unknown pred=medium
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"Guadalupe","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-056` [english; tags: -] Chain collision along Marcos Highway westbound, 4 vehicles involved, all lanes blocked
  - errors: severity: gold=high pred=medium
  - predicted: {"incident_type":"road_accident","location":{"road":"Marcos Highway","landmark":null,"direction":"westbound"},"severity":"medium","road_obstruction":"full","language":"english"}
- `te-057` [taglish; tags: -] May nabangga na naman sa Taft, ayun nakahandusay pa ang motor
  - errors: severity: gold=unknown pred=medium
  - predicted: {"incident_type":"road_accident","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-058` [taglish; tags: -] Nasalpok ng truck ang overpass railing sa C5 Pasig, kalahati ng daan bukas
  - errors: incident_type: gold=road_accident pred=road_hazard; road_obstruction: gold=partial pred=unknown
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":"Pasig","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-059` [english; tags: -] bus vs tricycle collision near Cubao terminal, no word on injuries
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":null,"landmark":"Cubao terminal","direction":null},"severity":"low","road_obstruction":"none","language":"english"}
- `te-153` [taglish; tags: noisy] bngga ng bus ung kotse sa roxas blvd, 1 lane blckd
  - errors: incident_type: gold=road_accident pred=road_closure
  - predicted: {"incident_type":"road_closure","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-154` [taglish; tags: noisy] aksdnte sa slex sb, ambulansya andito na
  - errors: severity: gold=high pred=medium; location.road: gold=SLEX pred=None; location.direction: gold=southbound pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-172` [taglish; tags: contradictory] Sabi walang accident sa SLEX pero sarado ang dalawang lane
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"road_accident","location":{"road":"SLEX","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-176` [taglish; tags: contradictory] No injuries pero dalawang ambulansya ang nandito sa Commonwealth crash
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"Commonwealth Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}

### road_hazard (18)

- `te-008` [filipino; tags: -] Maraming bato sa Marcos Hwy
  - errors: severity: gold=medium pred=unknown
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-014` [filipino; tags: -] Ingat sa Congressional, madulas dahil sa ulan
  - errors: incident_type: gold=road_hazard pred=heavy_traffic; severity: gold=low pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Congressional Avenue pred=None
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"filipino"}
- `te-060` [taglish; tags: -] Nalaglag ang mga bakal ng truck sa Marcos Highway, kalat sa dalawang lane
  - errors: incident_type: gold=road_hazard pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=partial pred=unknown; location.road: gold=SLEX pred=Marcos Highway
  - predicted: {"incident_type":"road_accident","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-061` [taglish; tags: -] Natanggal ang takip ng drainage sa Taft near Vito Cruz, delikado sa motor
  - errors: severity: gold=low pred=medium; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_hazard","location":{"road":"Taft Avenue","landmark":"Vito Cruz","direction":null},"severity":"medium","road_obstruction":"unknown","language":"filipino"}
- `te-062` [filipino; tags: -] May butas na kalsada sa Quezon Avenue, ingat
  - errors: severity: gold=low pred=medium; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-063` [taglish; tags: -] May natumbang billboard sa Commonwealth, hindi na madaanan
  - errors: severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown
  - predicted: {"incident_type":"road_hazard","location":{"road":"Commonwealth Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-064` [taglish; tags: -] Gumuhong lupa sa Marcos Highway Antipolo, isang lane ang natabunan
  - errors: severity: gold=medium pred=unknown; road_obstruction: gold=partial pred=unknown
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway","landmark":"Antipolo","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-065` [filipino; tags: -] Kalat ang basura sa kalsada sa Dimasalang matapos ang baha
  - errors: location.road: gold=Dimasalang pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":null,"landmark":null,"direction":null},"severity":"low","road_obstruction":"unknown","language":"filipino"}
- `te-067` [filipino; tags: -] May butas sa tulay ng Guadalupe, may nasirang gulong na
  - errors: severity: gold=low pred=unknown; location.road: gold=None pred=Guadalupe Avenue; location.landmark: gold=Guadalupe pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Guadalupe Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-068` [taglish; tags: -] Sirang manhole cover sa Roxas Boulevard, delikado sa mga nagmomotor
  - errors: severity: gold=low pred=medium
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-069` [taglish; tags: -] Nagkalat na bubog at bakal sa EDSA southbound pagkatapos ng aksidente
  - errors: incident_type: gold=road_hazard pred=road_accident; location.landmark: gold=None pred=southbound
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"southbound","direction":"southbound"},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-070` [filipino; tags: -] May natumbang poste ng Meralco sa Kamias, kalahati ng kalye nakaharang
  - errors: severity: gold=medium pred=unknown; road_obstruction: gold=partial pred=unknown; location.road: gold=None pred=Kamias Avenue; location.landmark: gold=Kamias pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Kamias Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-071` [english; tags: -] Oil spill on Skyway northbound, vehicles slipping
  - errors: severity: gold=medium pred=unknown
  - predicted: {"incident_type":"road_hazard","location":{"road":"Skyway","landmark":null,"direction":"northbound"},"severity":"unknown","road_obstruction":"unknown","language":"english"}
- `te-072` [filipino; tags: -] May mga basura sa kalsada sa Tanay, sagabal sa daan
  - errors: language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":null,"landmark":"Tanay","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-073` [english; tags: -] Boulders on the road at Kennon Road km 5
  - errors: language: gold=english pred=taglish; location.landmark: gold=km 5 pred=Kennon
  - predicted: {"incident_type":"road_hazard","location":{"road":"Kennon Road","landmark":"Kennon","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-074` [taglish; tags: -] Nahulog na container sa Roxas Blvd, nakaharang sa isang lane
  - errors: severity: gold=medium pred=low; road_obstruction: gold=partial pred=unknown
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"low","road_obstruction":"unknown","language":"taglish"}
- `te-155` [taglish; tags: noisy] may nalaglag na sako sa C5 nb sa tapat ng ayala, pls avoid
  - errors: incident_type: gold=road_hazard pred=road_closure; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"C5","landmark":"Ayala","direction":"northbound"},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-156` [filipino; tags: noisy] natumbang puno sa marcos hwy, d na madaan
  - errors: severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}

### flooding (24)

- `te-003` [filipino; tags: -] Sasakyan lumubog sa baha sa Mel Lopez Blvd
  - errors: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_hazard","location":{"road":"Mel Lopez Boulevard","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"filipino"}
- `te-009` [taglish; tags: -] Flooded na naman daw ung underpass sa España, wag nyo na daanan
  - errors: severity: gold=high pred=unknown; location.landmark: gold=underpass pred=None
  - predicted: {"incident_type":"flooding","location":{"road":"España Boulevard","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-019` [taglish; tags: -] BAHA!!! sa Taft near Buendia LRT, tuhod level
  - errors: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=unknown; road_obstruction: gold=partial pred=unknown; location.landmark: gold=Buendia LRT pred=Buendia
  - predicted: {"incident_type":"road_hazard","location":{"road":"Taft Avenue","landmark":"Buendia","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-026` [taglish; tags: noisy] DI MAKADAAN BUS SA FLOODED NA ESPAÑA
  - errors: language: gold=taglish pred=filipino; location.landmark: gold=None pred=Flooded Area
  - predicted: {"incident_type":"flooding","location":{"road":"España Boulevard","landmark":"Flooded Area","direction":null},"severity":"high","road_obstruction":"full","language":"filipino"}
- `te-076` [taglish; tags: -] Hanggang bewang na ang baha sa Espana corner Lacson, wala nang dumadaan
  - errors: incident_type: gold=flooding pred=road_closure; severity: gold=high pred=medium; road_obstruction: gold=full pred=partial; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_closure","location":{"road":"España Boulevard","landmark":"Lacson","direction":null},"severity":"medium","road_obstruction":"partial","language":"filipino"}
- `te-077` [taglish; tags: -] Baha sa Roxas Blvd near Manila Bay, hanggang gutter lang
  - errors: incident_type: gold=flooding pred=road_hazard; severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":"Manila Bay","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-078` [taglish; tags: -] Flood sa Commonwealth Batasan, nagsisitigil ang mga sasakyan
  - errors: road_obstruction: gold=unknown pred=full; language: gold=taglish pred=filipino; location.road: gold=Commonwealth Avenue pred=None; location.landmark: gold=Batasan pred=Commonwealth Avenue
  - predicted: {"incident_type":"flooding","location":{"road":null,"landmark":"Commonwealth Avenue","direction":null},"severity":"high","road_obstruction":"full","language":"filipino"}
- `te-079` [filipino; tags: -] Nakalubog sa baha ang kalahati ng kalsada sa Aurora Boulevard
  - errors: incident_type: gold=flooding pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=partial pred=unknown
  - predicted: {"incident_type":"road_accident","location":{"road":"Aurora Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"filipino"}
- `te-080` [taglish; tags: -] Underpass flooded sa Quezon Ave at Mother Ignacia, bawal dumaan ang sedan
  - errors: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=partial pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Quezon Avenue","landmark":"Mother Ignacia","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-081` [filipino; tags: -] Baha sa Marikina, tumataas pa ang tubig
  - errors: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"flooding","location":{"road":null,"landmark":"Marikina","direction":null},"severity":"high","road_obstruction":"full","language":"filipino"}
- `te-082` [taglish; tags: -] Lubog ang kalsada sa Dr. A. Santos Ave, mga motor lang ang nakakalusot
  - errors: incident_type: gold=flooding pred=road_accident; severity: gold=high pred=low; road_obstruction: gold=partial pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"Dr. A. Santos Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-083` [filipino; tags: -] Katamtamang baha lang sa C5 Ortigas, mabagal ang takbo pero pwede pa
  - errors: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":"Ortigas","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-084` [taglish; tags: -] Water at knee level na sa Recto, stranded mga jeep
  - errors: road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"flooding","location":{"road":"Recto Avenue","landmark":null,"direction":null},"severity":"high","road_obstruction":"partial","language":"taglish"}
- `te-085` [filipino; tags: short] Muling bumaha sa Pasong Tamo
  - errors: incident_type: gold=flooding pred=road_closure; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"Pasong Tamo","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"filipino"}
- `te-086` [english; tags: -] Waist-deep flood on Taft Ave near Quirino, even trucks cannot pass
  - errors: road_obstruction: gold=full pred=partial
  - predicted: {"incident_type":"flooding","location":{"road":"Taft Avenue","landmark":"Quirino","direction":null},"severity":"high","road_obstruction":"partial","language":"english"}
- `te-087` [taglish; tags: -] Binaha ang EDSA Kamuning northbound, isang lane lang ang ligtas
  - errors: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=low
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":"Kamuning","direction":"northbound"},"severity":"low","road_obstruction":"partial","language":"taglish"}
- `te-088` [taglish; tags: noisy] baha d2 sa Dimasalang, pls avoid
  - errors: incident_type: gold=flooding pred=road_hazard; location.landmark: gold=None pred=Baha
  - predicted: {"incident_type":"road_hazard","location":{"road":"Dimasalang","landmark":"Baha","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-089` [filipino; tags: short, ambiguous] Binaha na ba ang Shaw ngayon?
  - errors: incident_type: gold=flooding pred=unknown; location.road: gold=Shaw Boulevard pred=None
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-090` [filipino; tags: -] Malalim na baha sa ilalim ng tulay sa Pasig, hindi madaanan ng kahit anong sasakyan
  - errors: severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown
  - predicted: {"incident_type":"flooding","location":{"road":null,"landmark":"Pasig","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-157` [taglish; tags: noisy] bha n nmn sa espna, lubog na mga kotse
  - errors: incident_type: gold=flooding pred=heavy_traffic; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=none; language: gold=taglish pred=filipino; location.road: gold=España Boulevard pred=None
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"filipino"}
- `te-158` [taglish; tags: noisy] flooded na ang quezn ave cor timog, d makadaan sedan
  - errors: severity: gold=high pred=unknown; road_obstruction: gold=partial pred=unknown; location.landmark: gold=Timog pred=Corazon; location.direction: gold=None pred=eastbound
  - predicted: {"incident_type":"flooding","location":{"road":"Quezon Avenue","landmark":"Corazon","direction":"eastbound"},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-159` [taglish; tags: noisy] ankle deep lng baha sa rox blvd, ok pa
  - errors: severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; location.landmark: gold=None pred=Lng. Baha
  - predicted: {"incident_type":"flooding","location":{"road":"Roxas Boulevard","landmark":"Lng. Baha","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-170` [taglish; tags: contradictory] Wala daw bumaha sa Recto pero stranded ang mga bus
  - errors: incident_type: gold=flooding pred=road_accident; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"Recto Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-175` [taglish; tags: contradictory] Minor flooding lang daw sa Taft pero di na madaanan ng bus
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"flooding","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}

### road_closure (15)

- `te-005` [filipino; tags: -] Wag dumaan sa Anda Circle, sarado
  - errors: incident_type: gold=road_closure pred=road_hazard; severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; location.road: gold=None pred=Anda Boulevard; location.landmark: gold=Anda Circle pred=Circle
  - predicted: {"incident_type":"road_hazard","location":{"road":"Anda Boulevard","landmark":"Circle","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-023` [filipino; tags: contradictory] Sarado raw buong Commonwealth pero dumadaan pa kami ngayon
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"Commonwealth Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"filipino"}
- `te-032` [taglish; tags: -] Isinara ang Escolta dahil sa shooting ng pelikula
  - errors: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_accident","location":{"road":"Escolta","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"filipino"}
- `te-091` [taglish; tags: -] Sarado ang Mabini bridge para sa repair, gamitin ang Quezon bridge
  - errors: location.road: gold=None pred=Mabini; location.landmark: gold=Mabini bridge pred=Quezon
  - predicted: {"incident_type":"road_closure","location":{"road":"Mabini","landmark":"Quezon","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-092` [taglish; tags: -] Isinara ang Roxas Blvd southbound lanes para sa parade, northbound lang bukas
  - errors: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"Roxas Boulevard","landmark":null,"direction":"southbound"},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-096` [english; tags: -] Philippine Navy parade, all roads along Roxas Boulevard closed starting 4am
  - errors: severity: gold=high pred=medium
  - predicted: {"incident_type":"road_closure","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"english"}
- `te-097` [taglish; tags: -] Sarado ang buong Quezon Avenue dahil sa rehabilitasyon
  - errors: language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_closure","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"filipino"}
- `te-099` [taglish; tags: -] Marathon sa BGC, sarado ang 5th Avenue hanggang tanghali
  - errors: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"5th Avenue","landmark":"BGC","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-100` [filipino; tags: no_location] kalsada sa harap ng simbahan sarado dahil sa prusisyon
  - errors: incident_type: gold=road_closure pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; location.landmark: gold=None pred=Samburan
  - predicted: {"incident_type":"road_hazard","location":{"road":null,"landmark":"Samburan","direction":null},"severity":"medium","road_obstruction":"unknown","language":"filipino"}
- `te-101` [english; tags: -] Partial closure on Commonwealth southbound due to utility works, use inner lanes
  - errors: location.landmark: gold=None pred=southbound
  - predicted: {"incident_type":"road_closure","location":{"road":"Commonwealth Avenue","landmark":"southbound","direction":"southbound"},"severity":"medium","road_obstruction":"partial","language":"english"}
- `te-102` [taglish; tags: -] Isa na lang ang bukas na lane sa Skyway Buendia exit dahil sa maintenance
  - errors: location.landmark: gold=Buendia exit pred=Buendia
  - predicted: {"incident_type":"road_closure","location":{"road":"Skyway","landmark":"Buendia","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-103` [filipino; tags: -] SARADO ANG BUONG EDSA PAPUNTANG MAKATI NGAYONG GABI
  - errors: incident_type: gold=road_closure pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":"Makati","direction":null},"severity":"medium","road_obstruction":"unknown","language":"filipino"}
- `te-160` [taglish; tags: noisy] closed ang taft ave for fun run til 10am
  - errors: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-162` [taglish; tags: noisy] sarado d2 sa recto, my parade
  - errors: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; location.road: gold=Recto Avenue pred=D2; location.landmark: gold=None pred=Recto
  - predicted: {"incident_type":"road_accident","location":{"road":"D2","landmark":"Recto","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-173` [taglish; tags: contradictory] Open na raw ang Roxas Blvd pero may barikada pa rin
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}

### heavy_traffic (15)

- `te-004` [taglish; tags: -] traffic sa SCTEX near Tarlac exit, 3 hrs daw
  - errors: severity: gold=high pred=medium; location.landmark: gold=Tarlac exit pred=Tarlac
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"SCTEX","landmark":"Tarlac","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-024` [taglish; tags: contradictory] Light traffic daw sa Shaw pero di gumagalaw ang mga sasakyan
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Shaw Boulevard pred=None; location.landmark: gold=None pred=Shaw Boulevard
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":"Shaw Boulevard","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-105` [filipino; tags: -] Mahaba ang pila ng sasakyan sa Skyway toll gate
  - errors: incident_type: gold=heavy_traffic pred=road_accident; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_accident","location":{"road":"Skyway","landmark":"toll gate","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-108` [filipino; tags: -] Halos hindi umuusad ang trapiko sa Commonwealth, dalawang oras na
  - errors: severity: gold=high pred=medium; location.road: gold=Commonwealth Avenue pred=None
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"filipino"}
- `te-109` [english; tags: -] Slow traffic going to Sta. Rosa exit SLEX northbound
  - errors: location.landmark: gold=Sta. Rosa exit pred=Sta. Rosa
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"SLEX","landmark":"Sta. Rosa","direction":"northbound"},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-112` [taglish; tags: noisy] trafik malala sa Pasong Tamo, almost 1 hour na
  - errors: severity: gold=high pred=medium; location.road: gold=Pasong Tamo pred=None; location.landmark: gold=None pred=Pasong Tamo
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":"Pasong Tamo","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-113` [english; tags: -] Moderate traffic on Quezon Ave from Timog to Kamuning
  - errors: location.direction: gold=None pred=eastbound
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Quezon Avenue","landmark":"Timog","direction":"eastbound"},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-114` [taglish; tags: -] Walang gumagalaw sa Aurora Blvd Cubao, stuck lahat ng bus
  - errors: incident_type: gold=heavy_traffic pred=vehicle_breakdown; severity: gold=high pred=medium
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Aurora Boulevard","landmark":"Cubao","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-115` [filipino; tags: -] Daloy ng trapiko sa Taft ay mabagal pero gumagalaw
  - errors: incident_type: gold=heavy_traffic pred=road_hazard; road_obstruction: gold=none pred=unknown
  - predicted: {"incident_type":"road_hazard","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"filipino"}
- `te-116` [taglish; tags: -] may build up sa Macapagal papuntang airport
  - errors: language: gold=taglish pred=filipino; location.road: gold=Macapagal Boulevard pred=None; location.landmark: gold=airport pred=Macapagal Boulevard
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":"Macapagal Boulevard","direction":null},"severity":"medium","road_obstruction":"none","language":"filipino"}
- `te-118` [taglish; tags: ambiguous] ang tagal ng green light, mahaba ang pila sa kanto ng Shaw at EDSA
  - errors: incident_type: gold=heavy_traffic pred=other; road_obstruction: gold=none pred=unknown
  - predicted: {"incident_type":"other","location":{"road":"Shaw Boulevard","landmark":"EDSA","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-163` [taglish; tags: noisy] grabe trapik sa edsa nb mkati papuntang ortgas
  - errors: incident_type: gold=heavy_traffic pred=road_accident; road_obstruction: gold=none pred=unknown; location.landmark: gold=Makati pred=None; location.direction: gold=northbound pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-164` [taglish; tags: noisy] sbrang bagal s nlex, 2 hrs n kmi dto
  - errors: severity: gold=high pred=medium; language: gold=taglish pred=filipino; location.road: gold=NLEX pred=None
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"filipino"}
- `te-165` [filipino; tags: noisy] trapik nmn sa aurora blvd cubao, ang bgal
  - errors: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Aurora Boulevard","landmark":"Cubao","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-171` [taglish; tags: contradictory] Light traffic sa Katipunan pero 2 oras na akong stuck
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Katipunan Avenue pred=None; location.landmark: gold=None pred=Katipunan
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":"Katipunan","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}

### other (17)

- `te-028` [taglish; tags: -] traffic enforcer nag-dedirect sa Cubao kasi brownout
  - errors: severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown
  - predicted: {"incident_type":"other","location":{"road":null,"landmark":"Cubao","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-035` [english; tags: -] Tunnel lights out near Quezon Ave, cars moving slowly.
  - errors: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=unknown; location.landmark: gold=tunnel pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"english"}
- `te-119` [taglish; tags: -] Brownout sa Cubao, walang traffic light at nagma-manual ang MMDA
  - errors: location.road: gold=None pred=Cubao Avenue; location.landmark: gold=Cubao pred=None
  - predicted: {"incident_type":"other","location":{"road":"Cubao Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-120` [taglish; tags: -] Checkpoint ng pulis sa Katipunan pagpasok ng UP, nagsisikip ang dalawang lane
  - errors: incident_type: gold=other pred=road_accident; location.landmark: gold=UP pred=University of the Philippines
  - predicted: {"incident_type":"road_accident","location":{"road":"Katipunan Avenue","landmark":"University of the Philippines","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-121` [taglish; tags: -] Truck inspection ng LTO sa Marcos Highway, nagkakapila sa isang lane
  - errors: incident_type: gold=other pred=road_accident
  - predicted: {"incident_type":"road_accident","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-122` [taglish; tags: -] May motorcade ng artista sa EDSA, saglit na pinahinto ang mga sasakyan
  - errors: road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"other","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-123` [taglish; tags: -] Sirang traffic light sa Taft-Quirino, nag-aabang ang mga sasakyan
  - errors: incident_type: gold=other pred=road_accident; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; location.road: gold=Taft Avenue pred=Sirang; location.landmark: gold=Quirino pred=Taft-Quirino
  - predicted: {"incident_type":"road_accident","location":{"road":"Sirang","landmark":"Taft-Quirino","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-124` [english; tags: -] Concert crowd spilling onto Aurora Boulevard near the Big Dome, traffic enforcers on site
  - errors: road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"other","location":{"road":"Aurora Boulevard","landmark":"Big Dome","direction":null},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-125` [taglish; tags: -] Fire truck na nakatigil sa tabi ng kalsada sa Aurora, may sunog sa katabing building
  - errors: incident_type: gold=other pred=road_accident; location.road: gold=Aurora Boulevard pred=None; location.landmark: gold=None pred=Aurora
  - predicted: {"incident_type":"road_accident","location":{"road":null,"landmark":"Aurora","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-126` [taglish; tags: -] Naglagay ng bagong pedestrian lane markings sa Katipunan, kaya mabagal ang mga sasakyan
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=low
  - predicted: {"incident_type":"road_hazard","location":{"road":"Katipunan Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-127` [english; tags: -] Road sweepers blocking the right lane along Roxas Boulevard
  - errors: incident_type: gold=other pred=road_hazard
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"english"}
- `te-128` [taglish; tags: -] Checkpoint sa NLEX Valenzuela entry, mahaba ang pila
  - errors: incident_type: gold=other pred=road_accident; severity: gold=medium pred=low
  - predicted: {"incident_type":"road_accident","location":{"road":"NLEX","landmark":"Valenzuela","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-130` [taglish; tags: -] Delivery trucks double-parked sa harap ng Divisoria market, naka-block sa isang lane
  - errors: incident_type: gold=other pred=vehicle_breakdown; location.landmark: gold=Divisoria market pred=Divisoria
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":null,"landmark":"Divisoria","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-131` [taglish; tags: -] Malfunctioning ang boom barrier sa Skyway toll
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=medium
  - predicted: {"incident_type":"road_hazard","location":{"road":"Skyway","landmark":"toll","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-132` [taglish; tags: -] Street vendors occupying the road sa Baclaran, mabagal ang daloy
  - errors: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=partial; location.road: gold=None pred=Baclaran Avenue; location.landmark: gold=Baclaran pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Baclaran Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-133` [taglish; tags: -] Naka-hazard ang MMDA truck sa EDSA, nagtatanggal ng sirang barrier
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=medium
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-167` [taglish; tags: noisy] checkpt sa edsa guadalupe, pumipila mga kotse
  - errors: incident_type: gold=other pred=road_accident; road_obstruction: gold=none pred=unknown
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"Guadalupe","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}

### unknown (16)

- `te-020` [taglish; tags: no_location, ambiguous] Malayo pa ang daan pero stuck na kami, di ko alam bakit
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-021` [filipino; tags: ambiguous] ano po kaya ang nangyari sa EDSA Monumento?
  - errors: location.landmark: gold=Monumento pred=EDSA Monumento
  - predicted: {"incident_type":"unknown","location":{"road":"EDSA","landmark":"EDSA Monumento","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-135` [filipino; tags: ambiguous] ano meron sa Katipunan? di ako makadaan
  - errors: location.road: gold=Katipunan Avenue pred=None; location.landmark: gold=None pred=Katipunan
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":"Katipunan","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-136` [filipino; tags: no_location, ambiguous] may nakita akong ambulansya kanina
  - errors: incident_type: gold=unknown pred=vehicle_breakdown; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-138` [taglish; tags: no_location] Please be safe po sa mga naka-motor
  - errors: language: gold=taglish pred=filipino
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-140` [filipino; tags: ambiguous] Parang may problema sa C5
  - errors: incident_type: gold=unknown pred=road_hazard
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-141` [english; tags: short] anyone coming from Quezon Ave?
  - errors: location.road: gold=Quezon Avenue pred=None; location.landmark: gold=None pred=Quezon Avenue
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":"Quezon Avenue","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"english"}
- `te-143` [filipino; tags: ambiguous] May naririnig akong sirena sa Commonwealth
  - errors: incident_type: gold=unknown pred=other; location.road: gold=Commonwealth Avenue pred=None
  - predicted: {"incident_type":"other","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-144` [filipino; tags: ambiguous] Delikado raw dumaan sa Marcos Highway
  - errors: incident_type: gold=unknown pred=road_accident
  - predicted: {"incident_type":"road_accident","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-145` [english; tags: no_location, short] road still open?
  - errors: incident_type: gold=unknown pred=road_closure; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_closure","location":{"road":null,"landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"english"}
- `te-146` [english; tags: no_location, short] TRAFFIC???
  - errors: invalid JSON
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"unknown"}
- `te-147` [filipino; tags: ambiguous] grabe ang daming tao sa Taft ngayon
  - errors: incident_type: gold=unknown pred=road_hazard
  - predicted: {"incident_type":"road_hazard","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-149` [filipino; tags: ambiguous] Kita ko may pulis sa Shaw, di ko alam bakit
  - errors: language: gold=filipino pred=taglish; location.road: gold=Shaw Boulevard pred=None
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-150` [taglish; tags: ambiguous] Sana okay lang ang lahat sa EDSA
  - errors: language: gold=taglish pred=filipino
  - predicted: {"incident_type":"unknown","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-168` [filipino; tags: noisy, ambiguous] anu ngyari sa cmwlth?? grbe ang daming sasakyan
  - errors: incident_type: gold=unknown pred=road_hazard; location.road: gold=Commonwealth Avenue pred=Cwm
  - predicted: {"incident_type":"road_hazard","location":{"road":"Cwm","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-169` [filipino; tags: noisy, no_location] ingat sa mga nagmmotor ngayon
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"filipino"}

## Wrong items by subset tag

### noisy (22)

- `te-026`: language: gold=taglish pred=filipino; location.landmark: gold=None pred=Flooded Area
- `te-029`: location.road: gold=McArthur Highway pred=McArthur; location.landmark: gold=Valenzuela pred=Hwy
- `te-055`: severity: gold=unknown pred=medium
- `te-088`: incident_type: gold=flooding pred=road_hazard; location.landmark: gold=None pred=Baha
- `te-112`: severity: gold=high pred=medium; location.road: gold=Pasong Tamo pred=None; location.landmark: gold=None pred=Pasong Tamo
- `te-151`: road_obstruction: gold=partial pred=unknown; location.landmark: gold=UST pred=None
- `te-152`: severity: gold=unknown pred=medium; location.road: gold=Commonwealth Avenue pred=CMW
- `te-153`: incident_type: gold=road_accident pred=road_closure
- `te-154`: severity: gold=high pred=medium; location.road: gold=SLEX pred=None; location.direction: gold=southbound pred=None
- `te-155`: incident_type: gold=road_hazard pred=road_closure; road_obstruction: gold=unknown pred=partial
- `te-156`: severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; language: gold=filipino pred=taglish
- `te-157`: incident_type: gold=flooding pred=heavy_traffic; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=none; language: gold=taglish pred=filipino; location.road: gold=España Boulevard pred=None
- `te-158`: severity: gold=high pred=unknown; road_obstruction: gold=partial pred=unknown; location.landmark: gold=Timog pred=Corazon; location.direction: gold=None pred=eastbound
- `te-159`: severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; location.landmark: gold=None pred=Lng. Baha
- `te-160`: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
- `te-162`: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; location.road: gold=Recto Avenue pred=D2; location.landmark: gold=None pred=Recto
- `te-163`: incident_type: gold=heavy_traffic pred=road_accident; road_obstruction: gold=none pred=unknown; location.landmark: gold=Makati pred=None; location.direction: gold=northbound pred=None
- `te-164`: severity: gold=high pred=medium; language: gold=taglish pred=filipino; location.road: gold=NLEX pred=None
- `te-165`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish
- `te-167`: incident_type: gold=other pred=road_accident; road_obstruction: gold=none pred=unknown
- `te-168`: incident_type: gold=unknown pred=road_hazard; location.road: gold=Commonwealth Avenue pred=Cwm
- `te-169`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none

### no_location (7)

- `te-020`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-100`: incident_type: gold=road_closure pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; location.landmark: gold=None pred=Samburan
- `te-136`: incident_type: gold=unknown pred=vehicle_breakdown; language: gold=filipino pred=taglish
- `te-138`: language: gold=taglish pred=filipino
- `te-145`: incident_type: gold=unknown pred=road_closure; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-146`: invalid JSON
- `te-169`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none

### short (6)

- `te-029`: location.road: gold=McArthur Highway pred=McArthur; location.landmark: gold=Valenzuela pred=Hwy
- `te-085`: incident_type: gold=flooding pred=road_closure; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-089`: incident_type: gold=flooding pred=unknown; location.road: gold=Shaw Boulevard pred=None
- `te-141`: location.road: gold=Quezon Avenue pred=None; location.landmark: gold=None pred=Quezon Avenue
- `te-145`: incident_type: gold=unknown pred=road_closure; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-146`: invalid JSON

### ambiguous (15)

- `te-010`: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-020`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-021`: location.landmark: gold=Monumento pred=EDSA Monumento
- `te-038`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-089`: incident_type: gold=flooding pred=unknown; location.road: gold=Shaw Boulevard pred=None
- `te-118`: incident_type: gold=heavy_traffic pred=other; road_obstruction: gold=none pred=unknown
- `te-135`: location.road: gold=Katipunan Avenue pred=None; location.landmark: gold=None pred=Katipunan
- `te-136`: incident_type: gold=unknown pred=vehicle_breakdown; language: gold=filipino pred=taglish
- `te-140`: incident_type: gold=unknown pred=road_hazard
- `te-143`: incident_type: gold=unknown pred=other; location.road: gold=Commonwealth Avenue pred=None
- `te-144`: incident_type: gold=unknown pred=road_accident
- `te-147`: incident_type: gold=unknown pred=road_hazard
- `te-149`: language: gold=filipino pred=taglish; location.road: gold=Shaw Boulevard pred=None
- `te-150`: language: gold=taglish pred=filipino
- `te-168`: incident_type: gold=unknown pred=road_hazard; location.road: gold=Commonwealth Avenue pred=Cwm

### contradictory (10)

- `te-023`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-024`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Shaw Boulevard pred=None; location.landmark: gold=None pred=Shaw Boulevard
- `te-025`: incident_type: gold=road_accident pred=road_closure; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial; language: gold=taglish pred=filipino
- `te-170`: incident_type: gold=flooding pred=road_accident; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-171`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Katipunan Avenue pred=None; location.landmark: gold=None pred=Katipunan
- `te-172`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-173`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-174`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-175`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-176`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none

## Wrong items by language

### filipino (34)

- `te-003`: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=low; road_obstruction: gold=unknown pred=none
- `te-005`: incident_type: gold=road_closure pred=road_hazard; severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; location.road: gold=None pred=Anda Boulevard; location.landmark: gold=Anda Circle pred=Circle
- `te-007`: language: gold=filipino pred=taglish; location.road: gold=Kalayaan Avenue pred=Kalayaan; location.landmark: gold=Kalayaan flyover pred=Buendia
- `te-008`: severity: gold=medium pred=unknown
- `te-014`: incident_type: gold=road_hazard pred=heavy_traffic; severity: gold=low pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Congressional Avenue pred=None
- `te-021`: location.landmark: gold=Monumento pred=EDSA Monumento
- `te-023`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-062`: severity: gold=low pred=medium; language: gold=filipino pred=taglish
- `te-065`: location.road: gold=Dimasalang pred=None
- `te-067`: severity: gold=low pred=unknown; location.road: gold=None pred=Guadalupe Avenue; location.landmark: gold=Guadalupe pred=None
- `te-070`: severity: gold=medium pred=unknown; road_obstruction: gold=partial pred=unknown; location.road: gold=None pred=Kamias Avenue; location.landmark: gold=Kamias pred=None
- `te-072`: language: gold=filipino pred=taglish
- `te-079`: incident_type: gold=flooding pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=partial pred=unknown
- `te-081`: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-083`: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish
- `te-085`: incident_type: gold=flooding pred=road_closure; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-089`: incident_type: gold=flooding pred=unknown; location.road: gold=Shaw Boulevard pred=None
- `te-090`: severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown
- `te-100`: incident_type: gold=road_closure pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; location.landmark: gold=None pred=Samburan
- `te-103`: incident_type: gold=road_closure pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown
- `te-105`: incident_type: gold=heavy_traffic pred=road_accident; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish
- `te-108`: severity: gold=high pred=medium; location.road: gold=Commonwealth Avenue pred=None
- `te-115`: incident_type: gold=heavy_traffic pred=road_hazard; road_obstruction: gold=none pred=unknown
- `te-135`: location.road: gold=Katipunan Avenue pred=None; location.landmark: gold=None pred=Katipunan
- `te-136`: incident_type: gold=unknown pred=vehicle_breakdown; language: gold=filipino pred=taglish
- `te-140`: incident_type: gold=unknown pred=road_hazard
- `te-143`: incident_type: gold=unknown pred=other; location.road: gold=Commonwealth Avenue pred=None
- `te-144`: incident_type: gold=unknown pred=road_accident
- `te-147`: incident_type: gold=unknown pred=road_hazard
- `te-149`: language: gold=filipino pred=taglish; location.road: gold=Shaw Boulevard pred=None
- `te-156`: severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; language: gold=filipino pred=taglish
- `te-165`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish
- `te-168`: incident_type: gold=unknown pred=road_hazard; location.road: gold=Commonwealth Avenue pred=Cwm
- `te-169`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none

### english (18)

- `te-015`: severity: gold=medium pred=low; location.road: gold=Katipunan Avenue pred=Katipunan Boulevard
- `te-029`: location.road: gold=McArthur Highway pred=McArthur; location.landmark: gold=Valenzuela pred=Hwy
- `te-035`: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=unknown; location.landmark: gold=tunnel pred=None
- `te-040`: severity: gold=unknown pred=medium; language: gold=english pred=taglish
- `te-056`: severity: gold=high pred=medium
- `te-059`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-071`: severity: gold=medium pred=unknown
- `te-073`: language: gold=english pred=taglish; location.landmark: gold=km 5 pred=Kennon
- `te-086`: road_obstruction: gold=full pred=partial
- `te-096`: severity: gold=high pred=medium
- `te-101`: location.landmark: gold=None pred=southbound
- `te-109`: location.landmark: gold=Sta. Rosa exit pred=Sta. Rosa
- `te-113`: location.direction: gold=None pred=eastbound
- `te-124`: road_obstruction: gold=unknown pred=none
- `te-127`: incident_type: gold=other pred=road_hazard
- `te-141`: location.road: gold=Quezon Avenue pred=None; location.landmark: gold=None pred=Quezon Avenue
- `te-145`: incident_type: gold=unknown pred=road_closure; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-146`: invalid JSON

### taglish (91)

- `te-001`: incident_type: gold=road_accident pred=road_hazard; language: gold=taglish pred=filipino; location.road: gold=Nagtahan pred=None; location.landmark: gold=None pred=Nagtahan
- `te-002`: incident_type: gold=vehicle_breakdown pred=road_hazard; severity: gold=medium pred=high
- `te-004`: severity: gold=high pred=medium; location.landmark: gold=Tarlac exit pred=Tarlac
- `te-009`: severity: gold=high pred=unknown; location.landmark: gold=underpass pred=None
- `te-010`: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-017`: incident_type: gold=vehicle_breakdown pred=road_hazard
- `te-018`: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=taglish pred=filipino
- `te-019`: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=unknown; road_obstruction: gold=partial pred=unknown; location.landmark: gold=Buendia LRT pred=Buendia
- `te-020`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-024`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Shaw Boulevard pred=None; location.landmark: gold=None pred=Shaw Boulevard
- `te-025`: incident_type: gold=road_accident pred=road_closure; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial; language: gold=taglish pred=filipino
- `te-026`: language: gold=taglish pred=filipino; location.landmark: gold=None pred=Flooded Area
- `te-028`: severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown
- `te-032`: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; language: gold=taglish pred=filipino
- `te-033`: severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown
- `te-036`: severity: gold=medium pred=unknown; road_obstruction: gold=partial pred=unknown; location.landmark: gold=None pred=L300 van
- `te-037`: incident_type: gold=vehicle_breakdown pred=road_accident; location.landmark: gold=LRT Libertad pred=Libertad
- `te-038`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-039`: severity: gold=low pred=medium
- `te-041`: severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown
- `te-042`: road_obstruction: gold=partial pred=unknown
- `te-043`: road_obstruction: gold=partial pred=none
- `te-044`: location.direction: gold=southbound pred=None
- `te-045`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-046`: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown; language: gold=taglish pred=filipino
- `te-048`: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=full
- `te-049`: location.landmark: gold=None pred=Center Island
- `te-050`: severity: gold=high pred=medium
- `te-051`: severity: gold=high pred=low; road_obstruction: gold=unknown pred=none
- `te-053`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-055`: severity: gold=unknown pred=medium
- `te-057`: severity: gold=unknown pred=medium
- `te-058`: incident_type: gold=road_accident pred=road_hazard; road_obstruction: gold=partial pred=unknown
- `te-060`: incident_type: gold=road_hazard pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=partial pred=unknown; location.road: gold=SLEX pred=Marcos Highway
- `te-061`: severity: gold=low pred=medium; language: gold=taglish pred=filipino
- `te-063`: severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown
- `te-064`: severity: gold=medium pred=unknown; road_obstruction: gold=partial pred=unknown
- `te-068`: severity: gold=low pred=medium
- `te-069`: incident_type: gold=road_hazard pred=road_accident; location.landmark: gold=None pred=southbound
- `te-074`: severity: gold=medium pred=low; road_obstruction: gold=partial pred=unknown
- `te-076`: incident_type: gold=flooding pred=road_closure; severity: gold=high pred=medium; road_obstruction: gold=full pred=partial; language: gold=taglish pred=filipino
- `te-077`: incident_type: gold=flooding pred=road_hazard; severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown
- `te-078`: road_obstruction: gold=unknown pred=full; language: gold=taglish pred=filipino; location.road: gold=Commonwealth Avenue pred=None; location.landmark: gold=Batasan pred=Commonwealth Avenue
- `te-080`: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=partial pred=full
- `te-082`: incident_type: gold=flooding pred=road_accident; severity: gold=high pred=low; road_obstruction: gold=partial pred=none
- `te-084`: road_obstruction: gold=unknown pred=partial
- `te-087`: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=low
- `te-088`: incident_type: gold=flooding pred=road_hazard; location.landmark: gold=None pred=Baha
- `te-091`: location.road: gold=None pred=Mabini; location.landmark: gold=Mabini bridge pred=Quezon
- `te-092`: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
- `te-097`: language: gold=taglish pred=filipino
- `te-099`: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
- `te-102`: location.landmark: gold=Buendia exit pred=Buendia
- `te-112`: severity: gold=high pred=medium; location.road: gold=Pasong Tamo pred=None; location.landmark: gold=None pred=Pasong Tamo
- `te-114`: incident_type: gold=heavy_traffic pred=vehicle_breakdown; severity: gold=high pred=medium
- `te-116`: language: gold=taglish pred=filipino; location.road: gold=Macapagal Boulevard pred=None; location.landmark: gold=airport pred=Macapagal Boulevard
- `te-118`: incident_type: gold=heavy_traffic pred=other; road_obstruction: gold=none pred=unknown
- `te-119`: location.road: gold=None pred=Cubao Avenue; location.landmark: gold=Cubao pred=None
- `te-120`: incident_type: gold=other pred=road_accident; location.landmark: gold=UP pred=University of the Philippines
- `te-121`: incident_type: gold=other pred=road_accident
- `te-122`: road_obstruction: gold=unknown pred=none
- `te-123`: incident_type: gold=other pred=road_accident; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; location.road: gold=Taft Avenue pred=Sirang; location.landmark: gold=Quirino pred=Taft-Quirino
- `te-125`: incident_type: gold=other pred=road_accident; location.road: gold=Aurora Boulevard pred=None; location.landmark: gold=None pred=Aurora
- `te-126`: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=low
- `te-128`: incident_type: gold=other pred=road_accident; severity: gold=medium pred=low
- `te-130`: incident_type: gold=other pred=vehicle_breakdown; location.landmark: gold=Divisoria market pred=Divisoria
- `te-131`: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=medium
- `te-132`: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=partial; location.road: gold=None pred=Baclaran Avenue; location.landmark: gold=Baclaran pred=None
- `te-133`: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=medium
- `te-138`: language: gold=taglish pred=filipino
- `te-150`: language: gold=taglish pred=filipino
- `te-151`: road_obstruction: gold=partial pred=unknown; location.landmark: gold=UST pred=None
- `te-152`: severity: gold=unknown pred=medium; location.road: gold=Commonwealth Avenue pred=CMW
- `te-153`: incident_type: gold=road_accident pred=road_closure
- `te-154`: severity: gold=high pred=medium; location.road: gold=SLEX pred=None; location.direction: gold=southbound pred=None
- `te-155`: incident_type: gold=road_hazard pred=road_closure; road_obstruction: gold=unknown pred=partial
- `te-157`: incident_type: gold=flooding pred=heavy_traffic; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=none; language: gold=taglish pred=filipino; location.road: gold=España Boulevard pred=None
- `te-158`: severity: gold=high pred=unknown; road_obstruction: gold=partial pred=unknown; location.landmark: gold=Timog pred=Corazon; location.direction: gold=None pred=eastbound
- `te-159`: severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; location.landmark: gold=None pred=Lng. Baha
- `te-160`: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
- `te-162`: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; location.road: gold=Recto Avenue pred=D2; location.landmark: gold=None pred=Recto
- `te-163`: incident_type: gold=heavy_traffic pred=road_accident; road_obstruction: gold=none pred=unknown; location.landmark: gold=Makati pred=None; location.direction: gold=northbound pred=None
- `te-164`: severity: gold=high pred=medium; language: gold=taglish pred=filipino; location.road: gold=NLEX pred=None
- `te-167`: incident_type: gold=other pred=road_accident; road_obstruction: gold=none pred=unknown
- `te-170`: incident_type: gold=flooding pred=road_accident; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-171`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Katipunan Avenue pred=None; location.landmark: gold=None pred=Katipunan
- `te-172`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-173`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-174`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-175`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-176`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none

