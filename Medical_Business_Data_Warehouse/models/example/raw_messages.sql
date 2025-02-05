SELECT 
    channel_name,
    channel_title,
    text_date,
    message,
    emoji_used
FROM {{ source('medical_data', 'medical_datawarehouse') }}
