import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def _6_2(data):
    intention_metrics_by_n_objectives = {}
    intention_metrics_by_description_length = {}
    adaptive_intentions_metrics = []
    grounded_intentions_metrics = []
    predetermined_intentions_metrics = []
    desire_n_objectives_for_adaptive = []
    intention_n_objectives_for_adaptive = []
    desire_lengths_for_adaptive = []
    intention_lengths_for_adaptive = []
    desire_n_objectives_for_grounded = []
    intention_n_objectives_for_grounded = []
    desire_lengths_for_grounded = []
    intention_lengths_for_grounded = []
    desire_n_objectives_for_predetermined = []
    intention_n_objectives_for_predetermined = []
    desire_lengths_for_predetermined = []
    intention_lengths_for_predetermined = []
    for typology, experiments in data.items():
        for experiment in experiments:
            experiment_intentions_metrics = {}

            desire_description_lengths = {}
            intention_description_lenghts = {}
            ignore_intentions_ids = []
            for desire_id, desire in experiment['desires'].items():
                desire_description_lengths[desire_id] = len(desire['description'])
                for intention in desire['intentions']:
                    calls = []
                    for id in intention['calls']:
                        if int(id) not in [1,2,3,4,5,6]:
                            calls.append(id)
                    if len(calls) > 0:
                        ignore_intentions_ids.append(intention['id'])
                    else:
                        experiment_intentions_metrics[intention['id']] = intention['analysis']
                        if len(intention['description']) not in intention_metrics_by_description_length:
                            intention_metrics_by_description_length[len(intention['description'])] = []
                        intention_metrics_by_description_length[len(intention['description'])].append(intention['analysis'])
                        intention_description_lenghts[intention['id']] = len(intention['description'])
            

            for desire_id, desire in experiment['desire_analysis'].items():
                if desire_id not in desire_description_lengths:
                    raise ValueError(f"Desire {desire_id} not found in desire_description_lengths")
                for intention_id, intention in desire['intentions'].items():
                    if int(intention_id) in ignore_intentions_ids:
                        continue
                    assert int(intention_id) in experiment_intentions_metrics
                    assert int(intention_id) in intention_description_lenghts
                    if intention['n_objectives'] not in intention_metrics_by_n_objectives:
                        intention_metrics_by_n_objectives[intention['n_objectives']] = []
                    intention_metrics_by_n_objectives[intention['n_objectives']].append(experiment_intentions_metrics[int(intention_id)])
                    if intention['category'] == 'adaptive':
                        adaptive_intentions_metrics.append(experiment_intentions_metrics[int(intention_id)])
                        desire_n_objectives_for_adaptive.append(desire['n_objectives'])
                        desire_lengths_for_adaptive.append(desire_description_lengths[desire_id])
                        intention_n_objectives_for_adaptive.append(intention['n_objectives'])
                        intention_lengths_for_adaptive.append(intention_description_lenghts[int(intention_id)])
                    elif intention['category'] == 'grounded':
                        grounded_intentions_metrics.append(experiment_intentions_metrics[int(intention_id)])
                        desire_n_objectives_for_grounded.append(desire['n_objectives'])
                        desire_lengths_for_grounded.append(desire_description_lengths[desire_id])
                        intention_n_objectives_for_grounded.append(intention['n_objectives'])
                        intention_lengths_for_grounded.append(intention_description_lenghts[int(intention_id)])
                    elif intention['category'] == 'predetermined':
                        predetermined_intentions_metrics.append(experiment_intentions_metrics[int(intention_id)])
                        desire_n_objectives_for_predetermined.append(desire['n_objectives'])
                        desire_lengths_for_predetermined.append(desire_description_lengths[desire_id])
                        intention_n_objectives_for_predetermined.append(intention['n_objectives'])
                        intention_lengths_for_predetermined.append(intention_description_lenghts[int(intention_id)])
                    else:
                        raise ValueError(f"Unknown category: {intention['category']}")


    print(f'Number of intentions by number of objectives:')
    for n in sorted(intention_metrics_by_n_objectives.keys()):
        print(f"  {n}: {len(intention_metrics_by_n_objectives[n])}")

    average_intention_metrics_by_n_objectives = {}
    for n, metrics in intention_metrics_by_n_objectives.items():
        ccs, mis, raws, hals = [], [], [], []
        for metric in metrics:
            cc, mi, raw, hal = metric['cc']['complexity'], metric['mi']['mi'], metric['raw']['lloc'], metric['hal']['effort']
            ccs.append(cc)
            mis.append(mi)
            raws.append(raw)
            hals.append(hal)

        average_intention_metrics_by_n_objectives[n] = {
            'cc': sum(ccs) / len(ccs),
            'cc_confidence_interval': stats.t.interval(0.95, len(ccs)-1, loc=np.mean(ccs), scale=stats.sem(ccs)),
            'mi': sum(mis) / len(mis),
            'mi_confidence_interval': stats.t.interval(0.95, len(mis)-1, loc=np.mean(mis), scale=stats.sem(mis)),
            'raw': sum(raws) / len(raws),
            'raw_confidence_interval': stats.t.interval(0.95, len(raws)-1, loc=np.mean(raws), scale=stats.sem(raws)),
            'hal': sum(hals) / len(hals),
            'hal_confidence_interval': stats.t.interval(0.95, len(hals)-1, loc=np.mean(hals), scale=stats.sem(hals))
        }
    
    n_objectives = []
    ccs, mis, raws, hals = [], [], [], []
    cc_intervals, mi_intervals, raw_intervals, hal_intervals = [], [], [], []
    for n, metrics in sorted(average_intention_metrics_by_n_objectives.items()):
        n_objectives.append(n)
        ccs.append(metrics['cc'])
        mis.append(metrics['mi'])
        raws.append(metrics['raw'])
        hals.append(metrics['hal'])
        if n in [1, 2, 3, 4, 5, 6]:
            cc_intervals.append(metrics['cc_confidence_interval'])
            mi_intervals.append(metrics['mi_confidence_interval'])
            raw_intervals.append(metrics['raw_confidence_interval'])
            hal_intervals.append(metrics['hal_confidence_interval'])
        else:
            cc_intervals.append((metrics['cc'], metrics['cc']))
            mi_intervals.append((metrics['mi'], metrics['mi']))
            raw_intervals.append((metrics['raw'], metrics['raw']))
            hal_intervals.append((metrics['hal'], metrics['hal']))

    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    plt.axhspan(0, 5, facecolor='green', alpha=0.3)
    plt.axhspan(5, 10, facecolor='lightgreen', alpha=0.3)
    plt.axhspan(10, 20, facecolor='yellow', alpha=0.3)
    plt.axhspan(20, 30, facecolor='orange', alpha=0.3)
    plt.grid(axis='y', linestyle='dashed')
    plt.errorbar(n_objectives, ccs, yerr=[(top - bot) / 2 for bot, top in cc_intervals], label='Cyclomatic Complexity', marker='o', capsize=5)
    plt.xlabel('Number of Objectives')
    plt.ylabel('Cyclomatic Complexity')
    plt.ylim(6, 25) # 6 25
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/cc_by_n_objectives_without.png', dpi=400)

    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    plt.axhspan(20, 100, facecolor='green', alpha=0.3)
    plt.grid(axis='y', linestyle='dashed')
    plt.errorbar(n_objectives, mis, yerr=[(top - bot) / 2 for bot, top in mi_intervals], label='Maintainability Index', marker='o', capsize=5)
    plt.xlabel('Number of Objectives')
    plt.ylabel('Maintainability Index')
    plt.ylim(43, 64) # 43 62
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/mi_by_n_objectives_without.png', dpi=400)

    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    plt.grid(axis='y', linestyle='dashed')
    plt.errorbar(n_objectives, raws, yerr=[(top - bot) / 2 for bot, top in raw_intervals], label='Logical Lines of Code', marker='o', capsize=5)
    plt.xlabel('Number of Objectives')
    plt.ylabel('Logical Lines of Code')
    plt.ylim(13, 38) # 13 38
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/raw_by_n_objectives_without.png', dpi=400)

    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    plt.grid(axis='y', linestyle='dashed')
    plt.errorbar(n_objectives, hals, yerr=[(top - bot) / 2 for bot, top in hal_intervals], label='Halstead Effort', marker='o', capsize=5)
    plt.xlabel('Number of Objectives')
    plt.ylabel('Halstead Effort')
    plt.ylim(120, 2350) # 120 2350
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/hal_by_n_objectives_without.png', dpi=400)






    # bin_size = 10
    # print(f'Number description lengths: {len(intention_metrics_by_description_length)}')
    # n_int = 0
    # for k, v in intention_metrics_by_description_length.items():
    #     n_int += len(v)
    # print(f'Number intentions: {n_int}')

    # binned_intention_metrics_by_description_length = {}
    # for length, metrics in intention_metrics_by_description_length.items():
    #     bin_key = (length // bin_size) * bin_size
    #     if bin_key not in binned_intention_metrics_by_description_length:
    #         binned_intention_metrics_by_description_length[bin_key] = []
    #     binned_intention_metrics_by_description_length[bin_key].extend(metrics)
    
    # for bin_key in sorted(binned_intention_metrics_by_description_length.keys()):
    #     print(f"{bin_key}: {len(binned_intention_metrics_by_description_length[bin_key])}")

    # average_intention_metrics_by_description_length = {}
    # for bin_key, metrics in binned_intention_metrics_by_description_length.items():
    #     ccs, mis, raws, hals = [], [], [], []
    #     for metric in metrics:
    #         cc, mi, raw, hal = metric['cc']['complexity'], metric['mi']['mi'], metric['raw']['lloc'], metric['hal']['effort']
    #         ccs.append(cc)
    #         mis.append(mi)
    #         raws.append(raw)
    #         hals.append(hal)

    #     average_intention_metrics_by_description_length[bin_key] = {
    #         'cc': sum(ccs) / len(ccs),
    #         'cc_confidence_interval': stats.t.interval(0.95, len(ccs)-1, loc=np.mean(ccs), scale=stats.sem(ccs)),
    #         'mi': sum(mis) / len(mis),
    #         'mi_confidence_interval': stats.t.interval(0.95, len(mis)-1, loc=np.mean(mis), scale=stats.sem(mis)),
    #         'raw': sum(raws) / len(raws),
    #         'raw_confidence_interval': stats.t.interval(0.95, len(raws)-1, loc=np.mean(raws), scale=stats.sem(raws)),
    #         'hal': sum(hals) / len(hals),
    #         'hal_confidence_interval': stats.t.interval(0.95, len(hals)-1, loc=np.mean(hals), scale=stats.sem(hals))
    #     }
    
    # description_lengths = []
    # ccs, mis, raws, hals = [], [], [], []
    # cc_intervals, mi_intervals, raw_intervals, hal_intervals = [], [], [], []
    # for bin_key, metrics in sorted(average_intention_metrics_by_description_length.items()):
    #     description_lengths.append(bin_key)
    #     ccs.append(metrics['cc'])
    #     mis.append(metrics['mi'])
    #     raws.append(metrics['raw'])
    #     hals.append(metrics['hal'])
    #     cc_intervals.append(metrics['cc_confidence_interval'])
    #     mi_intervals.append(metrics['mi_confidence_interval'])
    #     raw_intervals.append(metrics['raw_confidence_interval'])
    #     hal_intervals.append(metrics['hal_confidence_interval'])
        
    # fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # axs[0, 0].errorbar(description_lengths, ccs, yerr=[(top - bot) / 2 for bot, top in cc_intervals], label='Cyclomatic Complexity (cc)', marker='o', capsize=5)
    # axs[0, 0].set_xlabel('Description Length (Binned)')
    # axs[0, 0].set_ylabel('Cyclomatic Complexity (cc)')
    # axs[0, 0].set_title('Cyclomatic Complexity vs Description Length')
    # axs[0, 0].grid(True)

    # axs[0, 1].errorbar(description_lengths, mis, yerr=[(top - bot) / 2 for bot, top in mi_intervals], label='Maintainability Index (mi)', marker='o', capsize=5)
    # axs[0, 1].set_xlabel('Description Length (Binned)')
    # axs[0, 1].set_ylabel('Maintainability Index (mi)')
    # axs[0, 1].set_title('Maintainability Index vs Description Length')
    # axs[0, 1].grid(True)

    # axs[1, 0].errorbar(description_lengths, raws, yerr=[(top - bot) / 2 for bot, top in raw_intervals], label='Logical Lines of Code (raw)', marker='o', capsize=5)
    # axs[1, 0].set_xlabel('Description Length (Binned)')
    # axs[1, 0].set_ylabel('Logical Lines of Code (raw)')
    # axs[1, 0].set_title('Logical Lines of Code vs Description Length')
    # axs[1, 0].grid(True)

    # axs[1, 1].errorbar(description_lengths, hals, yerr=[(top - bot) / 2 for bot, top in hal_intervals], label='Halstead Effort (hal)', marker='o', capsize=5)
    # axs[1, 1].set_xlabel('Description Length (Binned)')
    # axs[1, 1].set_ylabel('Halstead Effort (hal)')
    # axs[1, 1].set_title('Halstead Effort vs Description Length')
    # axs[1, 1].grid(True)

    # plt.tight_layout()
    # plt.show()





    # Adaptive binning
    target_per_bin = 40
    adaptive_bins = []
    current_bin = []
    current_count = 0

    bin_size = 1

    binned_intention_metrics_by_description_length = {}
    for length, metrics in intention_metrics_by_description_length.items():
        bin_key = (length // bin_size) * bin_size
        if bin_key not in binned_intention_metrics_by_description_length:
            binned_intention_metrics_by_description_length[bin_key] = []
        binned_intention_metrics_by_description_length[bin_key].extend(metrics)
    
    data_distribution = {length: len(metrics) for length, metrics in intention_metrics_by_description_length.items()}

    for length, count in sorted(data_distribution.items()):
        current_bin.append(length)
        current_count += count
        if current_count >= target_per_bin:
            print(current_count)
            adaptive_bins.append((min(current_bin), max(current_bin)))
            current_bin = []
            current_count = 0

    if current_bin:  # Handle remaining data
        print(current_count)
        adaptive_bins.append((min(current_bin), max(current_bin)))

    # Bin metrics according to adaptive bins
    binned_intention_metrics_by_description_length = {bin_range: [] for bin_range in adaptive_bins}

    for length, metrics in intention_metrics_by_description_length.items():
        for bin_range in adaptive_bins:
            if bin_range[0] <= length <= bin_range[1]:
                binned_intention_metrics_by_description_length[bin_range].extend(metrics)
                break

    # Compute average metrics and confidence intervals for each bin
    average_intention_metrics_by_description_length = {}

    for bin_key, metrics in binned_intention_metrics_by_description_length.items():
        ccs, mis, raws, hals = [], [], [], []
        for metric in metrics:
            cc, mi, raw, hal = metric['cc']['complexity'], metric['mi']['mi'], metric['raw']['lloc'], metric['hal']['effort']
            ccs.append(cc)
            mis.append(mi)
            raws.append(raw)
            hals.append(hal)

        average_intention_metrics_by_description_length[bin_key] = {
            'cc': np.mean(ccs),
            'cc_confidence_interval': stats.t.interval(0.95, len(ccs)-1, loc=np.mean(ccs), scale=stats.sem(ccs)),
            'mi': np.mean(mis),
            'mi_confidence_interval': stats.t.interval(0.95, len(mis)-1, loc=np.mean(mis), scale=stats.sem(mis)),
            'raw': np.mean(raws),
            'raw_confidence_interval': stats.t.interval(0.95, len(raws)-1, loc=np.mean(raws), scale=stats.sem(raws)),
            'hal': np.mean(hals),
            'hal_confidence_interval': stats.t.interval(0.95, len(hals)-1, loc=np.mean(hals), scale=stats.sem(hals))
        }

    # Plotting
    description_lengths = []
    ccs, mis, raws, hals = [], [], [], []
    cc_intervals, mi_intervals, raw_intervals, hal_intervals = [], [], [], []

    for bin_key, metrics in sorted(average_intention_metrics_by_description_length.items()):
        description_lengths.append(f"{bin_key[0]}-{bin_key[1]}")
        ccs.append(metrics['cc'])
        mis.append(metrics['mi'])
        raws.append(metrics['raw'])
        hals.append(metrics['hal'])
        cc_intervals.append(metrics['cc_confidence_interval'])
        mi_intervals.append(metrics['mi_confidence_interval'])
        raw_intervals.append(metrics['raw_confidence_interval'])
        hal_intervals.append(metrics['hal_confidence_interval'])

    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    plt.axhspan(0, 5, facecolor='green', alpha=0.3)
    plt.axhspan(5, 10, facecolor='lightgreen', alpha=0.3)
    plt.axhspan(10, 20, facecolor='yellow', alpha=0.3)
    plt.axhspan(20, 30, facecolor='orange', alpha=0.3)
    plt.grid(axis='y', linestyle='dashed')
    plt.errorbar(description_lengths, ccs, yerr=[(top - bot) / 2 for bot, top in cc_intervals], label='Cyclomatic Complexity (cc)', marker='o', capsize=5)
    plt.xlabel('Description Length')
    plt.ylabel('Cyclomatic Complexity')
    plt.ylim(5, 18) # 5 18
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/cc_by_description_length_without.png', dpi=400)

    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    plt.axhspan(20, 100, facecolor='green', alpha=0.3)
    plt.grid(axis='y', linestyle='dashed')
    plt.errorbar(description_lengths, mis, yerr=[(top - bot) / 2 for bot, top in mi_intervals], label='Maintainability Index (mi)', marker='o', capsize=5)
    plt.xlabel('Description Length')
    plt.ylabel('Maintainability Index')
    plt.ylim(48, 67) # 48 62
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/mi_by_description_length_without.png', dpi=400)

    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    plt.grid(axis='y', linestyle='dashed')
    plt.errorbar(description_lengths, raws, yerr=[(top - bot) / 2 for bot, top in raw_intervals], label='Logical Lines of Code (raw)', marker='o', capsize=5)
    plt.xlabel('Description Length')
    plt.ylabel('Logical Lines of Code')
    plt.ylim(13, 31) # 13 31
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/raw_by_description_length_without.png', dpi=400)

    plt.rc('font', size=15)
    plt.rc('axes', axisbelow=True)
    plt.figure(figsize=(9, 6))
    plt.grid(axis='y', linestyle='dashed')
    plt.errorbar(description_lengths, hals, yerr=[(top - bot) / 2 for bot, top in hal_intervals], label='Halstead Effort (hal)', marker='o', capsize=5)
    plt.xlabel('Description Length')
    plt.ylabel('Halstead Effort')
    plt.ylim(0, 1790) # 80 1345
    plt.tight_layout()
    # plt.show()
    plt.savefig('/Users/francesco/Desktop/Master-Thesis/images/hal_by_description_length_without.png', dpi=400)











    def print_comparison_with_confidence_interval(adaptive_metrics, grounded_metrics, predetermined_metrics):
        def extract_metrics(metrics):
            ccs, mis, raws, hals = [], [], [], []
            for metric in metrics:
                ccs.append(metric['cc']['complexity'])
                mis.append(metric['mi']['mi'])
                raws.append(metric['raw']['lloc'])
                hals.append(metric['hal']['effort'])
            return ccs, mis, raws, hals

        def mean_confidence_interval(data, confidence=0.95):
            a = 1.0 * np.array(data)
            n = len(a)
            m, se = np.mean(a), stats.sem(a)
            h = se * stats.t.ppf((1 + confidence) / 2., n-1)
            return m, m-h, m+h

        adaptive_ccs, adaptive_mis, adaptive_raws, adaptive_hals = extract_metrics(adaptive_metrics)
        grounded_ccs, grounded_mis, grounded_raws, grounded_hals = extract_metrics(grounded_metrics)
        predetermined_ccs, predetermined_mis, predetermined_raws, predetermined_hals = extract_metrics(predetermined_metrics)

        metrics = {
            'Cyclomatic Complexity (cc)': (adaptive_ccs, grounded_ccs, predetermined_ccs),
            'Maintainability Index (mi)': (adaptive_mis, grounded_mis, predetermined_mis),
            'Logical Lines of Code (raw)': (adaptive_raws, grounded_raws, predetermined_raws),
            'Halstead Effort (hal)': (adaptive_hals, grounded_hals, predetermined_hals)
        }

        for metric_name, (adaptive, grounded, predetermined) in metrics.items():
            adaptive_mean, adaptive_lower, adaptive_upper = mean_confidence_interval(adaptive)
            grounded_mean, grounded_lower, grounded_upper = mean_confidence_interval(grounded)
            predetermined_mean, predetermined_lower, predetermined_upper = mean_confidence_interval(predetermined)

            print(f"{metric_name}:")
            print(f"  Adaptive: {adaptive_mean:.2f} [{adaptive_lower:.2f}, {adaptive_upper:.2f}]")
            print(f"  Grounded: {grounded_mean:.2f} [{grounded_lower:.2f}, {grounded_upper:.2f}]")
            print(f"  Predetermined: {predetermined_mean:.2f} [{predetermined_lower:.2f}, {predetermined_upper:.2f}]")
            print()

    print_comparison_with_confidence_interval(adaptive_intentions_metrics, grounded_intentions_metrics, predetermined_intentions_metrics)

    def mean_confidence_interval(data, confidence=0.95):
        a = 1.0 * np.array(data)
        n = len(a)
        m, se = np.mean(a), stats.sem(a)
        h = se * stats.t.ppf((1 + confidence) / 2., n-1)
        return m, m-h, m+h

    # average n_objectives of desire when intention is adaptive, grounded, predetermined
    # adaptive_mean, adaptive_lower, adaptive_upper = mean_confidence_interval(desire_n_objectives_for_adaptive)
    # grounded_mean, grounded_lower, grounded_upper = mean_confidence_interval(desire_n_objectives_for_grounded)
    # predetermined_mean, predetermined_lower, predetermined_upper = mean_confidence_interval(desire_n_objectives_for_predetermined)
    # print("Average number of objectives of desire when intention is adaptive:")
    # print(f"{adaptive_mean:.2f} [{adaptive_lower:.2f}, {adaptive_upper:.2f}]")
    # print("Average number of objectives of desire when intention is grounded:")
    # print(f"{grounded_mean:.2f} [{grounded_lower:.2f}, {grounded_upper:.2f}]")
    # print("Average number of objectives of desire when intention is predetermined:")
    # print(f"{predetermined_mean:.2f} [{predetermined_lower:.2f}, {predetermined_upper:.2f}]")

    # average n_objectives of intention when intention is adaptive, grounded, predetermined
    adaptive_mean, adaptive_lower, adaptive_upper = mean_confidence_interval(intention_n_objectives_for_adaptive)
    grounded_mean, grounded_lower, grounded_upper = mean_confidence_interval(intention_n_objectives_for_grounded)
    predetermined_mean, predetermined_lower, predetermined_upper = mean_confidence_interval(intention_n_objectives_for_predetermined)
    print("Average number of objectives of intention when intention is adaptive:")
    print(f"{adaptive_mean:.2f} [{adaptive_lower:.2f}, {adaptive_upper:.2f}]")
    print("Average number of objectives of intention when intention is grounded:")
    print(f"{grounded_mean:.2f} [{grounded_lower:.2f}, {grounded_upper:.2f}]")
    print("Average number of objectives of intention when intention is predetermined:")
    print(f"{predetermined_mean:.2f} [{predetermined_lower:.2f}, {predetermined_upper:.2f}]")

    # average length of desire description when intention is adaptive, grounded, predetermined
    # adaptive_mean, adaptive_lower, adaptive_upper = mean_confidence_interval(desire_lengths_for_adaptive)
    # grounded_mean, grounded_lower, grounded_upper = mean_confidence_interval(desire_lengths_for_grounded)
    # predetermined_mean, predetermined_lower, predetermined_upper = mean_confidence_interval(desire_lengths_for_predetermined)
    # print("Average length of desire description when intention is adaptive:")
    # print(f"{adaptive_mean:.2f} [{adaptive_lower:.2f}, {adaptive_upper:.2f}]")
    # print("Average length of desire description when intention is grounded:")
    # print(f"{grounded_mean:.2f} [{grounded_lower:.2f}, {grounded_upper:.2f}]")
    # print("Average length of desire description when intention is predetermined:")
    # print(f"{predetermined_mean:.2f} [{predetermined_lower:.2f}, {predetermined_upper:.2f}]")

    # average length of intention description when intention is adaptive, grounded, predetermined
    adaptive_mean, adaptive_lower, adaptive_upper = mean_confidence_interval(intention_lengths_for_adaptive)
    grounded_mean, grounded_lower, grounded_upper = mean_confidence_interval(intention_lengths_for_grounded)
    predetermined_mean, predetermined_lower, predetermined_upper = mean_confidence_interval(intention_lengths_for_predetermined)
    print("Average length of intention description when intention is adaptive:")
    print(f"{adaptive_mean:.2f} [{adaptive_lower:.2f}, {adaptive_upper:.2f}]")
    print("Average length of intention description when intention is grounded:")
    print(f"{grounded_mean:.2f} [{grounded_lower:.2f}, {grounded_upper:.2f}]")
    print("Average length of intention description when intention is predetermined:")
    print(f"{predetermined_mean:.2f} [{predetermined_lower:.2f}, {predetermined_upper:.2f}]")




# vedere se a desire o intention con più obiettivi, o con più caratteri nella descrizione, corrispondono funzioni peggiori sia nel senso di metriche che nel senso di human analysis con funzioni a, g, p (a meno di funzioni con chiamate ad altre all'interno)

# controllare se nelle funzioni g ci sono più righe di codice (e forse anche peggiori complessivamente) perché sono più lunghe e complesse e quindi cercano di tagliare corto in altre parte tipo meno astrazione e vanno a inserire direttamente coordinate che vedono nel belief set

# Una cosa da considerare è che intention con molti obiettivi ma che contengono chiamate ad altre intention hanno probabilmente metriche migliore perché appunto sono più corte per via delle intention chiamate.