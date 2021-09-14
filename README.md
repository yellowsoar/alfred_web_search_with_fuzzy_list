# Web Search with Fuzzy List

![](demo.gif)

## Usage

### Web Search

1. Type workflow launch keyword `sfl` in Alfred.
1. Type the keyword that you want t o search in some website start with space.
1. Choose the website you want to search with the keyword.

### Fuzzy List Management

- `sflcsv` =>
  Open `list.csv` file.
- `sflcsv` & `CMD` =>
  Reveal `list.csv` in finder.
- `sflcsv [any command]` =>
  Launch `list.csv` via the given command.
- `sflcsv [any command with argument]` =>
  Launch `list.csv` via the given command and argument.

### Workflow Env

- Chage the launch keyword in workflow environment variables settings.
  (default: `sfl`)

## How it works

### Web Search

The workflow will:

1. Save the search keyword to `{var:keyword}`.
1. Replace `{query}` in the `list.csv` arg volume with `{var:keyword}`.
1. Open the arg (supposed to be a url) and copy `{var:query}` to clipboard.

### Open csv

1. The workflow will check given command first.
  - Open file if command not exist or without permission.

### More Info

- For fuzzy search, check [alfred-fuzzy][alfred-fuzzy]
- For fuzzy list filter, check [fuzzylist][fuzzylist]



[alfred-fuzzy]: https://github.com/deanishe/alfred-fuzzy
[fuzzylist]: https://github.com/derickfay/fuzzylist
