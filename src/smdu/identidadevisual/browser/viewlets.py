# -*- coding: utf-8 -*-
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry
from smdu.identidadevisual.interfaces import IVisualIdentitySettings
from zope.component import getUtility


class VisualIdentityViewlet(ViewletBase):

    """Identity Bar Viewlet."""

    def update(self):
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IVisualIdentitySettings)  # noqa: P001

    @property
    def enabled(self):
        return self.settings.show_identity_bar


class FooterViewlet(ViewletBase):

    """Identity Bar Viewlet."""

    def update(self):
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IVisualIdentitySettings)  # noqa: P001

    @property
    def enabled(self):
        return self.settings.show_footer

    @property
    def address(self):
        return self.settings.address.replace(u'\n', u'<br />')
