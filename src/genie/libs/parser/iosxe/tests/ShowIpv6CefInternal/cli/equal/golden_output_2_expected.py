expected_output = {
   'vrf':{
      'default':{
         'address_family':{
            'ipv6':{
               'prefix':{
                  '::/0':{
                     'epoch':0,
                     'flags':[
                        'DefRtHndlr',
                        'defrt'
                     ],
                     'output_chain':{
                        
                     },
                     'path_list':{
                        '7FCDF9805F40':{
                           'flags':'0x41 [shble, hwcn]',
                           'locks':4,
                           'path':{
                              '7FCDF98063E8':{
                                 'for':'IPv6',
                                 'share':'1/1',
                                 'type':'special prefix'
                              }
                           },
                           'sharing':'per-destination'
                        }
                     },
                     'refcnt':4,
                     'sharing':'per-destination',
                     'sources':[
                        'DRH'
                     ]
                  },
                  '::/127':{
                     'epoch':0,
                     'feature_space':{
                        'iprm':'0x00038002'
                     },
                     'flags':[
                        'att',
                        'dscrd'
                     ],
                     'output_chain':{
                        
                     },
                     'path_list':{
                        '7FCDF84DDDA8':{
                           'flags':'0x41 [shble, hwcn]',
                           'locks':7,
                           'path':{
                              '7FCDF84DE868':{
                                 'for':'IPv6',
                                 'share':'1/1',
                                 'type':'special prefix'
                              }
                           },
                           'sharing':'per-destination'
                        }
                     },
                     'refcnt':4,
                     'rib':'[C]',
                     'sharing':'per-destination',
                     'sources':[
                        'RIB'
                     ]
                  },
                  'FE80::/10':{
                     'epoch':0,
                     'feature_space':{
                        'iprm':'0x00038002'
                     },
                     'flags':[
                        'att',
                        'rcv',
                        'local'
                     ],
                     'output_chain':{
                        
                     },
                     'path_list':{
                        '7FCDF84DDCF8':{
                           'flags':'0x41 [shble, hwcn]',
                           'locks':10,
                           'path':{
                              '7FCDF84DE798':{
                                 'for':'IPv6',
                                 'share':'1/1',
                                 'type':'receive'
                              }
                           },
                           'sharing':'per-destination'
                        }
                     },
                     'refcnt':4,
                     'rib':'[C]',
                     'sharing':'per-destination',
                     'sources':[
                        'RIB'
                     ]
                  },
                  'FF00::/8':{
                     'epoch':0,
                     'feature_space':{
                        'iprm':'0x00038002'
                     },
                     'output_chain':{
                        
                     },
                     'path_list':{
                        '7FCDF84DDB98':{
                           'flags':'0x42 [nonsh, hwcn]',
                           'locks':2,
                           'path':{
                              '7FCDF84DE5F8':{
                                 'for':'IPv6',
                                 'share':'1/1',
                                 'type':'special prefix'
                              }
                           },
                           'sharing':'per-destination'
                        }
                     },
                     'refcnt':4,
                     'rib':'[C]',
                     'sharing':'per-destination',
                     'sources':[
                        'Spc,',
                        'RIB'
                     ]
                  }
               }
            }
         }
      }
   }
}