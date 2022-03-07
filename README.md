
# 0x00. AirBnB clone - The console

The AirBnB project approaches the first real web developer project, the console is the 
first step towards building our first full web application: the AirBnB clone. 

This first step is very important because you will use what you build during this project 
with all other following projects: HTML/CSS templating, database storage, API, 
front-end integration.

## Resources

Read or watch:

- [Python abstract classes](https://intranet.hbtn.io/rltoken/5Dv7z90qa94hYqtPRCe_wA)
- [cmd module](https://intranet.hbtn.io/rltoken/7dj8WbEE01SwPY2Qxy_Ixg)
- Packages concept page
- [uuid module](https://intranet.hbtn.io/rltoken/xJhjt-mMAchNu5WOb2X6DQ)
- [datetime](https://intranet.hbtn.io/rltoken/aEuCrtCn7p5xaYbNRM8ccQ)
- [unittest module](https://intranet.hbtn.io/rltoken/XfOae8zIhTiKYFMTF98qLg)
- [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg)
- [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A)

## Execution

The console should work both in interactive and non-interactive mode.

### Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Usage
The console works much like a Unix shell. It prints a prompt "(hbnb) " and waits for the user input command.
Possible commands are as follows:

| Command | Purpose                                                                    | Example                                                       |
|---------|----------------------------------------------------------------------------|---------------------------------------------------------------|
| quit    | quits the console                                                          | (hbnb) quit                                                   |
| EOF     | exists the console                                                         | (hbnb) crtl + D                                               |
| help    | opens the help menu                                                        | (hbnb) help                                                   |         
| create  | creates a new instance                                                     | (hbnb) create BaseModel                                       |
| show    | prints the string representation of an instance based on class name and id | (hbnb) show BaseModel                                         |
| destroy | deletes an instance based on class name and id                             | (hbnb) destroy BaseModel 1234-1234-1234                       |
| all     | Prints all string representations of all instances                         | (hbnb) all BaseModel                                          |
| update  | Updates an instance based on the class name and id                         | (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com" |

## Modules

Available modules with their corresponding class:

| Module                                                                                   | Description                                         | Attributes                                                                                                                      |
|------------------------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [base_module.py](https://github.com/Ella711/AirBnB_clone/blob/main/models/base_model.py) | Base model for all classes                          | id, created_at, updated_ at                                                                                                     |
| [amenity.py](https://github.com/Ella711/AirBnB_clone/blob/main/models/amenity.py)        | Will contain the available amenities for each place | name                                                                                                                            |
| [city.py](https://github.com/Ella711/AirBnB_clone/blob/main/models/city.py)              | City of where place is located                      | name, state_id                                                                                                                  |
| [place.py](https://github.com/Ella711/AirBnB_clone/blob/main/models/place.py)            | Information related to the place                    | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_id |
| [review.py](https://github.com/Ella711/AirBnB_clone/blob/main/models/review.py)          | Review of the property                              | place_id, user_id, text                                                                                                         |
| [state.py](https://github.com/Ella711/AirBnB_clone/blob/main/models/state.py)            | Name of state where property is located             | name                                                                                                                            |
| [user.py](https://github.com/Ella711/AirBnB_clone/blob/main/models/user.py)              | Information on the user procuring the property      | password, first_name, last_name                                                                                                 |

## Authors


[Angelica Rodriguez](https://github.com/angelicarm3)

[Ornella Russo](https://github.com/Ella711)
