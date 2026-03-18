london = {
    'id': 1,
    'capitals': [],
    'it_vlan': [],
    'user_vlan': 1010,
    'mngmt_vlan': 99,
    'to_name': None,
    'to_id': None,
    'port': 'G1/0/11'
}


def create_london():
    capitals = ['Paris', 'Moscow', 'Berlin', 'Budapest', 'Nigeria']
    for capital in capitals:
        london['capitals'].append(capital)

    it_vlan = list(range(1, 11))
    for vlan in it_vlan:
        london['it_vlan'].append(vlan)

    return london


london = create_london()



def get_london(cities_list):
    new_london = {'id': 1, 'capitals': [], 'it_vlan': []}

    for city in cities_list:
        new_london['capitals'].append(city)

    new_london['it_vlan'] = list(range(1, 11))

    return new_london


def test_capitals():
    updated_london = get_london(['Paris', 'Moscow'])
    assert len(updated_london['capitals']) == 2, f"Количество столиц должно быть {len(['Paris', 'Moscow'])}"
    assert 'Paris' in updated_london['capitals']


def test_it_vlan():
    updated_london = get_london([])
    assert len(updated_london['it_vlan']) == 10
    assert updated_london['it_vlan'][0] == 1 and updated_london['it_vlan'][-1] == 10


def test_empty_cities():
    empty_london = get_london([])
    assert len(empty_london['capitals']) == 0
    assert empty_london['it_vlan'] == list(range(1, 11))


if __name__ == "__main__":
    test_capitals()
    test_it_vlan()
    test_empty_cities()
