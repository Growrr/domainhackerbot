import os, urllib, sys, re, random, time, whois, mastodon

domainslist = urllib.urlopen("http://data.iana.org/TLD/tlds-alpha-by-domain.txt")
domains = set(filter(lambda a: not a.startswith('#'), [line.strip().lower() for line in domainslist]))
domainslist.close()

mindomainlen = min(map(len, domains))
maxdomainlen = max(map(len, domains))

words = open("/usr/share/dict/words").readlines()
random.shuffle(words)

historyfilename = "domainhistory.txt"

if os.path.exists(historyfile):
    history = set([s.strip() for s in open(historyfilename)])
    historyfile = open(historyfilename, 'a')
else:
    history = set()
    historyfile = open(historyfilename, 'w')

for word in words:
    word = word.strip()
    lword = re.sub("\\W", "", word.lower())
    for i in range(mindomainlen, min(len(lword)-1, maxdomainlen)):
        if lword[-i:] in domains:
            #row = []
            #row.append(word)
            domain = lword[:-i]+'.'+lword[-i:]
            #row.append(domain)
            '''exitCode = os.system("host -W 1 "+domain+"")
            if exitCode == 0:
                # If it has a host,
                # the website already exists.
                #row.append("Taken")
                continue
            elif exitCode in (1, 256):
                #row.append("Available")
                pass
            else:
                raise Exception("invalid exit code "+str(exitCode))'''
            if whois.whois(domain).expiration_date is not None: continue
            history.add(domain)
            historyfile.write(domain+'\n')
            historyfile.sleep()
            '''url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="+urllib.quote_plus(word)
            print url
            urldoc = urllib.urlopen(url)
            result = json.loads(urldoc.read())
            urldoc.close()
            row.append(result["responseData"]["cursor"]["estimatedResultCount"])'''
            #row.append(len(word))
            #row.append(i)
            #writer.writerow(row)
    time.sleep(5*60)
fout.close()
words.close()
