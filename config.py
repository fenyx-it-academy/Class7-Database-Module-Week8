#!/usr/bin/python
from configparser import ConfigParser

def config(filename, section):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {} #empty dictionary
    if parser.has_section(section):
        params = parser.items(section) #params is a list of tuples 
        # params = [('host', 'localhost'), ('database', 'Chinook_PostgreSql'), ('user', 'postgres'), ('password', 'postgres')]
        for param in params: #param is a tuple (0,1)>>>> param= ('host', 'localhost') 
            db[param[0]] = param[1] #dict_name[key]=value
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section,filename))
    # db = {'host': 'localhost', 'database': 'Chinook_PostgreSql', 'user': 'postgres', 'password': 'postgres'}
    return db