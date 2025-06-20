<!-- markdownlint-configure-file {"MD024": { "siblings_only": true } } -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

## [0.0.17] - 2025-06-08

### Added

- Added almost the entire interface except for most extractors and postprocessors. Not everything is
  as precise as it could.

## [0.0.16] - 2025-04-27

### Added

- `yt_dlp.minicurses` typing

### Changed

- Made `yt_dlp.cookies` more complete.

### Fixed

- Return value of `yt_dlp.cookies.extract_cookies_from_browser`.

## [0.0.15] - 2025-04-12

### Added

- Compatibility for Python 3.10 and Python 3.11
- Exports in `yt_dlp.networking`

### Changed

- Performed a cruft update
- Force keys in `yt_dlp.utils.networking.HTTPHeaderDict` to be `str`
- Updated copyright year

### Removed

- Useless `@override` decorators
- Field documentation in `YDLOpts`. While useful, this project does not generate Sphinx
  documentation and this documentation is generally not going to appear in an IDE. All original
  documentation can be found in the yt-dlp project's code.
- Tests. Tests that involve testing output from Pyright might be explored again in the future.

## [0.0.14] - 2025-02-21

### Added

- `yt_dlp.networking` stubs. Thanks to @thcrt

### Fixed

- Package name. Thanks to @Sky-NiniKo

[unreleased]: https://github.com/Tatsh/yt-dlp-types/compare/v0.0.17...HEAD
