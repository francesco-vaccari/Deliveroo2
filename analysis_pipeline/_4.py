import numpy as np
import scipy.stats as stats

def _4(data):    
    return
    for typology, experiments in data.items():
        first_halves_cc = []
        second_halves_cc = []
        first_halves_mi = []
        second_halves_mi = []
        first_halves_raw = []
        second_halves_raw = []
        first_halves_hal = []
        second_halves_hal = []

        n_intentions = 0

        for experiment in experiments:
            intentions_cc = []
            intentions_mi = []
            intentions_raw = []
            intentions_hal = []
            for desire_id, desire in experiment['desires'].items():
                for intention in desire['intentions']:
                    intentions_cc.append(intention['analysis']['cc']['complexity'])
                    intentions_mi.append(intention['analysis']['mi']['mi'])
                    intentions_raw.append(intention['analysis']['raw']['lloc'])
                    intentions_hal.append(intention['analysis']['hal']['effort'])
                    n_intentions += 1
            if len(intentions_cc) == 0:
                continue
            elif len(intentions_cc) == 1:
                first_half_cc = intentions_cc
                second_half_cc = intentions_cc
                first_half_mi = intentions_mi
                second_half_mi = intentions_mi
                first_half_raw = intentions_raw
                second_half_raw = intentions_raw
                first_half_hal = intentions_hal
                second_half_hal = intentions_hal
            else:
                half = len(intentions_cc) // 2
                first_half_cc = intentions_cc[:half]
                second_half_cc = intentions_cc[half:]
                first_half_mi = intentions_mi[:half]
                second_half_mi = intentions_mi[half:]
                first_half_raw = intentions_raw[:half]
                second_half_raw = intentions_raw[half:]
                first_half_hal = intentions_hal[:half]
                second_half_hal = intentions_hal[half:]
            
            first_halves_cc.append(np.mean(first_half_cc))
            second_halves_cc.append(np.mean(second_half_cc))
            first_halves_mi.append(np.mean(first_half_mi))
            second_halves_mi.append(np.mean(second_half_mi))
            first_halves_raw.append(np.mean(first_half_raw))
            second_halves_raw.append(np.mean(second_half_raw))
            first_halves_hal.append(np.mean(first_half_hal))
            second_halves_hal.append(np.mean(second_half_hal))

        cc_ttest = stats.ttest_rel(first_halves_cc, second_halves_cc)
        mi_ttest = stats.ttest_rel(first_halves_mi, second_halves_mi)
        raw_ttest = stats.ttest_rel(first_halves_raw, second_halves_raw)
        hal_ttest = stats.ttest_rel(first_halves_hal, second_halves_hal)

        if cc_ttest.pvalue < 0.05 or mi_ttest.pvalue < 0.05 or raw_ttest.pvalue < 0.05 or hal_ttest.pvalue < 0.05:
            print("Difference is significant")
            print(f"Typology: {typology}: {n_intentions} intentions")
            print(f"CC T-test: statistic={cc_ttest.statistic}, p-value={cc_ttest.pvalue}")
            print(f"MI T-test: statistic={mi_ttest.statistic}, p-value={mi_ttest.pvalue}")
            print(f"Raw T-test: statistic={raw_ttest.statistic}, p-value={raw_ttest.pvalue}")
            print(f"Hal T-test: statistic={hal_ttest.statistic}, p-value={hal_ttest.pvalue}")

    # the only significant differennce is in experiments of typology 5, where metrics are opposite of what I was expecting
    

    for typology, experiments in data.items():
        typology_cc = []
        typology_mi = []
        typology_raw = []
        typology_hal = []

        for experiment in experiments:
            experiment_cc = []
            experiment_mi = []
            experiment_raw = []
            experiment_hal = []

            for desire_id, desire in experiment['desires'].items():
                for intention in desire['intentions']:
                    experiment_cc.append(intention['analysis']['cc']['complexity'])
                    experiment_mi.append(intention['analysis']['mi']['mi'])
                    experiment_raw.append(intention['analysis']['raw']['lloc'])
                    experiment_hal.append(intention['analysis']['hal']['effort'])
                
            typology_cc.extend(experiment_cc)
            typology_mi.extend(experiment_mi)
            typology_raw.extend(experiment_raw)
            typology_hal.extend(experiment_hal)
            typology_cc_mean = np.mean(typology_cc)
            typology_mi_mean = np.mean(typology_mi)
            typology_raw_mean = np.mean(typology_raw)
            typology_hal_mean = np.mean(typology_hal)

            typology_cc_ci = stats.t.interval(0.95, len(typology_cc)-1, loc=typology_cc_mean, scale=stats.sem(typology_cc))
            typology_mi_ci = stats.t.interval(0.95, len(typology_mi)-1, loc=typology_mi_mean, scale=stats.sem(typology_mi))
            typology_raw_ci = stats.t.interval(0.95, len(typology_raw)-1, loc=typology_raw_mean, scale=stats.sem(typology_raw))
            typology_hal_ci = stats.t.interval(0.95, len(typology_hal)-1, loc=typology_hal_mean, scale=stats.sem(typology_hal))
        
        import matplotlib.pyplot as plt

    typologies = list(data.keys())
    cc_means = []
    cc_cis = []
    mi_means = []
    mi_cis = []
    raw_means = []
    raw_cis = []
    hal_means = []
    hal_cis = []

    for typology in typologies:
        typology_cc = []
        typology_mi = []
        typology_raw = []
        typology_hal = []

        for experiment in data[typology]:
            for desire_id, desire in experiment['desires'].items():
                for intention in desire['intentions']:
                    typology_cc.append(intention['analysis']['cc']['complexity'])
                    typology_mi.append(intention['analysis']['mi']['mi'])
                    typology_raw.append(intention['analysis']['raw']['lloc'])
                    typology_hal.append(intention['analysis']['hal']['effort'])

        typology_cc_mean = np.mean(typology_cc)
        typology_mi_mean = np.mean(typology_mi)
        typology_raw_mean = np.mean(typology_raw)
        typology_hal_mean = np.mean(typology_hal)

        typology_cc_ci = stats.t.interval(0.95, len(typology_cc)-1, loc=typology_cc_mean, scale=stats.sem(typology_cc))
        typology_mi_ci = stats.t.interval(0.95, len(typology_mi)-1, loc=typology_mi_mean, scale=stats.sem(typology_mi))
        typology_raw_ci = stats.t.interval(0.95, len(typology_raw)-1, loc=typology_raw_mean, scale=stats.sem(typology_raw))
        typology_hal_ci = stats.t.interval(0.95, len(typology_hal)-1, loc=typology_hal_mean, scale=stats.sem(typology_hal))

        cc_means.append(typology_cc_mean)
        cc_cis.append(typology_cc_ci)
        mi_means.append(typology_mi_mean)
        mi_cis.append(typology_mi_ci)
        raw_means.append(typology_raw_mean)
        raw_cis.append(typology_raw_ci)
        hal_means.append(typology_hal_mean)
        hal_cis.append(typology_hal_ci)

    metrics = [
        (cc_means, cc_cis, 'Cyclomatic Complexity'),
        (mi_means, mi_cis, 'Maintainability Index'),
        (raw_means, raw_cis, 'Lines of Code'),
        (hal_means, hal_cis, 'Halstead Effort')
    ]

    for metric_means, metric_cis, title in metrics:
        plt.figure(figsize=(10, 5))
        yerr = np.array([(mean - ci[0], ci[1] - mean) for mean, ci in zip(metric_means, metric_cis)]).T
        plt.errorbar([typo.split('/')[-1] for typo in typologies], metric_means, yerr=yerr, fmt='o')
        plt.title(title)
        plt.xlabel('Typology')
        plt.ylabel('Mean Value')
        plt.grid(True)
        plt.show()
    





