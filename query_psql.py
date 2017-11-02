from secret_connect import secret_connection

class PoliceQuery:
    def __init__(self):
        self.conn = secret_connection()
        self.cur = self.conn.cursor()
        # self.desired_fields = []
        # for not none in dict, append to desired fields

    def query_psql(self, query_dict):
        query = self.make_query(query_dict)
        self.cur.execute(query)
        # num_titles = self.cur.rowcount

        return self.cur.fetchall()

    def make_query(self, query_dict):
        query = ''
        query += self.selector(query_dict)
        query += "FROM FL_stops "
        if query_dict["WHERES"] is not None:
            query += self.wheres(query_dict)

        query += self.grouper()

        return query+";"

    def selector(self, query_dict):
        select_clause = "SELECT "
        # select_type = self.query_dict['select']
        # selector_funcs = {'totals': self._select_totals}
        # select_clause += selector_funcs[select_type]
        select_clause += self._select_totals()
        return select_clause

    def _select_totals(self):
        return "violation, count(*) "

    def grouper(self):
        return " GROUP BY county_name"

    def wheres(self, query_dict):
        lines = []
        for key, val in query_dict['WHERES'].items():
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
        if len(clause_list) == 0:
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

if __name__ == '__main__':
    q = PoliceQuery()
    my_dict = {'WHERES': {'driver_age_MIN': 39}}
    results = q.make_query(my_dict)
    print(results)