### Overview
It's annoying in python scripts to load data, wait a long time, then to realize that you have an error somewhere after the data has been loaded. This makes debugging super annoying.

To fight this, I give you basic ram db. Load the database in a separate process and then use the client object to access it like a normal dictionary.

Any improvements in making it multithreaded would be super appreciated.

### Sample run
#####Terminal window 1:
        python2.7 ramDB_s.py test_tab_separated.tsv

#####Terminal window 2:
        ipython
        from ramDB_c import DBClient
        d = DBClient()
        d['stanford']
                (some value returned)
        d['dima'] = 'procrastinating'
        d['stephen'] = 'unknown location'
        d['vikas'] = 'magic hands'
        d.set_batch({'rowan':'probably running', 'dima':'gotta stop procrastinating'})
        d['dima']
                (-> 'gotta stop procrastinating')

