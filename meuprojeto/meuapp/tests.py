from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.test import Client
from django.core import mail
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext as _
from django.utils.translation import activate
from django.utils.translation import deactivate
from django.utils.translation import get_language
from django.utils.translation import get_language_info
from django.utils.translation import get_language_bidi 
