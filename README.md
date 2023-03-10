![Community-Project](https://gitlab.com/softbutterfly/open-source/open-source-office/-/raw/master/banners/softbutterfly-open-source--banner--community-project.png)

![PyPI - Supported versions](https://img.shields.io/pypi/pyversions/wagtail-sb-admin-interface)
![PyPI - Package version](https://img.shields.io/pypi/v/wagtail-sb-admin-interface)
![PyPI - Downloads](https://img.shields.io/pypi/dm/wagtail-sb-admin-interface)
![PyPI - MIT License](https://img.shields.io/pypi/l/wagtail-sb-admin-interface)

[![Build Status](https://www.travis-ci.org/softbutterfly/wagtail-sb-admin-interface.svg?branch=develop)](https://www.travis-ci.org/softbutterfly/wagtail-sb-admin-interface)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e35e7095857b416696eb58a4ed5d9a15)](https://www.codacy.com/gh/softbutterfly/wagtail-sb-admin-interface/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=softbutterfly/wagtail-sb-admin-interface&amp;utm_campaign=Badge_Grade)
[![Codacy Badge Coverage](https://app.codacy.com/project/badge/Coverage/e35e7095857b416696eb58a4ed5d9a15)](https://www.codacy.com/gh/softbutterfly/wagtail-sb-admin-interface/dashboard?utm_source=github.com&utm_medium=referral&utm_content=softbutterfly/wagtail-sb-admin-interface&utm_campaign=Badge_Coverage)
[![codecov](https://codecov.io/gh/softbutterfly/wagtail-sb-admin-interface/branch/master/graph/badge.svg?token=pbqXUUOu1F)](https://codecov.io/gh/softbutterfly/wagtail-sb-admin-interface)

# Wagtail Admin Interface

Customize the Wagtail admin interface from the admin itself.

Inspired by [django-admin-interface](https://github.com/fabiocaccamo/django-admin-interface).

## Requirements

- Python 3.8.1 or higher
- Django 4.0.0 or higher
- Wagtail 4.0.0 or higher

## Install

```bash
pip install wagtail-sb-admin-interface
```

## Usage

Add `wagtail.contrib.settings`, `wagtail.contrib.modeladmin`, `colorfield` and `wagtail_sb_admin_interface` to your `INSTALLED_APPS` settings

```
INSTALLED_APPS = [
  "wagtail_sb_admin_interface",
  # ...
  "wagtail.contrib.settings",
  "wagtail.contrib.modeladmin",
  "colorfield",
  # ...
]
```

## Docs

- [Ejemplos](https://github.com/softbutterfly/wagtail-sb-admin-interface/wiki)
- [Wiki](https://github.com/softbutterfly/wagtail-sb-admin-interface/wiki)

## Changelog

All changes to versions of this library are listed in the [change history](CHANGELOG.md).

## Development

Check out our [contribution guide](CONTRIBUTING.md).

## Contributors

See the list of contributors [here](https://github.com/softbutterfly/wagtail-sb-admin-interface/graphs/contributors).
