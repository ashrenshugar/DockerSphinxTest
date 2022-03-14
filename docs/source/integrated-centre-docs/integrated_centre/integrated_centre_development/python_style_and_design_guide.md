# Python Style and Design Guide

## General Styling and Best Practice Guidance

Both the **Python PEP 8** and **Google Python Style Guide** provide good recommendations for Python development.
Developers should both read and familiarise themselves with the content in these guides:

- [Python PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

As a general rule the recommendations in the above guides should be followed, however, the recommendations stated below
in this document supersede these. If there are any inconsistencies between the PEP 8 and Google styling guides that
are not clarified here then raise this with the Integrated Centre development team.

## Consistency

Consistency is the key principle. When developing new libraries, packages or modules follow the styling recommendations
stated here, this includes the addition of new files to an existing repository. However, when extending or modifying
existing Python files, ensure your styling is consistent with the file that is being modified.

> Note: The implication is that new files added to an existing repository may have styling different to older files
> alongside them. This allows developers to utilise tooling that supports these styling rules (e.g. auto-formatters)
> and avoid having to search around the repository to learn the styling that was previously used.

Older modules, packages and libraries not consistent with these styling guidelines will be brought into line
iteratively. The process for when and how this will occur will be determined and then planned accordingly.

## Code Styling

### Line Length

Limit all lines to a maximum of 120 characters.

Python’s implicit line joining inside parentheses, brackets and braces should be used instead of the backslash '\'
character. If necessary, add an extra pair of parentheses around an expression.

```python
# Not recommended
from my_package.my_module import OneReallyLongClassName, AnotherReallyLongClassName \
    AnEvenLongerThanThePreviousClassName

# Do this instead
from my_package.my_module import (
    OneReallyLongClassName, AnotherReallyLongClassName
    AnEvenLongerThanThePreviousClassName,
)

# Not recommended
if width == 0 and height == 0 \
    and color == 'red' and emphasis == 'strong':

# Do this instead
if (width == 0 and height == 0
        and color == 'red' and emphasis == 'strong'):
```

When a literal string won’t fit on a single line, use parentheses for implicit line joining. The space character
that divides the two strings should be put on the first line.

```python
# Not recommended
x = "This will build a very long long " \
    "long long long long long long string"

# Do this instead
x = ("This will build a very long long "
     "long long long long long long string")
```

Break lines before binary and boolean operators as described in the [PEP 8](https://www.python.org/dev/peps/pep-0008/#id18).

```python
# Not recommended - operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

# Do this instead - easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# Not recommended
if (width == 0 and height == 0 and
        color == 'red' and emphasis == 'strong'):

# Do this instead
if (width == 0 and height == 0
        and color == 'red' and emphasis == 'strong'):
```

### Indentation

For lines longer than 120 characters that need to continue onto the next line, the continuation lines should align
wrapped elements using a hanging indent. When using a hanging indent there should be:

- no arguments on the first line, and
- further indentation of 4 spaces to clearly distinguish itself as a continuation line, and
- the closing parentheses (and return type for functions) should be lined up at the start of the line.

```python
# No arguments on the first line, new-line is immediately after the parentheses or bracket.
from my_package.my_module import (
    OneReallyLongClassName, AnotherReallyLongClassName
    AnEvenLongerThanThePreviousClassName,
)


# Closing parentheses and return type lined up as shown
def long_function_name(
    var_one, var_two, var_three,
    var_four,
) -> None:
    print(var_one)
```

When the conditional part of an _if-statement_ is long enough to require that it be written across multiple lines,
then to avoid the visual conflict with the indented suite of code nested inside the _if-statement_, add an extra level
of indentation.

```python
# Not recommended - No extra indentation means there is no distinction between conditional and code within the 'if'
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Do this instead - Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

The closing brace/bracket/parentheses on multiline constructs should be lined up under the first character of the line
that starts the multiline construct, as in:

```python
my_list = [
    1, 2, 3,
    4, 5, 6,
]

if a == b
    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f',
    )
```

### Imports

Imports should be grouped in the following order with a blank line between each group:

1. Standard library imports.
2. Related third party library imports (i.e. code from other repositories).
3. Dependent library imports (i.e. code from Integrated Centre repositories).
4. Local application/library specific imports.

Extra blank lines can be used within these groups to better distinguish sub-groupings.

Absolute imports should be used.

_Note: The comments in the example below are not required._

```python
# 1. Standard library imports
import sys
import uuid

from datetime import datetime, timezone
from math import atan2, cos, degrees, radians, sin, sqrt

# 2. Third-party library imports
from pydantic.types import OptionalInt
from filterpy.kalman.UKF import UnscentedKalmanFilter

# 3. Dependent library imports
from oaris.idl_utils import anonymous_blob_to_json
from tsi_core_interfaces.pydantic.models import Affiliation, TsicoreComponentIdentifier

# 4. Local library imports
from track_manager.types import Course, Range, Speed, Bearing
from track_manager.models import Covariance, SystemID, TrackID,
```

### String Quotes

The recommended string quote to use is double quotes (`"`).

When a string contains a quote, use single quotes within the string to avoid having backslashes in the string.

```python
my_question = "What will the temperature be tomorrow?"

# Not recommended
the_answer = "The weather person said, \"It will be 34 degrees.\""

# Do this instead - improves code readability
the_answer = "The weather person said, 'It will be 34 degrees.'"
```

### Trailing Commas

Trailing commas in sequences of items must be used when the closing container token ], ), or } does not appear on the
same line as the final element. Although the trailing commas are redundant, they are helpful for better tracking
the changes in version control. The pattern is to put each value (etc.) on a line by itself, always adding a trailing
comma, and add the close parenthesis/bracket/brace on the next line.

