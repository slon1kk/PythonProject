import csv

purchases = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    header = next(reader)
    for line in reader:
        user_id = line[0].strip('"')
        category = line[1].strip('"')
        purchases[user_id] = category

with open('visit_log.csv', 'r', encoding='utf-8') as visit_file, \
        open('funnel.csv', 'w', encoding='utf-8', newline='') as funnel_file:
    visit_reader = csv.reader(visit_file)
    funnel_writer = csv.writer(funnel_file)

    header = next(visit_reader)
    funnel_writer.writerow(['user_id', 'source', 'category'])

    for row in visit_reader:
        user_id = row[0]
        source = row[1]
        if user_id in purchases:
            funnel_writer.writerow([user_id, source, purchases[user_id]])