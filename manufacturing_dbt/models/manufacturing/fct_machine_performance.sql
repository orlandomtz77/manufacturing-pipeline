select
    machine_id,
    product_id,
    operator_id,
    timestamp,
    units_produced,
    defects,
    downtime_minutes,
    units_produced - defects as good_units,
    coalesce(round(round((480.0 - downtime_minutes) / 480.0, 2)*
    round(cast(units_produced - defects as float) / nullif(units_produced, 0), 2),2),0) as oee

from {{ ref('stg_production') }}