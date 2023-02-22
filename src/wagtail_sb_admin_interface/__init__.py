import django

if django.VERSION < (3, 2):
    default_app_config = "wagtail_sb_admin_interface.apps.WagtailSbInterfaceConfig"
