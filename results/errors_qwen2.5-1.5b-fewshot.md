# Error analysis

168 of 176 items have at least one wrong field (incident_type, severity, road_obstruction, language, any location field, or invalid JSON).

## Count summary

### By gold incident class

| group | errors / size |
|---|---|
| vehicle_breakdown | 19 / 22 |
| road_accident | 23 / 23 |
| road_hazard | 21 / 21 |
| flooding | 24 / 24 |
| road_closure | 20 / 23 |
| heavy_traffic | 23 / 23 |
| other | 19 / 20 |
| unknown | 19 / 20 |

### By subset tag

| group | errors / size |
|---|---|
| noisy | 26 / 26 |
| no_location | 9 / 9 |
| short | 10 / 10 |
| ambiguous | 17 / 18 |
| contradictory | 10 / 10 |

### By language

| group | errors / size |
|---|---|
| filipino | 38 / 38 |
| english | 27 / 28 |
| taglish | 103 / 110 |

## Wrong items by gold incident class

### vehicle_breakdown (19)

- `te-002` [taglish; tags: -] Sira yung makina ng bus sa Aurora, kaya mahaba ang pila ng sasakyan
  - errors: incident_type: gold=vehicle_breakdown pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Aurora","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-006` [english; tags: -] Pickup truck stalled in the middle of Commonwealth Ave near Zuzuarregui, tow on the way
  - errors: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; language: gold=english pred=taglish
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Commonwealth Avenue","landmark":"Zuzuarregui","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-010` [taglish; tags: ambiguous] tricycle nasiraan sa gitna ng Dr. A. Santos Ave, naghihintay ng tulong
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Dr. A. Santos Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-017` [taglish; tags: -] naghihirap ang daloy sa Ortigas Ave Extension, naka-hazard ang van
  - errors: incident_type: gold=vehicle_breakdown pred=road_hazard; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Ortigas Ave Extension","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-018` [taglish; tags: -] PUV na nasira sa may Cubao, wala namang nakaharang
  - errors: incident_type: gold=vehicle_breakdown pred=road_hazard; severity: gold=low pred=unknown; road_obstruction: gold=none pred=full; location.road: gold=None pred=may Cubao; location.landmark: gold=Cubao pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"may Cubao","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"full","language":"taglish"}
- `te-031` [taglish; tags: -] Truck na may sira malapit sa Balintawak toll, sarado ang kanang lane
  - errors: incident_type: gold=vehicle_breakdown pred=road_hazard; road_obstruction: gold=partial pred=full; location.road: gold=None pred=Balintawak Toll; location.landmark: gold=Balintawak toll pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Balintawak Toll","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-036` [taglish; tags: -] Tumirik ang L300 van sa kanang lane ng SLEX, hinihila na
  - errors: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"SLEX","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-037` [taglish; tags: -] Tumigil ang bus sa Taft Ave. southbound sa tapat ng LRT Libertad, mabagal na ang daloy
  - errors: incident_type: gold=vehicle_breakdown pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; location.landmark: gold=LRT Libertad pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Taft Avenue","landmark":null,"direction":"southbound"},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-038` [taglish; tags: ambiguous] wala nang gas ang kotse sa gitna ng Aurora, tinutulak ng mga tao
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Aurora","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-039` [taglish; tags: -] sira ang aircon bus sa Ayala Ave tapos nakahinto pa sa bus stop
  - errors: incident_type: gold=vehicle_breakdown pred=other; severity: gold=low pred=medium; road_obstruction: gold=none pred=partial; location.landmark: gold=bus stop pred=None
  - predicted: {"incident_type":"other","location":{"road":"Ayala Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-040` [english; tags: -] Truck stalled on the C5 flyover near Bagong Ilog, hazard on
  - errors: incident_type: gold=vehicle_breakdown pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full; language: gold=english pred=taglish; location.road: gold=C5 pred=C5 flyover
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5 flyover","landmark":"Bagong Ilog","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-042` [taglish; tags: -] Nakatirik pa rin ang trailer truck sa NLEX Bocaue, kanang lane
  - errors: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"NLEX","landmark":"Bocaue","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-043` [taglish; tags: -] dead battery daw ung SUV sa Marcos Hwy Marikina side, nakaharang pa sa lane
  - errors: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none; location.landmark: gold=Marikina pred=Marikina side
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Marcos Highway","landmark":"Marikina side","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-044` [taglish; tags: -] Taxi broke down sa Roxas Blvd sb near MOA, 2 lanes blocked daw
  - errors: severity: gold=medium pred=low; road_obstruction: gold=partial pred=full; location.landmark: gold=MOA pred=near MOA; location.direction: gold=southbound pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Roxas Boulevard","landmark":"near MOA","direction":null},"severity":"low","road_obstruction":"full","language":"taglish"}
- `te-045` [taglish; tags: -] stalled ang ambulance sa Quezon Ave, pls give way
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-048` [taglish; tags: -] Bus napagod ata, tumirik sa EDSA Boni, full stop traffic
  - errors: incident_type: gold=vehicle_breakdown pred=road_hazard; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":"Boni","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-151` [taglish; tags: noisy] tumirik jeep sa tpat ng ust, 1 lne lng bukas
  - errors: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none; location.landmark: gold=UST pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":null,"landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-152` [taglish; tags: noisy] stalled truck sa cmwlth near fairview ingat
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; location.road: gold=Commonwealth Avenue pred=CMWLT
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"CMWLT","landmark":"Fairview","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-174` [taglish; tags: contradictory] Truck na sira sa EDSA pero tumatakbo naman ang lahat ng lane
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"low","road_obstruction":"full","language":"taglish"}

### road_accident (23)

- `te-001` [taglish; tags: -] Nabaligtad na delivery truck sa Nagtahan, kalat ang gulay sa kalsada
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Nagtahan","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-007` [filipino; tags: -] may aksidente na naman sa Kalayaan flyover, pila hanggang Buendia
  - errors: road_obstruction: gold=unknown pred=partial; language: gold=filipino pred=taglish; location.road: gold=Kalayaan Avenue pred=Kalayaan Flyover; location.landmark: gold=Kalayaan flyover pred=Buendia
  - predicted: {"incident_type":"road_accident","location":{"road":"Kalayaan Flyover","landmark":"Buendia","direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-013` [taglish; tags: -] Bus vs truck sa Edsa-Taft, pila na hanggang MOA
  - errors: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"Taft","direction":null},"severity":"high","road_obstruction":"none","language":"taglish"}
- `te-015` [english; tags: -] Vehicular accident at Katipunan-Boni Serrano, sedan hit a post, no injuries, lane partially blocked.
  - errors: language: gold=english pred=taglish; location.road: gold=Katipunan Avenue pred=Katipunan-Boni Serrano; location.landmark: gold=Boni Serrano pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":"Katipunan-Boni Serrano","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-022` [english; tags: -] Truck skidded on wet road along Marcos Highway but already towed.
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; road_obstruction: gold=none pred=partial; language: gold=english pred=taglish
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"low","road_obstruction":"partial","language":"taglish"}
- `te-025` [taglish; tags: contradictory] Minor lang daw ang banggaan sa C5 pero buong kalsada ay sarado
  - errors: incident_type: gold=road_accident pred=road_closure; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_closure","location":{"road":"C5","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-029` [english; tags: noisy, short] accident mc arthur hway valenzuela
  - errors: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; location.road: gold=McArthur Highway pred=Mc Arthur Highway
  - predicted: {"incident_type":"road_accident","location":{"road":"Mc Arthur Highway","landmark":"Valenzuela","direction":null},"severity":"high","road_obstruction":"full","language":"english"}
