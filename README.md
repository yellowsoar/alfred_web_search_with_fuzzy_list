# Web Search with Fuzzy List

![](demo.gif)

## TOC

<!-- MarkdownTOC -->

- [Download](#download)
- [Usage](#usage)
  - [Web Search](#web-search)
  - [Fuzzy List Management](#fuzzy-list-management)
  - [Workflow Env](#workflow-env)
- [How it works](#how-it-works)
  - [Web Search](#web-search-1)
  - [Open csv](#open-csv)
  - [More Info](#more-info)
- [Credit](#credit)

<!-- /MarkdownTOC -->

---

## Download

<https://github.com/yellowsoar/alfred_web_search_with_fuzzy_list/releases/latest>

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

## Credit

- [alfred-fuzzy][alfred-fuzzy] by [@deanishe][deanishe]
- [fuzzylist][fuzzylist] by [@derickfay][derickfay]



[deanishe]: https://github.com/deanishe
[alfred-fuzzy]: https://github.com/deanishe/alfred-fuzzy
[derickfay]: https://github.com/derickfay
[fuzzylist]: https://github.com/derickfay/fuzzylist
