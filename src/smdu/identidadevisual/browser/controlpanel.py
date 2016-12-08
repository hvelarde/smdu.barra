# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from smdu.identidadevisual import _
from smdu.identidadevisual.interfaces import IVisualIdentitySettings


class VisualIdentitySettingsEditForm(controlpanel.RegistryEditForm):

    """Control panel edit form."""

    schema = IVisualIdentitySettings
    label = _(u'Visual Identity')
    description = _(u'Settings for the identity bar and footer.')


class VisualIdentitySettingsControlPanel(controlpanel.ControlPanelFormWrapper):

    """Control panel form wrapper."""

    form = VisualIdentitySettingsEditForm