- `te-033` [taglish; tags: -] dalawang motor nagbanggaan sa Visayas Ave, nasa gilid na
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Visayas Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-049` [taglish; tags: -] Sumalpok ang SUV sa center island ng Commonwealth, walang nasaktan
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; location.road: gold=Commonwealth Avenue pred=Commonwealth; location.landmark: gold=None pred=Center Island
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Commonwealth","landmark":"Center Island","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-050` [taglish; tags: -] Banggaan ng bus at jeep sa EDSA Ortigas flyover, may mga sugatan, 3 lane ang sarado
  - errors: incident_type: gold=road_accident pred=road_hazard; road_obstruction: gold=partial pred=full; location.road: gold=EDSA pred=EDSA Ortigas Flyover; location.landmark: gold=Ortigas flyover pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA Ortigas Flyover","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-051` [taglish; tags: -] Hit and run sa Shaw, isang pedestrian ang dinala sa ospital
  - errors: incident_type: gold=road_accident pred=unknown; road_obstruction: gold=unknown pred=none; location.road: gold=Shaw Boulevard pred=Shaw
  - predicted: {"incident_type":"unknown","location":{"road":"Shaw","landmark":null,"direction":null},"severity":"high","road_obstruction":"none","language":"taglish"}
- `te-052` [english; tags: -] Rear-end collision on SLEX southbound near Alabang, cars already moved to the side
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; road_obstruction: gold=none pred=partial; language: gold=english pred=taglish
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"SLEX","landmark":"Alabang","direction":"southbound"},"severity":"low","road_obstruction":"partial","language":"taglish"}
- `te-053` [taglish; tags: -] Tumaob ang tricycle sa Visayas Ave, nagtutulungan ang mga tao
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Visayas Avenue","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-054` [taglish; tags: -] Nagkabanggaan ang kotse at motor sa kanto ng Aurora at Katipunan, sarado ang isang lane
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=medium pred=low; road_obstruction: gold=partial pred=none; location.road: gold=Aurora Boulevard pred=Katipunan Avenue; location.landmark: gold=Katipunan pred=Aurora
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Katipunan Avenue","landmark":"Aurora","direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-055` [taglish; tags: noisy] accdent sa edsa guadalupe, 2 trak, madaming tao
  - errors: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":"Guadalupe","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-056` [english; tags: -] Chain collision along Marcos Highway westbound, 4 vehicles involved, all lanes blocked
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; language: gold=english pred=taglish
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Marcos Highway","landmark":null,"direction":"westbound"},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-057` [taglish; tags: -] May nabangga na naman sa Taft, ayun nakahandusay pa ang motor
  - errors: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Taft","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-058` [taglish; tags: -] Nasalpok ng truck ang overpass railing sa C5 Pasig, kalahati ng daan bukas
  - errors: incident_type: gold=road_accident pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.direction: gold=None pred=eastbound
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":"Pasig","direction":"eastbound"},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-059` [english; tags: -] bus vs tricycle collision near Cubao terminal, no word on injuries
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=english pred=taglish; location.road: gold=None pred=near Cubao Terminal; location.landmark: gold=Cubao terminal pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":"near Cubao Terminal","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-153` [taglish; tags: noisy] bngga ng bus ung kotse sa roxas blvd, 1 lane blckd
  - errors: incident_type: gold=road_accident pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=partial pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-154` [taglish; tags: noisy] aksdnte sa slex sb, ambulansya andito na
  - errors: road_obstruction: gold=unknown pred=none; location.direction: gold=southbound pred=None
  - predicted: {"incident_type":"road_accident","location":{"road":"SLEX","landmark":null,"direction":null},"severity":"high","road_obstruction":"none","language":"taglish"}
