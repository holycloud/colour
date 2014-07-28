# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Showcases some **Colour** package *illuminants* related examples.
"""

import colour

# Retrieving *D60* illuminant chromaticity coordinates.
print(colour.ILLUMINANTS["CIE 1931 2 Degree Standard Observer"]["D60"])

# Displaying all illuminants data per standard observers.
for observer, illuminants in colour.ILLUMINANTS.iteritems():
    print("Observer: '{0}'.".format(observer))
    for illuminant, xy in illuminants.iteritems():
        print("'{0}': {1}".format(illuminant, xy))