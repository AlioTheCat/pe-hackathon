---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
---

Licence CC BY-NC-ND, Thierry Parmentelat   -  (images courtesy of wikipedia)


# pentominoes and exact cover

```{image} media/board-8x8-pretty.png
:align: right
:width: 300px
```
in order to work on this exercise from your laptop, {download}`start with downloading the zip<./ARTEFACTS-pentominos.zip>`

this activity is about solving puzzles like the one pictured on the right, using a standard combinatorial algorithm



## the exact cover problem

### an example

in a nutshell, the exact cover problem is a standard, very basic mathematical problem; let's start with an example  
you feed the algorithm with a set of vectors that all have the same length, and contain 0 and 1, like e.g.

```
0:  (1 0 0 1 1 0 1 0)
1:  (1 0 0 0 1 1 0 1)
2:  (1 0 0 0 1 1 1 0)
3:  (1 0 1 0 1 1 0 0)
4:  (1 0 0 0 1 0 1 1)
5:  (1 0 1 1 1 0 0 0)
6:  (1 0 0 0 0 1 1 1)
7:  (0 1 0 1 1 0 1 0)
8:  (0 1 0 0 1 1 0 1)
9:  (0 1 0 0 1 1 1 0)
10: (0 1 1 0 1 1 0 0)
11: (0 1 0 0 1 0 1 1)
12: (0 1 1 1 1 0 0 0)
13: (0 1 0 0 0 1 1 1)
```

