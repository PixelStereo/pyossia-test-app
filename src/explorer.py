#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QAbstractListModel, QModelIndex, QVariant, Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel

        
class ZeroConfListener(object):
    def __init__(self, *args, **kwargs):
        #print(args[0])
        self.device_model = args[0]

    def remove_service(self, zeroconf, type, name):
        name = name.split('.' + type)[0]
        print('BYE BYE ' + name)
        for row in range(0, self.device_model.rowCount()+1):
            #if self.device.model.item(row).data() == name:
            self.device_model.removeRow(row)
        # TODO : SEND A SIGNAL to CLEAR thE tHREE

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        name = name.split('.' + type)[0]
        port = info.port
        server = info.server
        device = name + '@' + server + ':' + str(port)
        print(info)
        device_item = QStandardItem(device)
        print('ADDED ' + str(device))
        self.device_model.appendRow(device_item)
