from client import MarketingMixModelingAdstockSaturationEstimatorClient

def main():
    client = MarketingMixModelingAdstockSaturationEstimatorClient()
    res = client.estimate_media_elasticity({'YOUTUBE_SPONSORED': 35000, 'INFLUENCER_SEEDING': 20000})
    print('Marketing Mix Modeling Estimator: ' + res['mmm_model_id'] + ' (' + str(res['channels_evaluated_count']) + ' channels)')
    print('Saturation Point: $' + str(res['diminishing_return_saturation_point_usd']) + ' | Adstock Weight: ' + str(res['carryover_adstock_weight']))
    print('Reallocation Manifest: ' + res['optimal_reallocated_budget_manifest_url'])

if __name__ == '__main__':
    main()
