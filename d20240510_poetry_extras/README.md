# Poetry extras の確認

- depended: extras storage, bq をもつ
- depending: depended に依存を持つが、extras bq しか指定していない

期待する動作、depending で poetry install すると、extras bq に依存するパッケージだけで、extras storage のパッケージはインストールされない。

→ 結果期待通り

## depended pyproject.toml

```toml
[tool.poetry]
name = "depended"
version = "0.1.0"
description = ""
authors = ["Atsushi Morimoto (74th) <74th.tech@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.10"
google-cloud-storage = { version = "^2.16.0", optional = true }
google-cloud-bigquery = { version = "^3.22.0", optional = true }

[tool.poetry.extras]
storage = ["google-cloud-storage"]
bq = ["google-cloud-bigquery"]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## depending pyproject.toml

```toml
[tool.poetry]
name = "depending"
version = "0.1.0"
description = ""
authors = ["Atsushi Morimoto (74th) <74th.tech@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.10"
depended = {path = "../depended", extras = ["bq"]}


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```
