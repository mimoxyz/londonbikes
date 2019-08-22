### Londonbikes


Tested on Python 3.6.8 

#### Search london bikepoints by place name
```
$./londonbikes search ""
Please specify a search term

$./londonbikes search Toronto
No bikepoints named Toronto found

$./londonbikes search "Canary Wharf"
Id                  Name                                              Latitude    Longitude
BikePoints_448      Fisherman's Walk West, Canary Wharf               51.506230   -0.022960
BikePoints_494      South Quay East, Canary Wharf                     51.501960   -0.016251
BikePoints_532      Jubilee Plaza, Canary Wharf                       51.503570   -0.020068
BikePoints_551      Import Dock, Canary Wharf                         51.505772   -0.016460
BikePoints_556      Heron Quays DLR, Canary Wharf                     51.502661   -0.021596
BikePoints_570      Upper Bank Street, Canary Wharf                   51.503083   -0.017676
BikePoints_811      Westferry Circus, Canary Wharf                    51.505703   -0.027772
```


#### Search london bikepoints by lat, lon and radius

```
$ ./londonbikes search 51.53 -0.09 2
No bikepoints found with 51.53 meters of -0.09 lat, 2 lon

$ ./londonbikes search 51.53 -0.09 sushan
The search request is invalid

$ ./londonbikes search 51.53 -0.09 250
Id                  Name                                              Latitude    Longitude   Distance
BikePoints_63       Murray Grove , Hoxton                             51.530890   -0.089782   100.192250
BikePoints_50       East Road, Hoxton                                 51.528673   -0.087459   229.697289
```

#### Search london bikepoints by id

```
$ ./londonbikes id ""
Please specify a bike point id

$ ./londonbikes id "BikePoints_50"
Name                          Latitude            Longitude           Num Bikes           Empty Docks
East Road, Hoxton             51.528673           -0.087459           5                   19

$ ./londonbikes id "BikePoints_5023432"
Bike point id BikePoints_5023432 not recognised
```


### TODO:
1. Clean up loops
2. Improve variable names
3. Use argparse module 



