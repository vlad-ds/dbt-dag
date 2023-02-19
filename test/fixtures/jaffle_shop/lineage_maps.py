ancestors = {
    "model.jaffle_shop.customers": {
        1: {1: ['model.jaffle_shop.stg_orders',
                'model.jaffle_shop.stg_payments',
                'model.jaffle_shop.stg_customers']},
        2: {1: ['model.jaffle_shop.stg_orders',
                'model.jaffle_shop.stg_payments',
                'model.jaffle_shop.stg_customers'],
            2: ['seed.jaffle_shop.raw_orders',
                'seed.jaffle_shop.raw_payments',
                'seed.jaffle_shop.raw_customers']}
    }
}

descendants = {
    "seed.jaffle_shop.raw_customers": {
        1: {1: ['model.jaffle_shop.stg_customers']},
        2: {1: ['model.jaffle_shop.stg_customers'],
            2: ['test.jaffle_shop.unique_stg_customers_customer_id.c7614daada',
                'test.jaffle_shop.not_null_stg_customers_customer_id.e2cfb1f9aa',
                'model.jaffle_shop.customers']},
        3: {1: ['model.jaffle_shop.stg_customers'],
            2: ['test.jaffle_shop.unique_stg_customers_customer_id.c7614daada',
                'test.jaffle_shop.not_null_stg_customers_customer_id.e2cfb1f9aa',
                'model.jaffle_shop.customers'],
            3: ['test.jaffle_shop.unique_customers_customer_id.c5af1ff4b1',
                'test.jaffle_shop.relationships_orders_customer_id__customer_id__ref_customers_.c6ec7f58f2',
                'test.jaffle_shop.not_null_customers_customer_id.5c9bf9911d']}

    }
}