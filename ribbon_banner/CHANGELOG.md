# Changelog

## [18.0.2.0.1] - 2025-04-24
### Changed
- Migrated module to new `odoo-free-apps` repository from `ribbon-banner`.
- Updated `__manifest__.py`:
  - Changed `website` to `https://github.com/edgardorios/odoo-free-apps`.
  - Updated `version` to `18.0.2.0.1`.
- Moved `README.md` to `ribbon_banner` folder and updated links to point to `odoo-free-apps` repository.
- Created new root `README.md` for `odoo-free-apps` repository to describe the collection of free apps.

## [18.0.2.0.0] - 2025-04-23
### Fixed
- Prevented duplicate ribbon banner in the Odoo website editor by checking `website_id` context.

## [18.0.1.0.0] - 2025-04-20
### Added
- Initial release with customizable ribbon banner for environment and database name display.