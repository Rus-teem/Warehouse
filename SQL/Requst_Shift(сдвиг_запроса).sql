WITH inviters_results AS (
    SELECT
        to_char(a.created_at, 'YYYY-MM') AS date,
        inviter.id AS inviter_id,
        count(a.id) AS accounts
    FROM
        (
            SELECT
                id
            FROM
                accounts
            WHERE
                registration_type_id = 1
                AND created_at >= '2018-01-01'
        ) AS inviter
        JOIN accounts AS a ON (a.inviter_id = inviter.id)
    WHERE
        a.created_at >= '2018-01-01'
    group by
        date,
        inviter.id
    ORDER BY
        1 ASC
)
SELECT
    date,
    inviters,
    -- Можно использовать для проверкуи запроса
    -- inviters + curn_inviter_count - new_inviter_count AS prev,
    -- curn_inviter_ids, -- можно глянуть конкретные аккаунты
    curn_inviter_count,
    -- curn_inviter_count / prev * 100
    round(
        curn_inviter_count :: numeric / (
            inviters + curn_inviter_count - new_inviter_count
        ) * 100,
        2
    ) AS curn_percent,
    -- new_inviter_ids, --  можно глянуть конкретные аккаунты
    new_inviter_count
FROM
    (
        SELECT
            date,
            count(inviter_id) AS inviters,
            SUM(accounts) AS accounts
        FROM
            inviters_results
        GROUP BY
            date
    ) AS t1
    LEFT JOIN (
        SELECT
            COALESCE(
                to_char(
                    (d1.date || '-01') :: date + '1 month' :: interval,
                    'YYYY-MM'
                ),
                d2.date
            ) AS date,
            SUM(
                CASE
                    WHEN d2.date IS NULL THEN 1
                END
            ) AS curn_inviter_count,
            array_remove(
                array_agg(
                    DISTINCT CASE
                        WHEN d2.date IS NULL THEN d1.inviter_id
                    END
                ),
                NULL
            ) AS curn_inviter_ids,
            SUM(
                CASE
                    WHEN d1.date IS NULL THEN 1
                END
            ) AS new_inviter_count,
            array_remove(
                array_agg(
                    DISTINCT CASE
                        WHEN d1.date IS NULL THEN d2.inviter_id
                    END
                ),
                NULL
            ) AS new_inviter_ids
        FROM
            inviters_results AS d1 FULL
            OUTER JOIN inviters_results AS d2 ON (
                d1.inviter_id = d2.inviter_id
                AND to_char(
                    (d1.date || '-01') :: date + '1 month' :: interval,
                    'YYYY-MM'
                ) = d2.date
            )
        GROUP BY
            1
    ) AS t2 USING (date)
ORDER BY
    date;

-- Пример 
date   | inviters | curn_inviter_count | curn_percent | new_inviter_count 
---------+----------+--------------------+--------------+-------------------
 2018-01 |        6 |                    |              |                 6
 2018-02 |       10 |                  4 |        66.67 |                 8
 2018-03 |       10 |                  7 |        70.00 |                 7
 2018-04 |        8 |                  8 |        80.00 |                 6
 2018-05 |        8 |                  6 |        75.00 |                 6
 2018-06 |        9 |                  5 |        62.50 |                 6
 2018-07 |       12 |                  6 |        66.67 |                 9
 2018-08 |       12 |                  8 |        66.67 |                 8
 2018-09 |       15 |                  7 |        58.33 |                10
 2018-10 |       17 |                  9 |        60.00 |                11
 2018-11 |       18 |                 10 |        58.82 |                11
 2018-12 |       22 |                 10 |        55.56 |                14
 2019-01 |       24 |                 10 |        45.45 |                12
 2019-02 |       27 |                 10 |        41.67 |                13
 2019-03 |       37 |                  6 |        22.22 |                16
 2019-04 |       33 |                 19 |        51.35 |                15
 2019-05 |       26 |                 17 |        51.52 |                10
 2019-06 |       29 |                  9 |        34.62 |                12
 2019-07 |       30 |                 13 |        44.83 |                14
 2019-08 |       27 |                 15 |        50.00 |                12
 2019-09 |       24 |                 13 |        48.15 |                10