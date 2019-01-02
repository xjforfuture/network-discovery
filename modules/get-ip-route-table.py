#!/usr/bin/python
'''
        natlas

        Michael Laforest
        mjlaforest@gmail.com

        Copyright (C) 2015-2018 Michael Laforest

        This program is free software; you can redistribute it and/or
        modify it under the terms of the GNU General Public License
        as published by the Free Software Foundation; either version 2
        of the License, or (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program; if not, write to the Free Software
        Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''

import sys
import getopt
import natlas


def mod_load(mod):
    mod.name = 'get-ip-route-table'
    mod.version = '0.1'
    mod.author = 'Michael Laforest'
    mod.authoremail = 'xiongjun@tsinghuanet.com'
    mod.preload_conf = 0
    mod.about = 'Display the ipRouteTable table'
    mod.syntax = '-n <node IP> -c <snmp v2 community> '
    mod.help = '''
                        Query a switch display the ip route table.
                        '''
    mod.example = '''
                        Get all ip route entries 

                        # get-ip-route-table -n 10.10.1.66 -c public "

                        
                        '''
    return 1


def mod_entry(natlas_obj, argv):
    opt_devip = None
    opt_community = None

    try:
        opts, args = getopt.getopt(argv, 'n:c:')
    except getopt.GetoptError:
        return
    for opt, arg in opts:
        if (opt == '-n'):   opt_devip = arg
        if (opt == '-c'):   opt_community = arg

    if ((opt_devip == None) | (opt_community == None)):
        return

    # set some snmp credentials for us to use
    natlas_obj.snmp_add_credential(2, opt_community)

    # get the ip route table
    try:
        ip_routes = natlas_obj.get_ip_route_table(opt_devip)
    except Exception as e:
        print(e)
        return

    # print ip route table
    print()
    print('dest            mask            next_hop        type       proto      interface      ')
    print('----            ---             ----            ----       ----       ----           ')
    for route in ip_routes:
        print(f"{route.dest:<15} {route.mask:<15} {route.next_hop:<15} {route.type:<10} "
              f"{route.proto:<10} {route.ifname:<15}")

    print('\nFound %i ip route entries' % len(ip_routes))

