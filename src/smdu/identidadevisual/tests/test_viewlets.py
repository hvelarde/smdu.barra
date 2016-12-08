# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView as View
from smdu.identidadevisual.testing import INTEGRATION_TESTING
from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IViewletManager

import unittest


class ViewletsTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def _get_viewlet_manager(self, name=None):
        assert name is not None
        context, request = self.portal, self.request
        view = View(context, request)
        manager = getMultiAdapter(
            (context, request, view), IViewletManager, name)
        return manager

    def _get_viewlet(self, name=None, manager=None):
        assert name is not None
        manager = self._get_viewlet_manager(manager)
        manager.update()
        viewlet = [v for v in manager.viewlets if v.__name__ == name]
        assert len(viewlet) == 1
        return viewlet[0]

    def test_render_identity_bar(self):
        viewlet = self._get_viewlet('smdu.identity_bar', 'plone.portaltop')
        self.assertIn(u'id="smdu-identity-bar"', viewlet.render())

    def test_render_footer(self):
        viewlet = self._get_viewlet('smdu.footer', 'plone.portalfooter')
        self.assertIn(u'id="smdu-global-footer"', viewlet.render())
        self.assertIn(u'id="smdu-site-footer"', viewlet.render())
