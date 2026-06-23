# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-06-22
### Added
- Comprehensive unit tests with mocking for robust testing.
- Formatted output for the web interface.
- GitHub documentation: README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, PROJECT_REPORT, INSTALLATION, DEMO.
- Better error handling for blank/invalid text inputs.
- `requirements.txt` for dependency management.

### Changed
- Refactored `server.py` to return user-friendly strings instead of raw JSON.
- Updated `emotion_detection.py` to handle API status codes and dominant emotion logic.
- Switched project license to MIT.

### Fixed
- Fixed logical errors in unit test assertions (were checking for 'joy' consistently).
- Fixed `.gitignore` naming and redundancy.
