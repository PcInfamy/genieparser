# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ldp import (
    ShowLDPSession, ShowLDPOverview)

# =================================
# Unit test for 'show ldp session'
# =================================


class TestShowLDPSession(unittest.TestCase):
    '''unit test for "show ldp session'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'ldp-session-information': {
            'ldp-session': [{
                'ldp-neighbor-address': '59.128.2.250',
                'ldp-session-state': 'Operational',
                'ldp-connection-state': 'Open',
                'ldp-remaining-time': '26',
                'ldp-session-adv-mode': 'DU'
            }]
        }
    }

    golden_output = {
        'execute.return_value':
        '''
          Address                           State       Connection  Hold time  Adv. Mode
        59.128.2.250                        Operational Open          26         DU
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

# =================================
# Unit test for 'show ldp overview'
# =================================


class TestShowLDPOverview(unittest.TestCase):
    '''unit test for "show ldp overview'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ldp overview
        Instance: master
        Reference count: 2
        Router ID: 106.187.14.240
        LDP inet: enabled
        Transport preference: IPv4
        Message id: 4
        Configuration sequence: 1
        Deaggregate: disabled
        Explicit null: disabled
        IPv6 tunneling: disabled
        Strict targeted hellos: disabled
        Loopback if added: no
        Route preference: 9
        Unicast transit LSP chaining: disabled
        P2MP transit LSP chaining: disabled
        Transit LSP statistics based on route statistics: disabled
        LDP route acknowledgement: enabled
        BGP export: enabled
        LDP mtu discovery: disabled
        LDP SR Mapping Client: disabled
        Capabilities enabled: none
        Egress FEC capabilities enabled: entropy-label-capability
        Downstream unsolicited Sessions:
            Operational: 1
            Retention: liberal
            Control: ordered
        Auto targeted sessions:
            Auto targeted: disabled
            Dynamic tunnel session count: 0
        P2MP:
            Recursive route: disabled
            No rsvp tunneling: disabled
        Timers:
            Keepalive interval: 10, Keepalive timeout: 30
            Link hello interval: 5, Link hello hold time: 15
            Targeted hello interval: 15, Targeted hello hold time: 45
            Label withdraw delay: 60, Make before break timeout: 30
            Make before break switchover delay: 3
            Link protection timeout: 120
        Graceful restart:
            Restart: disabled, Helper: enabled, Restart in process: false
            Reconnect time: 60000, Max neighbor reconnect time: 120000
            Recovery time: 160000, Max neighbor recovery time: 240000
        Traffic Engineering:
            Bgp igp: disabled
            Both ribs: disabled
            Mpls forwarding: disabled
        IGP:
            Tracking igp metric: disabled
            Sync session up delay: 10
        Session protection:
            Session protection: disabled
            Session protection timeout: 0
        Interface addresses advertising:
            106.187.14.157
        LDP Job:
            Read job time quantum: 1000, Write job time quantum: 1000
            Read job loop quantum: 100, Write job loop quantum: 100
            Backup inbound read job time quantum: 1000, Backup outbound read job time quantum: 1000
            Backup inbound read job loop quantum: 100, Backup outbound read job loop quantum: 100
        Label allocation:
            Current number of LDP labels allocated: 1
            Total number of LDP labels allocated: 1
            Total number of LDP labels freed: 0
            Total number of LDP label allocation failure: 0
            Current number of labels allocated by all protocols: 0
    '''}

    golden_parsed_output = {
        'ldp-overview-information': {
            'ldp-overview': {
                'ldp-auto-targeted-session': {
                    'ldp-auto-targeted-dyn-tun-ses-count': 0,
                    'ldp-auto-targeted-session-enabled': 'disabled'
                },
                'ldp-bgp-export': 'enabled',
                'ldp-configuration-sequence': 1,
                'ldp-deaggregate': 'disabled',
                'ldp-explicit-null': 'disabled',
                'ldp-gr-overview': {
                    'ldp-gr-helper': 'enabled',
                    'ldp-gr-max-neighbor-reconnect-time': 120000,
                    'ldp-gr-max-neighbor-recovery-time': 240000,
                    'ldp-gr-reconnect-time': 60000,
                    'ldp-gr-recovery-time': 160000,
                    'ldp-gr-restart': 'disabled',
                    'ldp-gr-restarting': 'false'
                },
                'ldp-igp-overview': {
                    'ldp-igp-sync-session-up-delay': 10,
                    'ldp-tracking-igp-metric': 'disabled'
                },
                'ldp-inet': 'enabled',
                'ldp-instance-capability': {
                    'ldp-capability': 'none'
                },
                'ldp-instance-egress-fec-capability': {
                    'ldp-egress-fec-capability': 'entropy-label-capability'
                },
                'ldp-instance-name': 'master',
                'ldp-interface-address': {
                    'interface-address': '106.187.14.157'
                },
                'ldp-ipv6-tunneling': 'disabled',
                'ldp-job-overview': {
                    'ldp-inbound-read-job-loop-quantum': 100,
                    'ldp-inbound-read-job-time-quantum': 1000,
                    'ldp-outbound-read-job-loop-quantum': 100,
                    'ldp-outbound-read-job-time-quantum': 1000,
                    'ldp-read-job-loop-quantum': 100,
                    'ldp-read-job-time-quantum': 1000,
                    'ldp-write-job-loop-quantum': 100,
                    'ldp-write-job-time-quantum': 1000
                },
                'ldp-label-allocation': {
                    'ldp-global-label-current-allocs': 0,
                    'ldp-label-alloc-failure': 0,
                    'ldp-label-current-allocs': 1,
                    'ldp-label-total-allocs': 1,
                    'ldp-label-total-frees': 0
                },
                'ldp-loopback-if-added': 'no',
                'ldp-message-id': 4,
                'ldp-mtu-discovery': 'disabled',
                'ldp-p2mp': {
                    'ldp-p2mp-no-rsvp-tunneling-enabled': 'disabled',
                    'ldp-p2mp-recursive-route-enabled': 'disabled'
                },
                'ldp-p2mp-transit-lsp-chaining': 'disabled',
                'ldp-reference-count': 2,
                'ldp-route-acknowledgement': 'enabled',
                'ldp-route-preference': 9,
                'ldp-router-id': '106.187.14.240',
                'ldp-session-count': {
                    'ldp-control-mode': 'ordered',
                    'ldp-retention-mode': 'liberal',
                    'ldp-session-operational': 1
                },
                'ldp-session-protect-overview': {
                    'ldp-session-protect': 'disabled',
                    'ldp-session-protect-timeout': 0
                },
                'ldp-sr-mapping-client': 'disabled',
                'ldp-strict-targeted-hellos': 'disabled',
                'ldp-te-overview': {
                    'ldp-te-bgp-igp': 'disabled',
                    'ldp-te-both-ribs': 'disabled',
                    'ldp-te-mpls-forwarding': 'disabled'
                },
                'ldp-timer-overview': {
                    'ldp-instance-keepalive-interval': 10,
                    'ldp-instance-keepalive-timeout': 30,
                    'ldp-instance-label-withdraw-delay': 60,
                    'ldp-instance-link-hello-hold-time': 15,
                    'ldp-instance-link-hello-interval': 5,
                    'ldp-instance-link-protection-timeout': 120,
                    'ldp-instance-make-before-break-switchover-delay': 3,
                    'ldp-instance-make-before-break-timeout': 30,
                    'ldp-instance-targeted-hello-hold-time': 45,
                    'ldp-instance-targeted-hello-interval': 15
                },
                'ldp-transit-lsp-route-stats': 'disabled',
                'ldp-transport-preference': 'IPv4',
                'ldp-unicast-transit-lsp-chaining': 'disabled'
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPOverview(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPOverview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
