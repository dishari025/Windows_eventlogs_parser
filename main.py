#This is the python parser to extract the windows logs.
#This is the official documentation of the library evtx that we will be using: https://pypi.org/project/evtx/
#We will install the evtx library using the command: pip install evtx
#This parser will display the Event ID, Record ID, Timestamp and the Data of all records

import io
import xml.etree.ElementTree as ET  #Converts string data to XML to retrieve the information
from evtx import PyEvtxParser


def evtx_parser():
    disconnection_list=[2100, 2102]
    parser = PyEvtxParser("D:\drdoproject\eventlogsparser\Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx")
    print('DISCONNECTION LIST:')
    print('...................................................')
    for record in parser.records():
        f = io.StringIO(record['data'])
        tree = ET.parse(f)
        root = tree.getroot()
        #print(root[0][1].text)
        if int(root[0][1].text) in disconnection_list:
            print(f'Event ID: {root[0][1].text}')
            print(f'Event Record ID: {record["event_record_id"]}')
            print(f'Event Timestamp: {record["timestamp"]}')
            #print(f'Event data: {record["data"]}')
            print(f'------------------------------------------')

    connection_list=[2003, 2004, 2006]
    parser = PyEvtxParser("D:\drdoproject\eventlogsparser\Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx")
    print('CONNECTION LIST:')
    print('...................................................')
    for record in parser.records():
        f = io.StringIO(record['data'])
        tree = ET.parse(f)
        root = tree.getroot()
        #print(root[0][1].text)
        if int(root[0][1].text) in connection_list:
            print(f'Event ID: {root[0][1].text}')
            print(f'Event Record ID: {record["event_record_id"]}')
            print(f'Event Timestamp: {record["timestamp"]}')
            #print(f'Event data: {record["data"]}')
            print(f'------------------------------------------')

if __name__ == '__main__':
    evtx_parser()
