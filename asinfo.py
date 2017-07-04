import requests

def asn_from_endpoint(endpoint):
    asn = holder = None
    base = 'https://stat.ripe.net/data/prefix-overview/data.json'
    try: res = requests.get('%s?resource=%s'%(base,endpoint))
    except Exception as e: print(e)
    else:
      try:
            asn = res.json()['data']['asns'][0]['asn']
            holder = res.json()['data']['asns'][0]['holder']
      except Exception as e: print(e)
    return asn, holder


def holder_from_asn(asn):
    holder = None
    base = 'https://stat.ripe.net/data/as-overview/data.json'
    try: res = requests.get('%s?resource=%s'%(base,asn))
    except Exception as e: print(e)
    else:
      try: holder = res.json()['data']['holder']
      except Exception as e: print(e)
    return holder

def create_pretty_node_names(holder, asn):
    try: firstname = holder.split('-')[0].split(' ')[0]
    except Exception as e: print(e);nodename="";
    else:
      if 'AS' in str(asn): nodename = '%s (%s)'%(firstname, asn)
      else: nodename = '%s (AS%s)'%(firstname, asn)
    return nodename
