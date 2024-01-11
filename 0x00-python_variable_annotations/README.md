# Type Annotations in Python 3:
* Type annotations were introduced in Python 3.5 as a way to provide optional type information about variables and function return values.
* They do not affect the actual runtime behavior of the code but can be used by static analysis tools to catch potential type-related errors before the code is executed.
* Type annotations use the colon (:) syntax to indicate the expected type of a variable or the return type of a function.
* Using Type Annotations to Specify Function Signatures and Variable Types:
* Function Signatures: You can use type annotations to specify the types of parameters and the return type of a function.
* Duck Typing:
* Duck typing is a programming concept where the type or class of an object is less important than the methods and properties it possesses.
* The idea is that you don't check the type of an object; instead, you check for the presence of certain methods or attributes. If an object behaves like a duck (has the required methods), then it's considered a duck.
* This is in contrast to languages with static typing, where the type of an object is explicitly declared.
* Validating Code with Mypy:
* Mypy is a third-party static type checker for Python that uses the type annotations in your code to perform static analysis.
* It can catch common programming errors related to type mismatches before your code runs.
* To use Mypy, you need to install it (pip install mypy) and then run it on your Python files.
