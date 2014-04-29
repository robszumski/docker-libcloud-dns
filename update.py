#!/usr/bin/python

import argparse
import os
from libcloud.dns.providers import get_driver
from libcloud.dns.types import Provider, RecordType
from libcloud.common.types import LibcloudError
from pprint import pprint

parser = argparse.ArgumentParser(description='Create or update DNS record')
parser.add_argument('--domain', metavar='<DOMAIN>', default=os.environ.get('DOMAIN'),
                    help='Name of of the domain that contains the DNS record')
parser.add_argument('--type', metavar='<TYPE>', default=RecordType.A,
                    help='The type of DNS record. (A, AAAA, CNAME, etc)')
parser.add_argument('--identity', metavar='<IDENTITY>', default=os.environ.get('IDENTITY'),
                    help='The username or identity used to authenticate')
parser.add_argument('--secret', metavar='<SECRET>', default=os.environ.get('SECRET'),
                    help='Password, API key or other secret used to authenticate')
parser.add_argument('--value', metavar='<VALUE>', default=os.environ.get('VALUE'),
                    help='The value of the DNS record')
parser.add_argument('--ttl', metavar='<TTL>', default=300,
                    help='The desired TTL of the DNS record')
parser.add_argument('--provider', metavar='<PROVIDER>', default=Provider.ROUTE53,
                    help='The value of the DNS record')
parser.add_argument('--record', metavar='<RECORD>', default=os.environ.get('RECORD'),
                    help='The the DNS record to create')
args = parser.parse_args()

CREDENTIALS = (args.identity, args.secret)
DOMAIN = 'robszumski.com.'
RECORD_NAME = 'test'
RECORD_TYPE = RecordType.A
VALUE = '54.81.103.88'
TTL = 300
DEBUG = True

cls = get_driver(Provider.ROUTE53)
driver = cls(*CREDENTIALS)

zone = [z for z in driver.list_zones() if z.domain == args.domain][0]

records = driver.list_records(zone)

exists = any(record.name == args.record for record in records)

extra = {'ttl': args.ttl}

if exists is False:
  try:
    record = zone.create_record(name=args.record, type=args.type, data=args.value,
      extra=extra)
    print "Creating record for %s.%s with value %s" % (args.record, args.domain, args.value)
  except LibcloudError:
    print "Could not create %s.%s" % (args.record, args.domain)
else:
  try:
    record = [r for r in driver.list_records(zone) if r.name == args.record][0]
    newRecord = driver.update_record(record=record, name=args.record, type=args.type, data=args.value, extra=extra)
  except LibcloudError:
    print "something went wrong"
