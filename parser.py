# Access log parser v1.0
# Author: Sergei Safarov <inbox@sergeysafarov.com>

import csv
import os
import re
import sys
import geoip2.database
import wget
import gzip
import shutil

from os import path
from user_agents import parse


########################################################################################################################
# Functions declarations
# Start
########################################################################################################################

def file_name(filename):
    return os.path.splitext(os.path.basename(filename))[0]


def file_size(filename):
    return os.path.getsize(filename)


########################################################################################################################
# Settings
########################################################################################################################
lang = 'en'
input_file = 'log/access.log'
geoip_database = 'GeoLite2-Country.mmdb'
geoip_db_source = 'http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz'

########################################################################################################################
# Script body
########################################################################################################################

if not path.exists(input_file):
    sys.exit('Inboud log file not found. Stopped')

if_size = file_size(input_file)

if if_size == 0:
    sys.exit('Inboud log file is empty. Stopped')

if not path.exists(geoip_database):
    print('Geo IP database not found. Trying to download from ' + geoip_db_source)
    wgt_result = wget.download(geoip_db_source)
    if wgt_result:
        with gzip.open('GeoLite2-Country.mmdb.gz', 'rb') as f_in:
            with open('GeoLite2-Country.mmdb', 'wb') as f_out:
                print('Geo IP database downloaded. Extracting.')
                shutil.copyfileobj(f_in, f_out)
                print('Geo IP database extracted.')
        # Clean downloaded compressed db file
        if path.exists('GeoLite2-Country.mmdb.gz'):
            os.remove('GeoLite2-Country.mmdb.gz')

if not path.exists(geoip_database):
    print('Geo IP database not found. Countries will not be retrieved. ')
    print('Please obtain the database ' + geoip_database + ' file and put it into the script folder')
else:
    geo_ip_reader = geoip2.database.Reader(geoip_database)

output_file = file_name(input_file) + '.csv'

print('Parsing ' + input_file + ' [' + str(if_size) + ' bytes]')
print('Writing ' + output_file)

with open(input_file, encoding="UTF8") as fi, open(output_file, 'w', encoding="UTF8") as fo:
    writer = csv.writer(fo, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['#', 'IP', 'Country', 'Browser', 'Device', 'Type', 'RAW LINE'])

    i = 1
    for line in fi:
        sys.stdout.write("Processing line: %d   \r" % (i))
        sys.stdout.flush()

        ip_address = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)[0]
        try:
            # No problems here in case of geo DB not found as we are inside try/except block
            location = geo_ip_reader.country(ip_address)

            if location and location.country and location.country.names:
                country = location.country.names[lang]
            else:
                country = 'N/A'
        except:
            country = 'N/A'

        try:
            line_parts = re.findall(r'\"(.+?)\"', line)
            ua_record = line_parts[len(line_parts) - 1]
            parsed_ua = parse(ua_record)

            browser = parsed_ua.browser.family
            device_family = parsed_ua.device.family

            if parsed_ua.is_mobile:
                device_type = 'Mobile'
            elif parsed_ua.is_tablet:
                device_type = 'Tablet'
            elif parsed_ua.is_pc:
                device_type = 'Desktop'
            elif parsed_ua.is_bot:
                device_type = 'Bot'
            else:
                device_type = 'Unknown'
        except:
            browser = 'N/A'
            device_family = 'N/A'
            device_type = 'N/A'

        writer.writerow([i, ip_address, country, browser, device_family, device_type, line])
        i += 1

print("Parsing finished. " + str(i - 1) + " lines processed.")
