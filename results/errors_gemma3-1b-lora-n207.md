# Error analysis

159 of 176 items have at least one wrong field (incident_type, severity, road_obstruction, language, any location field, or invalid JSON).

## Count summary

### By gold incident class

| group | errors / size |
|---|---|
| vehicle_breakdown | 21 / 22 |
| road_accident | 22 / 23 |
| road_hazard | 20 / 21 |
| flooding | 21 / 24 |
| road_closure | 19 / 23 |
| heavy_traffic | 18 / 23 |
| other | 20 / 20 |
| unknown | 18 / 20 |

### By subset tag

| group | errors / size |
|---|---|
| noisy | 24 / 26 |
| no_location | 7 / 9 |
| short | 9 / 10 |
| ambiguous | 17 / 18 |
| contradictory | 10 / 10 |

### By language

| group | errors / size |
|---|---|
| filipino | 36 / 38 |
| english | 23 / 28 |
| taglish | 100 / 110 |

## Wrong items by gold incident class

### vehicle_breakdown (21)

- `te-002` [taglish; tags: -] Sira yung makina ng bus sa Aurora, kaya mahaba ang pila ng sasakyan
  - errors: road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Aurora Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-006` [english; tags: -] Pickup truck stalled in the middle of Commonwealth Ave near Zuzuarregui, tow on the way
  - errors: road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Commonwealth Avenue","landmark":"Zuzuarregui","direction":null},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-010` [taglish; tags: ambiguous] tricycle nasiraan sa gitna ng Dr. A. Santos Ave, naghihintay ng tulong
  - errors: severity: gold=unknown pred=medium
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Dr. A. Santos Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-017` [taglish; tags: -] naghihirap ang daloy sa Ortigas Ave Extension, naka-hazard ang van
  - errors: incident_type: gold=vehicle_breakdown pred=road_hazard; location.road: gold=Ortigas Avenue Extension pred=Ortigas Avenue
  - predicted: {"incident_type":"road_hazard","location":{"road":"Ortigas Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-018` [taglish; tags: -] PUV na nasira sa may Cubao, wala namang nakaharang
  - errors: severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=taglish pred=filipino; location.road: gold=None pred=Cubao Avenue; location.landmark: gold=Cubao pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Cubao Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-031` [taglish; tags: -] Truck na may sira malapit sa Balintawak toll, sarado ang kanang lane
  - errors: location.landmark: gold=Balintawak toll pred=Balintawak
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":null,"landmark":"Balintawak","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-036` [taglish; tags: -] Tumirik ang L300 van sa kanang lane ng SLEX, hinihila na
  - errors: road_obstruction: gold=partial pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"SLEX","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-037` [taglish; tags: -] Tumigil ang bus sa Taft Ave. southbound sa tapat ng LRT Libertad, mabagal na ang daloy
  - errors: road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Taft Avenue","landmark":"LRT Libertad","direction":"southbound"},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-038` [taglish; tags: ambiguous] wala nang gas ang kotse sa gitna ng Aurora, tinutulak ng mga tao
  - errors: severity: gold=unknown pred=medium
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Aurora Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-039` [taglish; tags: -] sira ang aircon bus sa Ayala Ave tapos nakahinto pa sa bus stop
  - errors: location.landmark: gold=bus stop pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Ayala Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-040` [english; tags: -] Truck stalled on the C5 flyover near Bagong Ilog, hazard on
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"C5","landmark":"Bagong Ilog","direction":null},"severity":"medium","road_obstruction":"partial","language":"english"}
- `te-041` [taglish; tags: -] umuusok ang makina ng jeep sa Mindanao Ave, nakatabi
  - errors: severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Mindanao Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-042` [taglish; tags: -] Nakatirik pa rin ang trailer truck sa NLEX Bocaue, kanang lane
  - errors: road_obstruction: gold=partial pred=unknown
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"NLEX","landmark":"Bocaue","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-043` [taglish; tags: -] dead battery daw ung SUV sa Marcos Hwy Marikina side, nakaharang pa sa lane
  - errors: location.landmark: gold=Marikina pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-045` [taglish; tags: -] stalled ang ambulance sa Quezon Ave, pls give way
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-046` [taglish; tags: -] Nagkaproblema sa makina ang tricycle sa Katipunan, nasa gilid na
  - errors: severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Katipunan Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-047` [taglish; tags: -] nasira motor ko sa C5 pero nakatabi na ako, ok lang
  - errors: incident_type: gold=vehicle_breakdown pred=road_accident
  - predicted: {"incident_type":"road_accident","location":{"road":"C5","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-048` [taglish; tags: -] Bus napagod ata, tumirik sa EDSA Boni, full stop traffic
  - errors: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"Boni","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-151` [taglish; tags: noisy] tumirik jeep sa tpat ng ust, 1 lne lng bukas
  - errors: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none; location.road: gold=None pred=Tapat Avenue; location.landmark: gold=UST pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Tapat Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-152` [taglish; tags: noisy] stalled truck sa cmwlth near fairview ingat
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial; location.road: gold=Commonwealth Avenue pred=CMWLEV
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"CMWLEV","landmark":"Fairview","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-174` [taglish; tags: contradictory] Truck na sira sa EDSA pero tumatakbo naman ang lahat ng lane
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}

### road_accident (22)

- `te-001` [taglish; tags: -] Nabaligtad na delivery truck sa Nagtahan, kalat ang gulay sa kalsada
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; road_obstruction: gold=unknown pred=partial; location.road: gold=Nagtahan pred=Nagtahan Boulevard
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Nagtahan Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-007` [filipino; tags: -] may aksidente na naman sa Kalayaan flyover, pila hanggang Buendia
  - errors: language: gold=filipino pred=taglish; location.landmark: gold=Kalayaan flyover pred=Buendia
  - predicted: {"incident_type":"road_accident","location":{"road":"Kalayaan Avenue","landmark":"Buendia","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-013` [taglish; tags: -] Bus vs truck sa Edsa-Taft, pila na hanggang MOA
  - errors: road_obstruction: gold=unknown pred=none; location.landmark: gold=Taft pred=MOA
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"MOA","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-015` [english; tags: -] Vehicular accident at Katipunan-Boni Serrano, sedan hit a post, no injuries, lane partially blocked.
  - errors: severity: gold=medium pred=low
  - predicted: {"incident_type":"road_accident","location":{"road":"Katipunan Avenue","landmark":"Boni Serrano","direction":null},"severity":"low","road_obstruction":"partial","language":"english"}
