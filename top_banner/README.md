# Top Banner Module for Odoo 18

The **Top Banner** module adds a customizable two-line banner at the top of all Odoo screens. It's ideal for displaying environment indicators (e.g., Test, Staging, Production), maintenance alerts, or company-wide announcements. The banner is highly configurable and ensures important messages are always visible to users.

## Features

- **Two-Line Banner**: Configure two separate lines, each with its own background color, text, and optional hyperlink.
- **Rich Customization**:
  - Background color
  - Text content and text color
  - Optional hyperlink: URL, link text, display type (text or button), and custom styles per type
- **Conditional Display**:
  - Show or hide the entire banner using a toggle
  - Show individual links or buttons based on display type selection
  - Automatically hides a line if information is empty
- **Odoo Settings Integration**: All configurations are available under **Settings > Top Banner**

## Use Cases

- Marking environments (e.g., Test, Staging, or Production)
- Announcing scheduled maintenance or outages
- Displaying internal notices or onboarding tips
- Reminding users of deadlines or policy updates
- Sharing contact or support information company-wide

## Installation

1. Copy the `top_banner` folder to your Odoo addons directory (e.g., `/odoo/addons/`).
2. Enable Developer Mode in Odoo.
3. Go to **Apps** > **Update Apps List**.
4. Search for "Top Banner" and click **Activate**.
5. Go to **Settings > Top Banner** to configure.

## Configuration

In **Settings > Top Banner**:

### General
- **Enable Top Banner**: Toggle to activate or deactivate the banner globally.

### Line 1 Configuration
- **Background Color**
- **Text** (supports `<b>` tags for bold formatting)
- **Text Color**
- **Link URL** (e.g., `https://www.odoo.com/`)
- **Link Text**
- **Link Type**: Select between text or button
  - If **Text**: Choose **Link Color**
  - If **Button**: Choose **Button Color**

### Line 2 Configuration
- All settings are the same as Line 1, independently configurable

## Screenshots

**Home Menu**
![Top banner displayed on the home menu](https://github.com/edgardorios/odoo-free-apps/raw/18.0/top_banner/screenshots/homescreen.png)

**Settings**
![Top Banner settings](https://github.com/edgardorios/odoo-free-apps/raw/18.0/top_banner/screenshots/settings.png)

**Two Lines**
![Top Banner announcement](https://github.com/edgardorios/odoo-free-apps/raw/18.0/top_banner/screenshots/announcement.png)

## Support

This module is free and open-source under the LGPL-3 license.  
For questions or feedback, contact [edgardo.rios@gmail.com](mailto:edgardo.rios@gmail.com) or visit the [GitHub repository](https://github.com/edgardorios/odoo-free-apps).

## License

This module is licensed under the [LGPL-3](https://www.gnu.org/licenses/lgpl-3.0.en.html).

## Contributing

Contributions are welcome!  
Submit pull requests or open issues on the [GitHub repository](https://github.com/edgardorios/odoo-free-apps).