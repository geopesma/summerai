servesFood(american_resturant, [salad, steak, sandwiches, burgers, fried_chicken]).
servesFood(burger_place, [burgers, fries, onion_rings]).
servesFood(chinese, [eggrolls, rice, shrimp, soup, noodles]).
servesFood(indian, [papadam, bagan_bharta, rice, tandoori, naan]).
servesFood(japanese, [sashimi, rice, tempura, noodles]).
servesFood(mediterranean, [gyros, hummus, pita, falafel]).
servesFood(mexican, [tacos, beans, rice, enchiladas, fish_tacos]).
servesFood(pizza_place, [pizza, salad, garlic_bread]).
servesFood(thai, [rice, noodles, larb, pad_thai]).

servesdish(vegetarian,[beans, bagan_bharta, enchiladas, falafel, hummus,
pizza, salad, soup, tempura, onion_rings, naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries ]).
servesdish(meat,[burgers, enchiladas, gyros, pad_thai, pizza, steak, sandwiches,
fried_chicken, tacos, tandoori, larb]).
servesdish(seafood,[snapper, cioppino, sashimi, shrimp, clams, fish_tacos, tempura]).
servesdish(starch,[naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]).

serveslocation(yans,[thayer_street]). 
serveslocation(pizza_marvin,[fox_point]).
serveslocation(bajas,[thayer_street]).
serveslocation(andreas,[thayer_street]).
serveslocation(chinatown,[thayer_street]).
serveslocation(kabob_n_curry,[thayer_street]).
serveslocation(waterman_grille,[wayland]).
serveslocation(dolores,[fox_point]).
serveslocation(tallulahs,[fox_point]).
serveslocation(red_stripe,[wayland]).
serveslocation(pasta_beach,[wayland]).
serveslocation(haruki,[wayland]).
serveslocation(heng,[thayer_street]).
serveslocation(mikes,[thayer_street]).
serveslocation(east_side_pocokets,[thayer_street]).
serveslocation(bees,[fox_point]).
serveslocation(shake_shack,[thayer_street]).
serveslocation(al_forno,[fox_point]).
serveslocation(lims,[wayland]).

servescuisine(yans,[chinese]).
servescuisine(pizza_marvin,[pizza_place]).
servescuisine(bajas,[mexican]).
servescuisine(andreas,[mediterranean]).
servescuisine(chinatown,[chinese]).
servescuisine(kabob_n_curry,[indian]).
servescuisine(waterman_grille,[american]).
servescuisine(dolores,[mexican]).
servescuisine(tallulahs,[mexican]).
servescuisine(red_stripe,[american]).
servescuisine(pasta_beach,[italian]).
servescuisine(haruki,[japanese]).
servescuisine(heng,[thai]).
servescuisine(mikes,[pizza_place]).
servescuisine(east_side_pocokets,[mediterranean]).;
servescuisine(bees,[thai]).
servescuisine(shake_shack,[burger_place]).
servescuisine(al_forno,[italian]).
servescuisine(lims,[thai]).

servessmt(vegetarian,[pizza_marvin]).
servessmt(vegetarian,[dolores]).
servessmt(vegetarian,[tallulahs]).
servessmt(vegetarian,[al_forno]).

serves(Type, Place) :-
    servessmt(Type, Place).

serves(Place, Cuisine) :-
    servescuisine(Place,Cuisine).

serves(Place, Location) :-
    serveslocation(Place,Location).
    

serves(Type, Dish) :-
    servesFood(Type,Dish).
    member(Dish, Dishes).

serves(Type, Dish) :-
    servesdish(Type,Dish).
    member(Dish, Dishes).
    