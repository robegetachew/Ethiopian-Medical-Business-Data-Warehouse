{{ config(materialized='table') }}

with filtered_data as (
    select
        channel_name,
        channel_title,
        message_date,  -- Using the message_date from the previous model
        message,
        emoji_used,
        message_length
    from {{ ref('calculate_message_length') }}  -- Referring to the updated model
    where emoji_used is not null
)

select *
from filtered_data
