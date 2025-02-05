WITH cleaned_data AS (
    SELECT
        channel_name,
        channel_title,
        CAST(text_date AS TIMESTAMP) AS message_date,
        message,
        emoji_used
    FROM {{ ref('raw_messages') }}
)
SELECT
    channel_name,
    channel_title,
    message_date,
    LENGTH(message) AS message_length,
    CASE
        WHEN emoji_used IS NOT NULL AND emoji_used != '' THEN TRUE
        ELSE FALSE
    END AS has_emoji
FROM cleaned_data
