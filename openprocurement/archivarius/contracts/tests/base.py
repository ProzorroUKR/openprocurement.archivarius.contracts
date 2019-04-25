# -*- coding: utf-8 -*-
import os

from openprocurement.contracting.api.tests.base import BaseContractWebTest


class BaseContractArchivariusWebTest(BaseContractWebTest):
    relative_to = os.path.dirname(__file__)
