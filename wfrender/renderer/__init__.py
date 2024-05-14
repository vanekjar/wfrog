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

import yaml

import chart
import data
import datatable
import file
import staticfile
import ftp
import http
import scheduler
import template
import value
import meteoclimatic
import wunderground
import pwsweather
import wettercom
import sticker
import openweathermap
import metofficewow
import housekeep

# YAML mappings

class YamlTestChartRenderer(chart.TestChartRenderer, yaml.YAMLObject):
    yaml_tag = u'!test'

class YamlChartRenderer(chart.ChartRenderer, yaml.YAMLObject):
    yaml_tag = u'!chart'

class YamlWindRadarChartRenderer(chart.ChartWindRadarRenderer, yaml.YAMLObject):
    yaml_tag = u'!windradar'

class YamlDataRenderer(data.DataRenderer, yaml.YAMLObject):
    yaml_tag = u'!data'

class YamlDataRenderer(datatable.DataTableRenderer, yaml.YAMLObject):
    yaml_tag = u'!datatable'

class YamlFileRenderer(file.FileRenderer, yaml.YAMLObject):
    yaml_tag = u'!file'

class YamlStaticFileRenderer(staticfile.StaticFileRenderer, yaml.YAMLObject):
    yaml_tag = u'!staticfile'

class YamlFtpRenderer(ftp.FtpRenderer, yaml.YAMLObject):
    yaml_tag = u'!ftp'

class YamlHttpRenderer(http.HttpRenderer, yaml.YAMLObject):
    yaml_tag = u'!http'

class YamlSchedulerRenderer(scheduler.SchedulerRenderer, yaml.YAMLObject):
    yaml_tag = u'!scheduler'

class YamlTemplateRenderer(template.TemplateRenderer, yaml.YAMLObject):
    yaml_tag = u'!template'

class YamlValueRenderer(value.ValueRenderer, yaml.YAMLObject):
    yaml_tag = u'!value'

class YamlMeteoclimaticRenderer(meteoclimatic.MeteoclimaticRenderer, yaml.YAMLObject):
    yaml_tag = u'!meteoclimatic'

class YamlWundergroundRenderer(wunderground.WeatherUndergroundPublisher, yaml.YAMLObject):
    yaml_tag = u'!wunderground'

class PwsWeatherRenderer(pwsweather.PwsWeatherPublisher, yaml.YAMLObject):
    yaml_tag = u'!pwsweather'

class WetterComRenderer(wettercom.WetterComPublisher, yaml.YAMLObject):
    yaml_tag = u'!wettercom'

class StickerRenderer(sticker.StickerRenderer, yaml.YAMLObject):
    yaml_tag = u'!sticker'

class OpenWeatherMapPublisher(openweathermap.OpenWeatherMapPublisher, yaml.YAMLObject):
    yaml_tag = u'!openweathermap'

class MetOfficeWowPublisher(metofficewow.MetOfficeWowPublisher, yaml.YAMLObject):
    yaml_tag = u'!metofficewow'

class HousekeepRenderer(housekeep.HousekeepRenderer, yaml.YAMLObject):
    yaml_tag = u'!housekeeper'
