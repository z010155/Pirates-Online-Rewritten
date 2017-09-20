from pandac.PandaModules import Point3, VBase3, Vec4, Vec3
objectStruct = {
    'Interact Links': [
        ['1179265920.0dxschafe3', '1179266176.0dxschafe0', 'Bi-directional'],
        ['1179266048.0dxschafe1', '1179265920.0dxschafe4', 'Bi-directional'],
        ['1179265920.0dxschafe5', '1179266048.0dxschafe0', 'Bi-directional'],
        ['1179266176.0dxschafe', '1179265920.0dxschafe', 'Bi-directional'],
        ['1179266048.0dxschafe3', '1179266048.0dxschafe2', 'Bi-directional']
    ],
    'Locator Links': [
        ['1172208953.19sdnaik', '1172172361.37kmuller', 'Bi-directional'],
        ['1172208953.17sdnaik', '1172209006.14sdnaik', 'Bi-directional']
    ],
    'Objects': {
        '1164135492.81dzlu': {
            'Type': 'Island',
            'Name': "Devil's Anvil",
            'File': '',
            'AdditionalData': ['WildIslandC'],
            'Environment': 'OpenSky',
            'Minimap': False,
            'Objects': {
                '1164766305.45sdnaik': {
                    'Type': 'Player Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Index': -1,
                    'Pos': Point3(383.541, 187.297, 25.49),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'Visual': {
                        'Model': 'models/misc/smiley'
                    }
                },
                '1168745928.39WDIG': {
                    'Type': 'Port Collision Sphere',
                    'Name': 'DevilsAnvilPort',
                    'Hpr': VBase3(0.0, 0.0, 0.0),
                    'Pos': Point3(141.014, -36.03, 0.0),
                    'Scale': VBase3(1435.579, 1435.579, 1435.579),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.5, 0.5, 1.0, 0.2),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1172172361.37kmuller': {
                    'Type': 'Locator Node',
                    'Name': 'portal_exterior_1',
                    'Hpr': VBase3(62.291, 0.0, 0.0),
                    'Pos': Point3(138.788, 208.05, 26.94),
                    'Scale': VBase3(1.0, 1.0, 1.0)
                },
                '1172208953.16sdnaik': {
                    'Type': 'Connector Tunnel',
                    'File': '',
                    'Hpr': VBase3(149.405, 0.0, 0.0),
                    'Objects': {
                        '1172208953.17sdnaik': {
                            'Type': 'Locator Node',
                            'Name': 'portal_connector_1',
                            'GridPos': Point3(359.595, 418.268, 14.54),
                            'Hpr': VBase3(90.0, 0.0, 0.0),
                            'Pos': Point3(95.197, 150.0, 0.0),
                            'Scale': VBase3(1.0, 1.0, 1.0)
                        },
                        '1172208953.19sdnaik': {
                            'Type': 'Locator Node',
                            'Name': 'portal_connector_2',
                            'GridPos': Point3(264.398, 271.529, 14.54),
                            'Hpr': VBase3(-90.0, 0.0, 0.0),
                            'Pos': Point3(8.658, 3.262, 0.0),
                            'Scale': VBase3(1.0, 1.0, 1.0)
                        }
                    },
                    'Pos': Point3(264.398, 268.268, 796.747),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/tunnels/pir_m_are_tun_cave'
                    }
                },
                '1172209006.11sdnaik': {
                    'Type': 'Island Game Area',
                    'File': 'anvil_island_area_barbossa_cave',
                    'Hpr': VBase3(44.069, 0.0, 0.0),
                    'Objects': {
                        '1172209006.14sdnaik': {
                            'Type': 'Locator Node',
                            'Name': 'portal_interior_1',
                            'GridPos': Point3(-189.152, -270.01, 621.081),
                            'Hpr': VBase3(95.675, 0.0, 0.0),
                            'Pos': Point3(85.919, -190.083, 24.757),
                            'Scale': VBase3(1.0, 1.0, 1.0)
                        }
                    },
                    'Pos': Point3(-1041.043, -125.656, 784.758),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/caves/pir_m_are_cav_barbossa'
                    }
                },
                '1179265792.0dxschafe0': {
                    'Type': 'Player Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Index': -1,
                    'Pos': Point3(92.182, 322.044, 14.274),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'Visual': {
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179265792.0dxschafe1': {
                    'Type': 'Player Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Index': -1,
                    'Pos': Point3(484.566, -152.122, 24.766),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'Visual': {
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179265792.0dxschafe2': {
                    'Type': 'Player Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Index': -1,
                    'Pos': Point3(274.556, -338.71, 19.625),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'Visual': {
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179265792.0dxschafe3': {
                    'Type': 'Player Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Index': -1,
                    'Pos': Point3(-39.93, -416.502, 17.591),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'VisSize': '',
                    'Visual': {
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179265920.0dxschafe': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(599.676, -99.293, 14.865),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T1',
                    'Start State': 'Ambush',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179265920.0dxschafe0': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(525.573, -246.82, 19.678),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T0',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179265920.0dxschafe1': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(475.158, 185.339, 17.029),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179265920.0dxschafe2': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(103.481, -443.445, 14.221),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T0',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179265920.0dxschafe3': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(-70.548, -470.441, 10.584),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T1',
                    'Start State': 'Ambush',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179265920.0dxschafe4': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(-191.895, -361.723, 10.601),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T3',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179265920.0dxschafe5': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(255.868, -260.416, 26.309),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Scorp T1',
                    'Start State': 'Ambush',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179266048.0dxschafe': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(146.583, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(-2.71, -313.549, 25.759),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Scorp T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179266048.0dxschafe0': {
                    'Type': 'Object Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(198.651, -280.033, 26.229),
                    'Priority': '1',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'SpawnDelay': '20',
                    'Spawnables': 'Buried Treasure',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.8, 0.2, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    },
                    'startingDepth': '12'
                },
                '1179266048.0dxschafe1': {
                    'Type': 'Object Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-120.407, -308.577, 22.002),
                    'Priority': '1',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'SpawnDelay': '20',
                    'Spawnables': 'Buried Treasure',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.8, 0.2, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    },
                    'startingDepth': '12'
                },
                '1179266048.0dxschafe2': {
                    'Type': 'Object Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-51.641, 316.748, 13.308),
                    'Priority': '1',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'SpawnDelay': '20',
                    'Spawnables': 'Buried Treasure',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.8, 0.2, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    },
                    'startingDepth': '12'
                },
                '1179266048.0dxschafe3': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(-34.752, 372.583, 6.103),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T3',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1179266176.0dxschafe': {
                    'Type': 'Object Spawn Node',
                    'Hpr': VBase3(0.0, 0.0, 8.13),
                    'Pos': Point3(594.806, -37.041, 13.963),
                    'Priority': '1',
                    'Scale': VBase3(0.926, 0.926, 0.926),
                    'SpawnDelay': '20',
                    'Spawnables': 'Buried Treasure',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.8, 0.2, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    },
                    'startingDepth': '12'
                },
                '1179266176.0dxschafe0': {
                    'Type': 'Object Spawn Node',
                    'Hpr': VBase3(0.0, 4.0, 0.0),
                    'Pos': Point3(-112.953, -473.594, 8.516),
                    'Priority': '1',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'SpawnDelay': '20',
                    'Spawnables': 'Buried Treasure',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.8, 0.2, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    },
                    'startingDepth': '12'
                },
                '1179288192.0JB0': {
                    'Type': 'Player Boot Node',
                    'AreaUid': '1172208953.16sdnaik',
                    'Hpr': VBase3(-26.706, 0.0, 0.0),
                    'Pos': Point3(156.168, 233.226, 24.553),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.5, 1.0, 0.5, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1184890880.0dxschafe0': {
                    'Type': 'Locator Node',
                    'Name': 'portal_exterior_2',
                    'Hpr': VBase3(-88.249, 0.0, 0.0),
                    'Pos': Point3(111.24, -257.791, 26.94),
                    'Scale': VBase3(1.0, 1.0, 1.0)
                },
                '1184890880.0dxschafe1': {
                    'Type': 'Dinghy',
                    'Aggro Radius': '20.0000',
                    'Hpr': VBase3(-61.301, -3.389, 0.0),
                    'Location': 'Water',
                    'Pos': Point3(439.778, 290.738, 0.913),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/shipparts/dingy-geometry_High'
                    }
                },
                '1184891008.0dxschafe': {
                    'Type': 'Dinghy',
                    'Aggro Radius': '20.0000',
                    'Hpr': VBase3(3.889, -6.361, 3.088),
                    'Location': 'Water',
                    'Pos': Point3(176.081, 347.603, 4.377),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/shipparts/dingy-geometry_High'
                    }
                },
                '1184891008.0dxschafe0': {
                    'Type': 'Player Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Index': 1,
                    'Pos': Point3(153.026, 334.063, 7.954),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'Visual': {
                        'Color': (0.5, 0.5, 0.5, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1184891008.0dxschafe1': {
                    'Type': 'Player Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Index': 1,
                    'Pos': Point3(323.216, 284.901, 8.216),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'Visual': {
                        'Color': (0.5, 0.5, 0.5, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1184891136.0dxschafe': {
                    'Type': 'Player Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Index': 1,
                    'Pos': Point3(514.201, 137.198, 13.158),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'Visual': {
                        'Color': (0.5, 0.5, 0.5, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1189100537.84kmuller': {
                    'Type': 'Dinghy',
                    'Aggro Radius': '20.0000',
                    'Hpr': VBase3(50.735, 0.0, 0.0),
                    'Location': 'Land',
                    'Pos': Point3(649.482, -78.732, 0.09),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/shipparts/dingy-geometry_High'
                    }
                },
                '1189100602.12kmuller': {
                    'Type': 'Dinghy',
                    'Aggro Radius': '20.0000',
                    'Hpr': VBase3(68.908, 0.0, 0.0),
                    'Location': 'Land',
                    'Pos': Point3(457.149, -385.579, -0.171),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/shipparts/dingy-geometry_High'
                    }
                },
                '1189100641.06kmuller': {
                    'Type': 'Dinghy',
                    'Aggro Radius': '20.0000',
                    'Hpr': VBase3(-35.56, 0.0, 0.0),
                    'Location': 'Water',
                    'Pos': Point3(-11.463, -540.969, 0.135),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/shipparts/dingy-geometry_High'
                    }
                },
                '1189100678.54kmuller': {
                    'Type': 'Dinghy',
                    'Aggro Radius': '20.0000',
                    'Hpr': VBase3(-33.496, 0.0, 0.0),
                    'Location': 'Land',
                    'Pos': Point3(-245.855, -324.606, 0.684),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/shipparts/dingy-geometry_High'
                    }
                },
                '1189100725.93kmuller': {
                    'Type': 'Collision Barrier',
                    'DisableCollision': False,
                    'Hpr': VBase3(74.707, 0.0, 0.0),
                    'Pos': Point3(-230.516, -311.041, 3.68),
                    'Scale': VBase3(0.32, 1.0, 3.524),
                    'Visual': {
                        'Model': 'models/misc/pir_m_prp_lev_cambarrier_plane'
                    }
                },
                '1189100753.31kmuller': {
                    'Type': 'Collision Barrier',
                    'DisableCollision': False,
                    'Hpr': VBase3(-55.758, 0.0, 0.0),
                    'Pos': Point3(-254.586, -316.186, -8.463),
                    'Scale': VBase3(1.12, 1.665, 6.122),
                    'Visual': {
                        'Model': 'models/misc/pir_m_prp_lev_cambarrier_plane'
                    }
                },
                '1189101604.12kmuller': {
                    'Type': 'Player Spawn Node',
                    'Hpr': VBase3(-79.286, 0.0, 0.0),
                    'Index': 1,
                    'Pos': Point3(496.556, -119.78, 24.341),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'Visual': {
                        'Color': (0.5, 0.5, 0.5, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1189101641.11kmuller': {
                    'Type': 'Player Spawn Node',
                    'Hpr': VBase3(-122.92, 0.0, 0.0),
                    'Index': 1,
                    'Pos': Point3(370.191, -357.047, 10.264),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'Visual': {
                        'Color': (0.5, 0.5, 0.5, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1189101693.67kmuller': {
                    'Type': 'Player Spawn Node',
                    'Hpr': VBase3(167.296, 0.0, 0.0),
                    'Index': 1,
                    'Pos': Point3(4.016, -471.999, 10.921),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.5, 0.5, 0.5, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357312.0dxschafe': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(126.164, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(528.486, 71.76, 17.725),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T0',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357312.0dxschafe0': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(126.164, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(578.324, -7.22, 14.717),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T0',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357312.0dxschafe1': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(126.164, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(545.118, -160.422, 21.495),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357312.0dxschafe2': {
                    'Type': 'Spawn Node',
                    'Aggro Radius': '21.0843',
                    'AnimSet': 'default',
                    'Hpr': VBase3(126.164, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(581.331, -230.437, 12.441),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357312.0dxschafe3': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(126.164, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(207.309, -426.927, 9.727),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357312.0dxschafe4': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(126.164, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(390.712, -234.692, 25.604),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T3',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357312.0dxschafe5': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(126.164, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(46.687, 368.522, 8.715),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357312.0dxschafe6': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(6.195, 326.657, 17.947),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357312.0dxschafe7': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(258.724, 301.051, 6.949),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T0',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357440.0dxschafe': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(543.666, -204.087, 19.874),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T0',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357440.0dxschafe0': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(126.164, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(555.765, -277.98, 10.425),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357440.0dxschafe1': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(12.388, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(590.354, -178.998, 13.951),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T0',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1193357440.0dxschafe2': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(163.412, -468.794, 6.478),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Crab T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1245890725.88piwanow': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(-159.444, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(57.897, -316.736, 26.041),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Scorp T1',
                    'Start State': 'Patrol',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1245890800.17piwanow': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(149.036, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': '30',
                    'Pos': Point3(445.205, -81.831, 25.172),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Scorp T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1245890808.98piwanow': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(-25.201, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': '30',
                    'Pos': Point3(311.639, -230.79, 26.009),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Scorp T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1245890842.97piwanow': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(401.465, -100.152, 25.367),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1245890893.36piwanow': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(347.257, -213.186, 25.759),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1245890966.97piwanow': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': VBase3(-95.545, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': '30',
                    'Pos': Point3(251.138, 185.153, 26.013),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Scorp T1',
                    'Start State': 'Idle',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1245890983.39piwanow': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(354.425, 125.546, 26.731),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1245890987.89piwanow': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(432.517, 7.348, 25.311),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1257277464.2caoconno': {
                    'Type': 'Holiday',
                    'DisableCollision': False,
                    'Holiday': 'WinterFestival',
                    'Hpr': VBase3(154.997, 3.126, -6.668),
                    'Pos': Point3(453.792, 157.389, 24.139),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Model': 'models/props/pir_m_prp_hol_snowman_generic_winter09'
                    }
                },
                '1257277510.51caoconno': {
                    'Type': 'Holiday',
                    'DisableCollision': False,
                    'Holiday': 'WinterFestival',
                    'Hpr': VBase3(-87.195, 0.0, 0.0),
                    'Pos': Point3(454.447, 155.965, 24.427),
                    'Scale': VBase3(1.662, 1.662, 1.662),
                    'VisSize': '',
                    'Visual': {
                        'Model': 'models/props/pir_m_prp_hol_sandpile02_winter09'
                    }
                }
            },
            'Undockable': False,
            'Visibility': 'Grid',
            'Visual': {
                'Model': 'models/islands/pir_m_are_isl_devilsAnvil'
            }
        }
    },
    'Node Links': [
        ['1245890808.98piwanow', '1245890842.97piwanow', 'Bi-directional'],
        ['1245890800.17piwanow', '1245890893.36piwanow', 'Bi-directional'],
        ['1245890983.39piwanow', '1245890966.97piwanow', 'Bi-directional'],
        ['1245890987.89piwanow', '1245890983.39piwanow', 'Bi-directional']
    ],
    'Layers': {},
    'ObjectIds': {
        '1164135492.81dzlu': '["Objects"]["1164135492.81dzlu"]',
        '1164766305.45sdnaik': '["Objects"]["1164135492.81dzlu"]["Objects"]["1164766305.45sdnaik"]',
        '1168745928.39WDIG': '["Objects"]["1164135492.81dzlu"]["Objects"]["1168745928.39WDIG"]',
        '1172172361.37kmuller': '["Objects"]["1164135492.81dzlu"]["Objects"]["1172172361.37kmuller"]',
        '1172208953.16sdnaik': '["Objects"]["1164135492.81dzlu"]["Objects"]["1172208953.16sdnaik"]',
        '1172208953.17sdnaik': '["Objects"]["1164135492.81dzlu"]["Objects"]["1172208953.16sdnaik"]["Objects"]["1172208953.17sdnaik"]',
        '1172208953.19sdnaik': '["Objects"]["1164135492.81dzlu"]["Objects"]["1172208953.16sdnaik"]["Objects"]["1172208953.19sdnaik"]',
        '1172209006.11sdnaik': '["Objects"]["1164135492.81dzlu"]["Objects"]["1172209006.11sdnaik"]',
        '1172209006.14sdnaik': '["Objects"]["1164135492.81dzlu"]["Objects"]["1172209006.11sdnaik"]["Objects"]["1172209006.14sdnaik"]',
        '1179265792.0dxschafe0': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265792.0dxschafe0"]',
        '1179265792.0dxschafe1': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265792.0dxschafe1"]',
        '1179265792.0dxschafe2': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265792.0dxschafe2"]',
        '1179265792.0dxschafe3': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265792.0dxschafe3"]',
        '1179265920.0dxschafe': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265920.0dxschafe"]',
        '1179265920.0dxschafe0': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265920.0dxschafe0"]',
        '1179265920.0dxschafe1': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265920.0dxschafe1"]',
        '1179265920.0dxschafe2': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265920.0dxschafe2"]',
        '1179265920.0dxschafe3': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265920.0dxschafe3"]',
        '1179265920.0dxschafe4': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265920.0dxschafe4"]',
        '1179265920.0dxschafe5': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179265920.0dxschafe5"]',
        '1179266048.0dxschafe': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179266048.0dxschafe"]',
        '1179266048.0dxschafe0': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179266048.0dxschafe0"]',
        '1179266048.0dxschafe1': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179266048.0dxschafe1"]',
        '1179266048.0dxschafe2': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179266048.0dxschafe2"]',
        '1179266048.0dxschafe3': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179266048.0dxschafe3"]',
        '1179266176.0dxschafe': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179266176.0dxschafe"]',
        '1179266176.0dxschafe0': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179266176.0dxschafe0"]',
        '1179288192.0JB0': '["Objects"]["1164135492.81dzlu"]["Objects"]["1179288192.0JB0"]',
        '1184890880.0dxschafe0': '["Objects"]["1164135492.81dzlu"]["Objects"]["1184890880.0dxschafe0"]',
        '1184890880.0dxschafe1': '["Objects"]["1164135492.81dzlu"]["Objects"]["1184890880.0dxschafe1"]',
        '1184891008.0dxschafe': '["Objects"]["1164135492.81dzlu"]["Objects"]["1184891008.0dxschafe"]',
        '1184891008.0dxschafe0': '["Objects"]["1164135492.81dzlu"]["Objects"]["1184891008.0dxschafe0"]',
        '1184891008.0dxschafe1': '["Objects"]["1164135492.81dzlu"]["Objects"]["1184891008.0dxschafe1"]',
        '1184891136.0dxschafe': '["Objects"]["1164135492.81dzlu"]["Objects"]["1184891136.0dxschafe"]',
        '1189100537.84kmuller': '["Objects"]["1164135492.81dzlu"]["Objects"]["1189100537.84kmuller"]',
        '1189100602.12kmuller': '["Objects"]["1164135492.81dzlu"]["Objects"]["1189100602.12kmuller"]',
        '1189100641.06kmuller': '["Objects"]["1164135492.81dzlu"]["Objects"]["1189100641.06kmuller"]',
        '1189100678.54kmuller': '["Objects"]["1164135492.81dzlu"]["Objects"]["1189100678.54kmuller"]',
        '1189100725.93kmuller': '["Objects"]["1164135492.81dzlu"]["Objects"]["1189100725.93kmuller"]',
        '1189100753.31kmuller': '["Objects"]["1164135492.81dzlu"]["Objects"]["1189100753.31kmuller"]',
        '1189101604.12kmuller': '["Objects"]["1164135492.81dzlu"]["Objects"]["1189101604.12kmuller"]',
        '1189101641.11kmuller': '["Objects"]["1164135492.81dzlu"]["Objects"]["1189101641.11kmuller"]',
        '1189101693.67kmuller': '["Objects"]["1164135492.81dzlu"]["Objects"]["1189101693.67kmuller"]',
        '1193357312.0dxschafe': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357312.0dxschafe"]',
        '1193357312.0dxschafe0': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357312.0dxschafe0"]',
        '1193357312.0dxschafe1': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357312.0dxschafe1"]',
        '1193357312.0dxschafe2': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357312.0dxschafe2"]',
        '1193357312.0dxschafe3': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357312.0dxschafe3"]',
        '1193357312.0dxschafe4': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357312.0dxschafe4"]',
        '1193357312.0dxschafe5': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357312.0dxschafe5"]',
        '1193357312.0dxschafe6': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357312.0dxschafe6"]',
        '1193357312.0dxschafe7': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357312.0dxschafe7"]',
        '1193357440.0dxschafe': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357440.0dxschafe"]',
        '1193357440.0dxschafe0': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357440.0dxschafe0"]',
        '1193357440.0dxschafe1': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357440.0dxschafe1"]',
        '1193357440.0dxschafe2': '["Objects"]["1164135492.81dzlu"]["Objects"]["1193357440.0dxschafe2"]',
        '1245890725.88piwanow': '["Objects"]["1164135492.81dzlu"]["Objects"]["1245890725.88piwanow"]',
        '1245890800.17piwanow': '["Objects"]["1164135492.81dzlu"]["Objects"]["1245890800.17piwanow"]',
        '1245890808.98piwanow': '["Objects"]["1164135492.81dzlu"]["Objects"]["1245890808.98piwanow"]',
        '1245890842.97piwanow': '["Objects"]["1164135492.81dzlu"]["Objects"]["1245890842.97piwanow"]',
        '1245890893.36piwanow': '["Objects"]["1164135492.81dzlu"]["Objects"]["1245890893.36piwanow"]',
        '1245890966.97piwanow': '["Objects"]["1164135492.81dzlu"]["Objects"]["1245890966.97piwanow"]',
        '1245890983.39piwanow': '["Objects"]["1164135492.81dzlu"]["Objects"]["1245890983.39piwanow"]',
        '1245890987.89piwanow': '["Objects"]["1164135492.81dzlu"]["Objects"]["1245890987.89piwanow"]',
        '1257277464.2caoconno': '["Objects"]["1164135492.81dzlu"]["Objects"]["1257277464.2caoconno"]',
        '1257277510.51caoconno': '["Objects"]["1164135492.81dzlu"]["Objects"]["1257277510.51caoconno"]'
    }
}
extraInfo = {
    'camPos': Point3(481.695, 145.91, 29.114),
    'camHpr': VBase3(68.916, -10.2185, 0),
    'focalLength': 1.39999997616,
    'skyState': 2,
    'fog': 0
}