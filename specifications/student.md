# Student

## Description
This class represents a student in real life.

## Parent class
Person class

## Attributes

* ```knowledge_level```
  * data type: integer
  * description: stores the knowledge level of the student in programming
* ```energy_level```
  * data type: integer
  * description: current energy level

## Class methods

### ```create_by_csv```

Creates a ```list of students``` list, that contains all the data needed to instantiate a student object.

#### Arguments
csv file path

#### Return value

```list of students``` list

## Instance methods

### ```__init__(Person)```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value

If any attributes are empty raise value error, else return list of students
