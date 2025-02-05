{{ config(materialized='table') }}

with source_data as (
    select
        channel_name,
        channel_title,
        text_date::timestamp,  
        message,
        emoji_used
    from {{ ref('raw_messages') }}  
    where message is not null       
)

select 
    channel_name,
    channel_title,
    text_date,
    message,
    emoji_used
from source_data