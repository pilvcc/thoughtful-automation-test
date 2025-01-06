For this challenge I opted for Python, which I'm familiar with.

The logic was fairly straightforward. I split out functions to test for
bulkiness and heaviness, and then implemented sort in terms of those functions.

I tried to cover various edge cases. I haven't setup Python unit tests in a
while so I just used standard `assert()`.

As a coding style, for `is_bulky` you'll notice I implemented it as a ladder of
if statements. This could be more consisely written as a single OR expression,
but I generally find a series of if statements to be more readable.
