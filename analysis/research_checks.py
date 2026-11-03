"""Read-only research checks. Never imports the optimizer or writes outside this vault."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_EVEN
from pathlib import Path

VAULT = Path(__file__).resolve().parents[1]
FILES = [
    'HANDOFF.md', 'RESUME.md', 'checkpoints/STATUS.json', 'docs/evaluation.md',
    'docs/nl-build-compiler.md', 'src/pov_opt/evaluate.py',
    'src/pov_opt/character.py', 'src/pov_opt/stats.py',
    'src/pov_opt/passives.py', 'src/pov_opt/incoming.py',
    'tools/compare_builds.py', 'tools/evaluate_corpus.py', 'tests/test_evaluate.py',
    'reports/community/evaluation.json', 'reports/community/validation.json',
    'data/5.3.6/passive_nodes.json',
]


def synthetic_checks():
    # Decimal makes the six-decimal reporting example independent of float noise.
    q = lambda x: Decimal(x).quantize(Decimal('0.000001'), rounding=ROUND_HALF_EVEN)
    early = q(q('0.00000051') - q('0.00000049'))
    late = q(Decimal('0.00000051') - Decimal('0.00000049'))
    assert early == Decimal('0.000001') and late == 0
    # Two connected candidate paths: shortest is not highest utility under budget.
    candidates = [dict(nodes=['a', 't'], cost=2, utility=1),
                  dict(nodes=['b', 'c', 't'], cost=3, utility=11)]
    cheapest = min(candidates, key=lambda x: x['cost'])
    best = max((x for x in candidates if x['cost'] <= 3), key=lambda x: x['utility'])
    assert cheapest['nodes'] != best['nodes']
    # Same mean, different low-health survival: expected damage hides lethal tails.
    deterministic = [5, 5]
    variable = [0, 10]
    assert sum(deterministic) == sum(variable)
    assert sum(x >= 8 for x in deterministic) == 0
    assert sum(x >= 8 for x in variable) == 1
    return {'round_before_subtraction': str(early), 'round_after_subtraction': str(late),
            'cheapest_route': cheapest, 'best_utility_route': best,
            'equal_mean_hits': {'health': 8, 'a': deterministic, 'b': variable,
                                'lethal_fractions': [0, 0.5]}}


def main(repo):
    captured = datetime.now(timezone.utc).isoformat()
    blobs = {name: (repo / name).read_bytes() for name in FILES}
    digest = lambda b: hashlib.sha256(b).hexdigest()
    source = {name: {'sha256': digest(blob), 'bytes': len(blob)} for name, blob in blobs.items()}
    report = json.loads(blobs['reports/community/evaluation.json'])
    validation = json.loads(blobs['reports/community/validation.json'])
    legality = {b['name']: b for b in validation['builds']}
    metrics = []
    for name, item in report['builds'].items():
        e = item['evaluation']
        assert item['legality']['level_d'] == legality[name]['levels']['D'], name
        points = next(c['evidence']['cost'] for c in legality[name]['checks']
                      if c['level'] == 'D' and c['id'] == 'points')
        assert e['cost'] == points, name
        metrics.append({'build': name, 'legality': item['legality']['level_d'],
                        'points': e['cost'], 'nonzero_stats': len(e['stats']),
                        'conditional_rows': sum(e['not_counted']['conditional_rows'].values()),
                        'subject_stat_keys': len(e['not_counted']['subject_rows']),
                        'live_source_stat_keys': len(e['assumed_zero_sources']),
                        'missing_nodes': len(e['missing_nodes']),
                        'dropped_choices': len(e['dropped_choices'])})
    for pair in report['comparisons']:
        a = report['builds'][pair['a']]
        b = report['builds'][pair['b']]
        assert a['legality']['level_d'] == b['legality']['level_d'] == 'PASS'
        assert set(pair['shared_start']) <= set(a['legality']['paths']) & set(b['legality']['paths'])
        assert pair['points']['delta'] == b['evaluation']['cost'] - a['evaluation']['cost']
    nodes = json.loads(blobs['data/5.3.6/passive_nodes.json'])['records']
    negative = []
    for node in nodes:
        for row in node['mods']:
            if row['value'] < 0 and (row.get('cond') or row.get('after') or row.get('conds')):
                negative.append({'node': node['id'], 'stat': row['stat'], 'value': row['value'],
                                 'condition': row.get('cond'), 'event': row.get('after')})
    assert any(x['node'] == 'own10355' and x['stat'] == 'CostPct' for x in negative)
    changed = [name for name, blob in blobs.items() if digest((repo / name).read_bytes()) != digest(blob)]
    result = {'captured_utc': captured, 'source_root': str(repo),
              'method': 'static reads and JSON checks; no optimizer imports or game execution',
              'changed_during_capture': changed, 'snapshot_atomic': False,
              'mutation_gate': json.loads(blobs['checkpoints/STATUS.json'])['mutation_gate'],
              'corpus': metrics, 'comparisons_checked': len(report['comparisons']),
              'negative_conditional_node_rows': negative,
              'synthetic_checks': synthetic_checks(),
              'limitations': ['Static files can be temporary mutation variants.',
                              'Hash recheck detects changes during capture, not all cross-file inconsistency.',
                              'Synthetic examples are mathematical counterexamples, not game simulations.']}
    (VAULT / 'evidence' / 'source-manifest.json').write_text(json.dumps(
        {'captured_utc': captured, 'source_root': str(repo), 'files': source}, indent=2) + '\n', encoding='utf-8')
    (VAULT / 'evidence' / 'checks.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'builds_checked': len(metrics), 'comparisons_checked': len(report['comparisons']),
                      'negative_conditional_rows': len(negative), 'changed_during_capture': changed,
                      'synthetic_checks': 'PASS'}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repo', type=Path)
    main(parser.parse_args().repo)
