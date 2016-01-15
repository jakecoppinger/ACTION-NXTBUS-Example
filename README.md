ACTION NXTBUS Example
====================

A very basic example for getting started with ACTION's NXTBUS API in Python. See ACTION's information at https://www.action.act.gov.au/rider_Info/apps

Getting started
---------------
1. Clone repository
2. Apply to ACTION for a [NXTBUS API key](https://www.action.act.gov.au/rider_Info/apps/nxtbus-data-feed-registration-form). You will receive an email that includes a key along with formal API documentation. Replace APIKEY in ``main.py`` with this key. 
3. Install Python requirements with Pip. For Python 2.*:
  ``pip install tornado xmltodict dicttoxml `` . For Python 3.*: ``pip3 install tornado xmltodict dicttoxml `` 
  
4. Run (compatible with Python 2.* and 3.*)
``python main.py``
