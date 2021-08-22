#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""

    load_dotenv(os.path.join('.env'))

    # This is where to set the environment (dev or prod) - Actually it's in wsgi.py
    if os.getenv("ENV") == "PRODUCTION":
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainsite.settings.production')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainsite.settings.development')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


