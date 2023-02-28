import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_myst_is_installed(host):
    myst = host.package("myst")
    assert myst.is_installed


@pytest.mark.parametrize('port', [
    "4449"
])
def test_ports_is_listening(host, port):
    socket = host.socket("tcp://127.0.0.1:" + port)

    assert socket.is_listening
