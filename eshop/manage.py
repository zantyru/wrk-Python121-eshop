#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pathlib
import dotenv


def load_environment():
    lookup_dir = pathlib.Path(__file__).resolve().parent.parent
    dotenv.read_dotenv(lookup_dir / '.env', override=True)


def main():
    """Run administrative tasks."""

    load_environment()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings')
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
