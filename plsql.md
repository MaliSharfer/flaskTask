# pl/sql:
## basic templete:
````
DECLARE
   //declare variebles
BEGIN
   //body...
EXCEPTION 
   //exseptions
END;
/

````
for Printing you have to runn= this command befor:
````
set serveroutput on;
````
## Types:
there are 3 mainig types in pl/sql:
* number (Precision, Scale) - Numeric values
* varchar2 (1-32767 byte/char) – String
* boolean – True/False
* date

## Collections:
there are 3 types of collections:
* Variable-size array (Varray) 
* Nested table 
* Index-by tables 
### Varray:
    TYPE array_typ IS VARRAY(<num>) OF element_type;
````
    TYPE array_typ IS VARRAY(5) OF varchar2    (200);l_array array_typ := array_typ(‘('אופיר',    'נתן','צפור;
````
### Nested table
TYPE type_name IS TABLE OF element_type;
````
TYPE table_typ IS TABLE OF varchar2(100);
l_table table_typ := table_typ();
````

### index-by tabeles:
consist of a set of keys and a set of values that are mapped to them.
The key must be unique and limited to integer or string types.
If we try to change a value in the collection by accessing a key that does not exist, then the key will be added and the value will be mapped under it - this is the way to add members to the collection.
Example:
````
TYPE salary IS TABLE OF NUMBER INDEX BY VARCHA(20);
salary_list salary;
salary_list(‘Martin’) := 40000;
````
## Control Flow:
you can exceptions is a block designed to catch errors in the code and define what happens next.
A specific exception can be caught (for example: NO_DATA_FOUND) and "everything else" (any other error not specified) can be caught by OTHERS.
We can define exceptions ourselves, in addition to the predefined exceptions.
## Cursors:
use ifelse, case ,loops and loops on collections
## Exceptions:
exceptions is a block designed to catch errors in the code and define what happens next.
A specific exception can be caught (for example: NO_DATA_FOUND) and "everything else" (any other error not specified) can be caught by OTHERS.
We can define exceptions ourselves, in addition to the predefined exceptions.
## dinamic sql:
We would like to run dynamic queries usually in one of the following two cases:
When we lack definitional data (schema name, table name, column name, function name, etc.).
When we want to run a DDL command.
Syntax: execute immediate sql_statement_string [(bulk collect) into] [using];
into - you can add the keyword into, assuming that the result returned from running the query is one line, in order to absorb the result into a variable (whose type matches the type of the result from the query).
using - we will use it when we want to add a list (one or more) of parameters to the sql we want to run. We will define the parameters by adding the character ':' in front of them. * Wherever we have to work with dynamic values and we can do it by using parameters, we choose to work with parameters and not with a chain of strings.
## Functions:
basic templete:
create [or replace] function function_name
[(param_name [in | out | in out] param_type [,…]]
return return_datatype {is | as} 
***replace***-to ovveride function with the same name:
***as/is***-Indicates the start of execution of the function
***return***-definrd the type of the value that will return from the function
## Procedures;
The same principles as we mentioned in the functions.
## Packages:
In packages we save functions, procedures as well as types and variables that will be recognized in the scope of the package.
package consists of two parts:
declaration - where we will declare the objects we want to expose as an API to the user.
body - where we will implement the subprograms we declared as well as additional subprograms for internal use within the package.
## Triggers
Triggers are stored programs that are automatically activated as soon as a certain event happens.
exsample:
```
create or replace trigger <trigger_name>
{ before | after {
{ insert | update [ of column_name ] | delete }
on table_name
[for each row]
when (condition)
declare …
begin
// what will happen when the event occurs
end;

```