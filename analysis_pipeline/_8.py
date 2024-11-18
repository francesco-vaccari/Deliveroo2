import scipy.stats as stats
import numpy as np
import scipy.stats as stats

def _8(data):
    return
    n_intentions = 0
    n_intentions_with_calls = 0

    intentions_with_calls_generated_correctly = 0
    intentions_with_calls_generated_incorrectly = 0

    intention_without_calls_generated_correctly = 0
    intention_without_calls_generated_incorrectly = 0

    intention_with_calls_invalidation_after_generation_reason = []
    intention_without_calls_invalidation_after_generation_reason = []

    intention_with_calls_lines_of_code = []
    intention_without_calls_lines_of_code = []

    for typology, experiments in data.items():

        for experiment in experiments:

            for desire_id, desire in experiment['desires'].items():

                for intention in desire['intentions']:
                    calls = []
                    for id in intention['calls']:
                        if int(id) not in [1,2,3,4,5,6]:
                            calls.append(id)
                    
                    if len(calls) > 0:
                        n_intentions_with_calls += 1
                    
                    n_intentions += 1

                    if intention['invalidation_after_generation_reason'] is None:
                        if len(calls) > 0:
                            intentions_with_calls_generated_correctly += 1
                        else:
                            intention_without_calls_generated_correctly += 1
                    else:
                        if len(calls) > 0:
                            intentions_with_calls_generated_incorrectly += 1
                            intention_with_calls_invalidation_after_generation_reason.append(intention['invalidation_after_generation_reason'])
                        else:
                            intention_without_calls_generated_incorrectly += 1
                            intention_without_calls_invalidation_after_generation_reason.append(intention['invalidation_after_generation_reason'])
                    
                    if len(calls) > 0:
                        intention_with_calls_lines_of_code.append(intention['analysis']['raw']['lloc'])
                    else:
                        intention_without_calls_lines_of_code.append(intention['analysis']['raw']['lloc'])
    


    print(f"Number of intentions: {n_intentions}")
    print(f"Number of intentions with calls: {n_intentions_with_calls}")
    print()

    print(f"Fraction of intentions with calls that generated correctly: {intentions_with_calls_generated_correctly/n_intentions_with_calls}")
    print(f"Fraction of intentions with calls that generated incorrectly: {intentions_with_calls_generated_incorrectly/n_intentions_with_calls}")
    print()

    print(f"Fraction of intentions without calls that generated correctly: {intention_without_calls_generated_correctly/(n_intentions - n_intentions_with_calls)}")
    print(f"Fraction of intentions without calls that generated incorrectly: {intention_without_calls_generated_incorrectly/(n_intentions - n_intentions_with_calls)}")
    print()

    # The fact that intentions with calls generate correctly less often might due to the fact that the resulting plan is not what the LLM expected when including the intention call in the generated function.

    # Given this, I would expect that, out of the intentions with calls that didn't pass the generation phase, the reason for not passing is due to negative evaluation more often (instead of execution error) than the intentions that do not contain calls.

    execution_error = 0
    negative_evaluation = 0
    for reason in intention_with_calls_invalidation_after_generation_reason:
        if reason == 'execution_error':
            execution_error += 1
        else:
            negative_evaluation += 1
    
    print(f"Fraction of intentions with calls that didn't pass generation phase due to execution error: {execution_error/intentions_with_calls_generated_incorrectly}")
    print(f"Fraction of intentions with calls that didn't pass generation phase due to negative evaluation: {negative_evaluation/intentions_with_calls_generated_incorrectly}")

    execution_error = 0
    negative_evaluation = 0
    for reason in intention_without_calls_invalidation_after_generation_reason:
        if reason == 'execution_error':
            execution_error += 1
        else:
            negative_evaluation += 1

    print(f"Fraction of intentions without calls that didn't pass generation phase due to execution error: {execution_error/intention_without_calls_generated_incorrectly}")
    print(f"Fraction of intentions without calls that didn't pass generation phase due to negative evaluation: {negative_evaluation/intention_without_calls_generated_incorrectly}")
    print()

    # Indeed intention with calls that don't pass the generation phase fail more often due to negative evaluation than the intentions without calls.



    # Also I want to show that intentions with calls are much shorter than intentions without calls

    def confidence_interval_95(data, conf=0.95):
        data = np.array(data)
        mean = np.mean(data)
        sem = stats.sem(data)
        ci_range = sem * stats.t.ppf((1 + conf) / 2, len(data) - 1)
        lower_bound = mean - ci_range
        upper_bound = mean + ci_range
        return mean, lower_bound, upper_bound

    mean_with_calls, lower_with_calls, upper_with_calls = confidence_interval_95(intention_with_calls_lines_of_code)
    mean_without_calls, lower_without_calls, upper_without_calls = confidence_interval_95(intention_without_calls_lines_of_code)

    print(f"Average lines of code for intentions with calls: {mean_with_calls} (95% CI: {lower_with_calls} - {upper_with_calls})")
    print(f"Average lines of code for intentions without calls: {mean_without_calls} (95% CI: {lower_without_calls} - {upper_without_calls})")


# Mi aspetto che intention che chiamano altre intention implementate prima siano meno complesse e quindi con metriche migliori e mi aspetto anche che abbiano successo più spesso visto che parti sono state confermante come funzionanti in precedenza.