Most messages start with

63 10 07 D1 00 5A B4 00
07D1: 2001

But some start with:

63 10 03 E9 00 5A B4 00
03E9: 1001

or

63 10 04 43 00 5A B4 00
0443: 1091

# CRC?
The last two bytes are often different. Could they be a CRC?
63:10:07:d1:00:5a:b4:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:07:d1:00:0e:01:e1:00:0a:01:19:00:00:00:00:00:00:00:00:00:71:00:af:00:ae:00:5a:00:61:00:d8:00:ae:00:01:00:f4:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:09:30:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:ce:00:36:00:05:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:73:d8

63:10:07:d1:00:5a:b4:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:07:d1:00:0e:01:e1:00:0a:01:19:00:00:00:00:00:00:00:00:00:71:00:af:00:ae:00:5a:00:61:00:d8:00:ae:00:01:00:f4:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:09:30:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:ce:00:36:00:05:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:73:d8

https://cyberchef.tjhowse.com/#recipe=From_Hex('Auto')NOT(/disabled)CRC-16_Checksum()NOT(/disabled)&input=NjM6MTA6MDc6ZDE6MDA6NWE6YjQ6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDc6ZDE6MDA6MGU6MDE6ZTE6MDA6MGE6MDE6MTk6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6NzE6MDA6YWY6MDA6YWU6MDA6NWE6MDA6NjE6MDA6ZDg6MDA6YWU6MDA6MDE6MDA6ZjQ6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDk6MzA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6Y2U6MDA6MzY6MDA6MDU6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA

a70a Hmm no.

https://cyberchef.tjhowse.com/#recipe=From_Hex('Auto')NOT()CRC-16_Checksum(/disabled)Generate_all_hashes('All',true)&input=NjM6MTA6MDc6ZDE6MDA6NWE6YjQ6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDc6ZDE6MDA6MGU6MDE6ZTE6MDA6MGE6MDE6MTk6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6NzE6MDA6YWY6MDA6YWU6MDA6NWE6MDA6NjE6MDA6ZDg6MDA6YWU6MDA6MDE6MDA6ZjQ6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDk6MzA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6Y2U6MDA6MzY6MDA6MDU6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA6MDA

At 2024-10-30T11:34:04 the HWS started drawing less power

This works:

https://crccalc.com/?crc=631007D1005AB400000000000000000000000000000000000007D1000E01E1000A01190000000000000000007D00B100B2006A007F00D800B2000100F40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003000010000000000000000000000000000000001E0003600050000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&method=CRC-16/MODBUS&datatype=1&outtype=0

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
(4195, 53511, 23040, 180, 0, 0, 0, 0, 0, 0, 0, 0, 1792, 209, 270, 225, 266, 25, 0, 0, 0, 0, 127, 177, 178, 106, 128, 216, 178, 1, 244, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 1, 0, 0, 0, 0, 0, 0, 0, 256, 224, 54, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 132)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
(4195, 53511, 23040, 180, 0, 0, 0, 0, 0, 0, 0, 0, 1792, 209, 270, 225, 266, 25, 0, 0, 0, 0, 126, 177, 178, 106, 128, 216, 178, 1, 244, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 1, 0, 0, 0, 0, 0, 0, 0, 256, 224, 54, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 40153)
