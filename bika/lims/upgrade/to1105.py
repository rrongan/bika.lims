import logging

from Acquisition import aq_base
from Acquisition import aq_inner
from Acquisition import aq_parent

from Products.CMFCore import permissions
from bika.lims.permissions import *

from Products.CMFCore.utils import getToolByName


def upgrade(tool):
    """ #757 - Fixed without acquire flag
    """
    portal = aq_parent(aq_inner(tool))
    setup = portal.portal_setup
    mp = portal.clients.manage_permission
    mp(permissions.ModifyPortalContent, ['Manager', 'LabManager', 'Owner', 'Analyst'], 0)
    mp(permissions.AddPortalContent, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'Analyst'], 0)

    return True
