# -*- coding: utf-8 -*-
from webtest_plus import TestApp

import website
from website.addons.base.testing import AddonTestCase


app = website.app.init_app(
    routes=True, set_backends=False, settings_module='website.settings'
)


class ForwardAddonTestCase(AddonTestCase):

    ADDON_SHORT_NAME = 'forward'

    OWNERS = ['node']
    NODE_USER_FIELD = None

    def create_app(self):
        return TestApp(app)

    def set_user_settings(self, settings):
        pass

    def set_node_settings(self, settings):
        settings.url = 'http://frozen.pizza.reviews/'
        settings.redirect_bool = True
        settings.redirect_secs = 15