# Mi aspetto che nel corso dell'esperimento le metriche peggiorino per via del fatto che l'agente impara a fare cose più complesse.

# Posso comparare codice generato in tipologie di esperimento diverse, più elementi nel belief set dovrebbero portare a codice più complesso sia perché ci sono più elementi e anche perché la LLM fa più "fatica" a comprendere l'ambiente.

# CC score	Rank	Risk
# 1 - 5	    A	    low - simple block
# 6 - 10	B	    low - well structured and stable block
# 11 - 20	C	    moderate - slightly complex block
# 21 - 30	D	    more than moderate - more complex block
# 31 - 40	E	    high - complex block, alarming
# 41+	    F	    very high - error-prone, unstable block

# MI score	Rank	Maintainability
# 100 - 20	A	    Very high
# 19 - 10	B	    Medium
# 9 - 0	    C	    Extremely low

'''
desires (dict)
│
├── desire_id (str) -> Each key represents a unique desire ID
│   │
│   ├── description (str) -> A description of the desire
│   ├── intentions (list of dict) -> List containing intention objects
│   │   │
│   │   ├── id (str) -> Unique ID of the intention
│   │   ├── description (str) -> Description of the intention
│   │   ├── executable_at_desire_end (bool) -> Whether it executes when the desire ends
│   │   ├── executable (bool) -> Whether it's executable at experiment end
│   │   ├── invalidation_reason (str or None) -> Reason for invalidation, if any
│   │   ├── invalidation_after_generation_reason (str or None) -> Invalidation after generation reason, if any
│   │   ├── calls (list of str) -> Functions or methods it calls
│   │   ├── called_by (list of str) -> Functions or methods that call this intention
│   │   ├── function (str) -> The function code or reference in string form
│   │   ├── analysis (dict) -> Analysis details for the intention
│   │       │
│   │       ├── cc (float) -> Cyclomatic complexity
│   │       ├── mi (float) -> Maintainability index
│   │       ├── raw (float) -> Raw analysis score
│   │       ├── hal (float) -> Halstead complexity measure
│   │
│   ├── executable (bool) -> Whether the desire is executable at the experiment end
│   ├── satisfied (bool) -> Whether the desire has been satisfied
│   ├── triggered_n_times (int) -> Number of times the desire was triggered
│   ├── evaluations (int) -> Number of times the desire was evaluated
│   ├── error (bool or None) -> Indicates whether last trigger errored out if invalidated
│   ├── trigger_function (str or None) -> Function code or reference for triggering the desire
│   ├── trigger_function_analysis (dict) -> Analysis of the trigger function, if present
│       │
│       ├── cc (float) -> Cyclomatic complexity
│       ├── mi (float) -> Maintainability index
│       ├── raw (float) -> Raw analysis score
│       ├── hal (float) -> Halstead complexity measure
'''