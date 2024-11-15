def _5(data):
    return
    total_bad = 0
    pos = []
    for typology, experiments in data.items():
        n_bad = 0
        for experiment in experiments:
            experiment_categories = []
            bad = []
            for desire_id, desire in experiment['desire_analysis'].items():
                # print(desire['n_objectives'])
                for intention_id, intention in desire['intentions'].items():
                    # print(intention['n_objectives'])
                    # print(intention['one_action'])
                    experiment_categories.append(intention['category'][0])
                    if intention['category'][0] == 'g' or intention['category'][0] == 'p':
                        bad.append(1)
                        n_bad += 1
                    else:
                        bad.append(0)

            if sum(bad) > 0:
                for i in range(len(bad)):
                    if bad[i] == 1:
                        pos.append((i+1, len(bad)))
                        total_bad += 1
        
        print(f'{typology} - Total number of bad intentions: {n_bad}')
            
    print('Total number of intentions either grounded or predetermined: ', total_bad)

    for fraction in [2, 3, 4, 5, 6, 7, 8]:
        last = 0
        total = 0
        for (a, b) in pos:
            c = b / fraction
            d = c * (fraction - 1)
            d = int(d)
            if a > d:
                last += 1
            total += 1

        print(f'Bad intentions found in last 1/{fraction} of intentions: {last}/{total}')

    # Effettivamente ci sono un po' più di funzioni peggiori alla fine dell'esperimento, però non direi che sono abbastanza da trarre delle conclusioni effettive
    # Stessa cosa tra categorie diverse, ci sono più funzioni peggiori nelle tipologie 5-8 rispetto alle 1-4 e anche all'interno della 1-4 le peggiori sono in 3 e 4 ma questo potrebbe anche essere dovuto al fatto che nelle prime tipologie ci sono proprio meno intentions.



# nel corso dell'esperimento ho notato che le funzioni tendevano a essere peggiori secondo la human analysis verso la fine dell'esperimento
# stessa cosa tra categorie diverse, più la tipologia è alta più ci sono funzioni fatte male secondo me