#!/usr/bin/env python3
import os
import subprocess
import sys

# Get all files from split_files
sys.path.insert(0, r'C:\StockSharp\AlgoTradingLib\ru\pedia')

# List of all 439 files
all_files = """rabbi_trust.md
race_to_the_bottom.md
racketeering.md
rally.md
ramp_up.md
random_forests_in_trading.md
random_variables.md
random_walk_theory.md
range.md
range_bound_market.md
range_breakout.md
range_trading.md
rankia.md
ratchet_effect.md
rate_of_change_(roc).md
rate_of_return.md
rate_of_return_analysis.md
rate_of_return_decomposition.md
rate_of_return_forecasting.md
rate_of_return_metrics.md
rate_of_return_stability.md
rate-and-term_refinance.md
rating.md
ratio_analysis.md
rational_behavior.md
rational_choice_theory.md
rational_expectations_theory.md
rationalization.md
rationing.md
ravenpack.md
raw_beta_analysis.md
raw_materials.md
reaganomics.md
real_asset.md
real_economic_growth_rate.md
real_effective_exchange_rate_(reer).md
real_estate_investment_trust_(reit).md
real_gross_domestic_product_(gdp).md
real_income.md
real_interest_rate.md
real_interest_rate_analysis.md
real_option.md
real_options_analysis.md
real_property.md
real_rate_of_return.md
real_time.md
realization_multiple.md
realized_gain.md
realized_gains_and_losses.md
realized_loss.md
realized_returns_analysis.md
realized_risk_management.md
realized_volatility.md
realized_volatility_models.md
realized_yield.md
real-time_data_analysis.md
real-time_gross_settlement_(rtgs).md
real-time_market_data.md
real-time_quote_(rtq).md
real-time_strategy_adjustment.md
real-time_trading_systems.md
real-time_volatility.md
rebalancing.md
rebalancing_algorithms.md
rebalancing_frequency.md
rebalancing_risk.md
rebalancing_rules.md
rebalancing_strategies.md
rebate.md
recapitalization.md
receipt.md
receivable.md
receivables_turnover_ratio.md
receivership.md
recency_frequency_monetary_value_(rfm).md
recession.md
recession_indicators.md
recession_risk_analysis.md
recessionary_gap.md
recessionary_trends.md
recession-proof_strategies.md
recharacterization.md
reciprocal_trading.md
reconciliation.md
record_date.md
recourse.md
recourse_loan.md
recovery_rate.md
recurrent_neural_networks_(rnn).md
recurring_billing.md
recurring_revenue.md
recursive_filter_in_trading.md
recursive_modeling_in_trading.md
redemption.md
redemption_risk.md
redlining.md
redundancy_analysis_in_trading.md
redundancy_reduction.md
redundancy_techniques.md
reference_number.md
reference_rate.md
refinance.md
reflexivity.md
reg_nms.md
regime_shifts_in_trading.md
regime_switching.md
registered_education_savings_plan.md
registered_investment_advisor_(ria).md
registered_representative_(rr).md
regression.md
regression_analysis.md
regression_methods_in_trading.md
regression_techniques.md
regression_trees_in_trading.md
regressional_analysis_in_trading.md
regression-based_strategies.md
regret_theory.md
regtech.md
regulated_investment_company_(ric).md
regulation_a.md
regulation_b_(reg_b)_in_the_equal_credit_opportunity_act_(ecoa).md
regulation_cc.md
regulation_dd.md
regulation_o.md
regulation_sho.md
regulation_t_(reg_t).md
regulation_u.md
regulation_w.md
regulation_z_(truth_in_lending).md
regulatory_capture.md
regulatory_risk.md
rehypothecation.md
reimbursement.md
reinforcement_learning.md
reinsurance.md
reinsurance_ceded.md
reinvestment.md
reinvestment_rate.md
reinvestment_risk.md
related-party_transactions.md
relationship_management.md
relationship_manager.md
relative_momentum_index_(rmi).md
relative_momentum_strategies.md
relative_performance_analysis.md
relative_performance_indicators.md
relative_performance_metrics.md
relative_purchasing_power_parity_(rppp).md
relative_strength.md
relative_strength_analysis.md
relative_strength_index_(rsi).md
relative_strength_ranking.md
relative_valuation_model.md
relative_value.md
relative_value_arbitrage.md
relative_value_models.md
relative_vigor_index_(rvi).md
relative_volatility_models.md
relative_volume.md
relevant_cost.md
relief_rally.md
remittance.md
remuneration.md
renewable_energy_certificate_(rec).md
renewable_resource.md
renko_chart.md
rent_control.md
rent_seeking.md
reorganization.md
repackaging.md
repatraiable.md
repatriation.md
repayment.md
replacement_cost.md
replacement_rate.md
repo_market_analysis.md
repo_market_strategies.md
repo_rate_analysis.md
repo_rate_strategies.md
repo_trading_strategies.md
representative_sample.md
repricing_risk.md
repudiation.md
repurchase_activity.md
repurchase_agreement_(repo).md
repurchase_agreements_(repos).md
repurchase_program_analysis.md
repurchase_transaction_strategies.md
reputational_risk.md
request_for_quote_(rfq).md
requests_for_proposal_(rfp).md
required_minimum_distribution_(rmd).md
required_rate_of_return_(rrr).md
requisition.md
requote.md
resampling_techniques_in_trading.md
research_analysts.md
research_and_development_(r&d).md
research_and_development_(r&d)_expenses.md
research_associate.md
research_report.md
reserve_bank_of_india_(rbi).md
reserve_currency.md
reserve_fund.md
reserve_price.md
reserve_ratio.md
reserve_requirements.md
resident_alien.md
residential_mortgage-backed_security_(rmbs).md
residual_analysis_in_trading.md
residual_dividend.md
residual_income.md
residual_risk_management.md
residual_standard_deviation.md
residual_sum_of_squares_(rss).md
residual_value.md
residual_volatility.md
resistance_(resistance_level).md
resolution_trust_corporation_(rtc).md
resource_curse.md
restatement.md
restricted_cash.md
restricted_stock.md
restricted_stock_unit_(rsu).md
restrictive_covenant.md
restructuring.md
restructuring_charge.md
resume.md
retail_banking.md
retail_investor.md
retail_order_flow.md
retail_price_index_(rpi).md
retail_sales.md
retained_earnings.md
retainer_fee.md
retention_bonus.md
retention_ratio.md
retirement_income_certified_professional_(ricp).md
retirement_money_market_account.md
retirement_planning.md
retracement.md
retrocession.md
return.md
return_analysis_frameworks.md
return_analysis_techniques.md
return_and_risk_analysis.md
return_attribution.md
return_dispersion_analysis.md
return_distribution_analysis.md
return_forecasting_models.md
return_forecasting_techniques.md
return_of_capital_(roc).md
return_on_assets_(roa).md
return_on_average_assets_(roaa).md
return_on_average_capital_employed_(roace).md
return_on_average_equity_(roae).md
return_on_capital_employed_(roce).md
return_on_equity_(roe).md
return_on_invested_capital_(roic).md
return_on_investment_(roi).md
return_on_net_assets_(rona).md
return_on_revenue_(ror).md
return_on_risk-adjusted_capital_(rorac).md
return_on_sales_(ros).md
return_on_tangible_equity_(rote).md
return_on_total_assets_(rota).md
return_on_working_capital_(rowc).md
return_to_risk_ratio.md
returned_payment_fee.md
reuters.md
revaluation.md
revaluation_reserve.md
revealed_preference.md
revenue.md
revenue_agent's_report_(rar).md
revenue_bond.md
revenue_cap_regulations.md
revenue_deficit.md
revenue_generating_unit_(rgu).md
revenue_officer.md
revenue_passenger_mile_(rpm).md
revenue_per_available_room_(revpar).md
revenue_per_available_seat_mile_(rasm).md
revenue_per_user_(rpu).md
revenue_recognition.md
reversal.md
reversal_day_trading.md
reversal_indicators.md
reversal_patterns.md
reversal_trading_strategies.md
reverse_auction.md
reverse_calendar_spread.md
reverse_collar_strategy.md
reverse_convertible_bonds.md
reverse_culture_shock.md
reverse_engineering_of_algorithms.md
reverse_engineering_trading_strategies.md
reverse_gamma_hedging.md
reverse_ico.md
reverse_iron_butterfly.md
reverse_iron_condor.md
reverse_morris_trust.md
reverse_repurchase_agreement.md
reverse_stock_split.md
reverse_stock_splits.md
reverse_straddle.md
reverse_takeover_(rto).md
reverse_triangular_mergers.md
reversion_to_mean.md
revocable_trust.md
revolver.md
revolving_credit.md
revolving_door.md
revolving_loan_facility.md
rho.md
ricardian_equivalence.md
rider.md
right_of_first_offer.md
right_of_first_refusal.md
right_of_rescission.md
rights_offering_(issue).md
right-to-work_law.md
ring-fence.md
ripple.md
ripple_(cryptocurrency).md
rise_fall.md
risk.md
risk_adjusted_performance.md
risk_allocation_models.md
risk_analysis.md
risk_and_return_analysis.md
risk_appetite_analysis.md
risk_arbitrage.md
risk_arbitrage_models.md
risk_arbitrage_opportunities.md
risk_assessment.md
risk_assessment_models.md
risk_budgeting.md
risk_capital_allocation.md
risk_capital_management.md
risk_control.md
risk_control_strategies.md
risk_factors_in_trading.md
risk_limit.md
risk_management.md
risk_management_frameworks.md
risk_management_plan.md
risk_management_systems.md
risk_management_techniques.md
risk_measures.md
risk_metrics.md
risk_models_in_trading.md
risk_neutral.md
risk_neutral_valuation.md
risk_parity.md
risk_parity_models.md
risk_premium.md
risk_premium_analysis.md
risk_profiles.md
risk_reversal.md
risk_reward_ratio.md
risk_tolerance.md
risk-adjusted_return.md
risk-adjusted_return_on_capital_(raroc).md
risk-averse.md
risk-based_capital_requirement.md
risk-free_asset.md
risk-free_rate_of_return.md
risk-neutral_measures.md
risk-neutral_probabilities.md
risk-on_risk-off.md
risk-return_tradeoff.md
risk-weighted_assets.md
risk-weighted_assets_(rwa).md
risk-weighted_return.md
rithmic.md
rival_good.md
roadshow.md
robber_baron.md
robinhood.md
robinson-patman_act.md
robo_advisor.md
robotic_process_automation_(rpa).md
robust.md
robust_optimization.md
robust_portfolio_construction.md
robust_regression_in_trading.md
robust_statistics_in_trading.md
rogue_trader.md
roll_back.md
roll_forward.md
roll_yield.md
roll-down_return.md
rolling_beta_analysis.md
rolling_correlation.md
rolling_forecasts.md
rolling_returns.md
rolling_sharpe_ratio.md
rolling_volatility.md
rolling_window_analysis.md
rolling_z-score_analysis.md
rollover.md
rollover_cost.md
rollover_risk.md
roth_401(k).md
roth_ira.md
round_lot.md
round_trip.md
routing_transit_number_(rtn).md
royalty.md
roy's_safety-first_criterion_(sfratio).md
r-squared_in_trading.md
rule_10b-18.md
rule_10b-5.md
rule_10b5-1.md
rule_144.md
rule_144a.md
rule_72(t).md
rule_development_in_trading.md
rule_mining_in_trading.md
rule_of_70.md
rule_of_72.md
rule_of_78.md
rule_of_thumb.md
rule-based_algorithm_design.md
rule-based_trading.md
run_rate.md
runaway_gaps.md
running_average_strategies.md
run-pullback_strategies.md
run-up_analysis.md
russell_1000_index.md
russell_2000_index.md
russell_2000_index_strategies.md
russell_3000_index.md
russell_3000_index_strategies.md
russell_index_analysis.md
russell_index_trading.md
rwanda_stock_exchange_(rse).md""".split('\n')

