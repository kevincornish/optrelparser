# optrelparser
2 Inspection Machines
- 1 Ampoule
- 1 Vial
Generate pdf reports

Todo
------
Import PDF's
1. Create PostgresSQL database
2. Parse PDF's
3. Export PDF strings to database

Search.py
------
1. Pick reports to search either ampoule/vial
2. Search PDF's via batch number or name eg 'Magnesium Sulfate', will then pull up all Magnesium Sulfate batches and be able to filter through them.
3. Search specific users who have ran batches eg Username: 'kevc'
4. Search common reject %'s
5. Look at trends between batches

# setup
1. run setup.py
2. to import batches run 'main.py -d vials' or 'pdf.py -d ampoules'

