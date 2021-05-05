import csv

def candidate_data_gen(filename='election_results.csv'):
    with open(filename, 'r') as file:
        dialect = csv.Sniffer().sniff(file.read(1000))
        reader = csv.reader(file, dialect=dialect)
        next(reader)
        yield from reader

def write_candidate_data(filename, data, header=('party', 'votes', 'percentage')):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

candidate_data = candidate_data_gen()
vote_count = dict()
for candidate, party, votes, constituency in candidate_data:
    vote_count[party] = vote_count.get(party, 0) + int(votes)

total_votes = sum(map(int, vote_count.values()))

vote_data = []
for party, votes in vote_count.items():
    vote_percent = dict()
    vote_percent['party'] = party
    vote_percent['votes'] = votes
    vote_percent['percentage'] = (votes / total_votes) * 100
    vote_data.append(vote_percent)

write_candidate_data('vote_percentage.csv', vote_data)

