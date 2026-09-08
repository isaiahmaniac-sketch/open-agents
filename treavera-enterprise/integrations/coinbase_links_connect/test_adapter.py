"""Adversarial regression tests for the Coinbase APEX boundary."""
from __future__ import annotations

import pytest

from adapter import Authority, CoinbaseLinksConnectAdapter, EmergencyStop, PolicyDenied


class FakeCoinbase:
    def __init__(self) -> None:
        self.transfers = 0

    def get_wallet_details(self):
        return {"id": "w1", "address": "0xabc", "network": "base", "secret": "must-not-leak"}

    def get_balance(self, asset_id=None):
        return {"asset_id": asset_id or "ETH", "balance": "1"}


def test_transfer_method_does_not_exist():
    adapter = CoinbaseLinksConnectAdapter(FakeCoinbase())
    assert not hasattr(adapter, "native_transfer")


def test_prepare_transfer_is_non_executable():
    adapter = CoinbaseLinksConnectAdapter(FakeCoinbase())
    intent, _ = adapter.prepare_native_transfer(
        Authority("prepare_native_transfer", "prepare", "base"), "1", "ETH", "0xdestination"
    )
    assert intent["executable"] is False
    assert intent["status"] == "PREPARED_ONLY"


def test_raw_provider_fields_are_not_returned():
    adapter = CoinbaseLinksConnectAdapter(FakeCoinbase())
    result, _ = adapter.wallet_details(Authority("get_wallet_details", "read"))
    assert "secret" not in result
    assert set(result) == {"provider", "wallet_id", "address", "network"}


def test_emergency_stop_blocks_operations():
    stop = EmergencyStop()
    stop.stop()
    adapter = CoinbaseLinksConnectAdapter(FakeCoinbase(), stop)
    with pytest.raises(PolicyDenied):
        adapter.balance(Authority("get_balance", "read"))


def test_wrong_mode_or_operation_is_denied():
    adapter = CoinbaseLinksConnectAdapter(FakeCoinbase())
    with pytest.raises(PolicyDenied):
        adapter.prepare_native_transfer(Authority("get_balance", "read"), "1", "ETH", "0xabc")
