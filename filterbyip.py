import pandas as pd
import ipaddress
import socket

def if_ipv6(address):
  """accepts a ip address as string, if the address is a IPv6 address, it
     returns True, otherwise returns False,"""

  try:
    ip = ipaddress.ip_address(address)
    if ip.version == 6: return True
    else: return False
  except:
    try:
      ipn = ipaddress.ip_network(address)
      if ipn.version == 6: return True
      else: return False
    except: return None


def if_ipv4(address):
  """accepts a ip address as string, if the address is a IPv4 address, it
     returns True, otherwise returns False,"""

  try:
    ip = ipaddress.ip_address(address)
    if ip.version == 4: return True
    else: return False
  except:
    try:
      ipn = ipaddress.ip_network(address)
      if ipn.version == 4: return True
      else: return False
    except: return None

def filter_v6(df, column):
  """applies if_ipv6(...) on the endpoint of each row of the DataFrame,
     returns the DataFrame with rows that returned True"""

  return df[df.apply(lambda x: if_ipv6(x[column]), axis=1)]

def filter_v4(df, column):
  """applies if_ipv4(...) on the endpoint of each row of the DataFrame,
     returns the DataFrame with rows that returned True"""

  return df[df.apply(lambda x: if_ipv4(x[column]), axis=1)]
