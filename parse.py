#!/usr/bin/env python3

import pymodbus
from hexdump import hexdump, dump
import struct


PACKET_LENGTH = 189

class hws_packet:
    def __init__(self, packet: bytes):
        # print(hexdump(packet, result='return'))
        # print(dump(packet, sep=" "))
        # print("-="*20)
        self.raw = packet

        a = pymodbus.pdu.decoders.DecodePDU(1).decode(packet[1:-2])
        # Check if a is a WriteMultipleRegisterRequest
        # print(type(a))
        if isinstance(a, pymodbus.pdu.register_write_message.WriteMultipleRegistersRequest):
            self.data = {}
            for i in range(a.address, a.address+a.count):
                self.data[i] = a.values[i-a.address]
                # if a.values[i-a.address] != 0:
                #     print(f"{i}: {a.values[i-a.address]}")

# This returns true if every item in the list is the same:
def all_same(items):
    return all(x == items[0] for x in items)


with open("log.raw", "rb") as f:
    packet_start = 0
    i = 0
    packet: bytes = b""
    packets = []
    for byte in f.read():
        # print(byte)
        if byte == 0x63:
            packet_start = i
            packet = b""
        if packet_start != 0:
            packet += bytes([byte])
        if len(packet) == PACKET_LENGTH:
            # print(hexdump(packet, result='return'))
            # print(dump(packet))
            packets.append(hws_packet(packet))
            packet_start = 0
            packet = b""
        i += 1

    keys = set()
    for packet in packets:
        for key in packet.data.keys():
            keys.add(key)
    keys = sorted(list(keys))
    for key in keys:
        addr = key
        values = []
        for packet in packets:
            if addr in packet.data:
                values.append(packet.data[addr])
                # print(packet.data[addr], end=" "
            # else:
            #     values.append(0)
        if (not all_same(values) and len(values) > 1) or (len(values) == 1 and values[0] != 0):
            print(f"{key}: ", end=" ")
            print(values)
