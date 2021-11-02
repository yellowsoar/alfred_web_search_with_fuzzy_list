# Web Search with Fuzzy List

Web search in 3 steps with fuzzy selection based on csv files.

![](demo/sigle_mode.gif)
![](demo/multiple_mode.gif)

## TOC

<!-- MarkdownTOC -->

- [Download and Releases](#download-and-releases)
- [Usage](#usage)
  - [Web Search](#web-search)
    - [Multiple CSV mode](#multiple-csv-mode)
    - [Single CSV mode](#single-csv-mode)
  - [CSV Management](#csv-management)
    - [Single CSV mode](#single-csv-mode-1)
  - [Workflow Env](#workflow-env)
- [How it works](#how-it-works)
  - [Web Search](#web-search-1)
  - [Open csv](#open-csv)
  - [More Info](#more-info)
- [References](#references)
- [Credit](#credit)

<!-- /MarkdownTOC -->

---

## Download and Releases

- **Download link**
  - Github: <https://github.com/yellowsoar/alfred_web_search_with_fuzzy_list/releases/latest>
- Version number follow [Semantic Versioning][semver] (Major.Minor.Patch).
- Release when:
  - Major upgrade
  - Minor upgrade
  - Hotfix Patch

## Usage

### Web Search

#### Multiple CSV mode

1. `sfl ` + keyword for web search then press`Return`/`Enter`
1. CSV file name
1. choose website

#### Single CSV mode

1. `sfl ` + keyword for web search then hold `CMD(⌘)` and press`Return`/`Enter`
1. choose website

### CSV Management

#### Single CSV mode

- `sflcsv` =>
  Open `list.csv` file.
- `sflcsv` and hold `CMD(⌘)` =>
  Reveal `list.csv` in finder.
- `sflcsv [any command]` =>
  Launch `list.csv` via the given command.
  ex: `sflcsv subl` (open CSV file in sublime text)
- `sflcsv [any command with argument]` =>
  Launch `list.csv` via the given command and argument.
  ex: `sflcsv open -a safari` (Open CSV file in Safari)

### Workflow Env

- Change the launch keyword in workflow environment variables settings.
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

## References

1. [Fuzzy List  Post][fuzzylistpost] on [Alfred forum][alfredforum] by [@derickfay][derickfay]
1. [Post][post_web_search_with_fuzzy_list] on [Alfred forum][alfredforum]

## Credit

- [alfred-fuzzy][alfred-fuzzy] by [@deanishe][deanishe]
- [fuzzylist][fuzzylist] by [@derickfay][derickfay]



[alfred-fuzzy]: https://github.com/deanishe/alfred-fuzzy
[alfredforum]: https://www.alfredforum.com
[deanishe]: https://github.com/deanishe
[derickfay]: https://github.com/derickfay
[fuzzylist]: https://github.com/derickfay/fuzzylist
[fuzzylistpost]: https://www.alfredforum.com/topic/11094-fuzzy-self-updating-list-filter-workflow-template/
[semver]: https://semver.org
[post_web_search_with_fuzzy_list]: https://www.alfredforum.com/topic/17499-web-search-with-fuzzy-list/
