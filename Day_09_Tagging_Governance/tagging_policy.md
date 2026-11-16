# Cloud Tagging Governance Policy — Sample
Required tags on supported billable resources:
- `owner`: accountable team or individual role
- `team`: cost-owning team
- `environment`: prod / staging / dev / test
- `application`: registered application identifier
- `cost_center`: finance-approved cost centre
- `expiry_date`: ISO date for temporary resources

Controls:
1. Apply tags at provisioning through IaC templates.
2. Validate required tags in CI before deployment.
3. Run daily inventory scans; notify owners of missing tags.
4. Escalate unresolved production gaps after the agreed SLA.
5. Do not place personal or secret information in tags.
6. Maintain exceptions with approver, reason and expiry date.
