DROP TABLE IF EXISTS #race
DROP TABLE IF EXISTS #ethnic

select distinct race_multi
from clientsocial


select contact_id, Race_multi,
       case
           when RACE_MULTI = '1' then 'American Indian/Native Alaskan'
           when RACE_MULTI = '10' then 'Asian'
           when RACE_MULTI = '5' then 'Black or African American'
           when RACE_MULTI = '12' then 'Native Hawaiian/Other Pacific Islander'
           when RACE_MULTI in ('6', '7') then 'White'
           when RACE_MULTI = '0' then 'Not Available'
           when RACE_MULTI = '14' then 'Refused to Answer'
           when RACE_MULTI is null then 'Not Availale'
       else 'Multi'
       end as Race
into #race       
from CLIENTSOCIAL


select contact_id, 
       case
	       when ethnicity = 'Hispanic or Latino' then 'Yes'
		   when ethnicity = 'Not Hispanic or Latino' then 'No'
		   when ethnicity in ('missing/unknown', 'unknown') then 'Missing'
		   when ethnicity is null then 'Missing'
	   else ethnicity
	   end as HispanicLatino
into #ethnic       
from CLIENTSOCIAL       


select distinct u.contact_id, PROGRAM_NAME, r.Race, e.HispanicLatino
from PROGRAM as p
     join SERVICE_UNITS as u
     on p.prg_id = u.PRG_ID
     join #race as r
     on u.CONTACT_ID = r.CONTACT_ID
     join #ethnic as e
     on u.CONTACT_ID = e.CONTACT_ID
where p.prg_id = 2161
      and u.SERVICE_DT>='07/01/2022' and u.SERVICE_DT<'07/01/2023'
      and u.CONTACT_ID<2000000000
      and u.CONTACT_ID<>99999
