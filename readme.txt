This project is developed individually 
by me, as a portfolio prooject.

In this project I used different 
techniques to display Python and Django
abilities.

Some of the used solutions are not optimal,
but more as demonstration and practice in
coding.

What Restaurant Manager Application Does:

- Register and Login Users for restcricted access purpose.
    - registratien has try and except methods, that
    imporove registration process and display 
    registration requirements.
    - Login has try and except methods, that display
    message if issue arises.

- View overall Restaurant data.
    - View Income, Cost and Profit for Today
        - Income is calculated by total of purchased 
        menu item prices.
        - Cost is calculated by ingredient price and their
        amount in each Menu Item.
        - Profit is calculated Income - Cost.

    - View Income, Cost and Profit for for past 15 days
    in total and for each day separately.

    -View all purchased Menu Items for last 10 days or over
    selected time period.

    - View top 3 most sold Menu Items and 3 least sold Menu
    Items.

    - Fetch all purchases of Menu Item by selecting one from
    the dropdown list. 

- View, Create, Update and Delete Ingredient Inventory 
that is necessarry for menu item recipes.
    - Ingredient stock calculates each 
    ingredient stock value and total stock
    value.
    - When Menu Item is purchasd, Ingredient stock 
    automatically updates those ingredients in 
    stock reserves that are in Menu Item Recipe 
    Requirements.

- View, Create, Update and Delete Menu items
    - Menu Items have option to create Recipe with
    ingredients in Inventory.
    - Menu Items have Purchase functionality that crates
    purchase and deducts ingredients from recipe from
    Inventory.
    - If in Inventory ingredients are less than required
    in menu item recipe, when purchasing menu item, issue
    message will be displayed and purchase cancelled.

- View, Create, Update and Delete Recipe Requirements.
    - Recipe can be created only for existing Menu Items.
    - Recipe Requirements has a method that converts 
    inventrory units like kg and litres to grams, 
    mililitres and table spoons.
    - Creating Recipe requirements automatically calculates 
    Menu Item cost considering added ingredient amout and 
    price.

 - View, Create, Update and Delete Purchase.
    - Purchase is created through Menu Item that has
    Recipe Requirements attached to it.
    - Purchase is possible only if Inventory has enough
    of required ingredients from recipe.
    - Purchase automatically converts ingredient 
    amount used in recipe and deducts from Ingredint 
    inventory.
    - After purchase is made, it is displayed in Purchase
    Log and can be updated or deleted.

Application will be improved by:
    - User groups, that will allow to limit User access 
    to some functionality
    - Create Order to purchase multiple ingredients at
    a time instead of updating each Ingredient individually.
    - Create a Bill that will allow to add multiple
    Menu Items to it and add them to purchased when bill 
    is payed for(marked as cleared).
    - Add recipe cost to each Menu Item that will decrease
    calculation amount when Menu Item is purchased.
    - Add charts to Application Dashboard.

More functionality can be added over time as inspiration comes.

Try the application and see how it works.

Kind Regards,
Emil Guseinov
emil.guseinov@icloud.com