- `te-172` [taglish; tags: contradictory] Sabi walang accident sa SLEX pero sarado ang dalawang lane
  - errors: incident_type: gold=road_accident pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"SLEX","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-176` [taglish; tags: contradictory] No injuries pero dalawang ambulansya ang nandito sa Commonwealth crash
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Commonwealth Avenue pred=Commonwealth
  - predicted: {"incident_type":"road_accident","location":{"road":"Commonwealth","landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}

### road_hazard (21)

- `te-008` [filipino; tags: -] Maraming bato sa Marcos Hwy
  - errors: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-014` [filipino; tags: -] Ingat sa Congressional, madulas dahil sa ulan
  - errors: invalid JSON
  - predicted: {"incident_type":"flooded","location":{"road":"Congressional","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-034` [taglish; tags: ambiguous] rock slide or something sa Kennon Road?
  - errors: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Kennon Road","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-060` [taglish; tags: -] Nalaglag ang mga bakal ng truck sa Marcos Highway, kalat sa dalawang lane
  - errors: incident_type: gold=road_hazard pred=vehicle_breakdown; severity: gold=high pred=low; road_obstruction: gold=partial pred=none; location.road: gold=SLEX pred=Marcos Highway
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-061` [taglish; tags: -] Natanggal ang takip ng drainage sa Taft near Vito Cruz, delikado sa motor
  - errors: severity: gold=low pred=high; road_obstruction: gold=unknown pred=full; location.landmark: gold=Vito Cruz pred=near Vito Cruz
  - predicted: {"incident_type":"road_hazard","location":{"road":"Taft","landmark":"near Vito Cruz","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-062` [filipino; tags: -] May butas na kalsada sa Quezon Avenue, ingat
  - errors: severity: gold=low pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-063` [taglish; tags: -] May natumbang billboard sa Commonwealth, hindi na madaanan
  - errors: severity: gold=high pred=low; location.road: gold=Commonwealth Avenue pred=Commonwealth
  - predicted: {"incident_type":"road_hazard","location":{"road":"Commonwealth","landmark":null,"direction":null},"severity":"low","road_obstruction":"full","language":"taglish"}
- `te-064` [taglish; tags: -] Gumuhong lupa sa Marcos Highway Antipolo, isang lane ang natabunan
  - errors: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.road: gold=Marcos Highway pred=Marcos Highway Antipolo; location.landmark: gold=Antipolo pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway Antipolo","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-065` [filipino; tags: -] Kalat ang basura sa kalsada sa Dimasalang matapos ang baha
  - errors: severity: gold=low pred=medium; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Dimasalang","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-066` [english; tags: -] Fallen branches along Katipunan, partially blocking the left lane
  - errors: language: gold=english pred=taglish; location.direction: gold=None pred=eastbound
  - predicted: {"incident_type":"road_hazard","location":{"road":"Katipunan","landmark":null,"direction":"eastbound"},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-067` [filipino; tags: -] May butas sa tulay ng Guadalupe, may nasirang gulong na
  - errors: incident_type: gold=road_hazard pred=vehicle_breakdown; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish; location.road: gold=None pred=Guadalupe; location.landmark: gold=Guadalupe pred=None
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Guadalupe","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-068` [taglish; tags: -] Sirang manhole cover sa Roxas Boulevard, delikado sa mga nagmomotor
  - errors: severity: gold=low pred=medium; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-069` [taglish; tags: -] Nagkalat na bubog at bakal sa EDSA southbound pagkatapos ng aksidente
  - errors: incident_type: gold=road_hazard pred=road_accident; severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_accident","location":{"road":"EDSA","landmark":null,"direction":"southbound"},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-070` [filipino; tags: -] May natumbang poste ng Meralco sa Kamias, kalahati ng kalye nakaharang
  - errors: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; language: gold=filipino pred=taglish; location.road: gold=None pred=Kamias; location.landmark: gold=Kamias pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Kamias","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-071` [english; tags: -] Oil spill on Skyway northbound, vehicles slipping
  - errors: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; language: gold=english pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Skyway","landmark":null,"direction":"northbound"},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-072` [filipino; tags: -] May mga basura sa kalsada sa Tanay, sagabal sa daan
  - errors: road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish; location.road: gold=None pred=Tanay; location.landmark: gold=Tanay pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Tanay","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-073` [english; tags: -] Boulders on the road at Kennon Road km 5
  - errors: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; language: gold=english pred=taglish; location.landmark: gold=km 5 pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Kennon Road","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-074` [taglish; tags: -] Nahulog na container sa Roxas Blvd, nakaharang sa isang lane
  - errors: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-075` [filipino; tags: ambiguous] hmm may malaking bato ata sa gitna ng daan sa Rizal Ave
  - errors: incident_type: gold=road_hazard pred=vehicle_breakdown; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Rizal Avenue","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-155` [taglish; tags: noisy] may nalaglag na sako sa C5 nb sa tapat ng ayala, pls avoid
  - errors: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; location.direction: gold=northbound pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":"Ayala","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-156` [filipino; tags: noisy] natumbang puno sa marcos hwy, d na madaan
  - errors: language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}

### flooding (24)

- `te-003` [filipino; tags: -] Sasakyan lumubog sa baha sa Mel Lopez Blvd
  - errors: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Mel Lopez Blvd","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-009` [taglish; tags: -] Flooded na naman daw ung underpass sa España, wag nyo na daanan
  - errors: road_obstruction: gold=unknown pred=full; location.road: gold=España Boulevard pred=underpass; location.landmark: gold=underpass pred=España
  - predicted: {"incident_type":"flooding","location":{"road":"underpass","landmark":"España","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-019` [taglish; tags: -] BAHA!!! sa Taft near Buendia LRT, tuhod level
  - errors: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=partial pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Taft","landmark":"Buendia LRT","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-026` [taglish; tags: noisy] DI MAKADAAN BUS SA FLOODED NA ESPAÑA
  - errors: incident_type: gold=flooding pred=road_hazard
  - predicted: {"incident_type":"road_hazard","location":{"road":"España","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-076` [taglish; tags: -] Hanggang bewang na ang baha sa Espana corner Lacson, wala nang dumadaan
  - errors: incident_type: gold=flooding pred=road_closure; location.road: gold=España Boulevard pred=Espana Corner Lacson; location.landmark: gold=Lacson pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Espana Corner Lacson","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-077` [taglish; tags: -] Baha sa Roxas Blvd near Manila Bay, hanggang gutter lang
  - errors: incident_type: gold=flooding pred=road_hazard; severity: gold=low pred=high; road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Blvd","landmark":"Manila Bay","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-078` [taglish; tags: -] Flood sa Commonwealth Batasan, nagsisitigil ang mga sasakyan
  - errors: road_obstruction: gold=unknown pred=partial; location.road: gold=Commonwealth Avenue pred=None; location.landmark: gold=Batasan pred=Commonwealth Batasan
  - predicted: {"incident_type":"flooding","location":{"road":null,"landmark":"Commonwealth Batasan","direction":null},"severity":"high","road_obstruction":"partial","language":"taglish"}
- `te-079` [filipino; tags: -] Nakalubog sa baha ang kalahati ng kalsada sa Aurora Boulevard
  - errors: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=partial pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Aurora Boulevard","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-080` [taglish; tags: -] Underpass flooded sa Quezon Ave at Mother Ignacia, bawal dumaan ang sedan
  - errors: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=partial pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Quezon Avenue","landmark":"Mother Ignacia","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-081` [filipino; tags: -] Baha sa Marikina, tumataas pa ang tubig
  - errors: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"flooding","location":{"road":null,"landmark":"Marikina","direction":null},"severity":"high","road_obstruction":"partial","language":"filipino"}
- `te-082` [taglish; tags: -] Lubog ang kalsada sa Dr. A. Santos Ave, mga motor lang ang nakakalusot
  - errors: incident_type: gold=flooding pred=vehicle_breakdown; severity: gold=high pred=low; road_obstruction: gold=partial pred=none
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Dr. A. Santos Ave","landmark":null,"direction":null},"severity":"low","road_obstruction":"none","language":"taglish"}
- `te-083` [filipino; tags: -] Katamtamang baha lang sa C5 Ortigas, mabagal ang takbo pero pwede pa
  - errors: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=none pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":"Ortigas","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-084` [taglish; tags: -] Water at knee level na sa Recto, stranded mga jeep
  - errors: invalid JSON
  - predicted: {"incident_type":"flooded","location":{"road":"Recto","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-085` [filipino; tags: short] Muling bumaha sa Pasong Tamo
  - errors: incident_type: gold=flooding pred=unknown; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"unknown","location":{"road":"Pasong Tamo","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-086` [english; tags: -] Waist-deep flood on Taft Ave near Quirino, even trucks cannot pass
  - errors: language: gold=english pred=taglish
  - predicted: {"incident_type":"flooding","location":{"road":"Taft Avenue","landmark":"Quirino","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-087` [taglish; tags: -] Binaha ang EDSA Kamuning northbound, isang lane lang ang ligtas
  - errors: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=medium
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":"Kamuning","direction":"northbound"},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-088` [taglish; tags: noisy] baha d2 sa Dimasalang, pls avoid
  - errors: incident_type: gold=flooding pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Dimasalang","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-089` [filipino; tags: short, ambiguous] Binaha na ba ang Shaw ngayon?
  - errors: incident_type: gold=flooding pred=unknown; language: gold=filipino pred=taglish; location.road: gold=Shaw Boulevard pred=Shaw
  - predicted: {"incident_type":"unknown","location":{"road":"Shaw","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-090` [filipino; tags: -] Malalim na baha sa ilalim ng tulay sa Pasig, hindi madaanan ng kahit anong sasakyan
  - errors: incident_type: gold=flooding pred=unknown; severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; language: gold=filipino pred=taglish; location.road: gold=None pred=Pasig; location.landmark: gold=Pasig pred=None
  - predicted: {"incident_type":"unknown","location":{"road":"Pasig","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-157` [taglish; tags: noisy] bha n nmn sa espna, lubog na mga kotse
  - errors: incident_type: gold=flooding pred=heavy_traffic; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=full; location.road: gold=España Boulevard pred=EDSA; location.landmark: gold=None pred=Magallanes
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"EDSA","landmark":"Magallanes","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-158` [taglish; tags: noisy] flooded na ang quezn ave cor timog, d makadaan sedan
  - errors: road_obstruction: gold=partial pred=full; location.road: gold=Quezon Avenue pred=Quezon Avenue Cor. Timog; location.landmark: gold=Timog pred=None
  - predicted: {"incident_type":"flooding","location":{"road":"Quezon Avenue Cor. Timog","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-159` [taglish; tags: noisy] ankle deep lng baha sa rox blvd, ok pa
  - errors: incident_type: gold=flooding pred=unknown; severity: gold=low pred=unknown; road_obstruction: gold=none pred=full; location.road: gold=Roxas Boulevard pred=Rox Blvrd
  - predicted: {"incident_type":"unknown","location":{"road":"Rox Blvrd","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"full","language":"taglish"}
- `te-170` [taglish; tags: contradictory] Wala daw bumaha sa Recto pero stranded ang mga bus
  - errors: incident_type: gold=flooding pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full; location.road: gold=Recto Avenue pred=Recto
  - predicted: {"incident_type":"road_hazard","location":{"road":"Recto","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-175` [taglish; tags: contradictory] Minor flooding lang daw sa Taft pero di na madaanan ng bus
  - errors: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=partial
  - predicted: {"incident_type":"flooding","location":{"road":"Taft","landmark":null,"direction":null},"severity":"low","road_obstruction":"partial","language":"taglish"}

### road_closure (20)

- `te-005` [filipino; tags: -] Wag dumaan sa Anda Circle, sarado
  - errors: incident_type: gold=road_closure pred=road_hazard; language: gold=filipino pred=taglish; location.road: gold=None pred=Anda Circle; location.landmark: gold=Anda Circle pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Anda Circle","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-011` [taglish; tags: -] MMDA: lahat ng lane southbound Roxas Blvd sarado mula Quirino para sa event
  - errors: language: gold=taglish pred=english
  - predicted: {"incident_type":"road_closure","location":{"road":"Roxas Boulevard","landmark":"Quirino","direction":"southbound"},"severity":"high","road_obstruction":"full","language":"english"}
- `te-016` [english; tags: -] Road closed due to fallen cables along Sumulong Highway westbound.
  - errors: language: gold=english pred=taglish
  - predicted: {"incident_type":"road_closure","location":{"road":"Sumulong Highway","landmark":null,"direction":"westbound"},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-023` [filipino; tags: contradictory] Sarado raw buong Commonwealth pero dumadaan pa kami ngayon
  - errors: incident_type: gold=road_closure pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=Commonwealth
  - predicted: {"incident_type":"road_hazard","location":{"road":"Commonwealth","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-027` [taglish; tags: noisy] cnstrctn sa c5 libis, 1 lane lang
  - errors: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.landmark: gold=Libis pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"C5","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-032` [taglish; tags: -] Isinara ang Escolta dahil sa shooting ng pelikula
  - errors: incident_type: gold=road_closure pred=road_hazard
  - predicted: {"incident_type":"road_hazard","location":{"road":"Escolta","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-091` [taglish; tags: -] Sarado ang Mabini bridge para sa repair, gamitin ang Quezon bridge
  - errors: location.road: gold=None pred=Mabini Bridge; location.landmark: gold=Mabini bridge pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Mabini Bridge","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-093` [taglish; tags: -] One lane open lang sa C5 dahil sa water pipe installation
  - errors: incident_type: gold=road_closure pred=road_hazard
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-094` [taglish; tags: -] Road closed sa Katipunan-Aurora, may sunog sa building
  - errors: location.road: gold=Katipunan Avenue pred=Katipunan-Aurora; location.landmark: gold=Aurora pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Katipunan-Aurora","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-095` [english; tags: -] Taft Avenue northbound closed from Pedro Gil to Vito Cruz for the procession
  - errors: language: gold=english pred=taglish; location.landmark: gold=Pedro Gil pred=None
  - predicted: {"incident_type":"road_closure","location":{"road":"Taft Avenue","landmark":null,"direction":"northbound"},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-098` [taglish; tags: -] Ginagawa ang kalsada sa Ortigas, kaya iisang lane lang ang madaanan
  - errors: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.road: gold=Ortigas Avenue pred=Ortigas
  - predicted: {"incident_type":"road_closure","location":{"road":"Ortigas","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-099` [taglish; tags: -] Marathon sa BGC, sarado ang 5th Avenue hanggang tanghali
  - errors: incident_type: gold=road_closure pred=other; severity: gold=high pred=medium; location.road: gold=5th Avenue pred=BGC; location.landmark: gold=BGC pred=5th Avenue
  - predicted: {"incident_type":"other","location":{"road":"BGC","landmark":"5th Avenue","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-100` [filipino; tags: no_location] kalsada sa harap ng simbahan sarado dahil sa prusisyon
  - errors: incident_type: gold=road_closure pred=road_hazard; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":null,"landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-101` [english; tags: -] Partial closure on Commonwealth southbound due to utility works, use inner lanes
  - errors: language: gold=english pred=taglish; location.road: gold=Commonwealth Avenue pred=Commonwealth
  - predicted: {"incident_type":"road_closure","location":{"road":"Commonwealth","landmark":null,"direction":"southbound"},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-102` [taglish; tags: -] Isa na lang ang bukas na lane sa Skyway Buendia exit dahil sa maintenance
  - errors: road_obstruction: gold=partial pred=full; location.landmark: gold=Buendia exit pred=Buendia
  - predicted: {"incident_type":"road_closure","location":{"road":"Skyway","landmark":"Buendia","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-103` [filipino; tags: -] SARADO ANG BUONG EDSA PAPUNTANG MAKATI NGAYONG GABI
  - errors: incident_type: gold=road_closure pred=heavy_traffic; language: gold=filipino pred=taglish; location.landmark: gold=Makati pred=None
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-160` [taglish; tags: noisy] closed ang taft ave for fun run til 10am
  - errors: severity: gold=high pred=unknown
  - predicted: {"incident_type":"road_closure","location":{"road":"Taft Avenue","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"full","language":"taglish"}
- `te-161` [taglish; tags: noisy] 2 lne lng bukas sa ortgas ave, my hukay
  - errors: incident_type: gold=road_closure pred=road_hazard; road_obstruction: gold=partial pred=full; location.road: gold=Ortigas Avenue pred=Orthgas Avenue
  - predicted: {"incident_type":"road_hazard","location":{"road":"Orthgas Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-162` [taglish; tags: noisy] sarado d2 sa recto, my parade
  - errors: incident_type: gold=road_closure pred=unknown; severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; location.road: gold=Recto Avenue pred=Recto
  - predicted: {"incident_type":"unknown","location":{"road":"Recto","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-173` [taglish; tags: contradictory] Open na raw ang Roxas Blvd pero may barikada pa rin
  - errors: incident_type: gold=road_closure pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}

### heavy_traffic (23)

- `te-004` [taglish; tags: -] traffic sa SCTEX near Tarlac exit, 3 hrs daw
  - errors: severity: gold=high pred=medium; road_obstruction: gold=none pred=full; location.landmark: gold=Tarlac exit pred=near Tarlac exit
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"SCTEX","landmark":"near Tarlac exit","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-012` [taglish; tags: noisy] heavy traffik papuntang Sucat galing Alabang
  - errors: road_obstruction: gold=none pred=full; location.road: gold=None pred=Alabang; location.landmark: gold=Sucat pred=None
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Alabang","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-024` [taglish; tags: contradictory] Light traffic daw sa Shaw pero di gumagalaw ang mga sasakyan
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial; location.road: gold=Shaw Boulevard pred=Shaw
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Shaw","landmark":null,"direction":null},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-030` [english; tags: -] Long line of vehicles going to NAIA Terminal 3.
  - errors: road_obstruction: gold=none pred=full; language: gold=english pred=taglish
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":"NAIA Terminal 3","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-104` [taglish; tags: -] stuck pa rin kami sa C5 southbound papuntang Libis, 45 mins na
  - errors: road_obstruction: gold=none pred=full; location.landmark: gold=Libis pred=None
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"C5","landmark":null,"direction":"southbound"},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-105` [filipino; tags: -] Mahaba ang pila ng sasakyan sa Skyway toll gate
  - errors: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Skyway","landmark":"toll gate","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-106` [english; tags: -] Traffic buildup along Roxas Boulevard near Mall of Asia
  - errors: road_obstruction: gold=none pred=full; language: gold=english pred=taglish; location.landmark: gold=Mall of Asia pred=near Mall of Asia
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Roxas Boulevard","landmark":"near Mall of Asia","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-107` [taglish; tags: -] Rush hour na naman sa EDSA, siksikan ang mga bus
  - errors: road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-108` [filipino; tags: -] Halos hindi umuusad ang trapiko sa Commonwealth, dalawang oras na
  - errors: severity: gold=high pred=medium; road_obstruction: gold=none pred=full; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=Commonwealth
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Commonwealth","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-109` [english; tags: -] Slow traffic going to Sta. Rosa exit SLEX northbound
  - errors: road_obstruction: gold=none pred=full; language: gold=english pred=taglish; location.landmark: gold=Sta. Rosa exit pred=None
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"SLEX","landmark":null,"direction":"northbound"},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-110` [taglish; tags: -] Heavy traffic daw sa Ortigas pauwi, iwasan na
  - errors: road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Ortigas Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-111` [filipino; tags: -] Pila hanggang Balintawak ang mga trak papuntang NLEX
  - errors: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; language: gold=filipino pred=taglish; location.landmark: gold=Balintawak pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"NLEX","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-112` [taglish; tags: noisy] trafik malala sa Pasong Tamo, almost 1 hour na
  - errors: road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Pasong Tamo","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-113` [english; tags: -] Moderate traffic on Quezon Ave from Timog to Kamuning
  - errors: road_obstruction: gold=none pred=partial; language: gold=english pred=taglish; location.landmark: gold=Timog pred=None; location.direction: gold=None pred=eastbound
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Quezon Avenue","landmark":null,"direction":"eastbound"},"severity":"medium","road_obstruction":"partial","language":"taglish"}
- `te-114` [taglish; tags: -] Walang gumagalaw sa Aurora Blvd Cubao, stuck lahat ng bus
  - errors: incident_type: gold=heavy_traffic pred=road_hazard; road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Aurora Boulevard","landmark":"Cubao","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-115` [filipino; tags: -] Daloy ng trapiko sa Taft ay mabagal pero gumagalaw
  - errors: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"Taft","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-116` [taglish; tags: -] may build up sa Macapagal papuntang airport
  - errors: incident_type: gold=heavy_traffic pred=unknown; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown; location.road: gold=Macapagal Boulevard pred=Macapagal Airports; location.landmark: gold=airport pred=None
  - predicted: {"incident_type":"unknown","location":{"road":"Macapagal Airports","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-117` [english; tags: -] Traffic in front of SM North, several buses queueing
  - errors: road_obstruction: gold=none pred=full; language: gold=english pred=taglish; location.road: gold=None pred=SM North; location.landmark: gold=SM North pred=None
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"SM North","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-118` [taglish; tags: ambiguous] ang tagal ng green light, mahaba ang pila sa kanto ng Shaw at EDSA
  - errors: severity: gold=medium pred=high; road_obstruction: gold=none pred=full; location.road: gold=Shaw Boulevard pred=Shaw
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Shaw","landmark":"EDSA","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-163` [taglish; tags: noisy] grabe trapik sa edsa nb mkati papuntang ortgas
  - errors: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; location.landmark: gold=Makati pred=None; location.direction: gold=northbound pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-164` [taglish; tags: noisy] sbrang bagal s nlex, 2 hrs n kmi dto
  - errors: incident_type: gold=heavy_traffic pred=road_hazard; road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"NLEX","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-165` [filipino; tags: noisy] trapik nmn sa aurora blvd cubao, ang bgal
  - errors: incident_type: gold=heavy_traffic pred=unknown; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"unknown","location":{"road":"Aurora Boulevard","landmark":"Cubao","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-171` [taglish; tags: contradictory] Light traffic sa Katipunan pero 2 oras na akong stuck
  - errors: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Katipunan","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}

### other (19)

- `te-028` [taglish; tags: -] traffic enforcer nag-dedirect sa Cubao kasi brownout
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=full; location.road: gold=None pred=Cubao; location.landmark: gold=Cubao pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Cubao","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"full","language":"taglish"}
- `te-035` [english; tags: -] Tunnel lights out near Quezon Ave, cars moving slowly.
  - errors: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=full; language: gold=english pred=taglish; location.landmark: gold=tunnel pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Quezon Avenue","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-119` [taglish; tags: -] Brownout sa Cubao, walang traffic light at nagma-manual ang MMDA
  - errors: road_obstruction: gold=none pred=full; location.road: gold=None pred=Cubao; location.landmark: gold=Cubao pred=None
  - predicted: {"incident_type":"other","location":{"road":"Cubao","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-120` [taglish; tags: -] Checkpoint ng pulis sa Katipunan pagpasok ng UP, nagsisikip ang dalawang lane
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.landmark: gold=UP pred=None; location.direction: gold=None pred=eastbound
  - predicted: {"incident_type":"road_hazard","location":{"road":"Katipunan","landmark":null,"direction":"eastbound"},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-121` [taglish; tags: -] Truck inspection ng LTO sa Marcos Highway, nagkakapila sa isang lane
  - errors: incident_type: gold=other pred=road_hazard; road_obstruction: gold=partial pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-122` [taglish; tags: -] May motorcade ng artista sa EDSA, saglit na pinahinto ang mga sasakyan
  - errors: road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"other","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-123` [taglish; tags: -] Sirang traffic light sa Taft-Quirino, nag-aabang ang mga sasakyan
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full; location.road: gold=Taft Avenue pred=Taft-Quirino; location.landmark: gold=Quirino pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Taft-Quirino","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-124` [english; tags: -] Concert crowd spilling onto Aurora Boulevard near the Big Dome, traffic enforcers on site
  - errors: incident_type: gold=other pred=heavy_traffic; road_obstruction: gold=unknown pred=full; language: gold=english pred=taglish
  - predicted: {"incident_type":"heavy_traffic","location":{"road":"Aurora Boulevard","landmark":"Big Dome","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-125` [taglish; tags: -] Fire truck na nakatigil sa tabi ng kalsada sa Aurora, may sunog sa katabing building
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Aurora","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-126` [taglish; tags: -] Naglagay ng bagong pedestrian lane markings sa Katipunan, kaya mabagal ang mga sasakyan
  - errors: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"Katipunan","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-127` [english; tags: -] Road sweepers blocking the right lane along Roxas Boulevard
  - errors: incident_type: gold=other pred=road_hazard; road_obstruction: gold=partial pred=full; language: gold=english pred=taglish; location.direction: gold=None pred=eastbound
  - predicted: {"incident_type":"road_hazard","location":{"road":"Roxas Boulevard","landmark":null,"direction":"eastbound"},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-128` [taglish; tags: -] Checkpoint sa NLEX Valenzuela entry, mahaba ang pila
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"NLEX","landmark":"Valenzuela","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-129` [taglish; tags: -] Funeral procession sa EDSA, mabagal ang takbo ng mga sasakyan
  - errors: road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"other","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-130` [taglish; tags: -] Delivery trucks double-parked sa harap ng Divisoria market, naka-block sa isang lane
  - errors: incident_type: gold=other pred=road_hazard; road_obstruction: gold=partial pred=full; location.road: gold=None pred=Divisoria Market; location.landmark: gold=Divisoria market pred=Harap
  - predicted: {"incident_type":"road_hazard","location":{"road":"Divisoria Market","landmark":"Harap","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-131` [taglish; tags: -] Malfunctioning ang boom barrier sa Skyway toll
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; location.landmark: gold=toll pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Skyway","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-132` [taglish; tags: -] Street vendors occupying the road sa Baclaran, mabagal ang daloy
  - errors: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=full; location.road: gold=None pred=Baclaran; location.landmark: gold=Baclaran pred=None
  - predicted: {"incident_type":"road_hazard","location":{"road":"Baclaran","landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-133` [taglish; tags: -] Naka-hazard ang MMDA truck sa EDSA, nagtatanggal ng sirang barrier
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-166` [taglish; tags: noisy] walang ilaw ang trafic light sa shaw cor edsa, nag-dedirect ang enforcer
  - errors: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; location.road: gold=Shaw Boulevard pred=EDSA; location.landmark: gold=EDSA pred=Shaw Cor
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":"Shaw Cor","direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-167` [taglish; tags: noisy] checkpt sa edsa guadalupe, pumipila mga kotse
  - errors: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=full
  - predicted: {"incident_type":"road_hazard","location":{"road":"EDSA","landmark":"Guadalupe","direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}

### unknown (19)

- `te-020` [taglish; tags: no_location, ambiguous] Malayo pa ang daan pero stuck na kami, di ko alam bakit
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"full","language":"taglish"}
- `te-021` [filipino; tags: ambiguous] ano po kaya ang nangyari sa EDSA Monumento?
  - errors: language: gold=filipino pred=taglish; location.landmark: gold=Monumento pred=EDSA Monumento
  - predicted: {"incident_type":"unknown","location":{"road":"EDSA","landmark":"EDSA Monumento","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-135` [filipino; tags: ambiguous] ano meron sa Katipunan? di ako makadaan
  - errors: language: gold=filipino pred=taglish
  - predicted: {"incident_type":"unknown","location":{"road":"Katipunan","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-136` [filipino; tags: no_location, ambiguous] may nakita akong ambulansya kanina
  - errors: language: gold=filipino pred=taglish; location.road: gold=None pred=unknown; location.landmark: gold=None pred=unknown
  - predicted: {"incident_type":"unknown","location":{"road":"unknown","landmark":"unknown","direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-137` [filipino; tags: short] Bakit ganyan ang EDSA kanina?
  - errors: language: gold=filipino pred=taglish
  - predicted: {"incident_type":"unknown","location":{"road":"EDSA","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-138` [taglish; tags: no_location] Please be safe po sa mga naka-motor
  - errors: invalid JSON
  - predicted: {"incident_type":"unknown","location":{"road":"unknown","landmark":"unknown","direction":"unknown"},"severity":"unknown","road_obstruction":"unknown","language":"english"}
- `te-139` [english; tags: no_location, short] Update on traffic please
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=english pred=taglish
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"taglish"}
- `te-140` [filipino; tags: ambiguous] Parang may problema sa C5
  - errors: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_hazard","location":{"road":"C5","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-141` [english; tags: short] anyone coming from Quezon Ave?
  - errors: language: gold=english pred=taglish; location.landmark: gold=None pred=Quezon Avenue; location.direction: gold=None pred=northbound
  - predicted: {"incident_type":"unknown","location":{"road":"Quezon Avenue","landmark":"Quezon Avenue","direction":"northbound"},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-142` [taglish; tags: short] Sino may info sa Ortigas?
  - errors: location.road: gold=None pred=Ortigas; location.landmark: gold=Ortigas pred=None
  - predicted: {"incident_type":"unknown","location":{"road":"Ortigas","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-143` [filipino; tags: ambiguous] May naririnig akong sirena sa Commonwealth
  - errors: language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=Commonwealth
  - predicted: {"incident_type":"unknown","location":{"road":"Commonwealth","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-144` [filipino; tags: ambiguous] Delikado raw dumaan sa Marcos Highway
  - errors: incident_type: gold=unknown pred=road_accident; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"road_accident","location":{"road":"Marcos Highway","landmark":null,"direction":null},"severity":"high","road_obstruction":"none","language":"taglish"}
- `te-145` [english; tags: no_location, short] road still open?
  - errors: incident_type: gold=unknown pred=road_closure; language: gold=english pred=taglish
  - predicted: {"incident_type":"road_closure","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-146` [english; tags: no_location, short] TRAFFIC???
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"medium","road_obstruction":"none","language":"english"}
- `te-147` [filipino; tags: ambiguous] grabe ang daming tao sa Taft ngayon
  - errors: incident_type: gold=unknown pred=vehicle_breakdown; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"vehicle_breakdown","location":{"road":"Taft","landmark":null,"direction":null},"severity":"high","road_obstruction":"none","language":"taglish"}
- `te-148` [filipino; tags: no_location, short, ambiguous] wag na dumaan dyan
  - errors: language: gold=filipino pred=taglish
  - predicted: {"incident_type":"unknown","location":{"road":null,"landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-149` [filipino; tags: ambiguous] Kita ko may pulis sa Shaw, di ko alam bakit
  - errors: language: gold=filipino pred=taglish; location.road: gold=Shaw Boulevard pred=Shaw
  - predicted: {"incident_type":"unknown","location":{"road":"Shaw","landmark":null,"direction":null},"severity":"unknown","road_obstruction":"unknown","language":"taglish"}
- `te-168` [filipino; tags: noisy, ambiguous] anu ngyari sa cmwlth?? grbe ang daming sasakyan
  - errors: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=CMW
  - predicted: {"incident_type":"road_hazard","location":{"road":"CMW","landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}
- `te-169` [filipino; tags: noisy, no_location] ingat sa mga nagmmotor ngayon
  - errors: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
  - predicted: {"incident_type":"heavy_traffic","location":{"road":null,"landmark":null,"direction":null},"severity":"high","road_obstruction":"full","language":"taglish"}

## Wrong items by subset tag

### noisy (26)

- `te-012`: road_obstruction: gold=none pred=full; location.road: gold=None pred=Alabang; location.landmark: gold=Sucat pred=None
- `te-026`: incident_type: gold=flooding pred=road_hazard
- `te-027`: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.landmark: gold=Libis pred=None
- `te-029`: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; location.road: gold=McArthur Highway pred=Mc Arthur Highway
- `te-055`: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-088`: incident_type: gold=flooding pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-112`: road_obstruction: gold=none pred=full
- `te-151`: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none; location.landmark: gold=UST pred=None
- `te-152`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; location.road: gold=Commonwealth Avenue pred=CMWLT
- `te-153`: incident_type: gold=road_accident pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=partial pred=full
- `te-154`: road_obstruction: gold=unknown pred=none; location.direction: gold=southbound pred=None
- `te-155`: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; location.direction: gold=northbound pred=None
- `te-156`: language: gold=filipino pred=taglish
- `te-157`: incident_type: gold=flooding pred=heavy_traffic; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=full; location.road: gold=España Boulevard pred=EDSA; location.landmark: gold=None pred=Magallanes
- `te-158`: road_obstruction: gold=partial pred=full; location.road: gold=Quezon Avenue pred=Quezon Avenue Cor. Timog; location.landmark: gold=Timog pred=None
- `te-159`: incident_type: gold=flooding pred=unknown; severity: gold=low pred=unknown; road_obstruction: gold=none pred=full; location.road: gold=Roxas Boulevard pred=Rox Blvrd
- `te-160`: severity: gold=high pred=unknown
- `te-161`: incident_type: gold=road_closure pred=road_hazard; road_obstruction: gold=partial pred=full; location.road: gold=Ortigas Avenue pred=Orthgas Avenue
- `te-162`: incident_type: gold=road_closure pred=unknown; severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; location.road: gold=Recto Avenue pred=Recto
- `te-163`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; location.landmark: gold=Makati pred=None; location.direction: gold=northbound pred=None
- `te-164`: incident_type: gold=heavy_traffic pred=road_hazard; road_obstruction: gold=none pred=full
- `te-165`: incident_type: gold=heavy_traffic pred=unknown; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish
- `te-166`: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; location.road: gold=Shaw Boulevard pred=EDSA; location.landmark: gold=EDSA pred=Shaw Cor
- `te-167`: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=full
- `te-168`: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=CMW
- `te-169`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish

### no_location (9)

- `te-020`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-100`: incident_type: gold=road_closure pred=road_hazard; language: gold=filipino pred=taglish
- `te-136`: language: gold=filipino pred=taglish; location.road: gold=None pred=unknown; location.landmark: gold=None pred=unknown
- `te-138`: invalid JSON
- `te-139`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=english pred=taglish
- `te-145`: incident_type: gold=unknown pred=road_closure; language: gold=english pred=taglish
- `te-146`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-148`: language: gold=filipino pred=taglish
- `te-169`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish

### short (10)

- `te-029`: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; location.road: gold=McArthur Highway pred=Mc Arthur Highway
- `te-085`: incident_type: gold=flooding pred=unknown; language: gold=filipino pred=taglish
- `te-089`: incident_type: gold=flooding pred=unknown; language: gold=filipino pred=taglish; location.road: gold=Shaw Boulevard pred=Shaw
- `te-137`: language: gold=filipino pred=taglish
- `te-139`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=english pred=taglish
- `te-141`: language: gold=english pred=taglish; location.landmark: gold=None pred=Quezon Avenue; location.direction: gold=None pred=northbound
- `te-142`: location.road: gold=None pred=Ortigas; location.landmark: gold=Ortigas pred=None
- `te-145`: incident_type: gold=unknown pred=road_closure; language: gold=english pred=taglish
- `te-146`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none
- `te-148`: language: gold=filipino pred=taglish

### ambiguous (17)

- `te-010`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-020`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-021`: language: gold=filipino pred=taglish; location.landmark: gold=Monumento pred=EDSA Monumento
- `te-034`: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-038`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-075`: incident_type: gold=road_hazard pred=vehicle_breakdown; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-089`: incident_type: gold=flooding pred=unknown; language: gold=filipino pred=taglish; location.road: gold=Shaw Boulevard pred=Shaw
- `te-118`: severity: gold=medium pred=high; road_obstruction: gold=none pred=full; location.road: gold=Shaw Boulevard pred=Shaw
- `te-135`: language: gold=filipino pred=taglish
- `te-136`: language: gold=filipino pred=taglish; location.road: gold=None pred=unknown; location.landmark: gold=None pred=unknown
- `te-140`: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-143`: language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=Commonwealth
- `te-144`: incident_type: gold=unknown pred=road_accident; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
- `te-147`: incident_type: gold=unknown pred=vehicle_breakdown; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
- `te-148`: language: gold=filipino pred=taglish
- `te-149`: language: gold=filipino pred=taglish; location.road: gold=Shaw Boulevard pred=Shaw
- `te-168`: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=CMW

### contradictory (10)

- `te-023`: incident_type: gold=road_closure pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=Commonwealth
- `te-024`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial; location.road: gold=Shaw Boulevard pred=Shaw
- `te-025`: incident_type: gold=road_accident pred=road_closure; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-170`: incident_type: gold=flooding pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full; location.road: gold=Recto Avenue pred=Recto
- `te-171`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-172`: incident_type: gold=road_accident pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-173`: incident_type: gold=road_closure pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-174`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=full
- `te-175`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=partial
- `te-176`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Commonwealth Avenue pred=Commonwealth

## Wrong items by language

### filipino (38)

- `te-003`: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-005`: incident_type: gold=road_closure pred=road_hazard; language: gold=filipino pred=taglish; location.road: gold=None pred=Anda Circle; location.landmark: gold=Anda Circle pred=None
- `te-007`: road_obstruction: gold=unknown pred=partial; language: gold=filipino pred=taglish; location.road: gold=Kalayaan Avenue pred=Kalayaan Flyover; location.landmark: gold=Kalayaan flyover pred=Buendia
- `te-008`: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-014`: invalid JSON
- `te-021`: language: gold=filipino pred=taglish; location.landmark: gold=Monumento pred=EDSA Monumento
- `te-023`: incident_type: gold=road_closure pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=Commonwealth
- `te-062`: severity: gold=low pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-065`: severity: gold=low pred=medium; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-067`: incident_type: gold=road_hazard pred=vehicle_breakdown; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish; location.road: gold=None pred=Guadalupe; location.landmark: gold=Guadalupe pred=None
- `te-070`: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; language: gold=filipino pred=taglish; location.road: gold=None pred=Kamias; location.landmark: gold=Kamias pred=None
- `te-072`: road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish; location.road: gold=None pred=Tanay; location.landmark: gold=Tanay pred=None
- `te-075`: incident_type: gold=road_hazard pred=vehicle_breakdown; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-079`: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=partial pred=full; language: gold=filipino pred=taglish
- `te-081`: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=partial
- `te-083`: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=none pred=full; language: gold=filipino pred=taglish
- `te-085`: incident_type: gold=flooding pred=unknown; language: gold=filipino pred=taglish
- `te-089`: incident_type: gold=flooding pred=unknown; language: gold=filipino pred=taglish; location.road: gold=Shaw Boulevard pred=Shaw
- `te-090`: incident_type: gold=flooding pred=unknown; severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; language: gold=filipino pred=taglish; location.road: gold=None pred=Pasig; location.landmark: gold=Pasig pred=None
- `te-100`: incident_type: gold=road_closure pred=road_hazard; language: gold=filipino pred=taglish
- `te-103`: incident_type: gold=road_closure pred=heavy_traffic; language: gold=filipino pred=taglish; location.landmark: gold=Makati pred=None
- `te-105`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; language: gold=filipino pred=taglish
- `te-108`: severity: gold=high pred=medium; road_obstruction: gold=none pred=full; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=Commonwealth
- `te-111`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; language: gold=filipino pred=taglish; location.landmark: gold=Balintawak pred=None
- `te-115`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; language: gold=filipino pred=taglish
- `te-135`: language: gold=filipino pred=taglish
- `te-136`: language: gold=filipino pred=taglish; location.road: gold=None pred=unknown; location.landmark: gold=None pred=unknown
- `te-137`: language: gold=filipino pred=taglish
- `te-140`: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish
- `te-143`: language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=Commonwealth
- `te-144`: incident_type: gold=unknown pred=road_accident; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
- `te-147`: incident_type: gold=unknown pred=vehicle_breakdown; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=none; language: gold=filipino pred=taglish
- `te-148`: language: gold=filipino pred=taglish
- `te-149`: language: gold=filipino pred=taglish; location.road: gold=Shaw Boulevard pred=Shaw
- `te-156`: language: gold=filipino pred=taglish
- `te-165`: incident_type: gold=heavy_traffic pred=unknown; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown; language: gold=filipino pred=taglish
- `te-168`: incident_type: gold=unknown pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish; location.road: gold=Commonwealth Avenue pred=CMW
- `te-169`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; language: gold=filipino pred=taglish

### english (27)

- `te-006`: severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none; language: gold=english pred=taglish
- `te-015`: language: gold=english pred=taglish; location.road: gold=Katipunan Avenue pred=Katipunan-Boni Serrano; location.landmark: gold=Boni Serrano pred=None
- `te-016`: language: gold=english pred=taglish
- `te-022`: incident_type: gold=road_accident pred=vehicle_breakdown; road_obstruction: gold=none pred=partial; language: gold=english pred=taglish
- `te-029`: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; location.road: gold=McArthur Highway pred=Mc Arthur Highway
- `te-030`: road_obstruction: gold=none pred=full; language: gold=english pred=taglish
- `te-035`: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=full; language: gold=english pred=taglish; location.landmark: gold=tunnel pred=None
- `te-040`: incident_type: gold=vehicle_breakdown pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full; language: gold=english pred=taglish; location.road: gold=C5 pred=C5 flyover
- `te-052`: incident_type: gold=road_accident pred=vehicle_breakdown; road_obstruction: gold=none pred=partial; language: gold=english pred=taglish
- `te-056`: incident_type: gold=road_accident pred=vehicle_breakdown; language: gold=english pred=taglish
- `te-059`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=english pred=taglish; location.road: gold=None pred=near Cubao Terminal; location.landmark: gold=Cubao terminal pred=None
- `te-066`: language: gold=english pred=taglish; location.direction: gold=None pred=eastbound
- `te-071`: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; language: gold=english pred=taglish
- `te-073`: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; language: gold=english pred=taglish; location.landmark: gold=km 5 pred=None
- `te-086`: language: gold=english pred=taglish
- `te-095`: language: gold=english pred=taglish; location.landmark: gold=Pedro Gil pred=None
- `te-101`: language: gold=english pred=taglish; location.road: gold=Commonwealth Avenue pred=Commonwealth
- `te-106`: road_obstruction: gold=none pred=full; language: gold=english pred=taglish; location.landmark: gold=Mall of Asia pred=near Mall of Asia
- `te-109`: road_obstruction: gold=none pred=full; language: gold=english pred=taglish; location.landmark: gold=Sta. Rosa exit pred=None
- `te-113`: road_obstruction: gold=none pred=partial; language: gold=english pred=taglish; location.landmark: gold=Timog pred=None; location.direction: gold=None pred=eastbound
- `te-117`: road_obstruction: gold=none pred=full; language: gold=english pred=taglish; location.road: gold=None pred=SM North; location.landmark: gold=SM North pred=None
- `te-124`: incident_type: gold=other pred=heavy_traffic; road_obstruction: gold=unknown pred=full; language: gold=english pred=taglish
- `te-127`: incident_type: gold=other pred=road_hazard; road_obstruction: gold=partial pred=full; language: gold=english pred=taglish; location.direction: gold=None pred=eastbound
- `te-139`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; language: gold=english pred=taglish
- `te-141`: language: gold=english pred=taglish; location.landmark: gold=None pred=Quezon Avenue; location.direction: gold=None pred=northbound
- `te-145`: incident_type: gold=unknown pred=road_closure; language: gold=english pred=taglish
- `te-146`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none

### taglish (103)

- `te-001`: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=medium pred=low; road_obstruction: gold=unknown pred=none
- `te-002`: incident_type: gold=vehicle_breakdown pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full
- `te-004`: severity: gold=high pred=medium; road_obstruction: gold=none pred=full; location.landmark: gold=Tarlac exit pred=near Tarlac exit
- `te-009`: road_obstruction: gold=unknown pred=full; location.road: gold=España Boulevard pred=underpass; location.landmark: gold=underpass pred=España
- `te-010`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-011`: language: gold=taglish pred=english
- `te-012`: road_obstruction: gold=none pred=full; location.road: gold=None pred=Alabang; location.landmark: gold=Sucat pred=None
- `te-013`: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=none
- `te-017`: incident_type: gold=vehicle_breakdown pred=road_hazard; road_obstruction: gold=unknown pred=full
- `te-018`: incident_type: gold=vehicle_breakdown pred=road_hazard; severity: gold=low pred=unknown; road_obstruction: gold=none pred=full; location.road: gold=None pred=may Cubao; location.landmark: gold=Cubao pred=None
- `te-019`: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=partial pred=full
- `te-020`: incident_type: gold=unknown pred=heavy_traffic; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-024`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=partial; location.road: gold=Shaw Boulevard pred=Shaw
- `te-025`: incident_type: gold=road_accident pred=road_closure; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-026`: incident_type: gold=flooding pred=road_hazard
- `te-027`: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.landmark: gold=Libis pred=None
- `te-028`: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=full; location.road: gold=None pred=Cubao; location.landmark: gold=Cubao pred=None
- `te-031`: incident_type: gold=vehicle_breakdown pred=road_hazard; road_obstruction: gold=partial pred=full; location.road: gold=None pred=Balintawak Toll; location.landmark: gold=Balintawak toll pred=None
- `te-032`: incident_type: gold=road_closure pred=road_hazard
- `te-033`: incident_type: gold=road_accident pred=vehicle_breakdown
- `te-034`: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-036`: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none
- `te-037`: incident_type: gold=vehicle_breakdown pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; location.landmark: gold=LRT Libertad pred=None
- `te-038`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-039`: incident_type: gold=vehicle_breakdown pred=other; severity: gold=low pred=medium; road_obstruction: gold=none pred=partial; location.landmark: gold=bus stop pred=None
- `te-042`: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none
- `te-043`: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none; location.landmark: gold=Marikina pred=Marikina side
- `te-044`: severity: gold=medium pred=low; road_obstruction: gold=partial pred=full; location.landmark: gold=MOA pred=near MOA; location.direction: gold=southbound pred=None
- `te-045`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-048`: incident_type: gold=vehicle_breakdown pred=road_hazard; road_obstruction: gold=unknown pred=full
- `te-049`: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; location.road: gold=Commonwealth Avenue pred=Commonwealth; location.landmark: gold=None pred=Center Island
- `te-050`: incident_type: gold=road_accident pred=road_hazard; road_obstruction: gold=partial pred=full; location.road: gold=EDSA pred=EDSA Ortigas Flyover; location.landmark: gold=Ortigas flyover pred=None
- `te-051`: incident_type: gold=road_accident pred=unknown; road_obstruction: gold=unknown pred=none; location.road: gold=Shaw Boulevard pred=Shaw
- `te-053`: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-054`: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=medium pred=low; road_obstruction: gold=partial pred=none; location.road: gold=Aurora Boulevard pred=Katipunan Avenue; location.landmark: gold=Katipunan pred=Aurora
- `te-055`: severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-057`: incident_type: gold=road_accident pred=vehicle_breakdown; severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none
- `te-058`: incident_type: gold=road_accident pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.direction: gold=None pred=eastbound
- `te-060`: incident_type: gold=road_hazard pred=vehicle_breakdown; severity: gold=high pred=low; road_obstruction: gold=partial pred=none; location.road: gold=SLEX pred=Marcos Highway
- `te-061`: severity: gold=low pred=high; road_obstruction: gold=unknown pred=full; location.landmark: gold=Vito Cruz pred=near Vito Cruz
- `te-063`: severity: gold=high pred=low; location.road: gold=Commonwealth Avenue pred=Commonwealth
- `te-064`: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.road: gold=Marcos Highway pred=Marcos Highway Antipolo; location.landmark: gold=Antipolo pred=None
- `te-068`: severity: gold=low pred=medium; road_obstruction: gold=unknown pred=full
- `te-069`: incident_type: gold=road_hazard pred=road_accident; severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full
- `te-074`: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full
- `te-076`: incident_type: gold=flooding pred=road_closure; location.road: gold=España Boulevard pred=Espana Corner Lacson; location.landmark: gold=Lacson pred=None
- `te-077`: incident_type: gold=flooding pred=road_hazard; severity: gold=low pred=high; road_obstruction: gold=none pred=full
- `te-078`: road_obstruction: gold=unknown pred=partial; location.road: gold=Commonwealth Avenue pred=None; location.landmark: gold=Batasan pred=Commonwealth Batasan
- `te-080`: incident_type: gold=flooding pred=road_hazard; road_obstruction: gold=partial pred=full
- `te-082`: incident_type: gold=flooding pred=vehicle_breakdown; severity: gold=high pred=low; road_obstruction: gold=partial pred=none
- `te-084`: invalid JSON
- `te-087`: incident_type: gold=flooding pred=road_hazard; severity: gold=high pred=medium
- `te-088`: incident_type: gold=flooding pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-091`: location.road: gold=None pred=Mabini Bridge; location.landmark: gold=Mabini bridge pred=None
- `te-093`: incident_type: gold=road_closure pred=road_hazard
- `te-094`: location.road: gold=Katipunan Avenue pred=Katipunan-Aurora; location.landmark: gold=Aurora pred=None
- `te-098`: severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.road: gold=Ortigas Avenue pred=Ortigas
- `te-099`: incident_type: gold=road_closure pred=other; severity: gold=high pred=medium; location.road: gold=5th Avenue pred=BGC; location.landmark: gold=BGC pred=5th Avenue
- `te-102`: road_obstruction: gold=partial pred=full; location.landmark: gold=Buendia exit pred=Buendia
- `te-104`: road_obstruction: gold=none pred=full; location.landmark: gold=Libis pred=None
- `te-107`: road_obstruction: gold=none pred=full
- `te-110`: road_obstruction: gold=none pred=full
- `te-112`: road_obstruction: gold=none pred=full
- `te-114`: incident_type: gold=heavy_traffic pred=road_hazard; road_obstruction: gold=none pred=full
- `te-116`: incident_type: gold=heavy_traffic pred=unknown; severity: gold=medium pred=unknown; road_obstruction: gold=none pred=unknown; location.road: gold=Macapagal Boulevard pred=Macapagal Airports; location.landmark: gold=airport pred=None
- `te-118`: severity: gold=medium pred=high; road_obstruction: gold=none pred=full; location.road: gold=Shaw Boulevard pred=Shaw
- `te-119`: road_obstruction: gold=none pred=full; location.road: gold=None pred=Cubao; location.landmark: gold=Cubao pred=None
- `te-120`: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=partial pred=full; location.landmark: gold=UP pred=None; location.direction: gold=None pred=eastbound
- `te-121`: incident_type: gold=other pred=road_hazard; road_obstruction: gold=partial pred=full
- `te-122`: road_obstruction: gold=unknown pred=full
- `te-123`: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full; location.road: gold=Taft Avenue pred=Taft-Quirino; location.landmark: gold=Quirino pred=None
- `te-125`: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full
- `te-126`: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=full
- `te-128`: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full
- `te-129`: road_obstruction: gold=none pred=full
- `te-130`: incident_type: gold=other pred=road_hazard; road_obstruction: gold=partial pred=full; location.road: gold=None pred=Divisoria Market; location.landmark: gold=Divisoria market pred=Harap
- `te-131`: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full; location.landmark: gold=toll pred=None
- `te-132`: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=full; location.road: gold=None pred=Baclaran; location.landmark: gold=Baclaran pred=None
- `te-133`: incident_type: gold=other pred=road_hazard; severity: gold=unknown pred=high; road_obstruction: gold=unknown pred=full
- `te-138`: invalid JSON
- `te-142`: location.road: gold=None pred=Ortigas; location.landmark: gold=Ortigas pred=None
- `te-151`: severity: gold=medium pred=low; road_obstruction: gold=partial pred=none; location.landmark: gold=UST pred=None
- `te-152`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=none; location.road: gold=Commonwealth Avenue pred=CMWLT
- `te-153`: incident_type: gold=road_accident pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=partial pred=full
- `te-154`: road_obstruction: gold=unknown pred=none; location.direction: gold=southbound pred=None
- `te-155`: severity: gold=medium pred=high; road_obstruction: gold=unknown pred=full; location.direction: gold=northbound pred=None
- `te-157`: incident_type: gold=flooding pred=heavy_traffic; severity: gold=high pred=medium; road_obstruction: gold=unknown pred=full; location.road: gold=España Boulevard pred=EDSA; location.landmark: gold=None pred=Magallanes
- `te-158`: road_obstruction: gold=partial pred=full; location.road: gold=Quezon Avenue pred=Quezon Avenue Cor. Timog; location.landmark: gold=Timog pred=None
- `te-159`: incident_type: gold=flooding pred=unknown; severity: gold=low pred=unknown; road_obstruction: gold=none pred=full; location.road: gold=Roxas Boulevard pred=Rox Blvrd
- `te-160`: severity: gold=high pred=unknown
- `te-161`: incident_type: gold=road_closure pred=road_hazard; road_obstruction: gold=partial pred=full; location.road: gold=Ortigas Avenue pred=Orthgas Avenue
- `te-162`: incident_type: gold=road_closure pred=unknown; severity: gold=high pred=unknown; road_obstruction: gold=full pred=unknown; location.road: gold=Recto Avenue pred=Recto
- `te-163`: incident_type: gold=heavy_traffic pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; location.landmark: gold=Makati pred=None; location.direction: gold=northbound pred=None
- `te-164`: incident_type: gold=heavy_traffic pred=road_hazard; road_obstruction: gold=none pred=full
- `te-166`: incident_type: gold=other pred=road_hazard; severity: gold=medium pred=high; road_obstruction: gold=none pred=full; location.road: gold=Shaw Boulevard pred=EDSA; location.landmark: gold=EDSA pred=Shaw Cor
- `te-167`: incident_type: gold=other pred=road_hazard; road_obstruction: gold=none pred=full
- `te-170`: incident_type: gold=flooding pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full; location.road: gold=Recto Avenue pred=Recto
- `te-171`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-172`: incident_type: gold=road_accident pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-173`: incident_type: gold=road_closure pred=road_hazard; severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=full
- `te-174`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=full
- `te-175`: severity: gold=unknown pred=low; road_obstruction: gold=unknown pred=partial
- `te-176`: severity: gold=unknown pred=medium; road_obstruction: gold=unknown pred=none; location.road: gold=Commonwealth Avenue pred=Commonwealth

