expected_output = {
    'mac_table':{
        'vlans':{
            '2000':{
                'vlan':2000,
                'mac_addresses':{
                    '000c.290e.8a72':{
                        'mac_address':'000c.290e.8a72',
                        'interfaces':{
                            'GigabitEthernet4/0/3':{
                                'interface':'GigabitEthernet4/0/3',
                                'entry_type':'static'
                            }
                        }
                    },
                    'd824.bdbb.b7f9':{
                        'mac_address':'d824.bdbb.b7f9',
                        'interfaces':{
                            'GigabitEthernet4/0/3':{
                                'interface':'GigabitEthernet4/0/3',
                                'entry_type':'static'
                            }
                        }
                    }
                }
            },
            '4003':{
                'vlan':4003,
                'mac_addresses':{
                    'd824.bdbb.b7f9':{
                        'mac_address':'d824.bdbb.b7f9',
                        'drop':{
                            'drop':True,
                            'entry_type':'dynamic'
                        }
                    }
                }
            }
        }
    },
    'total_mac_addresses':3
}
