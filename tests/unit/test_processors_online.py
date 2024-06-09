# SPDX-License-Identifier: AGPL-3.0-or-later
# pylint: disable=missing-module-docstring
from __future__ import annotations

from typing import Callable
from searx.engines import engines
from searx.enginelib import Engine
from tests import SearxTestCase
from unittest import mock
from unittest.mock import Mock
from searx.search import SearchQuery, EngineRef
from searx.search.processors import online


class TestProcessorOnline(SearxTestCase):  # pylint: disable=missing-class-docstring
    TEST_ENGINE_NAME = 'engine1'

    @classmethod
    def tearDownClass(cls) -> None:
        engines.pop(cls.TEST_ENGINE_NAME, None)
        return

    @classmethod
    def setUpClass(cls) -> None:
        # Setup mock engine information to instantiate processors
        cls.engine_mock = Mock(spec=Engine)
        cls.engine_mock.name = cls.TEST_ENGINE_NAME
        cls.engine_mock.logger = mock.DEFAULT
        cls.engine_mock.logger.debug = Mock(spec=Callable)
        cls.engine_mock.max_page = 1
        cls.engine_mock.send_accept_language_header = mock.DEFAULT
        cls.engine_mock.debug = mock.DEFAULT
        engines[cls.TEST_ENGINE_NAME] = cls.engine_mock
        return

    def test_get_params_default_params(self):
        online_processor = online.OnlineProcessor(self.engine_mock, self.TEST_ENGINE_NAME)
        search_query = SearchQuery('test', [EngineRef(self.TEST_ENGINE_NAME, 'general')], 'all', 0, 1, None, None, None)
        params = online_processor.get_params(search_query, 'general')
        self.assertIsNotNone(params)
        assert params is not None
        self.assertIn('method', params)
        self.assertIn('headers', params)
        self.assertIn('data', params)
        self.assertIn('url', params)
        self.assertIn('cookies', params)
        self.assertIn('auth', params)

    def test_get_params_has_gen_useragent(self):
        online_processor = online.OnlineProcessor(self.engine_mock, self.TEST_ENGINE_NAME)
        search_query = SearchQuery('test', [EngineRef(self.TEST_ENGINE_NAME, 'general')], 'all', 0, 1, None, None, None)
        params = online_processor.get_params(search_query, 'general')
        self.assertIsNotNone(params)
        assert params is not None
        self.assertIn('User-Agent', params['headers'])
        useragent = params['headers']['User-Agent']
        self.assertNotEqual(None, useragent)
        self.assertNotEqual("", useragent)
