# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        import collections
        self.elems = collections.defaultdict(list)

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "add":
            if query.s not in self.elems[self._hash_func(query.s)]:
                self.elems[self._hash_func(query.s)].append(query.s)
        elif query.type == "find":
            was_found = query.s in self.elems[self._hash_func(query.s)]
            self.write_search_result(was_found)
        elif query.type == "del":
            if query.s in self.elems[self._hash_func(query.s)]:
                self.elems[self._hash_func(query.s)].remove(query.s)
        else:
            self.write_chain([i for i in self.elems[query.ind][::-1]])

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
