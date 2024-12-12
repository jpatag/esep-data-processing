#Setup

To run the database, include the following line in your main python file

```
from InMemoryDB import InMemoryDB
```

#Example
An example of how to run the code is below

```
test = InMemoryDB()

// Must begin transaction before using get(), put(), commit()
test.begin_transaction()

// set's value of A to 5 but not committed
test.put("A", 5)

// commits the open transaction
test.commit()

//should return 5
test.get("A")

```

#
