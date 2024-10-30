# pe-hackathon

## The challenge

For a class exercise in my engineering school, in groups of 4, we were brought to chose a subject among a [list of prompts](https://github.com/ue12-p24/hackathon-PE/blob/main/sujets.md).
We were given 4 hours to work in teams and solve the chosen problem in Python.

## The prompt we chose
We're given a set of "petominos", a variant of tetris' "tetraminos" with 5 square instead of 4 in each piece. Here's every kind of piece we can come up with (keeping in mind that every transformation such as rotation or plane symmetry is allowed) :

![image](https://github.com/user-attachments/assets/177bad00-13e7-4a79-a63b-2acb112f2fd0)

The goal is the following : given a grid with some obstacles (place where petominos can't be placed) and a set of pieces (by default, one piece of every 12 kinds) find an arrangement of the pieces that fills every free slot in the grid (with every rotation and symmetry allowed).

**Here are some examples (w/o obstacles) :**

![image](https://github.com/user-attachments/assets/860a6929-dd26-4081-9f2c-cc339f29a9e5)

**And here's an example with a 2x2 obstacle in the middle :**

![image](https://github.com/user-attachments/assets/563bbb6c-106a-45f4-832c-e989debb58e8)

## Our solution

We give ourselves `g` a $h \times w$ binary grid where occurences of `1` are the obstacles in the grid, and a set of pieces in their representation.

First, we calculate each legal possible position of every piece. We represent these positions by a binary matrix, where 1 represents slots that are occupied by the piece, and each 0 is an empty slot.

Then, we convert each matrix into a flattened vector of this form :
```
(00...10...0    00...11001...00)
 <----N---->    <------X------>
```
Where `N` is the size of the piece set we must place in the grid, and `X` is the amount of free slots in the grid.

Here's how we compute this vector :
* The first part of the vector a sort of id that corresponds to the corresponding piece in our set : it is made of zeros, except at the index corresponding to the piece's id. For instance, piece n°2 in a 5 piece set will have id `00100`
* The second part is the coefficients of the binary matrix from top left to bottom right, where we removed coefficients corresponding to a slot with an obstacle.

Therefore, an arrangement of pieces will fill the grid correctly if and only if :
* We only use each piece of the set once, i.e the first part of each piece's vector adds up to `(1....1)`.
* There's no free slot (a), and no overlapping pieces (b). Therefore, the second part of each piece's vector must add up to `(1....1)`, because it shouldn't contain any 0 (a), and nor any value of 2 and above (b).

We're hence brought to solve a simpler problem : finding in a set of binary vectors a subset that adds up to `(1....1)`

The function `covers_bool` from module `xcover` does the job. Its output allows us to access the list of position matrix that fills the grid.
To obtain the resulting grid, we can calculate a linear combination of these matrix such as following :

```
filled_grid = 1*piece1_matrix + 2*piece2_matrix + ... + N*pieceN_matrix
```

For instance, tne last figure in the examples section corresponds to the following matrix :

```
(( 2  7  7  6 11 11 11 11)
 ( 2  7  6  6  6 10 11  4)
 ( 2  7  7  6 10 10 10  4)
 ( 2  5  5  0  0 10  4  4)
 ( 2  5  5  0  0  1  4  3)
 ( 8 12  5  1  1  1  9  3)
 ( 8 12 12 12  1  9  9  3)
 ( 8  8  8 12  9  9  3  3))
```

We obtain a grid where the only slots containing 0 are slots filled with an obstacle.

We can then display the result with matplotlib's `plt.matshow`
