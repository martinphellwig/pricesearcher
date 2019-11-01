# Pricesearcher
### API Example

This is an implementation of the task as described in
`_project\documentation\task.md` .

I used Django framework for it's convenience of creating database tables and
other tools I frequently use. To create the API I used the 
`django REST framework`. Generally I use Django in a way that all apps are
created in their own app container so that the app is better separated from the
Django server parts itself and I have the option to create later on a portable
app from it.

In the folder `_project\environment.txt` you find the environment I have created
this project in. However it should be reasonably portable (though not tested)
and just creating an environment where the `_project\requirements.txt` are
installed should be enough to use this project.

Please have a look at `_project\_initial_setup.sh` how I have started the
project up, which includes setting the admin password.

### To start the server
The django internal test server is sufficient for this example. 
You can start it up with: 
```
python manage.py runserver
```

Please note that as per the instructions upon startup it will first download and
update the json data, so you will see something like this:
```

$ python manage.py runserver
# Fetching data from: https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json
# - Done
# Storing data into the DB.
# - Removing previous entries.
# - - Done.
# - Sanitizing data.
100%|█████████████████████████████████| 50143/50143 [00:00<00:00, 138176.58it/s]
# - Storing Brands
# - - Determining delta.
100%|█████████████████████████████████| 50143/50143 [00:00<00:00, 106307.47it/s]
# - - Number of new brands to be stored: 0
# - - Done
# - Storing Retailers
# - - Determining delta.
100%|█████████████████████████████████| 50143/50143 [00:00<00:00, 106990.07it/s]
# - - Number of new retailers to be stored: 0
# - - Done
# - Storing Products
# - - Determining Products
100%|██████████████████████████████████| 50143/50143 [00:02<00:00, 20463.59it/s]
# - - Number of Products to be stored: 50,143
# - - Done.
# - Done.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 01, 2019 - 02:45:36
Django version 2.2.5, using settings '_server.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Using the API
I have chosen to use the Django REST Framework with it's browsable API.
Using your web browser you can explore the API by going to the root of it at:
<http://127.0.0.1:8000/api/>

#### Getting Product by ID
The base api for this is <http://127.0.0.1:8000/api/product/>

To get a specific product, for example `17787cdcad7d43d5a1106f` change the url
like this: <http://127.0.0.1:8000/api/product/17787cdcad7d43d5a1106f/>

Here is an example using curl:
```
$ curl http://127.0.0.1:8000/api/product/17787cdcad7d43d5a1106f/
{"url":"http://127.0.0.1:8000/api/product/17787cdcad7d43d5a1106f/","id":"17787cdcad7d43d5a1106f","name":null,"brand":"rokeage","retailer":"parodontitis","price":221.47,"in_stock":true}
``` 

#### Getting N Cheapest products
The base api for this is <http://127.0.0.1:8000/api/product_cheapest/> .
By default the amount is limited to `10`, you can change this by settings the
limit query parameter.

For example to change it to `3` it would be 
<http://127.0.0.1:8000/api/product_cheapest/?limit=3>

Here is an example using curl:
```
$ curl http://127.0.0.1:8000/api/product_cheapest/?limit=3
{"count":393666,"next":"http://127.0.0.1:8000/api/product_cheapest/?limit=3&offset=3","previous":null,"results":[{"url":"http://127.0.0.1:8000/api/product/4995610/","id":"4995610","name":"Adonian","brand":"Avicenniaceae","retailer":"","price":0.0,"in_stock":false},{"url":"http://127.0.0.1:8000/api/product/6840179/","id":"6840179","name":"Aesculapian","brand":"predominancy","retailer":"consolableness","price":0.0,"in_stock":false},{"url":"http://127.0.0.1:8000/api/product/5582413/","id":"5582413","name":"Augusti","brand":"colored","retailer":"interjacency","price":0.0,"in_stock":false}]}
```

## Scope Justification
Although it is defiantly not necessary to use a heavy framework like Django
and DRF, my experience  is that every time I want to do something neat and lean,
by for example going for Flask and SQLAlchemy, I quickly regret it as
requirements change and features are requested. So suddenly you have to deal
with migrations, different return formats, filtering, pagination, custom fields
and all of the other things that make life easier for the end-user.

Thus I have learned over the years that perhaps the Django+DRF is not the
simplest solution possible, it does have all the tools on-board to prevent the
future from becoming a pain to work with (though you still have to be
diciplined), the downside is that you start off with quite a large structure and
something that should reasonably not be more that 5 or 6 modules turns into the
behemoth as produced here.

For my github usage, I used a gitflow approach, I have kept the branches open
after I merged them in so you can easily follow my commits, normally I would
delete a branch after it has been merged it.


Thank you for your consideration!