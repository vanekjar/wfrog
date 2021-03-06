## Copyright 2009 Laurent Bovet <laurent.bovet@windmaster.ch>
##                Jordi Puigsegur <jordi.puigsegur@gmail.com>
##
##  This file is part of wfrog
##
##  wfrog is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

class CountFormula(object):
    '''
    Counts number of measures.
    '''
    def __init__(self, index):
        self.index = index

    index = None
    count = 0

    def append(self, sample):
        value = sample[self.index]
        if value is not None:
            self.count = self.count + 1

    def value(self):
        return self.count

class AverageFormula(object):
    '''
    Average.
    '''
    def __init__(self, index):
        self.index = index

    index = None
    sum = 0
    count = 0

    def append(self, sample):
        value = sample[self.index]
        if value is not None:
            self.sum = self.sum + value
            self.count = self.count + 1

    def value(self):
        if self.count==0:
            return None
        else:
            return float(self.sum) / float(self.count)


class LastFormula(object):
    '''
    Keeps last sample value.
    '''

    def __init__(self, index):
        self.index = index

    index = None
    last = None

    def append(self, sample):
        value = sample[self.index]
        if value is not None:
            self.last = value

    def value(self):
        return self.last


class MinFormula(object):
    '''
    Minimum.
    '''

    def __init__(self, index):
        self.index = index

    index = None
    min = sys.maxint

    def append(self, sample):
        value = sample[self.index]
        if value is not None:
            self.min = min(self.min, value)

    def value(self):
        if self.min == sys.maxint:
            return None
        else:
            return self.min


class MaxFormula(object):
    '''
    Maximum.
    '''

    def __init__(self, index):
        self.index = index

    index = None
    max = -sys.maxint

    def append(self, sample):
        value = sample[self.index]
        if value is not None:
            self.max = max(self.max, value)

    def value(self):
        if self.max == -sys.maxint:
            return None
        else:
            return self.max


class SumFormula(object):
    '''
    Sum.
    '''

    def __init__(self, index):
        self.index = index

    index = None
    sum = 0
    empty = True

    def append(self, sample):
        value = sample[self.index]
        if value is not None:
            self.empty = False
            self.sum = self.sum + value

    def value(self):
        if self.empty:
            return None
        else:
            return self.sum
