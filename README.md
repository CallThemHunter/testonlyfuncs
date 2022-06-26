## Purpose
Keep your code maintainable while limiting how much is exposed through
the public API. This decorator enables a more readable interface with
python's under and dunder fields that will ensure your tests
are less prone to errors


## Installation

This package is distributed as 'testonlyfuncs'

Install using 'pip install testonlyfuncs'

## Usage

Simply do 'from testonlyfuncs import test_only', then declare 
'@test_only' above any function you want only used in tests.
The function with this decorator *must* start with 'test_only' to
indicate its usage. Recommended to mark test only code as such in
documentation comments.


## Support

Currently only works with:
- unittest