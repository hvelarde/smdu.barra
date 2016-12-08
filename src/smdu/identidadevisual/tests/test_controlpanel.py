# -*- coding: utf-8 -*-
from plone import api
from plone.registry.interfaces import IRegistry
from smdu.identidadevisual.config import DEFAULT_ADDRESS
from smdu.identidadevisual.config import PROJECTNAME
from smdu.identidadevisual.interfaces import IVisualIdentitySettings
from smdu.identidadevisual.testing import INTEGRATION_TESTING
from zope.component import getUtility

import unittest


class ControlPanelTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.controlpanel = self.portal['portal_controlpanel']

    def test_controlpanel_has_view(self):
        view = api.content.get_view(u'visualidentity-settings', self.portal, self.request)
        view = view.__of__(self.portal)
        self.assertTrue(view())

    def test_controlpanel_view_is_protected(self):
        from AccessControl import Unauthorized
        from plone.app.testing import logout
        logout()
        with self.assertRaises(Unauthorized):
            self.portal.restrictedTraverse('@@visualidentity-settings')

    def test_controlpanel_installed(self):
        actions = [
            a.getAction(self)['id'] for a in self.controlpanel.listActions()]
        self.assertIn('visualidentity', actions)

    def test_controlpanel_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']

        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[PROJECTNAME])

        actions = [
            a.getAction(self)['id'] for a in self.controlpanel.listActions()]
        self.assertNotIn('visualidentity', actions)


class RegistryTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.registry = getUtility(IRegistry)
        self.settings = self.registry.forInterface(IVisualIdentitySettings)  # noqa: P001

    def test_show_identity_bar_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'show_identity_bar'))
        self.assertEqual(self.settings.show_identity_bar, True)

    def test_show_footer_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'show_footer'))
        self.assertEqual(self.settings.show_footer, True)

    def test_address_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'address'))
        self.assertEqual(self.settings.address, DEFAULT_ADDRESS)

    def test_records_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']
        qi.uninstallProducts(products=[PROJECTNAME])

        records = [
            IVisualIdentitySettings.__identifier__ + '.show_identity_bar',
            IVisualIdentitySettings.__identifier__ + '.show_footer',
            IVisualIdentitySettings.__identifier__ + '.address',
        ]

        for r in records:
            self.assertNotIn(r, self.registry)
