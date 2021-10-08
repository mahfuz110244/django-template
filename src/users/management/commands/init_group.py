import logging

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


def command():
    if not Group.objects.count():
        logger.info('-------------- ERROR --------------')
        logger.info("Group creation must be done")
        return
    logger.info("Initiating Groups")
    initial_groups = [
        {
            'name': 'Employee',
        },
        {
            'name': 'Manager',
        }
    ]
    for item in initial_groups:
        group = Group.objects.filter(name=item['name']).first()
        if not group:
            group = Group(
                **item
            )
            group.save()
    logger.info('-------------- SUCCESS --------------')


class Command(BaseCommand):
    def handle(self, **options):
        command()
