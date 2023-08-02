def pretty_print_bingo(bingos_grid, bingo_scores_grid):
    for i in range(len(bingos_grid)):
        bingo = bingos_grid[i]
        bingo_score = bingo_scores_grid[i]
        for j in range(len(bingo)):
            print(bingo[j], "\t", bingo_score[j])
        print("\n")


def is_win(bingo_scores_grid, num, bing, col_idx, line_idx):
    win_col = True
    for line in bingo_scores_grid[bing]:
        if line[col_idx] == 0:
            win_col = False
    win_line = True
    for num in bingo_scores_grid[bing][line_idx]:
        if num == 0:
            win_line = False
            break
    return win_line or win_col


def mark_draw(bingo_scores_grid, bing, col_idx, line_idx):
    bingo_scores_grid[bing][line_idx][col_idx] = 1


def count_non_marked(bingos, bingo_scores, bing):
    sum_val = 0
    for k, row in enumerate(bingo_scores[bing]):
        for j, col in enumerate(row):
            if col == 0:
                sum_val += bingos[bing][k][j]
    return sum_val


file = open('input.in', 'r')
drawing_string = file.readline()
drawing = [int(num) for num in drawing_string.split(',')]
lines_newline = file.readlines()
lines = [line.strip() for line in lines_newline]

set_bingo_nums = {}

bingos = []
bingo = []
bingo_scores = []
bingo_score = []
idx_bingo = 0
idx_line = 0
idx_col = 0
for i in range(len(lines)):
    if lines[i] != "":
        idx_col = 0
        bingo_line = []
        bingo_score_line = []
        for num in lines[i].split(' '):
            if num != '':
                bingo_line.append(int(num))
                bingo_score_line.append(0)
                num_set = set_bingo_nums.get(int(num))
                if num_set is None:
                    set_bingo_nums[int(num)] = [{'col': idx_col, 'line': idx_line, 'bingo': idx_bingo}]
                else:
                    num_set.append({'col': idx_col, 'line': idx_line, 'bingo': idx_bingo})
                idx_col += 1
        bingo.append(bingo_line)
        bingo_score.append(bingo_score_line)
        idx_line += 1
    else:
        if len(bingo) > 0:
            bingos.append(bingo)
            bingo = []
            bingo_scores.append(bingo_score)
            bingo_score = []
            idx_bingo += 1
            idx_line = 0

bing_won = set()

for draw in drawing:
    num_set = set_bingo_nums.get(draw)
    for pos in num_set:
        mark_draw(bingo_scores, pos['bingo'], pos['col'], pos['line'])
        has_already_won = bing_won.__contains__(pos['bingo'])
        if is_win(bingo_scores, draw, pos['bingo'], pos['col'], pos['line']) and not has_already_won:
            print("WIN = ", count_non_marked(bingos, bingo_scores, pos['bingo']) * draw)
            bing_won.add(pos['bingo'])



pretty_print_bingo(bingos, bingo_scores)


