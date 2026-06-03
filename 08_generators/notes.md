1. How generators are different than a normal function ?
   => In a normal function the return of whole function is stored in memory and we are just calling the function but in genreators we are actually generating the values one by one for each call .

- You save memory in generators like alot
- if you don't want results immedietely or you want a lazy evaluation

2. What is Yield ?
   => Yield is a keyword, we can send the data to yield too!

- next() - is used to loop over yields one by one
- send() - to send a valus to yield
- yield from () - getting things or deltegeting to another generator
- close() - memory cleanup / gracefully stopping a generator
