import pkg_resources
from distutils.version import LooseVersion

from django.http import JsonResponse

django_version = pkg_resources.get_distribution('django').version


DJANGO_ONE_SIX = (
    LooseVersion(django_version) < LooseVersion("1.7.0") and
    LooseVersion(django_version) > LooseVersion("1.5.12")
)
