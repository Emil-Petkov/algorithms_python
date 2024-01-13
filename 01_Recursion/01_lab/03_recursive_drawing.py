def draw_stars(n_stars: int):
    if n_stars == 0:
        return

    print('*' * n_stars)
    draw_stars(n_stars - 1)
    print('#' * n_stars)


n = int(input())
draw_stars(n)