# Check each batch
batches_content = {}
for batch_num in range(20):
    result = subprocess.run(['python', r'C:\StockSharp\AlgoTradingLib\ru\pedia\split_files.py', str(batch_num)],
                          capture_output=True, text=True)
    batch_files = result.stdout.strip().split('\n')
    batches_content[batch_num] = [f for f in batch_files if f.strip()]

# Get existing translated files
existing = set(os.listdir(r"C:\StockSharp\AlgoTradingLib\ru\pedia\r"))
existing_md = {f for f in existing if f.endswith('.md')}

print("Batch Analysis:")
print("=" * 60)

missing_in_batches = {}
for batch_num in range(20):
    batch_files = batches_content[batch_num]
    batch_missing = [f for f in batch_files if f not in existing_md]
    missing_in_batches[batch_num] = batch_missing

    print(f"Batch {batch_num}: {len(batch_files)} files, {len(batch_missing)} missing")
    if batch_missing:
        for f in batch_missing[:5]:  # Show first 5 missing
            print(f"  - {f}")
        if len(batch_missing) > 5:
            print(f"  ... and {len(batch_missing) - 5} more")

print("\n" + "=" * 60)
print("\nMissing files summary:")
total_missing = []
for batch_num, missing in missing_in_batches.items():
    total_missing.extend(missing)

print(f"Total missing: {len(total_missing)}")
print("\nAll missing files:")
for i, f in enumerate(total_missing, 1):
    print(f"{i}. {f}")
