import numpy as np
from scipy import stats

def _7(data):
    return
    desires_satisfied_trigger_executable = []
    desires_satisfied_trigger_not_executable = []
    desires_satisfied_no_trigger = []
    desires_not_satisfied = []

    intentions_generated_correctly = []
    intentions_not_generated_correctly = []

    for typology, experiments in data.items():

        for experiment in experiments:

            for desire_id, desire in experiment['desires'].items():

                desire_result = ''
                if desire['satisfied']:
                    if desire['trigger_function'] is None:
                        desire_result = 'no_trigger'
                    if desire['trigger_function'] is not None and desire['executable']:
                        desire_result = 'trigger_executable'
                    if desire['trigger_function'] is not None and not desire['executable']:
                        desire_result = 'trigger_not_executable'
                if not desire['satisfied']:
                    desire_result = 'not_satisfied'
                
                for intention in desire['intentions']:
                    
                    metric = intention['analysis']
                    cc, mi, raw, hal = metric['cc']['complexity'], metric['mi']['mi'], metric['raw']['lloc'], metric['hal']['effort']
                    if desire_result == 'trigger_executable':
                        desires_satisfied_trigger_executable.append({'cc': cc, 'mi': mi, 'raw': raw, 'hal': hal})
                    if desire_result == 'trigger_not_executable':
                        desires_satisfied_trigger_not_executable.append({'cc': cc, 'mi': mi, 'raw': raw, 'hal': hal})
                    if desire_result == 'no_trigger':
                        desires_satisfied_no_trigger.append({'cc': cc, 'mi': mi, 'raw': raw, 'hal': hal})
                    if desire_result == 'not_satisfied':
                        desires_not_satisfied.append({'cc': cc, 'mi': mi, 'raw': raw, 'hal': hal})
                    
                    if intention['invalidation_after_generation_reason'] is None:
                        intentions_generated_correctly.append({'cc': cc, 'mi': mi, 'raw': raw, 'hal': hal})
                    else:
                        intentions_not_generated_correctly.append({'cc': cc, 'mi': mi, 'raw': raw, 'hal': hal})
    


    desires_satisfied = desires_satisfied_trigger_executable + desires_satisfied_trigger_not_executable + desires_satisfied_no_trigger
    print('Number intentions in desires satisfied:', len(desires_satisfied))
    print('Number intentions in desires not satisfied:', len(desires_not_satisfied))

    desires_satisfied_ccs = [desire['cc'] for desire in desires_satisfied]
    desires_satisfied_mis = [desire['mi'] for desire in desires_satisfied]
    desires_satisfied_raws = [desire['raw'] for desire in desires_satisfied]
    desires_satisfied_hals = [desire['hal'] for desire in desires_satisfied]

    desires_not_satisfied_ccs = [desire['cc'] for desire in desires_not_satisfied]
    desires_not_satisfied_mis = [desire['mi'] for desire in desires_not_satisfied]
    desires_not_satisfied_raws = [desire['raw'] for desire in desires_not_satisfied]
    desires_not_satisfied_hals = [desire['hal'] for desire in desires_not_satisfied]

    ttest_results = {}
    ttest_results['cc'] = stats.ttest_ind(desires_satisfied_ccs, desires_not_satisfied_ccs, equal_var=False)
    ttest_results['mi'] = stats.ttest_ind(desires_satisfied_mis, desires_not_satisfied_mis, equal_var=False)
    ttest_results['raw'] = stats.ttest_ind(desires_satisfied_raws, desires_not_satisfied_raws, equal_var=False)
    ttest_results['hal'] = stats.ttest_ind(desires_satisfied_hals, desires_not_satisfied_hals, equal_var=False)

    for metric, result in ttest_results.items():
        print(f'T-test for {metric}: statistic={result.statistic}, p-value={result.pvalue}')
        # not even close to being significant

    




    print('Number intentions generated correctly:', len(intentions_generated_correctly))
    print('Number intentions not generated correctly:', len(intentions_not_generated_correctly))

    intentions_generated_correctly_ccs = [intention['cc'] for intention in intentions_generated_correctly]
    intentions_generated_correctly_mis = [intention['mi'] for intention in intentions_generated_correctly]
    intentions_generated_correctly_raws = [intention['raw'] for intention in intentions_generated_correctly]
    intentions_generated_correctly_hals = [intention['hal'] for intention in intentions_generated_correctly]

    intentions_not_generated_correctly_ccs = [intention['cc'] for intention in intentions_not_generated_correctly]
    intentions_not_generated_correctly_mis = [intention['mi'] for intention in intentions_not_generated_correctly]
    intentions_not_generated_correctly_raws = [intention['raw'] for intention in intentions_not_generated_correctly]
    intentions_not_generated_correctly_hals = [intention['hal'] for intention in intentions_not_generated_correctly]

    ttest_results = {}
    ttest_results['cc'] = stats.ttest_ind(intentions_generated_correctly_ccs, intentions_not_generated_correctly_ccs, equal_var=False)
    ttest_results['mi'] = stats.ttest_ind(intentions_generated_correctly_mis, intentions_not_generated_correctly_mis, equal_var=False)
    ttest_results['raw'] = stats.ttest_ind(intentions_generated_correctly_raws, intentions_not_generated_correctly_raws, equal_var=False)
    ttest_results['hal'] = stats.ttest_ind(intentions_generated_correctly_hals, intentions_not_generated_correctly_hals, equal_var=False)

    for metric, result in ttest_results.items():
        print(f'T-test for {metric}: statistic={result.statistic}, p-value={result.pvalue}')
        # close to being significant for cyclomatic complexity, complexity is higher in intentions that are not generated correctly




# Senza guardare alla tipologia di esperimento, fare medie di metriche delle seguenti categorie:

# Desire:
# - satisfied con trigger function e executable alla fine dell'esperimento (executable at desire end)
# - satisfied con trigger function ma non executable alla fine dell'esperimento (numero trigger)
# - satisfied senza trigger function
# - non satisfied

# Intention:
# - generazione corretta e executable alla fine dell'esperimento
# - generazione corretta ma non executable alla fine dell'esperimento, invalidata durante desire trigger
# - generazione corretta ma non executable alla fine dell'esperimento, invalidata per via di dependency
# - generazione non corretta per via di errore di esecuzione
# - generazione non corretta per via di valutazione negativa

# e vedere se le categorie funzionanti contengono codice con metriche migliori
# Anche qua posso fare con ttest e vedere se le differenze sono significative


# Dato il desire, prendo le metriche di tutte le intention che gli appartengono, anche se solo alcune sono eseguibili