and the goal is to find **a subset** of the input vectors, such that **each column of the input is covered exactly once**  
(of course there is the accessory question about whether there are several
solutions, but let's not dwelve into that, for now at least..)  
so in the above example, there would be 2 solutions, namely

```
# a solution has exactly one 1 in each column

5:  (1 0 1 1 1 0 0 0)
13: (0 1 0 0 0 1 1 1)
```
and
```
6:  (1 0 0 0 0 1 1 1)
12: (0 1 1 1 1 0 0 0)
```


### the algorithm and its implementation in Python

one possible way to solve this problem has been the subject of a famous article by Donald Knuth - one of
the fathers of Computer Science - and is known as Knuth's Algorithm X - interested students can find [more details in the links section below](#links).  
we're not going to go into the details of the algorithm either, but rather focus
on the application to solving pentominoes (see next section)

let us just outline that

- Algorithm X, also known as dancing links, is an extremely efficient
  implementation for solving the exact cover problem
- and fortunately for us, there are several Python implementations of it (see pypi.org for details):
  - `xcover`
  - `exact-cover`
  - `exact-cover-py`

So your first task is to search for one of these packages (`xcover` seems the most efficient one),
install it, and read the basics about how to use it


## application to pentominoes

### the pentominoes

and now for something completely different...  
the pentaminoes are the 12 patterns that can be made of 5 contiguous squares - modulo rotations and symmetry  
they have been given names, letters actually:

```{image} media/pentominos.png
:width: 60%
:align: center
```


### some standard problems

they can be taken as the pieces of a puzzle, and so the standard problems are to fill shapes with these 12 pieces - of course each piece is to be used exactly once, in any rotation / symmetry

we'll consider here the following shapes (of course each shape must have an area of $12 * 5 = 60$)

```{image} media/boards.png
:align: center
:width: 60%
```

as well as this one within a 8x8 square and a hole inside

```{image} media/board-8x8.png
:width: 40%
:align: center
```


### how to solve such a problem

the trick is to **transform the puzzle problem into an exact cover problem**  
there are many resources on the Internet that explain how to do that - and feel free to use them too  
on our end, let's consider a smaller problem as depicted ; note that the white squares are holes, and of course not part of the problem


#### our small example

```{image} media/small-problem.png
:width: 150px
:align: center
```

it turns out this problem can be mapped to the sample input quoted above in the introduction, i.e.

```
0:  (1 0   0 1 1 0 1 0)
1:  (1 0   0 0 1 1 0 1)
2:  (1 0   0 0 1 1 1 0)
3:  (1 0   1 0 1 1 0 0)
4:  (1 0   0 0 1 0 1 1)
5:  (1 0   1 1 1 0 0 0)
6:  (1 0   0 0 0 1 1 1)

7:  (0 1   0 1 1 0 1 0)
8:  (0 1   0 0 1 1 0 1)
9:  (0 1   0 0 1 1 1 0)
10: (0 1   1 0 1 1 0 0)
11: (0 1   0 0 1 0 1 1)
12: (0 1   1 1 1 0 0 0)
13: (0 1   0 0 0 1 1 1)
```


#### how is this obtained ?

you will find one line for each possible position of a piece on the board  
this line will contain:

- the first 2 columns (we have 2 pieces) correspond to the piece number  
  we set exactly one 1 to indicate which piece we're talking about  
  so for example the first 7 rows correspond to the 7 positions where we can place piece#0
- because there are 6 squares to be filled, the next 6 columns correspond to the slots that the piece in that position would occupy  
  (1 means the slot is occupied)  
  and since the 2 pieces are identical, the 7 last rows carry the same information, but for piece#1

````{admonition} note
:class: attention

obstacles (the white squares) in the board **must not** be given a column:
there would be only 0's in that column, and `exact_cover` would find no solution
````

```{image} media/subtitles.png
:align: right
:width: 300px
```

and so for example with our small problem, the line `3:` means:

- this is about piece#0 (hence col0=1 and col1=0)
- and that piece may be placed on the board in the following position

```
X o X
. o o
X . .
```

which, once you remove the obstacles, and flatten, reads `1 0 1 1 0 0`: the right-hand-side of first line

<!-- #region -->
#### how to read a solution ?

if you pick `xcover` as a solver engine, it will expose a generator over solutions; this means that you can wrote something like

```
solutions = covers_bool(problem)
first = next(solutions)
print(first)
-> [5, 13]
```

which maps to the following rows into the input problem:

```
5:  (1 0   1 1 1 0 0 0)
13: (0 1   0 0 0 1 1 1)
```

which we then interpret, the other way around, like so:
- there is at least one solution to the problem
- and in this solution we have piece#0 that spans these locations
  ```
  X o X
  o o .    (because 111000 for piece #0)
  X . .
  ```
- and piece#1 that spans these locations
  ```
  X . X
  . . o    (because 000111 for piece #1)
  X o o
  ```


#### quiz

how many columns are you going to need for a real-scale pentaminos problem ?

```{admonition} solution
:class: dropdown

you have 12 pieces and 60 slots to fill, so you need 72 columns
```
<!-- #endregion -->

## what to do

### model the problem

decide how to represent the board and pieces:
* using nd-arrays, so rectangular spaces
* use only **booleans** to model **obstacles** in the board and the actual **contour** of pieces

you will find some helper code in `pentominos_data.py` if you wish to use it  
in particular, note the presence of `SMALL_BOARD` and `SMALL_PIECE`
that correspond to the following solution, and that may turn out useful for debugging your code

```{image} media/small-problem.png
:width: 150px
:align: center
```


### rotations and symmetries

for each piece, compute its - possibly up to 8 - variants


### compute all possible translations

for each piece (supposed to have been rotated and/or swapped already)
compute all the possible locations on the board


### prepare the exact_cover input

given a board and a set of pieces, compute the input to `covers_bool()`


### pretty-print a solution

your solver will then compute one solution (if there's one, of course)  
from this solution, your job is to compute a 'pretty' view of the solution, something like e.g.
  ```
  (( 3  3  6  7  7  5  5  5 11 11 11 11)
   ( 3  6  6  6  7  9  5  5 10 11 12 12)
   ( 3  1  6  7  7  9  9 10 10 10 12  8)
   ( 3  1  1  4  4  4  9  9 10 12 12  8)
   ( 1  1  4  4  2  2  2  2  2  8  8  8))
  ```
  or, in the case where there are 'obstacles' on the board, it could be something like this (use 0 for the holes)
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


### matplotlib

if time permits, you could also transform this rough numpy solution into a nicer matplotlib drawing - or any other visual library of your choice, like e.g.

```{image} media/board-8x8-pretty.png
:align: center
:width: 60%
```

````{admonition} hints

to produce this we have
- used some predefined colormaps in matplotlib - see `matplotlib.pyplot.colormaps()` - you could consider accepting an argument that specifies one if them
- made the (color corresponding to) obstables transparent, by using the so-called alpha channel (fourth if you count first the red, green and blue channels)
````

```python
# import matplotlib
# matplotlib.pyplot.colormaps()
```


### testing

you should find at least one solution for
- rectangle 6x10
- rectangle 5x12
- rectangle 4x15
- rectangle 3x20
- rectangle 8x8 with a 2x2 obstacle in the middle
- 2 rectangles 5x6
- ... and many more of course, like e.g. `BOARD_8_9` in `pentominos_data`


## what now ?

### further applications

you can use `exact_cover` to solve a whole range of other problems, like for example sudoku - and it's actually less obvious to do the mapping; if you're done early you can give these some thought


### links

* <https://en.wikipedia.org/wiki/Exact_cover>
* <https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X>
* if you plan on going (much) further, and on implementing a solver yourself, make sure to read this step-by-step description of the algorithm (you need several hours/days to get through this ;):["The art of computer programming", section 7.2.2.1](https://www.inf.ufrgs.br/~mrpritt/lib/exe/fetch.php?media=inf5504:7.2.2.1-dancing_links.pdf)
