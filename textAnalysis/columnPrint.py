def col_print(lines, term_width=None, indent=0, pad=2, columnCount=0):
    """Print list of strings in multiple columns
    Original: https://gist.github.com/critiqjo/2ca84db26daaeb1715e1
    Adjusted: https://gist.github.com/Nachtalb/8a85c0793b4bea0a102b7414be5888d4
    ADJUSTED2: this file here, my 'lines' are a dict so I changed 
    """
    n_lines = len(lines)
    if n_lines == 0:
        return

    # added width for wider tab effect
    if columnCount > 4:
        col_width = max(len(line) for line in lines) 
    else:
        col_width = max(len(line) for line in lines) + 6

    n_cols = columnCount

    col_len = int(n_lines / n_cols) + (0 if n_lines % n_cols == 0 else 1)
    if (n_cols - 1) * col_len >= n_lines:
        n_cols -= 1

    cols = [lines[i * col_len: i * col_len + col_len] for i in range(n_cols)]

    rows = list(zip(*cols))
    rows_missed = zip(*[col[len(rows):] for col in cols[:-1]])
    rows.extend(rows_missed)

    for row in rows:
        # OLD: line below is changed from original for tuple indexing 'line[0]' instead of line
        # NEW: reset to original context after modding textInputReader.py/plainListDisplay() to pass just dict keys to columnPrint/col_print()
        print(" " * indent + (" " * pad).join(line.ljust(col_width) for line in row))