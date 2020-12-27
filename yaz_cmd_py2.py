from PyZ3950 import zoom
from pymarc import MARCReader
import argparse, os











def get_yaz(host, port, dbname, user, pw, syntax, query):
    conn = zoom.Connection(host , int(port))
    conn.databaseName = dbname
    # conn.user = login
    conn.user = user
    conn.password = pw
    conn.preferredRecordSyntax = syntax.lower()
    query1 = zoom.Query('CCL', query)
    res = conn.search(query1)
    if len(res) > 0:
        print res[0]
    # for r in res:
    #
    #     temp_list = []
    #     for i in range(0, 2):  # You can take len(res) here for all results
    #         temp_list.append(res[i].data)
    #     for i in range(0, 2):  # You can take len(res) here for all results
    #         reader = MARCReader(temp_list[i])
    #         for i in reader:
    #             print i.isbn()
    # conn.close ()



def get_yaz_test(test):
    host = None
    port = None
    dbname = None
    login = None
    syntax = None
    user = None
    pw = None
    query = None

    if int(test) == 1:
        host = '193.30.112.135'
        port = '9991'
        dbname = 'HBZ01'
        login = ''
        syntax = 'mab'
        query = 'funktion'
    else:
        pass
    print test
    print host, port, dbname, user, pw, syntax, query
    get_yaz(host, port, dbname, user, pw, syntax, query)





def get_records():
    pass




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get results for yaz")
    parser.add_argument('-t', '--test', nargs='?')
    parser.add_argument('host', nargs='?')
    parser.add_argument('port', nargs='?')
    parser.add_argument('dbname', nargs='?')
    parser.add_argument('user', nargs='?')
    parser.add_argument('pw', nargs='?')
    parser.add_argument('syntax', nargs='?')
    parser.add_argument('query', nargs='?')
    args = parser.parse_args()
    if (args.host and args.port and args.dbname and args.login and args.syntax and args.query):
        get_yaz(args.host, args.port, args.dbname, args.user, args.pw, args.syntax, args.query)
    elif (args.test):
        get_yaz_test(args.test)
