# DK Property Trades 1992-2023

A curated data set of 1.2 million Danish residential real estate trades in the period 1992-2023 compiled from recordings of deeds (tinglysningsdata) and the [BBR registry](https://bbr.dk). Read more about the curation in the following. 

## How to use

---
The data set is partitioned in this repository due to GitHub file size restrictions. You can use the loader function in the data folder to merge the partitions and return a dataframe e.g. by

```
from loader import load_dataset

df = load_dataset(as_frame=True)

```

```
# Or alternatively just run:

load_dataset()
```
which will create the file `data.parquet` of the merged partitions.

## Overall Description

The dataset consists of legally recorded property trades from 5 January 1992 until 31 December 2023. In terms of residential property trading in Denmark there are two overall types; "almindeligt salg" and "familiesalg". This data set contains only trades of the former type, as the price of the latter is likely to be discounted compared to what an open-market trade with an unrelated buyer.

Furthermore, sadly, the practise of recording property trades in Denmark is such that for a property consisting of several units e.g. an apartment block, each unit is recorded with the total sale price of the property when sold as part of that lot. This means that such prices are unrealistic and they are therefore removed in this data set. 

## Feature Description

```
'address':                      "Full address within a zip code",
'price':                        "Sold price in DKK", 
'date':                         "Sold date in %Y-%m-%d format",
'size':                         "Total floor area in square meters (BBR)", 
'n_rooms':                      "Number of rooms (BBR)",
'year':                         "Year built (BBR)",
'city':                         "City name within zip code",
'zip':                          "Postal code",
'use':                          "Usage of the property (BBR)"
'type':                         "Type of property (BBR)",
'n_floors':                     "Number of floors (BBR)",
'kitchen_type':                 "Type of kitchen (BBR)",
'year_rebuilt':                 "Latest year of major renovation (BBR)",
'n_toilets':                    "Number of toilets (BBR)",
'n_bathrooms':                  "Number of bathrooms (BBR)",
'heating_system':               "Primary heating system (BBR)", 
'additional_heating_system':    "Secondary heating system (BBR)"
'heating_agent':                "Primary heating agent (BBR)",
'drain_type':                   "Type of drainage (BBR)",
'roof_type',:                   "Type of roof material (BBR)"
'water_supply':                 "Type of water supply, if any (BBR)"
'outer_wall_type':              "Type of outer wall material (BBR)",
"building_area":                "Building area at ground floor in square meters (BBR",
'weighted_area':                "Weighted area in square meters (BBR)", 
'latitude':                     "Latitude coordinate (BBR)",
'longitude':                    "Longitude coordinate (BBR)",
'elevation':                    "Elevation in meters (BBR)",
'oil_tank':                     "1 if Oil tank on property else 0 (BBR)",
'pollution_info':               "Recorded or suspected soil pollution if any (BBR)",
'n_restrictive_covenants':      "Number of recorded restrictive coventants (Danish: servitutter) on the property, if any",
'first_restrictive_covenant':   "Year of first restrictive covenant, -1 if none",
'latest_restrictive_covenant':  "Year of latest restrictive covnenant, -1 if none"
```

## Caveats

BBR data is known to be of questionable quality - particularly regarding the recorded heating systems.

An interesting yet elusive piece of information is the lot size associated with each property. It is not recorded in the consulted data sources and thus does not appear in the resulting compiled data set.