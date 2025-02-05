{{ config(materialized='table') }}

with source_data as (
    select
        channel_name,
        channel_title,
        text_date::timestamp as message_date,  -- Converting text_date to message_date
        message,
        emoji_used
    from {{ ref('select_cleaned_data') }}  -- Referencing the select_cleaned_data model
)

select 
    channel_name,
    channel_title,
    message_date,
    message,
    emoji_used
from source_data
