## GET /
get recommended products by customer_id.

### Request

#### Header
```
application/json
```

#### Params
```
{
    "customer_id": SOME_CUSTOMER_ID,
}
```

### Resonse
#### Header
```
application/json
```

#### Body
```json
{
    ["Product_id"]
}
```

## PUT /db/product
post product id to database

### Request

#### Header
```
application/json
```

#### Body
```
{
    "customer_id": SOME_CUSTOMER_ID,
    "product_id": SOME_PRODUCT_ID
}
```

### Resonse
#### Header
```
application/json
```

#### Body
```json
{
    "success"
}
```

### DB modal: UA1
