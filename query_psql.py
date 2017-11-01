from secret_connect import secret_connection

class PoliceQuery:
    def __init__(self, query_dict):
        self.query_dict = query_dict
        self.conn = secret_connection()
        self.cur = self.conn.cursor()
        self.desired_fields = []
        # for not none in dict, append to desired fields

    def query_psql(self):
        query = self.construct_query()
        self.cur.execute(query)
        num_titles = self.cur.rowcount

        return self.cur.fetchall()

    def construct_query(self):
        query = ''
        query += self.selector()
        # TODO targets
        # TODO targ_lists
        if self.query_dict["WHERES"] is not None:
            query += self.wheres()

        query += self.grouper()

        return query+";"

    def selector(self):
        select_clause = "SELECT "
        return select_clause

    def grouper(self):
        return " GROUP BY county_name"

    def wheres(self):
        lines = []
        for key, val in self.query_dict['wheres'].items():
            if val is None:
                pass
            if "_MIN" in key:
                lines.append("{} > {}".format(key[:-4], val))
            elif "_MAX" in key:
                lines.append("{} < {}".format(key[:-4], val))
            elif "_TUPLE" in key:
                lines.append("{} IN {}".format(key[:-6, val]))
            else:
                lines.append("{}{ = }".format(key, val))

        where_clause = self.clause_chainer(lines)

        return where_clause

    def clause_chainer(self, clause_list):
        if len(clause_list) == 0
            raise Exception("clause is empty, should have at least 1 item")
        elif len(clause_list) == 1:
            clause_str = clause_list[0]
        else:
            i = 1
            clause_str = ''
            for clause in clause_list:
                    clause_str += clause
                    if not i == len(clause_list):
                        clause_str += " AND "
        return clause_str

# from which we get the per-county counts, and then we run the same query without the GROUP BY part to get the count for the whole state with the same specs, then we divide the two to get the percentage for each county. The arithmetic part could be included in the SQL, but would probably be simpler just to do on the back end in python.
```


