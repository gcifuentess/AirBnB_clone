![hbnb](https://i.ibb.co/fG97cHQ/Hbnb.png)
-
# AirBnB clone :hotel:

The goal of the project is to deploy on your server a simple copy of the AirBnB website.

    - [x] A command interpreter to manipulate data without a
          visual interface, like in a Shell (perfect for development
          and debugging)
    - [x] A website (the front-end) that shows the final product to
          everybody: static and dynamic
    - [x] A database or files that store data (data = objects)
    - [x] An API that provides a communication interface between the
          front-end and your data (retrieve, create, delete, update
          them)


## 0x00. AirBnB clone - The console

In this module our focus the command interpreter.

### The console features are:

    - Create your data model
    - Create a new object (ex: a new User or a new Place)
    - Retrieve an object from a file, a database etc…
    - Do operations on objects (count, compute stats, etc…)
    - Update attributes of an object
    - Destroy an object
    - Store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.


The console will be a tool to validate this storage engine

![1st](https://i.ibb.co/fG97cHQ/Hbnb.png)
___
### Execution Modes:

#### Working in interactive mode:

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

#### Working  in non-interactive mode:

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


### Examples:

- Intro:

![INTRO](https://i.ibb.co/Z2rV1Pq/Intro-consola.jpg)

- help:

![HELP](https://i.ibb.co/f1Mfm6s/help-console.jpg)

- create <classname>:

![CREATE](https://i.ibb.co/zJyY0Fx/create-console.jpg)

- show <classname> <id>:

![SHOW](https://i.ibb.co/4KbmQ94/show-console.jpg)

___

AUTHORS:

Cifuentes, Gabriel - [Twitter](https://twitter.com/_gcifuentess_)

Lorenzo, Daniel - [Twitter](https://twitter.com/dlscoccia)


> A journey of a thousand miles begins with a single step. -  Lao Tzu