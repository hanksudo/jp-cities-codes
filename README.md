# Japan Cities Codes

Convert [都道府県コード及び市区町村コード](http://www.soumu.go.jp/denshijiti/code.html
) to json

## Files

- data/000618153.xls (都道府県コード及び市区町村コード)
- data/prefectures.json (Output of R1.5.1現在の団体)
- data/cities.json (Output of H30.10.1政令指定都市)

## Usage

[Pipenv](https://github.com/pypa/pipenv)

```bash
pipenv run python app.py
```
