package main

import (
	"context"
	"fmt"
)

type ctxKey string

func main() {
	ctx := context.WithValue(context.Background(), ctxKey("a"), "b")

	get := func(ctx context.Context, k ctxKey) {
		if v, ok := ctx.Value(k).(string); ok {
			fmt.Println("key is %v value is %v", k, v)
		}
	}

	get(ctx, ctxKey("a"))
	get(ctx, ctxKey("b"))
}
