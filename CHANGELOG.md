# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Compatibility down to Python 3.10

### Changed

- Performed a cruft update

### Removed

- Useless `@override` decorators
- Field documentation in `YDLOpts`. While useful, this project does not generate Sphinx
  documentation and this documentation is generally not going to appear in an IDE. All original
  documentation can be found in the yt-dlp project's code.