```python
# Not recommended - trailing comma should be used
initialize(FILES,
    error=True
)

# Not recommended - trailing comma not required for single line statements
FILES = ['setup.cfg', 'tox.ini',]


# Do this instead
initialize(
    FILES,
    error=True,
)

FILES = [
    'setup.cfg',
    'tox.ini',
]
```

### Comments

The [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) has an
excellent explanation of the expected style and level of documentation.

Refer to [PEP 257](https://www.python.org/dev/peps/pep-0257/) for guidelines on writing good documentation strings
(a.k.a. "docstrings").

The following are some specific clarifications for development within Integrated Centre:

- Comments should be complete sentences. The first word should be capitalised, unless it is an identifier that begins
  with a lower case letter. Periods are not required for single-line comments.
- Block comments generally consist of one or more paragraphs built out of complete sentences, each sentence should
  end in a period.
- Only one space is required after a sentence-ending period in multi-sentence comments, except after the final
  sentence.
- The styling of docstring comments should follow the Google styling as shown below:

#### Google Style Docstrings

```python
def fetch_smalltable_rows(
    table_handle: smalltable.Table,
    keys: Sequence[Union[bytes, str]],
    require_all_keys: bool = False,
) -> Mapping[bytes, Tuple[str, ...]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: An open smalltable.Table instance.
        keys: A sequence of strings representing the key of each table
          row to fetch.  String keys will be UTF-8 encoded.
        require_all_keys: If True only rows with values set for all keys will be
          returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """
```

### Naming

Naming should follow the recommendations stated in the [PEP 8 - Prescriptive: Naming Conventions](https://www.python.org/dev/peps/pep-0008/#id35)
section. Slight adjustments to these recommendations and some of the less familiar guidelines are clarified here:

- Exceptions should be classes and be suffixed with "Error" for the exception name (if the exception actually is an
  error).
- If a function argument's name clashes with a reserved keyword, first seek to be creative in determining an
  alternative name. However, as a last resort append a single trailing underscore rather than use an abbreviation or
  spelling corruption. Thus `class_` is better than `clss`.
- Use one leading underscore only for non-public methods and instance variables.
- For simple public data attributes (i.e. no impact on runtime behaviour when getting or setting values), expose just
  the attribute name without complicated accessor/mutator methods.
- When using acronyms in class or exception names, capitalise all the letters of the acronym. Thus `HTTPServerError` is
  better than `HttpServerError`.
- If your class is intended to be subclassed, and you have attributes that you do not want subclasses to use, do not use
  double leading underscores as suggested by PEP 8, rather follow Google's advice to just use 1 underscore.
- To better support introspection, PEP 8 suggests all modules should explicitly declare the names in their public API
  using the `__all__` attribute. As a general rule this advice should not be followed. However, for interface
  repositories which have lots of imports (e.g. where many small classes are used and split across lots of modules)
  then set the `__all__` variable accordingly.
- Names of type variables should use `CapWords` name-style and preferring short names: T, `AnyStr`, `Num`. It is
  recommended to add suffixes `_co` or `_contra` to the variables used to declare covariant or contravariant behaviour
  correspondingly:

```python
from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)
```

#### File and Folder Naming

- Python filenames must have a `.py` extension, be in lowercase and use underscores `_` for separation.
- Python related folder names should also be in lowercase and use underscores `_` for separation.
- Non-Python folder and filenames should as a default follow these naming guidelines (unless imposed otherwise by
  other tooling).
- Hyphens (`-`) can be used in non-Python filenames where the file is expected to be used in an URL.

### Miscellaneous

Review the [PEP 8 - Programming Recommendations](https://www.python.org/dev/peps/pep-0008/#id49) to develop
familiarisation with some both good design and styling principles.

The following are some of the more commonly encountered styling recommendations re-stated for greater awareness:

- Comparisons to singletons like `None` should always be done with `is` or `is not`, never the equality operators.
- Comparisons to enumerations should be done with `is` or `is not`, never the equality operators.
- Don't compare boolean values to `True` or `False` using the equality operator `==`.
- Use `is not` operator rather than `not ... is`. While both expressions are functionally identical, the former is more
  readable and preferred.
- Use `.startswith()` and `.endswith()` instead of string slicing to check for prefixes or suffixes.
- Object type comparisons should always use `isinstance()` instead of comparing types directly.
- For `Sequence`s, `Mapping`s, and `Set`s (strings, lists, tuples, sets, dicts), use the fact that empty collections are
  false instead of explicitly comparing the length to zero. This can be used for any type that conforms to the [`Sized`][ref-sized]
  protocol.

[ref-sized]: https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized

## Code Design

This section is intended to evolve and expand as best-practice design techniques are learned and developed.
It should aid both onboarding and improvement of code quality. Designs or techniques described here may be generally
related to Python but others may be specific to the Integrated Centre domain and/or architectures used. Where possible
the design principles or techniques should not just be stated simply in text but rather typical use-cases and
coding problems should first be detailed. Then how the technique or design principle addresses this should follow.

### Handling Magic Numbers [^1]

A magic number is a numeric value that’s encountered in the source but has no obvious meaning. This “anti-pattern”
makes it harder to understand the program and refactor the code.

#### Magic Numbers - Use Cases

Your code uses a number that has a certain meaning to it.

```python
def potential_energy(mass: float, height: float) -> float:
    return mass * height * 9.81

def add_user(user: User) -> None:
    if len(users) >= 10:
        raise RuntimeError("Too many users already.")

    users.append(user)
```

#### Magic Numbers - Recommendations

Replace this number with a constant that has a human-readable name explaining the meaning of the number.

```python
GRAVITATIONAL_CONSTANT = 9.81

def potential_energy(mass: float, height: float) -> float:
    return mass * height * GRAVITATIONAL_CONSTANT

def add_user(user: User) -> None:
    CONCURRENT_USER_LIMIT = 10
    if len(users) >= CONCURRENT_USER_LIMIT:
        raise RuntimeError("Too many users already.")

    users.append(user)
```

Occasionally magic numbers can be a place-holder for a future more complex algorithmic calculation. In these cases and
in cases where standard methods exist for getting the value - use a function call instead.

**Benefits:**

- The constant value provides documentation of the meaning of its value and makes code more readable.
- Changing the value becomes a lot easier.
- Reduces duplication of numbers in the code.

### Regex Overuse

Regular expressions are a powerful language for matching text patterns. As they are so powerful there can thousands
or potential use cases for them, however, just because a regex can solve the problem does not mean there are not
alternative approaches that may provide better clarity, readability or maintainability.

#### Regex - Use Cases

In this example a regex is used to ensure only files with the supported file extensions are provided.

```python
def parse_file(filename: str) -> None:
    # Currently supporting JSON and YAML
    if re.search("\.(json|yml|yaml})$", filename):
        extract_data(filename)
    else
        raise ("Unsupported file type")

# A better approach
def parse_file(filename: str) -> None:
    VALID_EXTENSIONS = (".json", ".yml", ".yaml")
    if any(filename.endswith(ext) for ext in VALID_EXTENSIONS):
        extract_data(filename)
    else
        raise ("Unsupported file type")
```

This example highlights using regex where enumerations would provide better clarity.

```python
if EntityDomain(entity_type.Domain) is EntityDomain.ROAD:
    car_category = CarCategory(entity_type.Category).name
    if re.search("ford|holden", category, re.IGNORECASE):
        print("Found an Australian made car.")

# A better approach
if EntityDomain(entity_type.Domain) is EntityDomain.ROAD:
    car_category = CarCategory(entity_type.Category)
    if car_category in (CarCategory.FORD, CarCategory.HOLDEN):
        print("Found an Australian made car.")
```

#### Regex - Recommendations

1. Preference standard string related functions where they exist e.g. `endswith()` or `startswith()`.
2. Prefer `findall()` instead of `search()`, `fullmatch()` over `match()`.
3. Avoid dynamic/runtime-assembled regexes, pre-compile where possible and store in module-global namespace.
4. When using match groups:

- Name any groups you wish to extract from the match e.g. `(?P<match-name>\w+)`
- Use non-capturing groups when you don't wish to extract particular fragments, but you need a group for validation
  e.g. `(?:json|yaml)`

```python
# Defined at the module level, will validate on module load, and be much faster on every match
REFACTORY_PATH_REGEX = re.compile(
    r'/(?P<project>[\w\-/]+)/-/(?:raw|blob)/(?P<ref>[\w\-]+)/(?P<path>[\w\-/.]+)', re.ASCII)

# Used within a function
matches = REFACTORY_PATH_REGEX.fullmatch("/my-group/my-project/-/raw/master/my_module/main.py")
```

### Ternary Operator Overuse

Ternary operators are more commonly known as conditional expressions in Python. These operators evaluate something
based on a condition being true or not. Here is a blueprint and an example of using these conditional expressions.

```python
value_if_true if condition else value_if_false
```

#### Ternary Operator - Use Cases

Ternary operators are exceptional helpful to consolidate what would have been a multiline if statement into 1 line.
This makes the code more compact and in some situations concise.

```python
LOW_TEMP = 21.0
HIGH_TEMP = 22.5

if today_temp > HIGH_TEMP:
    air_conditioner_temp = LOW_TEMP
else:
    air_conditioner_temp = HIGH_TEMP

# Using ternary operator
air_conditioner_temp = LOW_TEMP if today_temp > HIGH_TEMP else HIGH_TEMP
```

#### Ternary Operator - Recommendations

Although ternary operators are great at reducing lines of code, in some situations they can decrease code-readability,
therefore it is recommended that:

- Ternary operators are utilised for short and logically simple statements.
- If the `condition` or the `value_if_true`/`value_if_false` are particularly long or involve a function call with
  several arguments then prefer a standard `if-else` statement.
- Avoid nested ternary operators.

```python
# Avoid
air_con_temp = calculate_low_temp(today_temp, humidity, time_of_day) if today_temp > get_high_temp() else calculate_high_temp(today_temp, time)
```

**Benefits:**

- Code readability is improved along with maintainability.

### Avoiding Stringly Typed Code

A definition taken from [Techopedia.com](https://www.techopedia.com/definition/31876/stringly-typed#:~:text=Stringly%20typed%20code%20is%20code,used%20rigidly%20to%20enforce%20results.):

> Stringly typed code is code in which variables are often typed as strings, and handled as strings, when there are
> better alternatives available to programmers. It is also a word play off of “strongly typed” code, which describes
> code where types are used rigidly to enforce results. Stringly typed code may be strongly typed, in that it
> reinforces the use of strings, but it is generally not “strongly written,” as it typically does not make use of the
> most efficient solutions.

#### Stringly Typed Code - Recommendations

In the absence of specific and relevant Python examples, refer to the following resources for descriptions of the
problem and how stringly-typed code can be avoided:

- [The Danger of String Literals and Stringly Typed Code](https://cocoacasts.com/the-danger-of-string-literals-and-stringly-typed-code)
- [Stringly Typed - Anti-pattern](https://devcards.io/stringly-typed)

### Bare \* Operator

The bare `*` operator in a function definition forces the caller to use keyword arguments after the operator. Put another
way the `*` operator signals the end of positional arguments.

```python
def my_function(name: str, *, age: int, hair_colour: str, height: float):
    pass

# Invalid
my_function("John", 24, "Brown", 180.0)

# Valid
my_function("John", age=24, hair_colour="Brown", height=180.0)
my_function("Mary", age=22, height=153.5, hair_colour="Black")
```

#### Bare \* Use Cases

There is a long list of arguments to your class or function resulting in client code looking something like this
(Note: Bad function design is overused to emphasise this point).

```python
def health_check(name: str, age: int, weight: float, height: float, shoe_size: int) -> float:
    pass

# It can be hard while reading code on the client side to know which parameter is which
health_score = health_check("John", 68, 100.0, 140.0, 9)
```

By using the bare `*` operator, it will allow the code to be more readable on the client side when arguments to the
function can be easily confused, e.g. many numeric/boolean arguments. It also forces client code to be less sensitive
to the order of arguments, and allows the modification of function signatures (e.g. making arguments optional/adding
defaults) without breaking client code, and requiring a major version bump.

The bare `*` operator can be used to signal to library consumers which arguments are values that are operated upon
(Objects/Subjects) and which are configuration options or modify the operation of the function.

```python
# Not recommended
def check_service_health(name: str, context: Context, try_restart: bool, timeout: float = 0) -> float:
    pass

health_score = check_service_health("transformulator", ctx, True, 10.0)

# Do this instead - much better design, readability, usability, extendability
def check_service_health(name: str, context: Context, *, try_restart: bool, timeout: float = 0) -> float:
    pass

health_score = check_service_health("transformulator", ctx, try_restart=False)
health_score = check_service_health("payments_gateway", ctx, try_restart=True, timeout=10.0)
```

#### Bare \* Recommendations

- Generally aim to have 3 or at most 4 positional parameters. As more are added use the bare \* operator for the
  benefits describe below.

**Benefits:**

- Makes code more readable as in the calling location it disambiguates the parameters.
- Avoids breaking changes to client code when rearranging or adding new keyword parameters.

### Assertions [^2]

#### Assertions - Use Cases

1. For a portion of code to work correctly, certain conditions or values must be true.

```python
def get_expense_limit() -> float:
    # Should have either expense limit or a primary project.
    if general_expense_limit is not None:
        return general_expense_limit.get_value()
    else:
        return primary_project.get_member_limit()
```

#### Assertions - Recommendations

Replace these assumptions or data structure invariants with specific assertion checks. Put string statements after the
assert to provide context to aid debugging.

```python
def get_expense_limit() -> float:
    assert general_expense_limit is not None || primary_project is not None, "general_expense_limit or primary_project must be set"

    if general_expense_limit is not None:
        return general_expense_limit.get_value()
    else:
        return primary_project.get_member_limit()
```

In performance critical code, assertions can be removed by running Python with the `-O` option for release builds or
deployed systems. Therefore it is important that all checks for values derived from user input or network traffic
follow standard check-and-raise validation patterns. Assertions should only be used to check internal code invariants,
to inform the type checker of trivially provable facts, and as part of `pytest` tests on the results of operations and
the state of objects.

```python
# Not recommended
parsed_message = json.loads(message.read())
assert isinstance(parsed_message, dict), "Received message should be a single object"

# Do this instead
parsed_message = json.loads(message.read())
if not isinstance(parsed_message, dict):
    raise ValueError("Received message should be a single object")
```

### Interfaces

#### Interfaces - General Recommendations

1. Inherit from pydantic `BaseModel` class to gain pydantic parsing and data validation guarantees for the interface.

### Testing

#### Testing - General Recommendations

#### Checking Code Was Executed/Reached

In testing there are times when you just want to ensure a message was received or that a certain code point was reached.

```python
async def subscribe_my_messages(pool: ClientPool, subscription_start_event: Event) -> None:
    subscription = await pool.get_subscription(MessageType, 'subscribeMyMessages')
    async for message in subscription.messages(subscription_start_event):
        print("Received a message")
        message_received = true
```

To avoid relying on print statements or setting a flag, consider using mock functionality to better test this code.

```python
from unittest.mock import MagicMock, call

mock = MagicMock()

async def subscribe_my_messages(pool: ClientPool, subscription_start_event: Event) -> None:
    subscription = await pool.get_subscription(MessageType, 'subscribeMyMessages')
    async for message in subscription.messages(subscription_start_event):
        mock("my-message-received")

@pytest.mark.asyncio
async def test_app() -> None:
    # ensure that at least 1 message received
    mock.assert_has_calls([call("my-message-received")])
```

Note: Alternative functions within `MagicMock` exist that can be used to achieve the same functionality.

### Microservices

#### Microservices - General Design Principles

[^1]: Some content adapted from: https://refactoring.guru/replace-magic-number-with-symbolic-constant
[^2]: Some content adapted from: https://refactoring.guru/introduce-assertion
