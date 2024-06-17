-- кейс
WITH prtn AS (
    SELECT
        id
    FROM
        accounts
    WHERE
        registration_type_id = 1
)
-- Тело запроса 
SELECT
    oppp.day,
    oppp.count_prtn AS "Количество реферальщиков",
    oppp.count_user AS "Количество пользователей",
    ABS(oppp.count_prtn - AVG(oppp.count_prtn)) as lol,
    -- разница от среднего
    corr(oppp.count_prtn, oppp.count_user) as lol2,
    -- корреляция 
    count_user / oppp.count_prtn as "Количество пользователей на одного партнера",
    love.withcontr AS "Количество реф с контрактом",
    love.withcontr / oppp.count_prtn as "Доля с контрактми",
    sum(love.withcontr),
    amount_prtn.coun_prtn_money,
    -- количество партнеров которые сняли деньги (реферальщики)
    ABS(amount_prtn.prtn_money) AS "Сумма вывода партнера" --    amount_prtn.prtn_money / amount_prtn.coun_prtn_money
FROM
    (
        SELECT
            to_char(created_at, 'YYYY-MM') as day,
            COUNT(DISTINCT inviter_id) as count_prtn,
            COUNT(id) as count_user
        FROM
            accounts
        WHERE
            inviter_id IN (
                SELECT
                    id
                FROM
                    prtn
            )
            AND created_at > '2021-01-01'
        GROUP BY
            1
    ) as oppp
    JOIN (
        SELECT
            to_char(pc.created_at, 'YYYY-MM') as DAY,
            COUNT(c.account_id) as withcontr
        FROM
            contractors AS pc
            JOIN contracts AS c ON (pc.id = c.contractor_id)
        WHERE
            c.account_id in (
                SELECT
                    id
                FROM
                    prtn
            )
            AND pc.created_at > '2021-01-01' --BETWEEN '2021-04-01' and '2021-04-30'
        GROUP BY
            1
    ) as love ON (love.day = oppp.day)
    JOIN (
        SELECT
            to_char(created_at, 'YYYY-MM') as day,
            COUNT(account_id) as coun_prtn_money,
            SUM(amount) as prtn_money
        FROM
            transactions
        WHERE
            amount < 0
            AND type_string = ('Withdrawal')
            AND account_id in (
                SELECT
                    id
                FROM
                    prtn
            )
            AND created_at > '2021-01-01'
        GROUP BY
            1
    ) as amount_prtn ON (amount_prtn.day = oppp.day)
-- Группировка запроса 
-- PHYSICAL_ACCOUNTING  = 0
-- JURIDICAL_ACCOUNTING = 1
-- SELF_EMPLOYED_ACCOUNTING = 2
GROUP BY
    oppp.day,
    oppp.count_prtn,
    oppp.count_user,
    love.withcontr,
    amount_prtn.coun_prtn_money,
    amount_prtn.prtn_money