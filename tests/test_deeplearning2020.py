#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `deeplearning2020` package."""

import unittest.mock

import keras

from deeplearning2020 import Submission


def test_construction() -> None:
    with unittest.mock.patch(
        "kerasltisubmission.LTIProvider", autospec=True
    ) as mocked_provider:
        mock_provider = unittest.mock.MagicMock()
        mock_submit = unittest.mock.MagicMock()
        mock_provider.submit = mock_submit

        mocked_provider.return_value = mock_provider

        model = unittest.mock.MagicMock(spec=keras.Model)
        Submission(user_token="12", assignment_id=2, model=model).submit()

        mocked_provider.assert_called_with(
            input_api_endpoint="https://neuralnet.xopic.de/ltiprovider",
            submission_api_endpoint="https://neuralnet.xopic.de/ltiprovider/submit",
            user_token="12",
        )

        assert len(mock_submit.call_args_list) == 1
        args, kwargs = mock_submit.call_args_list[0]
        assert args[0].assignment_id == 2
        assert args[0].model == model


def test_ignores_exceptions() -> None:
    with unittest.mock.patch(
        "kerasltisubmission.LTIProvider.submit", autospec=True
    ) as mocked_submit:
        mocked_submit.side_effect = ValueError("Something went wrong")
        model = unittest.mock.MagicMock(spec=keras.Model)
        Submission(user_token="12", assignment_id=2, model=model).submit()
