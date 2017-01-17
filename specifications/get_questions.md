# GetQuestions

## Description
This class represents the mentor's attitude of the different amount of questions.

## Parent class
Mentor class

## Attributes

* ```questions_list```
  * data type: list (containing some question)
  * description: stores some random questions
* ```tolerance_limit```
  * data type: integer
  * description: containing the numeric data of the mentors tolerance about questions.

## Class methods

### ```how_many_questions```

Generate a random number as the amount of questions.

#### Arguments
None

#### Return value

An integer.

## Instance methods

### ```__init__(Mentor)```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```depend_on_questions```

Depending on the number of questions and the tolerance_limit, it's calculate an integer as an indicator of the mentor's satisfaction

#### Arguments
None

#### Return value
Print out a randomly selected string form the question_list and the integer of satisfaction.
