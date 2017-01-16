# Person

## Description
This class represents a Person in real life. We use it to inherit it's features in Student and Mentor classes.

## Parent class
None

## Attributes

* ```first_name```
  * data type: string
  * description: stores the first name of the students and the mentors
* ```last_name```
  * data type: string
  * description: stores the last name of the students and the mentors
* ```year_of_birth```
  * data type: integer
  * description: stores the year when a student or a mentor was born
* ```gender```
  * data type: string
  * description: stores the sex of a student or the sex of a mentor (male/female/notsure)

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
If any of the attributes is empty, or gender is not valid raise an error, else return None
