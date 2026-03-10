with machine_avg as(
select
machine_id,
oee,
avg(oee) as avg_oee
from {{ ref('fct_machine_performance') }}
group by machine_id)
select
machine_id,
avg_oee,
case
    when avg_oee >= .70 then 'Bueno'
    when avg_oee >= .40 then 'Regular'
    else 'Critico'
end as 'estado'
from machine_avg
order by avg_oee desc
