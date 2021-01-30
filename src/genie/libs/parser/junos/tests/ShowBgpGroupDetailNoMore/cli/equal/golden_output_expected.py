expected_output = {
    "bgp-group-information": {
        "bgp-group": [{
            "bgp-option-information": {
                "bgp-options": "Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy": "(v4_WATARI && NEXT-HOP-SELF)",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "bgp-rib": [{
                "accepted-prefix-count": "682",
                "active-prefix-count": "0",
                "advertised-prefix-count": "682",
                "name": "inet.0",
                "received-prefix-count": "682",
                "suppressed-prefix-count": "0"
            }],
            "established-count":
            "1",
            "group-flags":
            "Export Eval",
            "group-index":
            "0",
            "local-as":
            "65171",
            "name":
            "Genie",
            "peer-address": ["10.189.5.253+179"],
            "peer-as":
            "65171",
            "peer-count":
            "1",
            "route-queue": {
                "state": "empty",
                "timer": "unset"
            },
            "type":
            "Internal"
        }, {
            "bgp-option-information": {
                "bgp-options": "Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy": "(v6_WATARI && NEXT-HOP-SELF)",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "bgp-rib": [{
                "accepted-prefix-count": "0",
                "active-prefix-count": "0",
                "advertised-prefix-count": "0",
                "name": "inet6.0",
                "received-prefix-count": "0",
                "suppressed-prefix-count": "0"
            }],
            "established-count":
            "1",
            "group-flags":
            "Export Eval",
            "group-index":
            "1",
            "local-as":
            "65171",
            "name":
            "v6_Genie",
            "peer-address": ["2001:db8:223c:ca45::c+60268"],
            "peer-as":
            "65171",
            "peer-count":
            "1",
            "route-queue": {
                "state": "empty",
                "timer": "unset"
            },
            "type":
            "Internal"
        }, {
            "bgp-option-information": {
                "bgp-options": "Cluster Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy": "(ALL_out && v4_NEXT-HOP-SELF_hktGCS001)",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "established-count":
            "0",
            "group-flags":
            "Export Eval",
            "group-index":
            "2",
            "local-as":
            "65171",
            "name":
            "v4_RRC_72_TRIANGLE",
            "peer-address":
            ["10.189.5.245", "10.189.5.243", "10.189.5.242+179"],
            "peer-as":
            "65171",
            "peer-count":
            "3",
            "type":
            "Internal"
        }, {
            "bgp-option-information": {
                "bgp-options": "Cluster Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy": "(ALL_out && v6_NEXT-HOP-SELF_hktGCS001)",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "established-count":
            "0",
            "group-flags":
            "Export Eval",
            "group-index":
            "3",
            "local-as":
            "65171",
            "name":
            "v6_RRC_72_TRIANGLE",
            "peer-address":
            ["2001:db8:223c:ca45::7+179", "2001:db8:223c:ca45::8+179"],
            "peer-as":
            "65171",
            "peer-count":
            "2",
            "type":
            "Internal"
        }, {
            "bgp-option-information": {
                "bgp-options": "Cluster Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy": "ALL_out",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "established-count":
            "0",
            "group-flags":
            "Export Eval",
            "group-index":
            "4",
            "local-as":
            "65171",
            "name":
            "v6_RRC_72_SQUARE",
            "peer-address":
            ["2001:db8:223c:ca45::9", "2001:db8:223c:ca45::a+179"],
            "peer-as":
            "65171",
            "peer-count":
            "2",
            "type":
            "Internal"
        }, {
            "bgp-option-information": {
                "bgp-options": "Cluster Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy": "ALL_out",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "established-count": "0",
            "group-flags": "Export Eval",
            "group-index": "5",
            "local-as": "65171",
            "name": "v4_RRC_72_SQUARE",
            "peer-address": ["10.189.5.241+179", "10.189.5.240"],
            "peer-as": "65171",
            "peer-count": "2",
            "type": "Internal"
        }, {
            "bgp-option-information": {
                "bgp-options": "Cluster Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy": "v4_Kentik_NO-DEFAULT",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "established-count": "0",
            "group-flags": "Export Eval",
            "group-index": "6",
            "local-as": "65171",
            "name": "v4_Kentik",
            "peer-address": ["10.49.216.179"],
            "peer-as": "65171",
            "peer-count": "1",
            "type": "Internal"
        }, {
            "bgp-option-information": {
                "bgp-options": "Cluster Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy": "v6_Kentik_NO-DEFAULT",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "established-count": "0",
            "group-flags": "Export Eval",
            "group-index": "7",
            "local-as": "65171",
            "name": "v6_Kentik",
            "peer-address": ["2001:db8:6be:89bb::1:140"],
            "peer-as": "65171",
            "peer-count": "1",
            "type": "Internal"
        }, {
            "bgp-option-information": {
                "bgp-options": "Multihop Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy":
                "(ALL_out && (NEXT-HOP-SELF && HKG-SNG_AddMED))",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "established-count": "0",
            "group-flags": "Export Eval",
            "group-index": "8",
            "local-as": "65171",
            "name": "sggjbb001",
            "peer-address": ["10.189.6.250"],
            "peer-count": "1",
            "type": "External"
        }, {
            "bgp-option-information": {
                "bgp-options": "Multihop Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy":
                "(ALL_out && (NEXT-HOP-SELF && v6_HKG-SNG_AddMED))",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "established-count": "0",
            "group-flags": "Export Eval",
            "group-index": "9",
            "local-as": "65171",
            "name": "v6_sggjbb001",
            "peer-address": ["2001:db8:5961:ca45::1"],
            "peer-count": "1",
            "type": "External"
        }, {
            "bgp-option-information": {
                "bgp-options": "Multihop Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy":
                "((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED))",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "bgp-rib": [{
                "accepted-prefix-count": "684",
                "active-prefix-count": "682",
                "advertised-prefix-count": "0",
                "name": "inet.0",
                "received-prefix-count": "684",
                "suppressed-prefix-count": "0"
            }, {
                "accepted-prefix-count": "2",
                "active-prefix-count": "2",
                "advertised-prefix-count": "0",
                "name": "inet.3",
                "received-prefix-count": "2",
                "suppressed-prefix-count": "0"
            }],
            "established-count":
            "1",
            "group-flags":
            "Export Eval",
            "group-index":
            "10",
            "local-as":
            "65171",
            "name":
            "sjkGCS001-EC11",
            "peer-address": ["10.169.14.240+60606"],
            "peer-count":
            "1",
            "route-queue": {
                "state": "empty",
                "timer": "unset"
            },
            "type":
            "External"
        }, {
            "bgp-option-information": {
                "bgp-options": "Multihop Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy":
                "(v6_HKG-EC_out && (NEXT-HOP-SELF && v6_HKG-EC_AddMED))",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "bgp-rib": [{
                "accepted-prefix-count": "0",
                "active-prefix-count": "0",
                "advertised-prefix-count": "0",
                "name": "inet6.0",
                "received-prefix-count": "0",
                "suppressed-prefix-count": "0"
            }],
            "established-count":
            "1",
            "group-flags":
            "Export Eval",
            "group-index":
            "11",
            "local-as":
            "65171",
            "name":
            "v6_sjkGCS001-EC11",
            "peer-address": ["2001:db8:eb18:ca45::1+179"],
            "peer-count":
            "1",
            "route-queue": {
                "state": "empty",
                "timer": "unset"
            },
            "type":
            "External"
        }, {
            "bgp-option-information": {
                "bgp-options": "Multihop Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy":
                "(HKG-WC_out && (NEXT-HOP-SELF && HKG-WC_AddMED))",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "established-count": "0",
            "group-flags": "Export Eval",
            "group-index": "12",
            "local-as": "65171",
            "name": "obpGCS001-WC11",
            "peer-address": ["10.169.14.249"],
            "peer-count": "1",
            "type": "External"
        }, {
            "bgp-option-information": {
                "bgp-options": "Multihop Confed",
                "bgp-options-extended": "GracefulShutdownRcv",
                "export-policy":
                "(v6_HKG-WC_out && (NEXT-HOP-SELF && v6_HKG-WC_AddMED))",
                "gshut-recv-local-preference": "0",
                "holdtime": "0"
            },
            "established-count": "0",
            "group-flags": "Export Eval",
            "group-index": "13",
            "local-as": "65171",
            "name": "v6_obpGCS001-WC11",
            "peer-address": ["2001:db8:eb18:ca45::11"],
            "peer-count": "1",
            "type": "External"
        }],
        "bgp-information": {
            "bgp-rib": [{
                "accepted-prefix-count": "1366",
                "active-external-prefix-count": "682",
                "active-internal-prefix-count": "0",
                "active-prefix-count": "682",
                "bgp-rib-state": "BGP restart is complete",
                "name": "inet.0",
                "received-prefix-count": "1366",
                "suppressed-external-prefix-count": "0",
                "suppressed-internal-prefix-count": "0",
                "suppressed-prefix-count": "0",
                "total-external-prefix-count": "684",
                "total-internal-prefix-count": "682"
            }, {
                "accepted-prefix-count": "2",
                "active-external-prefix-count": "2",
                "active-internal-prefix-count": "0",
                "active-prefix-count": "2",
                "bgp-rib-state": "BGP restart is complete",
                "name": "inet.3",
                "received-prefix-count": "2",
                "suppressed-external-prefix-count": "0",
                "suppressed-internal-prefix-count": "0",
                "suppressed-prefix-count": "0",
                "total-external-prefix-count": "2",
                "total-internal-prefix-count": "0"
            }, {
                "accepted-prefix-count": "0",
                "active-external-prefix-count": "0",
                "active-internal-prefix-count": "0",
                "active-prefix-count": "0",
                "bgp-rib-state": "BGP restart is complete",
                "name": "inet6.0",
                "received-prefix-count": "0",
                "suppressed-external-prefix-count": "0",
                "suppressed-internal-prefix-count": "0",
                "suppressed-prefix-count": "0",
                "total-external-prefix-count": "0",
                "total-internal-prefix-count": "0"
            }],
            "down-peer-count":
            "15",
            "external-peer-count":
            "6",
            "flap-count":
            "359",
            "group-count":
            "14",
            "internal-peer-count":
            "13",
            "peer-count":
            "19"
        }
    }
}
