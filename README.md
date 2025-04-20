# Ribbon Banner Module for Odoo 18

The **Ribbon Banner** module adds a customizable ribbon to your Odoo instance, displaying the environment (e.g., DEV, TEST, STAGING) and database name in the top-left corner. Configure the banner's text, background color, text color, and opacity directly in **Settings &gt; General Settings**. Perfect for multi-environment setups to avoid confusion!

## Features

- Displays a ribbon banner with the environment and database name.
- Configurable settings in **General Settings**:
  - **Banner Text**: Set custom text (e.g., "DEV").
  - **Banner Opacity**: Set opacity between 0.0 (fully transparent) and 1.0 (fully opaque).
  - **Banner Text Color**: Choose the text color.
  - **Banner Background Color**: Choose a color via a color picker.
- Lightweight and easy to install.
- Open-source under LGPL-3 license.

## Installation

### Install from Odoo Apps

1. Visit Ribbon Banner on Odoo Apps.
2. Click **Download** to get the ZIP file.
3. Extract the ZIP to obtain the `ribbon_banner` folder.
4. Copy the `ribbon_banner` folder to your Odoo `addons` directory (defined in `odoo.conf`).
5. Log in to Odoo with admin rights.
6. Go to **Settings &gt; About** and click **Activate the developer mode**.
7. Go to **Apps** and click **Update Apps List**.
8. Search for "Ribbon Banner" and click **Install**.
9. Configure the banner in **Settings &gt; General Settings** (see below).

### For Developers: Install from GitHub

1. **Prerequisites**:

   - Odoo 18 installed.
   - Access to the Odoo `addons` folder (defined in `odoo.conf`).

2. **Copy the Module**:

   - Download the module as a ZIP from GitHub or clone it:

     ```bash
     git clone https://github.com/edgardorios/ribbon-banner.git
     ```

   - Copy the `ribbon_banner` folder to your Odoo `addons` folder.

3. **Update Module List**:

   - Log in to Odoo with admin rights.

   - Go to **Settings &gt; About** and click **Activate the developer mode**.

   - Go to **Apps** and click **Update Apps List**.

   - Alternatively, restart your Odoo server:

     ```bash
     sudo systemctl restart odoo
     ```

4. **Install the Module**:

   - In **Apps**, search for "Ribbon Banner" and click **Install**.

### Configuration

1. Go to **Settings &gt; General Settings**.
2. Scroll to the **Ribbon Banner** section (at the bottom).
3. Set the Banner Text (e.g., "DEV"), Opacity, Text Color, and Background Color, then click **Save**.

## Screenshots

![Ribbon banner displayed on a page](https://github.com/edgardorios/ribbon-banner/raw/18.0/ribbon_banner/screenshots/banner.png)

![Configuration in General Settings](https://github.com/edgardorios/ribbon-banner/raw/18.0/ribbon_banner/screenshots/settings.png)

## License

This module is licensed under the GNU Lesser General Public License v3.0 (LGPL-3).

## Support

For issues or feature requests, contact edgardo.rios@gmail.com or visit https://github.com/edgardorios/ribbon-banner.

## Contributing

Contributions are welcome! Fork the repository, make changes, and submit a pull request.
