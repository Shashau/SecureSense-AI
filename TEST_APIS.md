# SecureSense AI --- 100 Public API Test Endpoints

Use these endpoints in SecureSense AI to test the scanner. They are GET
endpoints and are intended for public/testing use. Expected status codes
are indicative; public services can rate-limit or change behavior.

> **Note:** A 200/404/500 status does not determine the SecureSense
> security score. The score currently depends mainly on the presence of
> the three checked security headers. Public APIs may also change
> headers over time.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    \# API               Test URL                                                                                                    Expected status
  -------------------- ----------------- ------------------------------------------------------------------------------------------------------ --------------------
                     1 JSONPlaceholder   `https://jsonplaceholder.typicode.com/posts/1`                                                                          200

                     2 JSONPlaceholder   `https://jsonplaceholder.typicode.com/users/1`                                                                          200

                     3 JSONPlaceholder   `https://jsonplaceholder.typicode.com/todos/1`                                                                          200

                     4 JSONPlaceholder   `https://jsonplaceholder.typicode.com/comments/1`                                                                       200

                     5 JSONPlaceholder   `https://jsonplaceholder.typicode.com/albums/1`                                                                         200

                     6 JSONPlaceholder   `https://jsonplaceholder.typicode.com/photos/1`                                                                         200

                     7 JSONPlaceholder   `https://jsonplaceholder.typicode.com/posts/99999`                                                                      404

                     8 JSONPlaceholder   `https://jsonplaceholder.typicode.com/users/99999`                                                                      404

                     9 DummyJSON         `https://dummyjson.com/products/1`                                                                                      200

                    10 DummyJSON         `https://dummyjson.com/products/2`                                                                                      200

                    11 DummyJSON         `https://dummyjson.com/users/1`                                                                                         200

                    12 DummyJSON         `https://dummyjson.com/users/2`                                                                                         200

                    13 DummyJSON         `https://dummyjson.com/carts/1`                                                                                         200

                    14 DummyJSON         `https://dummyjson.com/posts/1`                                                                                         200

                    15 DummyJSON         `https://dummyjson.com/todos/1`                                                                                         200

                    16 DummyJSON         `https://dummyjson.com/products/99999`                                                                                  404

                    17 DummyJSON         `https://dummyjson.com/users/99999`                                                                                     404

                    18 Random User       `https://randomuser.me/api/?results=1`                                                                                  200

                    19 Random User       `https://randomuser.me/api/?results=5`                                                                                  200

                    20 Random User       `https://randomuser.me/api/?gender=male&results=1`                                                                      200

                    21 Random User       `https://randomuser.me/api/?gender=female&results=1`                                                                    200

                    22 PokeAPI           `https://pokeapi.co/api/v2/pokemon/pikachu`                                                                             200

                    23 PokeAPI           `https://pokeapi.co/api/v2/pokemon/charizard`                                                                           200

                    24 PokeAPI           `https://pokeapi.co/api/v2/pokemon/bulbasaur`                                                                           200

                    25 PokeAPI           `https://pokeapi.co/api/v2/pokemon/25`                                                                                  200

                    26 PokeAPI           `https://pokeapi.co/api/v2/pokemon/999999`                                                                              404

                    27 Rick and Morty    `https://rickandmortyapi.com/api/character/1`                                                                           200

                    28 Rick and Morty    `https://rickandmortyapi.com/api/character/2`                                                                           200

                    29 Rick and Morty    `https://rickandmortyapi.com/api/location/1`                                                                            200

                    30 Rick and Morty    `https://rickandmortyapi.com/api/episode/1`                                                                             200

                    31 Rick and Morty    `https://rickandmortyapi.com/api/character/999999`                                                                      404

                    32 SWAPI             `https://swapi.dev/api/people/1/`                                                                                       200

                    33 SWAPI             `https://swapi.dev/api/people/2/`                                                                                       200

                    34 SWAPI             `https://swapi.dev/api/planets/1/`                                                                                      200

                    35 SWAPI             `https://swapi.dev/api/films/1/`                                                                                        200

                    36 SWAPI             `https://swapi.dev/api/starships/9/`                                                                                    200

                    37 SWAPI             `https://swapi.dev/api/people/999999/`                                                                                  404

                    38 Open Trivia DB    `https://opentdb.com/api.php?amount=1`                                                                                  200

                    39 Open Trivia DB    `https://opentdb.com/api.php?amount=5`                                                                                  200

                    40 Open Trivia DB    `https://opentdb.com/api.php?amount=1&type=multiple`                                                                    200

                    41 Dog CEO           `https://dog.ceo/api/breeds/image/random`                                                                               200

                    42 Dog CEO           `https://dog.ceo/api/breeds/image/random/3`                                                                             200

                    43 Dog CEO           `https://dog.ceo/api/breed/hound/list`                                                                                  200

                    44 Dog CEO           `https://dog.ceo/api/breed/labrador/images/random`                                                                      200

                    45 Open-Meteo        `https://api.open-meteo.com/v1/forecast?latitude=12.9716&longitude=77.5946&current=temperature_2m`                      200

                    46 Open-Meteo        `https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&current=temperature_2m`                      200

                    47 Open-Meteo        `https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current=temperature_2m`                      200

                    48 Open-Meteo        `https://api.open-meteo.com/v1/forecast?latitude=13.0827&longitude=80.2707&current=temperature_2m`                      200

                    49 Open-Meteo        `https://api.open-meteo.com/v1/forecast?latitude=17.3850&longitude=78.4867&current=temperature_2m`                      200

                    50 Open-Meteo        `https://api.open-meteo.com/v1/forecast?latitude=22.5726&longitude=88.3639&current=temperature_2m`                      200

                    51 Open-Meteo        `https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current=temperature_2m`                      200

                    52 Open-Meteo        `https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&current=temperature_2m`                     200

                    53 Open-Meteo        `https://api.open-meteo.com/v1/forecast?latitude=35.6762&longitude=139.6503&current=temperature_2m`                     200

                    54 Open-Meteo        `https://api.open-meteo.com/v1/forecast?latitude=-33.8688&longitude=151.2093&current=temperature_2m`                    200

                    55 Frankfurter       `https://api.frankfurter.app/latest?from=EUR&to=USD`                                                                    200

                    56 Frankfurter       `https://api.frankfurter.app/latest?from=USD&to=INR`                                                                    200

                    57 Frankfurter       `https://api.frankfurter.app/latest?from=GBP&to=EUR`                                                                    200

                    58 Frankfurter       `https://api.frankfurter.app/latest?from=JPY&to=USD`                                                                    200

                    59 Frankfurter       `https://api.frankfurter.app/latest?from=CAD&to=USD`                                                                    200

                    60 REST Countries    `https://restcountries.com/v3.1/name/India`                                                                             200

                    61 REST Countries    `https://restcountries.com/v3.1/name/Japan`                                                                             200

                    62 REST Countries    `https://restcountries.com/v3.1/name/Canada`                                                                            200

                    63 REST Countries    `https://restcountries.com/v3.1/name/Brazil`                                                                            200

                    64 REST Countries    `https://restcountries.com/v3.1/name/Germany`                                                                           200

                    65 REST Countries    `https://restcountries.com/v3.1/alpha/IN`                                                                               200

                    66 REST Countries    `https://restcountries.com/v3.1/alpha/US`                                                                               200

                    67 REST Countries    `https://restcountries.com/v3.1/alpha/GB`                                                                               200

                    68 TheMealDB         `https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata`                                                        200

                    69 TheMealDB         `https://www.themealdb.com/api/json/v1/1/search.php?s=Chicken`                                                          200

                    70 TheMealDB         `https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood`                                                          200

                    71 TheMealDB         `https://www.themealdb.com/api/json/v1/1/filter.php?a=Canadian`                                                         200

                    72 TheMealDB         `https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772`                                                            200

                    73 TheCocktailDB     `https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita`                                                    200

                    74 TheCocktailDB     `https://www.thecocktaildb.com/api/json/v1/1/search.php?s=mojito`                                                       200

                    75 TheCocktailDB     `https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail`                                                     200

                    76 TheCocktailDB     `https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Ordinary_Drink`                                               200

                    77 TheCocktailDB     `https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11007`                                                        200

                    78 Agify             `https://api.agify.io?name=michael`                                                                                     200

                    79 Agify             `https://api.agify.io?name=shashank`                                                                                    200

                    80 Agify             `https://api.agify.io?name=alex`                                                                                        200

                    81 Genderize         `https://api.genderize.io?name=alex`                                                                                    200

                    82 Genderize         `https://api.genderize.io?name=emma`                                                                                    200

                    83 Nationalize       `https://api.nationalize.io?name=michael`                                                                               200

                    84 Nationalize       `https://api.nationalize.io?name=alex`                                                                                  200

                    85 Bored API         `https://bored-api.appbrewery.com/random`                                                                               200

                    86 Bored API         `https://bored-api.appbrewery.com/filter?type=education`                                                                200

                    87 Bored API         `https://bored-api.appbrewery.com/filter?participants=1`                                                                200

                    88 Quotable          `https://api.quotable.io/random`                                                                                        200

                    89 Quotable          `https://api.quotable.io/quotes?limit=5`                                                                                200

                    90 Hacker News       `https://hacker-news.firebaseio.com/v0/item/8863.json`                                                                  200

                    91 Hacker News       `https://hacker-news.firebaseio.com/v0/topstories.json`                                                                 200

                    92 Hacker News       `https://hacker-news.firebaseio.com/v0/newstories.json`                                                                 200

                    93 Hacker News       `https://hacker-news.firebaseio.com/v0/beststories.json`                                                                200

                    94 ipify             `https://api.ipify.org?format=json`                                                                                     200

                    95 GitHub            `https://api.github.com/repos/public-apis/public-apis`                                                                  200

                    96 httpbin           `https://httpbin.org/get`                                                                                               200

                    97 httpbin           `https://httpbin.org/status/404`                                                                                        404

                    98 httpbin           `https://httpbin.org/status/500`                                                                                        500

                    99 httpbin           `https://httpbin.org/status/429`                                                                                        429

                   100 httpbin           `https://httpbin.org/redirect/1`                                                                                        302
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Recommended demo sequence

1.  `https://httpbin.org/get` --- normal 200 response.
2.  `https://httpbin.org/status/404` --- Client Error anomaly.
3.  `https://httpbin.org/status/500` --- Server Error anomaly.
4.  `https://httpbin.org/status/429` --- Rate Limit anomaly.
5.  `https://httpbin.org/redirect/1` --- Redirect anomaly.
6.  Test several public APIs above and compare their security headers,
    score, risk level, response time, and AI insight.

## Suggested GitHub location

Save this file in the repository root as `TEST_APIS.md`, then link it
from the main README.
