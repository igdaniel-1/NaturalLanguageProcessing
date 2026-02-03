def col_print(lines, term_width=None, indent=0, pad=2, columnCount=0):
    """Print list of strings in multiple columns
    Original: https://gist.github.com/critiqjo/2ca84db26daaeb1715e1
    Adjusted: https://gist.github.com/Nachtalb/8a85c0793b4bea0a102b7414be5888d4
    ADJUSTED2: this file here, my 'lines' are a dict so I changed 
    """
    n_lines = len(lines)
    if n_lines == 0:
        return

    # added 14 to width for wide tab effect
    col_width = max(len(line) for line in lines) + 14

    n_cols = columnCount

    col_len = int(n_lines / n_cols) + (0 if n_lines % n_cols == 0 else 1)
    if (n_cols - 1) * col_len >= n_lines:
        n_cols -= 1

    cols = [lines[i * col_len: i * col_len + col_len] for i in range(n_cols)]

    rows = list(zip(*cols))
    rows_missed = zip(*[col[len(rows):] for col in cols[:-1]])
    rows.extend(rows_missed)

    for row in rows:
        # line below is changed from origianl for tuple indexing 'line[0]' instead of line
        print(" " * indent + (" " * pad).join(line[0].ljust(col_width) for line in row))