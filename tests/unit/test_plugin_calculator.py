# SPDX-License-Identifier: AGPL-3.0-or-later
# pylint: disable=missing-module-docstring

from mock import Mock
from parameterized.parameterized import parameterized
from searx import plugins
from tests import SearxTestCase
from .test_utils import random_string

from .test_plugins import get_search_mock


class PluginCalculator(SearxTestCase):  # pylint: disable=missing-class-docstring
    def setUp(self):
        self.store = plugins.PluginStore()
        plugin = plugins.load_and_initialize_plugin('searx.plugins.calculator', False, (None, {}))
        self.store.register(plugin)

    def test_plugin_store_init(self):
        self.assertEqual(1, len(self.store.plugins))

    def test_single_page_number_true(self):
        request = Mock(remote_addr='127.0.0.1')
        search = get_search_mock(query=random_string(10), pageno=2)
        result = self.store.call(self.store.plugins, 'post_search', request, search)
        self.assertTrue(result)
        self.assertNotIn('calculate', search.result_container.answers)

    def test_long_query_true(self):
        request = Mock(remote_addr='127.0.0.1')
        search = get_search_mock(query=random_string(101), pageno=1)
        result = self.store.call(self.store.plugins, 'post_search', request, search)
        self.assertTrue(result)
        self.assertNotIn('calculate', search.result_container.answers)

    def test_alpha_true(self):
        request = Mock(remote_addr='127.0.0.1')
        search = get_search_mock(query=random_string(10), pageno=1)
        result = self.store.call(self.store.plugins, 'post_search', request, search)
        self.assertTrue(result)
        self.assertNotIn('calculate', search.result_container.answers)

    @parameterized.expand(
        [
            "1+1",
            "1-1",
            "1*1",
            "1/1",
            "1**1",
            "1^1",
        ]
    )
    def test_int_operations(self, operation):
        request = Mock(remote_addr='127.0.0.1')
        search = get_search_mock(query=operation, pageno=1)
        result = self.store.call(self.store.plugins, 'post_search', request, search)
        self.assertTrue(result)
        self.assertIn('calculate', search.result_container.answers)

    @parameterized.expand(
        [
            "1/0",
        ]
    )
    def test_invalid_operations(self, operation):
        request = Mock(remote_addr='127.0.0.1')
        search = get_search_mock(query=operation, pageno=1)
        result = self.store.call(self.store.plugins, 'post_search', request, search)
        self.assertTrue(result)
        self.assertNotIn('calculate', search.result_container.answers)
