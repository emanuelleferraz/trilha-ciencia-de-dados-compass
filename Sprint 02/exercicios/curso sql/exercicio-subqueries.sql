-- EXERCÍCIOS ########################################################################

-- (Exercício 1) Crie uma coluna calculada com o número de visitas realizadas por cada
-- cliente da tabela sales.customers

with visit_per_client as (
	select customer_id, count(*) as number_of_visit
	from sales.funnel
	group by customer_id
)

select ctm.first_name, ctm.last_name, ctm.email, 
number_of_visit
from sales.customers as ctm
left join visit_per_client as vpc
	on ctm.customer_id = vpc.customer_id
order by number_of_visit desc
