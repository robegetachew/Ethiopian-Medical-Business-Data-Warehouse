{{ config(materialized='table') }}

with message_data as (
    select
        channel_name,
        channel_title,
        message_date,  -- Using the message_date from the previous model
        message,
        emoji_used,
        length(message) as message_length
    from {{ ref('convert_text_date_to_message_date') }}  -- Referring to the updated model
)

select *
from message_data
