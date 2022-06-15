# qsqlmysql-builds

`Qt` does not distribute `qsqlmysql` plugin in binary form, so if you need one you have to compile it. In order to work it must be compiled with same compiler that your specific `Qt` binaries were build. This script aims to produce build recepies for qsqlmysql plugins that are compatible with binaries distributed by official `Qt` installer, or custom recepies for your specific case. Recepie can be used on local machine, just run generated `main.bat` or on `github actions` pipeline (`.github/workflow/main.yml`).

Two architectures implemented: `i686` and `x86_64`

Two compilers implemented: `MinGW` (various) and `msvc` (`msvc2019`)

Two major Qt version implemented: `5.x.x` and `6.x.x`

`MinGW` version chosen for each `Qt` version accordingly to https://wiki.qt.io/MinGW

`msvc` compiler chosen accordingly to [aqt](https://github.com/miurahr/aqtinstall) output.

Run `python generate.py --help` for details.