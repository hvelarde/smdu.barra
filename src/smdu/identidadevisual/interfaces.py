# -*- coding:utf-8 -*-
from plone.autoform import directives as form
from plone.supermodel import model
from smdu.identidadevisual import _
from smdu.identidadevisual.config import DEFAULT_ADDRESS
from zope import schema
from zope.interface import Interface


class IAddOnLayer(Interface):

    """A layer specific for this add-on product."""


class IVisualIdentitySettings(model.Schema):

    """Schema for the control panel form."""

    show_identity_bar = schema.Bool(
        title=_(u'Show identity bar?'),
        description=_(u''),
        default=True,
    )

    show_footer = schema.Bool(
        title=_(u'Show footer?'),
        description=_(u''),
        default=True,
    )

    form.widget('address', rows=7)
    address = schema.Text(
        title=_(u'Address'),
        description=_(u''),
        default=DEFAULT_ADDRESS,
    )
