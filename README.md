![hbnb](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201029%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201029T134839Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=14f6b29a5706c62e3159df7dafabe438dd309590938427e763c082012145c4ce)

# 0x00. AirBnB clone - The console

The goal of the project is to deploy on your server a simple copy of the AirBnB website.

    - [x] A command interpreter to manipulate data without a visual interface,
    like in a Shell (perfect for development and debugging)
    - [x] A website (the front-end) that shows the final product to everybody:
    static and dynamic
    - [x] A database or files that store data (data = objects)
    - [x] An API that provides a communication interface between the front-end
    and your data (retrieve, create, delete, update them)


In this first step we build the parent class (called **BaseModel**) to take care of the initialization, serialization and deserialization of your future instances and a command line interpreter to manage our **AirBnB objects**.

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

![1st](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201029%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201029T204846Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=45578af9adc53f7fe1c3dd8ba04a9285d3f06cf453dd2de83f20398e66d5e82c)
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

INSERT EXAMPLES HERE PLEASE (:

- Command list

___

AUTHORS:

Cifuentes, Gabriel - [Twitter](https://twitter.com/_gcifuentess_)

Lorenzo, Daniel - [Twitter](https://twitter.com/dlscoccia)




> A journey of a thousand miles begins with a single step. -  Lao Tzu