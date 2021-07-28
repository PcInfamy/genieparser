expected_output = {
    'summary': {
        'total_shmwin_usage': 984,
        '1': {'virtual_mem_range_end': '0xb0000000',
              'virtual_mem_range_start': '0x50000000',
              'virtual_mem_size': 1536
              },
    },
    'windows': {
        0: {'window_name': 'subdb_sco_tbl',
            'group': '1',
            'id': 70,
            'num_users': 1,
            'num_writers': 1,
            'owner': '159',
            'peak': 0,
            'peak_date': '',
            'peak_time': '',
            'usage': 3},
        1: {'window_name': 'subsession_db',
            'group': '1',
            'id': 81,
            'num_users': 2,
            'num_writers': 2,
            'owner': '0',
            'peak': 9859,
            'peak_date': '03/21/2021',
            'peak_time': '21:13:51',
            'usage': 9859},
        2: {'window_name': 'ifo_ea_shm',
            'group': 'P',
            'id': 130,
            'num_users': 1,
            'num_writers': 1,
            'owner': '0',
            'peak': 2795,
            'peak_date': '03/18/2021',
            'peak_time': '02:09:01',
            'usage': 1234},
    }
}


