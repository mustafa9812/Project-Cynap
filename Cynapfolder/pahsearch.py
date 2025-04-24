from amespahdbpythonsuite.amespahdb import AmesPAHdb
import os
os.environ['AMESPAHDEFAULTDB'] = r'C:\Users\Mustafa\Downloads\pahdb-selection-theoretical-1cyano.xml'

pahdb = AmesPAHdb()

uids = pahdb.search("c<=20 neutral n=2 neutral")

pahs = pahdb.getspeciesbyuid(uids)

transitions = pahdb.gettransitionsbyuid(uids)

geometry = pahdb.getgeometrybyuid(uids)

laboratory = pahdb.getlaboratorybyuid(uids)

pahs.print(str=True)