- `te-022` [english; tags: -] Truck skidded on wet road along Marcos Highway but already towed.
  - errors: severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown
  - predicted: {"incident_type":"road_accident","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"english"}
- `te-025` [taglish; tags: contradictory] Minor lang daw ang banggaan sa C5 pero buong kalsada ay sarado
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_accident","location":{"road":"C5","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-029` [english; tags: noisy, short] accident mc arthur hway valenzuela
  - errors: language: gold=english pred=taglish; location.road: gold=McArthur Highway pred=Arthur Hway; location.landmark: gold=Valenzuela pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":"Arthur Hway","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-033` [taglish; tags: -] dalawang motor nagbanggaan sa Visayas Ave, nasa gilid na
  - errors: severity: gold=low pred=medium
  - predicted: {"incident_type":"road_accident","location":{"road":"Visayas Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-049` [taglish; tags: -] Sumalpok ang SUV sa center island ng Commonwealth, walang nasaktan
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Commonwealth Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-050` [taglish; tags: -] Banggaan ng bus at jeep sa EDSA Ortigas flyover, may mga sugatan, 3 lane ang sarado
  - errors: severity: gold=high pred=medium; road_obstruction: gold=partial pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"Ortigas flyover","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-052` [english; tags: -] Rear-end collision on SLEX southbound near Alabang, cars already moved to the side
  - errors: severity: gold=low pred=medium
  - predicted: {"incident_type":"road_accident","location":{"road":"SLEX","landmark":"Alabang","direction":"southbound"},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-053` [taglish; tags: -] Tumaob ang tricycle sa Visayas Ave, nagtutulungan ang mga tao
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Visayas Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-054` [taglish; tags: -] Nagkabanggaan ang kotse at motor sa kanto ng Aurora at Katipunan, sarado ang isang lane
  - errors: location.landmark: gold=Katipunan pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":"Aurora Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-055` [taglish; tags: noisy] accdent sa edsa guadalupe, 2 trak, madaming tao
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.landmark: gold=Guadalupe pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-056` [english; tags: -] Chain collision along Marcos Highway westbound, 4 vehicles involved, all lanes blocked
  - errors: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
  - predicted: {"incident_type":"road_accident","location":{"road":"Marcos Highway","landmark":null,"direction":"westbound"},"severity":"medium","road_obstruction":"partial","language":"english"}
- `te-057` [taglish; tags: -] May nabangga na naman sa Taft, ayun nakahandusay pa ang motor
  - errors: severity: gold=unknown pred=medium
  - predicted: {"incident_type":"road_accident","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-058` [taglish; tags: -] Nasalpok ng truck ang overpass railing sa C5 Pasig, kalahati ng daan bukas
  - errors: location.landmark: gold=Pasig pred=overpass
  - predicted: {"incident_type":"road_accident","location":{"road":"C5","landmark":"overpass","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-059` [english; tags: -] bus vs tricycle collision near Cubao terminal, no word on injuries
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":null,"landmark":"Cubao terminal","direction":null},"severity":"low","road_obstruction":"none","language":"english"}
- `te-153` [taglish; tags: noisy] bngga ng bus ung kotse sa roxas blvd, 1 lane blckd
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-154` [taglish; tags: noisy] aksdnte sa slex sb, ambulansya andito na
  - errors: severity: gold=high pred=unknown; location.road: gold=SLEX pred=None; location.direction: gold=southbound pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-172` [taglish; tags: contradictory] Sabi walang accident sa SLEX pero sarado ang dalawang lane
  - errors: incident_type: gold=road_accident pred=road_closure; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"SLEX","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-176` [taglish; tags: contradictory] No injuries pero dalawang ambulansya ang nandito sa Commonwealth crash
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"Commonwealth Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}

### road_hazard (20)

- `te-008` [filipino; tags: -] Maraming bato sa Marcos Hwy
  - errors: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-014` [filipino; tags: -] Ingat sa Congressional, madulas dahil sa ulan
  - errors: incident_type: gold=road_hazard pred=flooding; severity: gold=low pred=unknown; location.road: gold=Congressional Avenue pred=None
  - predicted: {"incident_type":"flooding","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-034` [taglish; tags: ambiguous] rock slide or something sa Kennon Road?
  - errors: language: gold=taglish pred=english
  - predicted: {"incident_type":"road_hazard","location":{"road":"Kennon Road","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"english"}
- `te-060` [taglish; tags: -] Nalaglag ang mga bakal ng truck sa Marcos Highway, kalat sa dalawang lane
  - errors: severity: gold=high pred=medium; location.road: gold=SLEX pred=Marcos Highway
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-061` [taglish; tags: -] Natanggal ang takip ng drainage sa Taft near Vito Cruz, delikado sa motor
  - errors: road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_hazard","location":{"road":"Taft Avenue","landmark":"Vito Cruz","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-062` [filipino; tags: -] May butas na kalsada sa Quezon Avenue, ingat
  - errors: road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-063` [taglish; tags: -] May natumbang billboard sa Commonwealth, hindi na madaanan
  - errors: incident_type: gold=road_hazard pred=road_closure; severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"Commonwealth Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-064` [taglish; tags: -] Gumuhong lupa sa Marcos Highway Antipolo, isang lane ang natabunan
  - errors: severity: gold=medium pred=low; location.landmark: gold=Antipolo pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"low","road_obstruction":"partial","language":"taglish"}
- `te-065` [filipino; tags: -] Kalat ang basura sa kalsada sa Dimasalang matapos ang baha
  - errors: road_obstruction: gold=unknown pred=none; location.road: gold=Dimasalang pred=Dimasalang Boulevard
  - predicted: {"incident_type":"road_hazard","location":{"road":"Dimasalang Boulevard","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"filipino"}
- `te-066` [english; tags: -] Fallen branches along Katipunan, partially blocking the left lane
  - errors: severity: gold=medium pred=low
  - predicted: {"incident_type":"road_hazard","location":{"road":"Katipunan Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"partial","language":"english"}
- `te-067` [filipino; tags: -] May butas sa tulay ng Guadalupe, may nasirang gulong na
  - errors: severity: gold=low pred=medium; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":null,"landmark":"Guadalupe","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-068` [taglish; tags: -] Sirang manhole cover sa Roxas Boulevard, delikado sa mga nagmomotor
  - errors: road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-069` [taglish; tags: -] Nagkalat na bubog at bakal sa EDSA southbound pagkatapos ng aksidente
  - errors: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":null,"direction":"southbound"},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-070` [filipino; tags: -] May natumbang poste ng Meralco sa Kamias, kalahati ng kalye nakaharang
  - errors: severity: gold=medium pred=low; language: gold=filipino pred=taglish; location.road: gold=None pred=Kamias Avenue; location.landmark: gold=Kamias pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Kamias Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"partial","language":"taglish"}
- `te-071` [english; tags: -] Oil spill on Skyway northbound, vehicles slipping
  - errors: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_hazard","location":{"road":"Skyway","landmark":null,"direction":"northbound"},"severity":"low","road_obstruction":"none","language":"english"}
- `te-072` [filipino; tags: -] May mga basura sa kalsada sa Tanay, sagabal sa daan
  - errors: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish; location.road: gold=None pred=Tanay Avenue; location.landmark: gold=Tanay pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Tanay Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-073` [english; tags: -] Boulders on the road at Kennon Road km 5
  - errors: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; location.landmark: gold=km 5 pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Kennon Road","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"english"}
- `te-075` [filipino; tags: ambiguous] hmm may malaking bato ata sa gitna ng daan sa Rizal Ave
  - errors: language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Rizal Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-155` [taglish; tags: noisy] may nalaglag na sako sa C5 nb sa tapat ng ayala, pls avoid
  - errors: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; location.direction: gold=northbound pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":"Ayala","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-156` [filipino; tags: noisy] natumbang puno sa marcos hwy, d na madaan
  - errors: incident_type: gold=road_hazard pred=road_closure; severity: gold=high pred=medium; language: gold=filipino pred=taglish; location.road: gold=Marcos Highway pred=Marcos Avenue
  - predicted: {"incident_type":"road_closure","location":{"road":"Marcos Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}

### flooding (21)

- `te-003` [filipino; tags: -] Sasakyan lumubog sa baha sa Mel Lopez Blvd
  - errors: road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"flooding","location":{"road":"Mel Lopez Boulevard","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-009` [taglish; tags: -] Flooded na naman daw ung underpass sa España, wag nyo na daanan
  - errors: severity: gold=high pred=unknown; language: gold=taglish pred=filipino; location.landmark: gold=underpass pred=None
  - predicted: {"incident_type":"flooding","location":{"road":"España Boulevard","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-019` [taglish; tags: -] BAHA!!! sa Taft near Buendia LRT, tuhod level
  - errors: incident_type: gold=flooding pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=partial pred=none; location.landmark: gold=Buendia LRT pred=Buendia
  - predicted: {"incident_type":"road_accident","location":{"road":"Taft Avenue","landmark":"Buendia","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-026` [taglish; tags: noisy] DI MAKADAAN BUS SA FLOODED NA ESPAÑA
  - errors: severity: gold=high pred=medium; road_obstruction: gold=full pred=none; location.road: gold=España Boulevard pred=None
  - predicted: {"incident_type":"flooding","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-077` [taglish; tags: -] Baha sa Roxas Blvd near Manila Bay, hanggang gutter lang
  - errors: incident_type: gold=flooding pred=road_hazard
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":"Manila Bay","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-078` [taglish; tags: -] Flood sa Commonwealth Batasan, nagsisitigil ang mga sasakyan
  - errors: severity: gold=high pred=unknown; language: gold=taglish pred=filipino; location.landmark: gold=Batasan pred=None
  - predicted: {"incident_type":"flooding","location":{"road":"Commonwealth Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-081` [filipino; tags: -] Baha sa Marikina, tumataas pa ang tubig
  - errors: severity: gold=unknown pred=medium
  - predicted: {"incident_type":"flooding","location":{"road":null,"landmark":"Marikina","direction":null},"severity":"medium","road_obstruction":"unknown","language":"filipino"}
- `te-082` [taglish; tags: -] Lubog ang kalsada sa Dr. A. Santos Ave, mga motor lang ang nakakalusot
  - errors: incident_type: gold=flooding pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=partial pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"Dr. A. Santos Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-083` [filipino; tags: -] Katamtamang baha lang sa C5 Ortigas, mabagal ang takbo pero pwede pa
  - errors: severity: gold=medium pred=low; location.landmark: gold=Ortigas pred=None
  - predicted: {"incident_type":"flooding","location":{"road":"C5","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"filipino"}
- `te-084` [taglish; tags: -] Water at knee level na sa Recto, stranded mga jeep
  - errors: severity: gold=high pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"flooding","location":{"road":"Recto Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-085` [filipino; tags: short] Muling bumaha sa Pasong Tamo
  - errors: location.road: gold=Pasong Tamo pred=Pasong Tamo Avenue
  - predicted: {"incident_type":"flooding","location":{"road":"Pasong Tamo Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-086` [english; tags: -] Waist-deep flood on Taft Ave near Quirino, even trucks cannot pass
  - errors: severity: gold=high pred=medium; road_obstruction: gold=full pred=none; location.landmark: gold=Quirino pred=None
  - predicted: {"incident_type":"flooding","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-087` [taglish; tags: -] Binaha ang EDSA Kamuning northbound, isang lane lang ang ligtas
  - errors: incident_type: gold=flooding pred=vehicle_breakdown; severity: gold=high pred=medium
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"EDSA","landmark":"Kamuning","direction":"northbound"},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-088` [taglish; tags: noisy] baha d2 sa Dimasalang, pls avoid
  - errors: location.road: gold=Dimasalang pred=None; location.landmark: gold=None pred=Baha Avenue
  - predicted: {"incident_type":"flooding","location":{"road":null,"landmark":"Baha Avenue","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-089` [filipino; tags: short, ambiguous] Binaha na ba ang Shaw ngayon?
  - errors: incident_type: gold=flooding pred=unknown; location.road: gold=Shaw Boulevard pred=None
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-090` [filipino; tags: -] Malalim na baha sa ilalim ng tulay sa Pasig, hindi madaanan ng kahit anong sasakyan
  - errors: road_obstruction: gold=full pred=partial; location.road: gold=None pred=Pasig; location.landmark: gold=Pasig pred=None
  - predicted: {"incident_type":"flooding","location":{"road":"Pasig","landmark":null,"direction":null},"severity":"high","road_obstruction":"partial","language":"filipino"}
- `te-157` [taglish; tags: noisy] bha n nmn sa espna, lubog na mga kotse
  - errors: road_obstruction: gold=unknown pred=partial; location.road: gold=España Boulevard pred=None
  - predicted: {"incident_type":"flooding","location":{"road":null,"landmark":null,"direction":null},"severity":"high","road_obstruction":"partial","language":"taglish"}
- `te-158` [taglish; tags: noisy] flooded na ang quezn ave cor timog, d makadaan sedan
  - errors: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=partial pred=unknown
  - predicted: {"incident_type":"road_hazard","location":{"road":"Quezon Avenue","landmark":"Timog","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-159` [taglish; tags: noisy] ankle deep lng baha sa rox blvd, ok pa
  - errors: road_obstruction: gold=none pred=unknown; location.road: gold=Roxas Boulevard pred=Rox Boulevard
  - predicted: {"incident_type":"flooding","location":{"road":"Rox Boulevard","landmark":null,"direction":null},"severity":"low","road_obstruction":"unknown","language":"taglish"}
- `te-170` [taglish; tags: contradictory] Wala daw bumaha sa Recto pero stranded ang mga bus
  - errors: incident_type: gold=flooding pred=road_closure; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_closure","location":{"road":"Recto Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-175` [taglish; tags: contradictory] Minor flooding lang daw sa Taft pero di na madaanan ng bus
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"flooding","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}

### road_closure (19)

- `te-005` [filipino; tags: -] Wag dumaan sa Anda Circle, sarado
  - errors: severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; language: gold=filipino pred=taglish; location.landmark: gold=Anda Circle pred=Wag dumaan sa Anda Circle
  - predicted: {"incident_type":"road_closure","location":{"road":null,"landmark":"Wag dumaan sa Anda Circle","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-011` [taglish; tags: -] MMDA: lahat ng lane southbound Roxas Blvd sarado mula Quirino para sa event
  - errors: location.direction: gold=southbound pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Roxas Boulevard","landmark":"Quirino","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-016` [english; tags: -] Road closed due to fallen cables along Sumulong Highway westbound.
  - errors: invalid JSON
  - predicted: {"incident_type":"road_closure","location":{"road":"Sumulong Highway","landmark":null,"direction":"westbound"},"severity":"high","road_obstruction":"cable","language":"english"}
- `te-023` [filipino; tags: contradictory] Sarado raw buong Commonwealth pero dumadaan pa kami ngayon
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_closure","location":{"road":"Commonwealth Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-027` [taglish; tags: noisy] cnstrctn sa c5 libis, 1 lane lang
  - errors: incident_type: gold=road_closure pred=road_hazard; severity: gold=medium pred=low; location.landmark: gold=Libis pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":null,"direction":null},"severity":"low","road_obstruction":"partial","language":"taglish"}
- `te-032` [taglish; tags: -] Isinara ang Escolta dahil sa shooting ng pelikula
  - errors: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=low; road_obstruction: gold=full pred=none; language: gold=taglish pred=filipino; location.road: gold=Escolta pred=Escolta Avenue
  - predicted: {"incident_type":"road_accident","location":{"road":"Escolta Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"filipino"}
- `te-091` [taglish; tags: -] Sarado ang Mabini bridge para sa repair, gamitin ang Quezon bridge
  - errors: severity: gold=high pred=medium; location.road: gold=None pred=Quezon Avenue; location.landmark: gold=Mabini bridge pred=Sarado ang Mabini
  - predicted: {"incident_type":"road_closure","location":{"road":"Quezon Avenue","landmark":"Sarado ang Mabini","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-092` [taglish; tags: -] Isinara ang Roxas Blvd southbound lanes para sa parade, northbound lang bukas
  - errors: severity: gold=high pred=medium; location.direction: gold=southbound pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-093` [taglish; tags: -] One lane open lang sa C5 dahil sa water pipe installation
  - errors: incident_type: gold=road_closure pred=road_hazard; severity: gold=medium pred=low; road_obstruction: gold=partial pred=none
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-094` [taglish; tags: -] Road closed sa Katipunan-Aurora, may sunog sa building
  - errors: location.landmark: gold=Aurora pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Katipunan Avenue","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-095` [english; tags: -] Taft Avenue northbound closed from Pedro Gil to Vito Cruz for the procession
  - errors: severity: gold=high pred=medium
  - predicted: {"incident_type":"road_closure","location":{"road":"Taft Avenue","landmark":"Pedro Gil","direction":"northbound"},"severity":"medium","road_obstruction":"full","language":"english"}
- `te-097` [taglish; tags: -] Sarado ang buong Quezon Avenue dahil sa rehabilitasyon
  - errors: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_closure","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"filipino"}
- `te-099` [taglish; tags: -] Marathon sa BGC, sarado ang 5th Avenue hanggang tanghali
  - errors: severity: gold=high pred=medium; location.landmark: gold=BGC pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"5th Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-100` [filipino; tags: no_location] kalsada sa harap ng simbahan sarado dahil sa prusisyon
  - errors: incident_type: gold=road_closure pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; language: gold=filipino pred=taglish; location.landmark: gold=None pred=simbahan
  - predicted: {"incident_type":"road_hazard","location":{"road":null,"landmark":"simbahan","direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-102` [taglish; tags: -] Isa na lang ang bukas na lane sa Skyway Buendia exit dahil sa maintenance
  - errors: location.road: gold=Skyway pred=Skyway Buendia; location.landmark: gold=Buendia exit pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Skyway Buendia","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-103` [filipino; tags: -] SARADO ANG BUONG EDSA PAPUNTANG MAKATI NGAYONG GABI
  - errors: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; location.landmark: gold=Makati pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"filipino"}
- `te-161` [taglish; tags: noisy] 2 lne lng bukas sa ortgas ave, my hukay
  - errors: road_obstruction: gold=partial pred=full
  - predicted: {"incident_type":"road_closure","location":{"road":"Ortigas Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-162` [taglish; tags: noisy] sarado d2 sa recto, my parade
  - errors: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=full pred=none; location.road: gold=Recto Avenue pred=España Boulevard
  - predicted: {"incident_type":"road_accident","location":{"road":"España Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-173` [taglish; tags: contradictory] Open na raw ang Roxas Blvd pero may barikada pa rin
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}

### heavy_traffic (18)

- `te-004` [taglish; tags: -] traffic sa SCTEX near Tarlac exit, 3 hrs daw
  - errors: severity: gold=high pred=medium
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"SCTEX","landmark":"Tarlac exit","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-024` [taglish; tags: contradictory] Light traffic daw sa Shaw pero di gumagalaw ang mga sasakyan
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Shaw Boulevard","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-030` [english; tags: -] Long line of vehicles going to NAIA Terminal 3.
  - errors: location.road: gold=None pred=NAIA Avenue; location.landmark: gold=NAIA Terminal 3 pred=None
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"NAIA Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-104` [taglish; tags: -] stuck pa rin kami sa C5 southbound papuntang Libis, 45 mins na
  - errors: incident_type: gold=heavy_traffic pred=road_accident
  - predicted: {"incident_type":"road_accident","location":{"road":"C5","landmark":"Libis","direction":"southbound"},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-105` [filipino; tags: -] Mahaba ang pila ng sasakyan sa Skyway toll gate
  - errors: incident_type: gold=heavy_traffic pred=vehicle_breakdown; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish; location.landmark: gold=toll gate pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Skyway","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-108` [filipino; tags: -] Halos hindi umuusad ang trapiko sa Commonwealth, dalawang oras na
  - errors: severity: gold=high pred=medium; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Commonwealth Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-109` [english; tags: -] Slow traffic going to Sta. Rosa exit SLEX northbound
  - errors: location.landmark: gold=Sta. Rosa exit pred=Sta. Rosa
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"SLEX","landmark":"Sta. Rosa","direction":"northbound"},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-111` [filipino; tags: -] Pila hanggang Balintawak ang mga trak papuntang NLEX
  - errors: incident_type: gold=heavy_traffic pred=vehicle_breakdown; language: gold=filipino pred=taglish; location.road: gold=NLEX pred=Pila
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Pila","landmark":"Balintawak","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-112` [taglish; tags: noisy] trafik malala sa Pasong Tamo, almost 1 hour na
  - errors: severity: gold=high pred=medium; location.road: gold=Pasong Tamo pred=Pasong Tamo Avenue
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Pasong Tamo Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-114` [taglish; tags: -] Walang gumagalaw sa Aurora Blvd Cubao, stuck lahat ng bus
  - errors: incident_type: gold=heavy_traffic pred=road_closure; severity: gold=high pred=medium; road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"road_closure","location":{"road":"Aurora Boulevard","landmark":"Cubao","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-115` [filipino; tags: -] Daloy ng trapiko sa Taft ay mabagal pero gumagalaw
  - errors: severity: gold=medium pred=low; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-116` [taglish; tags: -] may build up sa Macapagal papuntang airport
  - errors: incident_type: gold=heavy_traffic pred=road_closure; road_obstruction: gold=none pred=full; location.landmark: gold=airport pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Macapagal Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-117` [english; tags: -] Traffic in front of SM North, several buses queueing
  - errors: incident_type: gold=heavy_traffic pred=vehicle_breakdown; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown; location.road: gold=None pred=SM Avenue; location.landmark: gold=SM North pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"SM Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"english"}
- `te-118` [taglish; tags: ambiguous] ang tagal ng green light, mahaba ang pila sa kanto ng Shaw at EDSA
  - errors: incident_type: gold=heavy_traffic pred=other; location.road: gold=Shaw Boulevard pred=EDSA; location.landmark: gold=EDSA pred=Shaw
  - predicted: {"incident_type":"other","location":{"road":"EDSA","landmark":"Shaw","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-163` [taglish; tags: noisy] grabe trapik sa edsa nb mkati papuntang ortgas
  - errors: incident_type: gold=heavy_traffic pred=road_accident; road_obstruction: gold=none pred=partial; location.landmark: gold=Makati pred=Ortigas; location.direction: gold=northbound pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"Ortigas","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-164` [taglish; tags: noisy] sbrang bagal s nlex, 2 hrs n kmi dto
  - errors: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=high pred=low; location.road: gold=NLEX pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":null,"landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-165` [filipino; tags: noisy] trapik nmn sa aurora blvd cubao, ang bgal
  - errors: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=low; language: gold=filipino pred=taglish; location.landmark: gold=Cubao pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Aurora Boulevard","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-171` [taglish; tags: contradictory] Light traffic sa Katipunan pero 2 oras na akong stuck
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Katipunan Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}

### other (20)

- `te-028` [taglish; tags: -] traffic enforcer nag-dedirect sa Cubao kasi brownout
  - errors: incident_type: gold=other pred=road_closure; road_obstruction: gold=none pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":null,"landmark":"Cubao","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-035` [english; tags: -] Tunnel lights out near Quezon Ave, cars moving slowly.
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=low; location.landmark: gold=tunnel pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"english"}
- `te-119` [taglish; tags: -] Brownout sa Cubao, walang traffic light at nagma-manual ang MMDA
  - errors: incident_type: gold=other pred=road_closure; language: gold=taglish pred=filipino; location.road: gold=None pred=Cubao; location.landmark: gold=Cubao pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Cubao","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"filipino"}
- `te-120` [taglish; tags: -] Checkpoint ng pulis sa Katipunan pagpasok ng UP, nagsisikip ang dalawang lane
  - errors: incident_type: gold=other pred=road_closure; location.landmark: gold=UP pred=Katipunan
  - predicted: {"incident_type":"road_closure","location":{"road":"Katipunan Avenue","landmark":"Katipunan","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-121` [taglish; tags: -] Truck inspection ng LTO sa Marcos Highway, nagkakapila sa isang lane
  - errors: incident_type: gold=other pred=road_hazard
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-122` [taglish; tags: -] May motorcade ng artista sa EDSA, saglit na pinahinto ang mga sasakyan
  - errors: incident_type: gold=other pred=road_accident; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-123` [taglish; tags: -] Sirang traffic light sa Taft-Quirino, nag-aabang ang mga sasakyan
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"other","location":{"road":"Taft Avenue","landmark":"Quirino","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-124` [english; tags: -] Concert crowd spilling onto Aurora Boulevard near the Big Dome, traffic enforcers on site
  - errors: incident_type: gold=other pred=road_closure; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"Aurora Boulevard","landmark":"Big Dome","direction":null},"severity":"medium","road_obstruction":"partial","language":"english"}
- `te-125` [taglish; tags: -] Fire truck na nakatigil sa tabi ng kalsada sa Aurora, may sunog sa katabing building
  - errors: road_obstruction: gold=unknown pred=none; location.road: gold=Aurora Boulevard pred=None; location.landmark: gold=None pred=Aurora
  - predicted: {"incident_type":"other","location":{"road":null,"landmark":"Aurora","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-126` [taglish; tags: -] Naglagay ng bagong pedestrian lane markings sa Katipunan, kaya mabagal ang mga sasakyan
  - errors: incident_type: gold=other pred=road_closure; road_obstruction: gold=none pred=partial
  - predicted: {"incident_type":"road_closure","location":{"road":"Katipunan Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-127` [english; tags: -] Road sweepers blocking the right lane along Roxas Boulevard
  - errors: incident_type: gold=other pred=road_hazard
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"english"}
- `te-128` [taglish; tags: -] Checkpoint sa NLEX Valenzuela entry, mahaba ang pila
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=low
  - predicted: {"incident_type":"road_hazard","location":{"road":"NLEX","landmark":"Valenzuela","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-129` [taglish; tags: -] Funeral procession sa EDSA, mabagal ang takbo ng mga sasakyan
  - errors: incident_type: gold=other pred=road_accident
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-130` [taglish; tags: -] Delivery trucks double-parked sa harap ng Divisoria market, naka-block sa isang lane
  - errors: incident_type: gold=other pred=road_hazard; location.road: gold=None pred=Divisoria Avenue; location.landmark: gold=Divisoria market pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Divisoria Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-131` [taglish; tags: -] Malfunctioning ang boom barrier sa Skyway toll
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=medium; location.landmark: gold=toll pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Skyway","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-132` [taglish; tags: -] Street vendors occupying the road sa Baclaran, mabagal ang daloy
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=low; location.road: gold=None pred=Baclaran Avenue; location.landmark: gold=Baclaran pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Baclaran Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-133` [taglish; tags: -] Naka-hazard ang MMDA truck sa EDSA, nagtatanggal ng sirang barrier
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=medium
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"unknown","language":"taglish"}
- `te-134` [taglish; tags: -] Students marching along Taft Avenue near DLSU, lane open pa naman
  - errors: incident_type: gold=other pred=road_closure; severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; location.landmark: gold=DLSU pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-166` [taglish; tags: noisy] walang ilaw ang trafic light sa shaw cor edsa, nag-dedirect ang enforcer
  - errors: location.road: gold=Shaw Boulevard pred=Shaw Road
  - predicted: {"incident_type":"other","location":{"road":"Shaw Road","landmark":"EDSA","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-167` [taglish; tags: noisy] checkpt sa edsa guadalupe, pumipila mga kotse
  - errors: incident_type: gold=other pred=road_accident; location.road: gold=EDSA pred=None; location.landmark: gold=Guadalupe pred=Edsa Guadalupe
  - predicted: {"incident_type":"road_accident","location":{"road":null,"landmark":"Edsa Guadalupe","direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}

### unknown (18)

- `te-020` [taglish; tags: no_location, ambiguous] Malayo pa ang daan pero stuck na kami, di ko alam bakit
  - errors: invalid JSON
  - predicted: {"incident_type":"road_closure","location":{"road":null,"landmark":Malayo pa ang daan","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-021` [filipino; tags: ambiguous] ano po kaya ang nangyari sa EDSA Monumento?
  - errors: incident_type: gold=unknown pred=road_accident; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"Monumento","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-135` [filipino; tags: ambiguous] ano meron sa Katipunan? di ako makadaan
  - errors: location.road: gold=Katipunan Avenue pred=None; location.landmark: gold=None pred=Katipunan
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":"Katipunan","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-137` [filipino; tags: short] Bakit ganyan ang EDSA kanina?
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-138` [taglish; tags: no_location] Please be safe po sa mga naka-motor
  - errors: incident_type: gold=unknown pred=road_hazard; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_hazard","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-139` [english; tags: no_location, short] Update on traffic please
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-140` [filipino; tags: ambiguous] Parang may problema sa C5
  - errors: incident_type: gold=unknown pred=road_accident; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_accident","location":{"road":"C5","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-141` [english; tags: short] anyone coming from Quezon Ave?
  - errors: location.road: gold=Quezon Avenue pred=None
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"english"}
- `te-142` [taglish; tags: short] Sino may info sa Ortigas?
  - errors: language: gold=taglish pred=filipino; location.landmark: gold=Ortigas pred=None
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-143` [filipino; tags: ambiguous] May naririnig akong sirena sa Commonwealth
  - errors: language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=None; location.landmark: gold=None pred=Commonwealth
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":"Commonwealth","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-144` [filipino; tags: ambiguous] Delikado raw dumaan sa Marcos Highway
  - errors: incident_type: gold=unknown pred=road_accident
  - predicted: {"incident_type":"road_accident","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-145` [english; tags: no_location, short] road still open?
  - errors: incident_type: gold=unknown pred=road_closure
  - predicted: {"incident_type":"road_closure","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"english"}
- `te-147` [filipino; tags: ambiguous] grabe ang daming tao sa Taft ngayon
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-148` [filipino; tags: no_location, short, ambiguous] wag na dumaan dyan
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=english
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-149` [filipino; tags: ambiguous] Kita ko may pulis sa Shaw, di ko alam bakit
  - errors: location.road: gold=Shaw Boulevard pred=None
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-150` [taglish; tags: ambiguous] Sana okay lang ang lahat sa EDSA
  - errors: incident_type: gold=unknown pred=road_closure; language: gold=taglish pred=filipino
  - predicted: {"incident_type":"road_closure","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"filipino"}
- `te-168` [filipino; tags: noisy, ambiguous] anu ngyari sa cmwlth?? grbe ang daming sasakyan
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=CMWLT
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"CMWLT","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-169` [filipino; tags: noisy, no_location] ingat sa mga nagmmotor ngayon
  - errors: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":null,"landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}

## Wrong items by subset tag

### noisy (24)

- `te-026`: severity: gold=high pred=medium; road_obstruction: gold=full pred=none; location.road: gold=España Boulevard pred=None
- `te-027`: incident_type: gold=road_closure pred=road_hazard; severity: gold=medium pred=low; location.landmark: gold=Libis pred=None
- `te-029`: language: gold=english pred=taglish; location.road: gold=McArthur Highway pred=Arthur Hway; location.landmark: gold=Valenzuela pred=None
- `te-055`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.landmark: gold=Guadalupe pred=None
- `te-088`: location.road: gold=Dimasalang pred=None; location.landmark: gold=None pred=Baha Avenue
- `te-112`: severity: gold=high pred=medium; location.road: gold=Pasong Tamo pred=Pasong Tamo Avenue
- `te-151`: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none; location.road: gold=None pred=Tapat Avenue; location.landmark: gold=UST pred=None
- `te-152`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial; location.road: gold=Commonwealth Avenue pred=CMWLEV
- `te-153`: incident_type: gold=road_accident pred=vehicle_breakdown
- `te-154`: severity: gold=high pred=unknown; location.road: gold=SLEX pred=None; location.direction: gold=southbound pred=None
- `te-155`: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; location.direction: gold=northbound pred=None
- `te-156`: incident_type: gold=road_hazard pred=road_closure; severity: gold=high pred=medium; language: gold=filipino pred=taglish; location.road: gold=Marcos Highway pred=Marcos Avenue
- `te-157`: road_obstruction: gold=unknown pred=partial; location.road: gold=España Boulevard pred=None
- `te-158`: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=partial pred=unknown
- `te-159`: road_obstruction: gold=none pred=unknown; location.road: gold=Roxas Boulevard pred=Rox Boulevard
- `te-161`: road_obstruction: gold=partial pred=full
- `te-162`: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=full pred=none; location.road: gold=Recto Avenue pred=España Boulevard
- `te-163`: incident_type: gold=heavy_traffic pred=road_accident; road_obstruction: gold=none pred=partial; location.landmark: gold=Makati pred=Ortigas; location.direction: gold=northbound pred=None
- `te-164`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=high pred=low; location.road: gold=NLEX pred=None
- `te-165`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=low; language: gold=filipino pred=taglish; location.landmark: gold=Cubao pred=None
- `te-166`: location.road: gold=Shaw Boulevard pred=Shaw Road
- `te-167`: incident_type: gold=other pred=road_accident; location.road: gold=EDSA pred=None; location.landmark: gold=Guadalupe pred=Edsa Guadalupe
- `te-168`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=CMWLT
- `te-169`: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish

### no_location (7)

- `te-020`: invalid JSON
- `te-100`: incident_type: gold=road_closure pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; language: gold=filipino pred=taglish; location.landmark: gold=None pred=simbahan
- `te-138`: incident_type: gold=unknown pred=road_hazard; language: gold=taglish pred=filipino
- `te-139`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-145`: incident_type: gold=unknown pred=road_closure
- `te-148`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=english
- `te-169`: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish

### short (9)

- `te-029`: language: gold=english pred=taglish; location.road: gold=McArthur Highway pred=Arthur Hway; location.landmark: gold=Valenzuela pred=None
- `te-085`: location.road: gold=Pasong Tamo pred=Pasong Tamo Avenue
- `te-089`: incident_type: gold=flooding pred=unknown; location.road: gold=Shaw Boulevard pred=None
- `te-137`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
- `te-139`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-141`: location.road: gold=Quezon Avenue pred=None
- `te-142`: language: gold=taglish pred=filipino; location.landmark: gold=Ortigas pred=None
- `te-145`: incident_type: gold=unknown pred=road_closure
- `te-148`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=english

### ambiguous (17)

- `te-010`: severity: gold=unknown pred=medium
- `te-020`: invalid JSON
- `te-021`: incident_type: gold=unknown pred=road_accident; language: gold=filipino pred=taglish
- `te-034`: language: gold=taglish pred=english
- `te-038`: severity: gold=unknown pred=medium
- `te-075`: language: gold=filipino pred=taglish
- `te-089`: incident_type: gold=flooding pred=unknown; location.road: gold=Shaw Boulevard pred=None
- `te-118`: incident_type: gold=heavy_traffic pred=other; location.road: gold=Shaw Boulevard pred=EDSA; location.landmark: gold=EDSA pred=Shaw
- `te-135`: location.road: gold=Katipunan Avenue pred=None; location.landmark: gold=None pred=Katipunan
- `te-140`: incident_type: gold=unknown pred=road_accident; language: gold=filipino pred=taglish
- `te-143`: language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=None; location.landmark: gold=None pred=Commonwealth
- `te-144`: incident_type: gold=unknown pred=road_accident
- `te-147`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
- `te-148`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=english
- `te-149`: location.road: gold=Shaw Boulevard pred=None
- `te-150`: incident_type: gold=unknown pred=road_closure; language: gold=taglish pred=filipino
- `te-168`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=CMWLT

### contradictory (10)

- `te-023`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-024`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-025`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-170`: incident_type: gold=flooding pred=road_closure; language: gold=taglish pred=filipino
- `te-171`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-172`: incident_type: gold=road_accident pred=road_closure; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-173`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-174`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-175`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-176`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none

## Wrong items by language

### filipino (36)

- `te-003`: road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-005`: severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; language: gold=filipino pred=taglish; location.landmark: gold=Anda Circle pred=Wag dumaan sa Anda Circle
- `te-007`: language: gold=filipino pred=taglish; location.landmark: gold=Kalayaan flyover pred=Buendia
- `te-008`: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
- `te-014`: incident_type: gold=road_hazard pred=flooding; severity: gold=low pred=unknown; location.road: gold=Congressional Avenue pred=None
- `te-021`: incident_type: gold=unknown pred=road_accident; language: gold=filipino pred=taglish
- `te-023`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-062`: road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
- `te-065`: road_obstruction: gold=unknown pred=none; location.road: gold=Dimasalang pred=Dimasalang Boulevard
- `te-067`: severity: gold=low pred=medium; language: gold=filipino pred=taglish
- `te-070`: severity: gold=medium pred=low; language: gold=filipino pred=taglish; location.road: gold=None pred=Kamias Avenue; location.landmark: gold=Kamias pred=None
- `te-072`: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish; location.road: gold=None pred=Tanay Avenue; location.landmark: gold=Tanay pred=None
- `te-075`: language: gold=filipino pred=taglish
- `te-081`: severity: gold=unknown pred=medium
- `te-083`: severity: gold=medium pred=low; location.landmark: gold=Ortigas pred=None
- `te-085`: location.road: gold=Pasong Tamo pred=Pasong Tamo Avenue
- `te-089`: incident_type: gold=flooding pred=unknown; location.road: gold=Shaw Boulevard pred=None
- `te-090`: road_obstruction: gold=full pred=partial; location.road: gold=None pred=Pasig; location.landmark: gold=Pasig pred=None
- `te-100`: incident_type: gold=road_closure pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; language: gold=filipino pred=taglish; location.landmark: gold=None pred=simbahan
- `te-103`: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=full pred=unknown; location.landmark: gold=Makati pred=None
- `te-105`: incident_type: gold=heavy_traffic pred=vehicle_breakdown; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish; location.landmark: gold=toll gate pred=None
- `te-108`: severity: gold=high pred=medium; language: gold=filipino pred=taglish
- `te-111`: incident_type: gold=heavy_traffic pred=vehicle_breakdown; language: gold=filipino pred=taglish; location.road: gold=NLEX pred=Pila
- `te-115`: severity: gold=medium pred=low; language: gold=filipino pred=taglish
- `te-135`: location.road: gold=Katipunan Avenue pred=None; location.landmark: gold=None pred=Katipunan
- `te-137`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
- `te-140`: incident_type: gold=unknown pred=road_accident; language: gold=filipino pred=taglish
- `te-143`: language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=None; location.landmark: gold=None pred=Commonwealth
- `te-144`: incident_type: gold=unknown pred=road_accident
- `te-147`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
- `te-148`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=english
- `te-149`: location.road: gold=Shaw Boulevard pred=None
- `te-156`: incident_type: gold=road_hazard pred=road_closure; severity: gold=high pred=medium; language: gold=filipino pred=taglish; location.road: gold=Marcos Highway pred=Marcos Avenue
- `te-165`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=low; language: gold=filipino pred=taglish; location.landmark: gold=Cubao pred=None
- `te-168`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=CMWLT
- `te-169`: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish

### english (23)

- `te-006`: road_obstruction: gold=unknown pred=none
- `te-015`: severity: gold=medium pred=low
- `te-016`: invalid JSON
- `te-022`: severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown
- `te-029`: language: gold=english pred=taglish; location.road: gold=McArthur Highway pred=Arthur Hway; location.landmark: gold=Valenzuela pred=None
- `te-030`: location.road: gold=None pred=NAIA Avenue; location.landmark: gold=NAIA Terminal 3 pred=None
- `te-035`: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=low; location.landmark: gold=tunnel pred=None
- `te-040`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-052`: severity: gold=low pred=medium
- `te-056`: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
- `te-059`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-066`: severity: gold=medium pred=low
- `te-071`: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none
- `te-073`: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; location.landmark: gold=km 5 pred=None
- `te-086`: severity: gold=high pred=medium; road_obstruction: gold=full pred=none; location.landmark: gold=Quirino pred=None
- `te-095`: severity: gold=high pred=medium
- `te-109`: location.landmark: gold=Sta. Rosa exit pred=Sta. Rosa
- `te-117`: incident_type: gold=heavy_traffic pred=vehicle_breakdown; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown; location.road: gold=None pred=SM Avenue; location.landmark: gold=SM North pred=None
- `te-124`: incident_type: gold=other pred=road_closure; road_obstruction: gold=unknown pred=partial
- `te-127`: incident_type: gold=other pred=road_hazard
- `te-139`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-141`: location.road: gold=Quezon Avenue pred=None
- `te-145`: incident_type: gold=unknown pred=road_closure

### taglish (100)

- `te-001`: incident_type: gold=road_accident pred=vehicle_breakdown; road_obstruction: gold=unknown pred=partial; location.road: gold=Nagtahan pred=Nagtahan Boulevard
- `te-002`: road_obstruction: gold=unknown pred=none
- `te-004`: severity: gold=high pred=medium
- `te-009`: severity: gold=high pred=unknown; language: gold=taglish pred=filipino; location.landmark: gold=underpass pred=None
- `te-010`: severity: gold=unknown pred=medium
- `te-011`: location.direction: gold=southbound pred=None
- `te-013`: road_obstruction: gold=unknown pred=none; location.landmark: gold=Taft pred=MOA
- `te-017`: incident_type: gold=vehicle_breakdown pred=road_hazard; location.road: gold=Ortigas Avenue Extension pred=Ortigas Avenue
- `te-018`: severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=taglish pred=filipino; location.road: gold=None pred=Cubao Avenue; location.landmark: gold=Cubao pred=None
- `te-019`: incident_type: gold=flooding pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=partial pred=none; location.landmark: gold=Buendia LRT pred=Buendia
- `te-020`: invalid JSON
- `te-024`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-025`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-026`: severity: gold=high pred=medium; road_obstruction: gold=full pred=none; location.road: gold=España Boulevard pred=None
- `te-027`: incident_type: gold=road_closure pred=road_hazard; severity: gold=medium pred=low; location.landmark: gold=Libis pred=None
- `te-028`: incident_type: gold=other pred=road_closure; road_obstruction: gold=none pred=partial
- `te-031`: location.landmark: gold=Balintawak toll pred=Balintawak
- `te-032`: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=low; road_obstruction: gold=full pred=none; language: gold=taglish pred=filipino; location.road: gold=Escolta pred=Escolta Avenue
- `te-033`: severity: gold=low pred=medium
- `te-034`: language: gold=taglish pred=english
- `te-036`: road_obstruction: gold=partial pred=none
- `te-037`: road_obstruction: gold=unknown pred=none
- `te-038`: severity: gold=unknown pred=medium
- `te-039`: location.landmark: gold=bus stop pred=None
- `te-041`: severity: gold=low pred=medium; road_obstruction: gold=none pred=unknown
- `te-042`: road_obstruction: gold=partial pred=unknown
- `te-043`: location.landmark: gold=Marikina pred=None
- `te-045`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-046`: severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=taglish pred=filipino
- `te-047`: incident_type: gold=vehicle_breakdown pred=road_accident
- `te-048`: incident_type: gold=vehicle_breakdown pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=full
- `te-049`: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-050`: severity: gold=high pred=medium; road_obstruction: gold=partial pred=none
- `te-053`: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-054`: location.landmark: gold=Katipunan pred=None
- `te-055`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.landmark: gold=Guadalupe pred=None
- `te-057`: severity: gold=unknown pred=medium
- `te-058`: location.landmark: gold=Pasig pred=overpass
- `te-060`: severity: gold=high pred=medium; location.road: gold=SLEX pred=Marcos Highway
- `te-061`: road_obstruction: gold=unknown pred=none
- `te-063`: incident_type: gold=road_hazard pred=road_closure; severity: gold=high pred=medium; road_obstruction: gold=full pred=partial
- `te-064`: severity: gold=medium pred=low; location.landmark: gold=Antipolo pred=None
- `te-068`: road_obstruction: gold=unknown pred=none
- `te-069`: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none
- `te-077`: incident_type: gold=flooding pred=road_hazard
- `te-078`: severity: gold=high pred=unknown; language: gold=taglish pred=filipino; location.landmark: gold=Batasan pred=None
- `te-082`: incident_type: gold=flooding pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=partial pred=none
- `te-084`: severity: gold=high pred=low; road_obstruction: gold=unknown pred=none
- `te-087`: incident_type: gold=flooding pred=vehicle_breakdown; severity: gold=high pred=medium
- `te-088`: location.road: gold=Dimasalang pred=None; location.landmark: gold=None pred=Baha Avenue
- `te-091`: severity: gold=high pred=medium; location.road: gold=None pred=Quezon Avenue; location.landmark: gold=Mabini bridge pred=Sarado ang Mabini
- `te-092`: severity: gold=high pred=medium; location.direction: gold=southbound pred=None
- `te-093`: incident_type: gold=road_closure pred=road_hazard; severity: gold=medium pred=low; road_obstruction: gold=partial pred=none
- `te-094`: location.landmark: gold=Aurora pred=None
- `te-097`: severity: gold=high pred=medium; road_obstruction: gold=full pred=partial; language: gold=taglish pred=filipino
- `te-099`: severity: gold=high pred=medium; location.landmark: gold=BGC pred=None
- `te-102`: location.road: gold=Skyway pred=Skyway Buendia; location.landmark: gold=Buendia exit pred=None
- `te-104`: incident_type: gold=heavy_traffic pred=road_accident
- `te-112`: severity: gold=high pred=medium; location.road: gold=Pasong Tamo pred=Pasong Tamo Avenue
- `te-114`: incident_type: gold=heavy_traffic pred=road_closure; severity: gold=high pred=medium; road_obstruction: gold=none pred=full
- `te-116`: incident_type: gold=heavy_traffic pred=road_closure; road_obstruction: gold=none pred=full; location.landmark: gold=airport pred=None
- `te-118`: incident_type: gold=heavy_traffic pred=other; location.road: gold=Shaw Boulevard pred=EDSA; location.landmark: gold=EDSA pred=Shaw
- `te-119`: incident_type: gold=other pred=road_closure; language: gold=taglish pred=filipino; location.road: gold=None pred=Cubao; location.landmark: gold=Cubao pred=None
- `te-120`: incident_type: gold=other pred=road_closure; location.landmark: gold=UP pred=Katipunan
- `te-121`: incident_type: gold=other pred=road_hazard
- `te-122`: incident_type: gold=other pred=road_accident; road_obstruction: gold=unknown pred=none
- `te-123`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-125`: road_obstruction: gold=unknown pred=none; location.road: gold=Aurora Boulevard pred=None; location.landmark: gold=None pred=Aurora
- `te-126`: incident_type: gold=other pred=road_closure; road_obstruction: gold=none pred=partial
- `te-128`: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=low
- `te-129`: incident_type: gold=other pred=road_accident
- `te-130`: incident_type: gold=other pred=road_hazard; location.road: gold=None pred=Divisoria Avenue; location.landmark: gold=Divisoria market pred=None
- `te-131`: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=medium; location.landmark: gold=toll pred=None
- `te-132`: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=low; location.road: gold=None pred=Baclaran Avenue; location.landmark: gold=Baclaran pred=None
- `te-133`: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=medium
- `te-134`: incident_type: gold=other pred=road_closure; severity: gold=low pred=unknown; road_obstruction: gold=none pred=unknown; location.landmark: gold=DLSU pred=None
- `te-138`: incident_type: gold=unknown pred=road_hazard; language: gold=taglish pred=filipino
- `te-142`: language: gold=taglish pred=filipino; location.landmark: gold=Ortigas pred=None
- `te-150`: incident_type: gold=unknown pred=road_closure; language: gold=taglish pred=filipino
- `te-151`: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none; location.road: gold=None pred=Tapat Avenue; location.landmark: gold=UST pred=None
- `te-152`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial; location.road: gold=Commonwealth Avenue pred=CMWLEV
- `te-153`: incident_type: gold=road_accident pred=vehicle_breakdown
- `te-154`: severity: gold=high pred=unknown; location.road: gold=SLEX pred=None; location.direction: gold=southbound pred=None
- `te-155`: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; location.direction: gold=northbound pred=None
- `te-157`: road_obstruction: gold=unknown pred=partial; location.road: gold=España Boulevard pred=None
- `te-158`: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=partial pred=unknown
- `te-159`: road_obstruction: gold=none pred=unknown; location.road: gold=Roxas Boulevard pred=Rox Boulevard
- `te-161`: road_obstruction: gold=partial pred=full
- `te-162`: incident_type: gold=road_closure pred=road_accident; severity: gold=high pred=medium; road_obstruction: gold=full pred=none; location.road: gold=Recto Avenue pred=España Boulevard
- `te-163`: incident_type: gold=heavy_traffic pred=road_accident; road_obstruction: gold=none pred=partial; location.landmark: gold=Makati pred=Ortigas; location.direction: gold=northbound pred=None
- `te-164`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=high pred=low; location.road: gold=NLEX pred=None
- `te-166`: location.road: gold=Shaw Boulevard pred=Shaw Road
- `te-167`: incident_type: gold=other pred=road_accident; location.road: gold=EDSA pred=None; location.landmark: gold=Guadalupe pred=Edsa Guadalupe
- `te-170`: incident_type: gold=flooding pred=road_closure; language: gold=taglish pred=filipino
- `te-171`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-172`: incident_type: gold=road_accident pred=road_closure; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-173`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial
- `te-174`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-175`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-176`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none

