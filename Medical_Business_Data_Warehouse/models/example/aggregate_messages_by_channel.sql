{{ config(materialized='table') }}

with aggregated_data as (
    select
        channel_name,
        channel_title,
        count(message) as message_count,
        avg(message_length) as avg_message_length
    from {{ ref('filter_messages_with_emojis') }}  -- Referring to the updated model
    group by channel_name, channel_title
)

select *
from aggregated_data
