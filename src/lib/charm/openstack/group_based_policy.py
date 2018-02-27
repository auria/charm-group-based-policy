import socket
import subprocess

import charmhelpers.core.hookenv as hookenv
import charmhelpers.contrib.network.ip as ch_ip
import charms_openstack.charm
# import charms_openstack.sdn.odl as odl
# import charms_openstack.sdn.ovs as ovs


class GroupBasedPolicyCharm(charms_openstack.charm.OpenStackCharm):

    # Internal name of charm
    service_name = name = 'group-based-policy'

    # First release supported
    release = 'mitaka'

    # List of packages to install for this charm
    packages = ["group-based-policy"]
