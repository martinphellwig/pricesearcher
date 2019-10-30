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


