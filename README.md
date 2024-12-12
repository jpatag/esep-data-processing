# Setup

To run the database, include the following line in your main python file

```
from InMemoryDB import InMemoryDB
```

# Example
An example of how to use the database is below

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

# Functions
begin_transaction() - Starts a new transaction. Must occur before calling get(), put(), commit() or else exception will be thrown.

put(key, value) - Creates a new key with the provided value. If key already exists, it will update the value of the existing value. Note that the change must be committed to take effect.

get(key) - Returns the value associated with the key or null if the key does not exist in the database.

commmit() - Applies the changes made within the transaction to the database.

rollback() - Aborts all changes made within the transaction and empties the transactions.

# Feedback
I believe the assignment should be a bit harder to become an official assignment. I thought the underlying concepts were interesting behind assignment, but possibly requiring to use a database like MongoDB could increase the difficulty. Adding a testing suite for the assignment would make it easier to grade as I only referenced the test cases included in the document. I think the rollback() function was a bit confusing at first as I thought it was supposed to rollback the previous commit, instead of the transactions. If the assignment document had better organization in defining the functions, I think it would make communication clearer to the students. Maybe organizing the 15 bullet points underneath the "Instructions" heading would help making the task easier to understand.
