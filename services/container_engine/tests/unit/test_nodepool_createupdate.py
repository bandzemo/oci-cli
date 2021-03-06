# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestNodePoolCreateUpdate(unittest.TestCase):
    def setUp(self):
        pass

    def test_nodepool_create(self):
        result = util.invoke_command(['ce', 'node-pool', 'create', '--size', '1', '--placement-configs', 'config'])
        assert 'Error: Missing option(s)' in result.output

    def test_nodepool_update(self):
        result = util.invoke_command(['ce', 'node-pool', 'update', '--size', '1', '--placement-configs', 'config'])
        assert 'Error: Missing option(s) --node-pool-id.' in result.output

    def test_nodepool_create_via_imageId(self):
        result = util.invoke_command(['ce', 'node-pool', 'create', '--node-image-id', 'id'])
        assert 'Error: Missing option(s)' in result.output
