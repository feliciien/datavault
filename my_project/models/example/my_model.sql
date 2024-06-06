{% set metadata = read_csv('data/metadata.csv') %}

{% for row in metadata %}
{% if row['role'] == 'hub' %}
-- Hub Model
{% set hub_model %}
{{ dbtvault.hub(
    src_pk=row['column_name'],
    src_nk=row['column_name'],
    src_ldts=row['load_date'],
    src_source=row['source']
) }}
{% endset %}
{{ hub_model }}

{% elif row['role'] == 'satellite' %}
-- Satellite Model
{% set sat_model %}
{{ dbtvault.satellite(
    src_pk=row['hub_name'] ~ '_hub_id',
    src_sat_name=row['column_name'],
    src_ldts=row['load_date'],
    src_source=row['source']
) }}
{% endset %}
{{ sat_model }}

{% elif row['role'] == 'link' %}
-- Link Model
{% set link_model %}
{{ dbtvault.link(
    src_pk=row['hub1_name'] ~ '_hub_id',
    src_fk=row['hub2_name'] ~ '_hub_id',
    src_ldts=row['load_date'],
    src_source=row['source']
) }}
{% endset %}
{{ link_model }}

{% endif %}
{% endfor %}
